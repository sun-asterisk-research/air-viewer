from flask_restful import Resource, reqparse
from app.models import UserModel, RevokedTokenModel, NodeModel, DataNodesModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

parserNode = reqparse.RequestParser()
parserNode.add_argument('name', help = 'This field cannot be blank', required = True)
parserNode.add_argument('address', help = 'This field cannot be blank', required = True)
parserNode.add_argument('lat', help = 'This field cannot be blank', required = True)
parserNode.add_argument('long', help = 'This field cannot be blank', required = True)
parserNode.add_argument('manager', help = 'This field cannot be blank', required = True)

parserData = reqparse.RequestParser()
parserData.add_argument('aqi', help = 'This field cannot be blank', required = True)
parserData.add_argument('pm25', help = 'This field cannot be blank', required = True)
parserData.add_argument('pm10', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        if UserModel.count_user() > 0:
            return {'message': 'cannot create account'}

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()
    
    def delete(self):
        return UserModel.delete_all()

class AllNodesPublic(Resource):
    def get(self):
        return NodeModel.return_all_public()

class AllNodesPrivate(Resource):
    @jwt_required
    def get(self):
        return NodeModel.return_all_private()

class CreateNode(Resource):
    @jwt_required
    def post(self):
        data = parserNode.parse_args()
        generateCode = NodeModel.randomString(8)

        while NodeModel.find_by_key(generateCode):
            generateCode = NodeModel.randomString(8)

        new_node = NodeModel(
            name = data['name'],
            address = data['address'],
            lat = data['lat'],
            long = data['long'],
            manager = data['manager'],
            key = generateCode
        )
        try:
            new_node.save_to_db()
            return {
                    'message': 'Node {} was created'.format(data['name']),
                    'key': generateCode
                }
        except:
            return {'message': 'Something went wrong'}, 500

class UpdateNode(Resource):
    @jwt_required
    def post(self, id):
        data = parserNode.parse_args()
        try:
            node = NodeModel.find_by_id(id)
            node.name = data['name']
            node.addres = data['address']
            node.lat = data['lat']
            node.long = data['long']
            node.manager = data['manager']
            node.save_to_db()
            return {
                    'message': 'Node {} was updated'.format(data['name']),
                }
        except:
            return {'message': 'Something went wrong'}, 500

class DeleteNode(Resource):
    @jwt_required
    def delete(self, id):
        try:
            NodeModel.delete_by_id(id)
            return {
                    'message': 'Node was deleted'
                }
        except:
            return {'message': 'Something went wrong'}, 500

class StoreData(Resource):
    def post(self, key):
        data = parserData.parse_args()

        try:
            node_id = NodeModel.find_by_key(key)
            print(node_id)
            new_node = DataNodesModel(
                aqi = data['aqi'],
                pm25 = data['pm25'],
                pm10 = data['pm10'],
                node_id = node_id.id
            )
            new_node.save_to_db()
            return {
                    'message': 'Data from node {} was created'.format(node_id.name),
                    'aqi': data['aqi'],
                    'pm25': data['pm25'],
                    'pm10': data['pm10']
                }
        except:
            return {'message': 'Something went wrong'}, 500
