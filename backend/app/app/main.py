import os

# Import installed packages
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Import app code
app = Flask(__name__)
api = Api(app)

# Config Mysql
DB_HOST = os.getenv('DB_HOST', 'localhost')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@' + DB_HOST + '/air_visual'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

# After creating the app, so that cors can import it
from app import cors

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

from app import models, resources, views

#post
api.add_resource(resources.UserRegistration, '/api/registration')
#post
api.add_resource(resources.UserLogin, '/api/login')
#post
api.add_resource(resources.UserLogoutAccess, '/api/logout/access')
#post
api.add_resource(resources.UserLogoutRefresh, '/api/logout/refresh')
#post
api.add_resource(resources.TokenRefresh, '/api/token/refresh')
#get
api.add_resource(resources.AllNodesPublic, '/api/node/public')
#get
api.add_resource(resources.AllNodesPrivate, '/api/node/private')
#put
api.add_resource(resources.CreateNode, '/api/node')
#post
api.add_resource(resources.UpdateNode, '/api/node/<int:id>')
#delete
api.add_resource(resources.DeleteNode, '/api/node/<int:id>')
