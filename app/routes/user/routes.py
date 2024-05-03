import datetime
import os
import traceback
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Resource
from app.app_config.config import get_logger
from app.app_config.response_code import *
from app.app_config.response_message import *
from app.app_config.swagger_config import SECURITY
from app.decorators.authorizer import is_authorized
from app.enum.user_role_enum import USER_ROLE
from app.routes import api

from app.routes.user.payload import *
from app.routes.user.response import *
from app.routes.user.service import *

logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1].replace('_', '-'),
    description='API connected to user module',
    ordered=False
)


# Mock user data for demonstration purposes
users: dict = {
    'user1': {'password': 'password1', 'roles': ['ADMIN', 'USER']},
    'user2': {'password': 'password2', 'roles': ['USER']}
}


@ns.route('/login', methods=['POST'])
class Login(Resource):

    @ns.expect(*login_payload())
    @ns.response(SUCCESS_CODE, SUCCESS_MESSGAE, login_response())
    def post(self):
        try:
            payload = request.get_json()
            username = payload['username']
            password = payload['password']

            if username in users and users[username]['password'] == password:
                roles = users[username]['roles']
                access_token = create_access_token(
                    identity=username,
                    expires_delta=datetime.timedelta(hours=24),
                    additional_claims={'roles': roles, 'username': username}
                )
                
                return {
                    'code': SUCCESS_CODE,
                    'message': SUCCESS_MESSGAE,
                    'jwt': access_token
                }
            else:
                return {'code': 401, 'message': 'Invalid username or password'}
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/add', methods=['POST'])
class AddUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_user_payload())
    @ns.response(SUCCESS_CODE, INSERT_SUCCESS_MESSGAE, add_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def post(self, jwt_data):
        try:
            print(jwt_data)
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/update', methods=['PATCH'])
class UpdateUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*update_user_payload())
    @ns.response(SUCCESS_CODE, UPDATE_SUCCESS_MESSGAE, update_user_response())
    @jwt_required()
    def patch(self):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get', methods=['GET'])
class GetUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*get_user_payload())
    @ns.response(SUCCESS_CODE, GET_SUCCESS_MESSGAE, get_user_response())
    @jwt_required()
    def get(self):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get-all', methods=['GET'])
class GetAllUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.response(SUCCESS_CODE, GET_ALL_SUCCESS_MESSGAE, get_user_list_response())
    @jwt_required()
    def get(self):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/delete', methods=['DELETE'])
class DeleteUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*delete_user_payload())
    @ns.response(SUCCESS_CODE, DELETE_SUCCESS_MESSGAE, delete_user_response())
    @jwt_required()
    def delete(self):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}
