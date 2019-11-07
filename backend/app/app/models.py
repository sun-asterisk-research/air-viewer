from app.main import db
from passlib.hash import pbkdf2_sha256 as sha256

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
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

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
    key = db.Column(db.String(8), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all_public(cls):
        def to_json(x):
            return {
                'name': x.name,
                'address': x.address,
                'lat': x.lat,
                'long': x.long
            }
        return {'nodes': list(map(lambda x: to_json(x), NodeModel.query.all()))}
    
    @classmethod
    def return_all_private(cls):
        def to_json(x):
            return {
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
    def delete_by_id(cls, id):
        cls.query.filter_by(id = id).delete()
        db.session.commit()

    @staticmethod
    def randomString(stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))
    