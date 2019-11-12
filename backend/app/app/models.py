from app.main import db
from passlib.hash import pbkdf2_sha256 as sha256
from pytz import timezone
from datetime import datetime

import random
import string

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
                    "info": "Good"
                }
            elif data <= 100:
                return {
                    "type": 2,
                    "info": "Moderate"
                }
            elif data <= 150:
                return {
                    "type": 3,
                    "info": "Unhealthy for Sensitive Groups"
                }
            elif data <= 200:
                return {
                    "type": 4,
                    "info": "Unhealthy"
                }
            elif data <= 300:
                return {
                    "type": 5,
                    "info": "Very Unhealthy"
                }
            else:
                return {
                    "type": 6,
                    "info": "Hazardous"
                }
        # fractal datas of node
        def to_json_data(data):
            return {
                'aqi': data.aqi,
                'pm25': data.pm25,
                'pm10': data.pm10,
                'status': air_status(data.aqi),
                'created_at': data.created_at.strftime("%m/%d/%Y, %H:%M:%S")
            }
        # fractal nodes
        def to_json(x):
            return {
                'id': x.id,
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'data': to_json_data(DataNodesModel.query.filter_by(node_id = x.id).first())
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}
    
    @classmethod
    def return_all_private(cls):
        # fractal datas of node
        def to_json_data(data):
            return {
                'aqi': data.aqi,
                'pm25': data.pm25,
                'pm10': data.pm10,
                'created_at': data.created_at.strftime("%m/%d/%Y, %H:%M:%S")
            }

        def to_json(x):
            return {
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long,
                'manager': x.manager,
                'key': x.key,
                'datas': list(map(lambda y: to_json_data(y), DataNodesModel.query.filter_by(node_id = x.id).all()))
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}

    @classmethod
    def find_by_key(cls, key):
        return cls.query.filter_by(key = key).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

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
    