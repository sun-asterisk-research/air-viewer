from app.main import db
from passlib.hash import pbkdf2_sha256 as sha256
from pytz import timezone
from datetime import datetime, timedelta
from sqlalchemy.sql import func
from sqlalchemy import text

import random
import string
import json
from decimal import Decimal

# encode Decimal
class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)

def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def count_user(cls):
        return cls.query.count()

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)

class NodeModel(db.Model):
    __tablename__ = 'nodes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    address = db.Column(db.String(400), nullable = False)
    lat = db.Column(db.Float, nullable = False)
    long = db.Column(db.Float, nullable = False)
    manager = db.Column(db.String(200), nullable = False)
    key = db.Column(db.String(30), nullable = False)
    datas = db.relationship('DataNodesModel', backref='nodes')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all_public(cls):
        # fractal datas of node
        def to_json_data(data):
            return {
                'aqi': data.aqi,
                'pm25': data.pm25,
                'pm10': data.pm10,
                'created_at': data.created_at.strftime("%m/%d/%Y, %H:%M:%S")
            }
        # fractal nodes
        def to_json(x):
            return {
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'datas': list(map(lambda y: to_json_data(y), DataNodesModel.query.filter_by(node_id = x.id).limit(10).all()))
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}

    @classmethod
    def return_all_public_current(cls):
        # status air 1,2,3,4,5,6
        def air_status(data):
            if data <= 50:
                return {
                    "type": 1,
                    "info": "Tốt",
                    "infoEng": "Good"
                }
            elif data <= 100:
                return {
                    "type": 2,
                    "info": "Vừa phải",
                    "infoEng": "Moderate"
                }
            elif data <= 150:
                return {
                    "type": 3,
                    "info": "Không tốt cho sức khỏe với nhóm người nhạy cảm",
                    "infoEng": "Unhealthy for Sensitive Groups"
                }
            elif data <= 200:
                return {
                    "type": 4,
                    "info": "Ô nhiễm",
                    "infoEng": "Unhealthy"
                }
            elif data <= 300:
                return {
                    "type": 5,
                    "info": "Rất ô nhiễm",
                    "infoEng": "Very Unhealthy"
                }
            else:
                return {
                    "type": 6,
                    "info": "Nguy hiểm",
                    "infoEng": "Hazardous"
                }
        # fractal datas of node
        def to_json_data(data):
            return {
                'aqi': data.aqi,
                'pm25': data.pm25,
                'pm10': data.pm10,
                'status': air_status(data.aqi),
                'created_at': data.created_at.strftime("%d/%m/%Y, %H:%M:%S")
            }
        # fractal nodes
        def to_json(x):
            # time 24 hours ago
            data24h = db.session.execute('SELECT AVG(aqi) as aqi, AVG(pm25) as pm25, AVG(pm10) as pm10, \
                        HOUR(created_at) as created_at FROM datas \
                        WHERE node_id = :node_id AND DATE_SUB(`created_at`,INTERVAL 1 HOUR) And \
                        created_at > DATE_SUB(NOW(), INTERVAL 1 DAY) \
                        GROUP BY HOUR(created_at) ORDER BY id', {'node_id': x.id})
            if data24h.returns_rows == False:
                response_24h = []
            # Convert the response to a plain list of dicts
            else:
                response_24h = [dict(row.items()) for row in data24h]
            
            # time 7 days ago
            data7day = db.session.execute("SELECT AVG(aqi) as aqi, AVG(pm25) as pm25, AVG(pm10) as pm10, \
                        DATE_FORMAT(created_at, '%d/%m') as created_at FROM datas \
                        WHERE node_id = :node_id AND DATE_SUB(`created_at`, INTERVAL 7 DAY) And \
                        created_at > DATE_SUB(NOW(), INTERVAL 7 DAY) \
                        GROUP BY DATE_FORMAT(created_at, '%d/%m') ORDER BY id", {'node_id': x.id})
            if data7day.returns_rows == False:
                response_7day = []
            # Convert the response to a plain list of dicts
            else:
                response_7day = [dict(row.items()) for row in data7day]

            try:
                one_hour_interval_before = datetime.now(timezone('Asia/Ho_Chi_Minh')) - timedelta(hours=1)
                data = to_json_data(DataNodesModel.query.filter_by(node_id = x.id).filter(DataNodesModel.created_at > one_hour_interval_before).order_by(DataNodesModel.created_at.desc()).first())
            except:
                data = ''
            return {
                'id': x.id,
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'data':  data,
                '_24h': json.loads(json.dumps(response_24h, default=defaultencode)),
                '_7day': json.loads(json.dumps(response_7day, default=defaultencode))
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}
    
    @classmethod
    def return_all_private(cls):
        def to_json(x):
            return {
                'id': x.id,
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'manager': x.manager,
                'key': x.key
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}

    @classmethod
    def find_by_key(cls, key):
        return cls.query.filter_by(key = key).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    
    @classmethod
    def get_json_node_by_id(cls, id):
        def to_json(x):
            return {
                'id': x.id,
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'manager': x.manager,
                'key': x.key
            }
        return {'data': to_json(cls.query.filter_by(id = id).first())}

    @classmethod
    def delete_by_id(cls, id):
        cls.query.filter_by(id = id).delete()
        db.session.commit()

    @staticmethod
    def randomString(stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

class DataNodesModel(db.Model):
    __tablename__ = 'datas'

    id = db.Column(db.Integer, primary_key = True)
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    aqi = db.Column(db.Integer, nullable = False)
    pm25 = db.Column(db.Float, nullable = False)
    pm10 = db.Column(db.Float, nullable = False)
    created_at = db.Column(db.DateTime,  default=datetime.now(timezone('Asia/Ho_Chi_Minh')))
    updated_at = db.Column(db.DateTime,  default=datetime.now(timezone('Asia/Ho_Chi_Minh')),
                                       onupdate=datetime.now(timezone('Asia/Ho_Chi_Minh')))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all_public(cls):
        def to_json(x):
            return {
                'aqi': x.aqi,
                'pm25': x.pm25,
                'pm10': x.pm10,
                'node_id': x.node_id
            }
        return {'nodes': list(map(lambda x: to_json(x), DataNodesModel.query.all()))}
    