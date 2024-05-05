import datetime
import os
import traceback
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from app.app_config.config import get_logger
from app.app_config.response_code import *
from app.app_config.response_message import *
from app.app_config.swagger_config import SECURITY
from app.decorators.authorizer import is_authorized
from app.enum.user_role_enum import USER_ROLE
from app.routes import api

from app.routes.user.payload import *
from app.routes.user.response import *
from app.routes.user.dao_service import *
from app.routes.user.validator import *


logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1].replace('_', '-'),
    description='API connected to user module',
    ordered=False
)


@ns.route('/login', methods=['POST'])
class Login(Resource):

    @ns.expect(*login_payload())
    @ns.response(SUCCESS_CODE, SUCCESS_MESSAGE, login_response())
    def post(self):
        try:
            validator = LoginValidator()
            payload = validator.load(request.get_json())

            username: str = payload['username']
            password: str = payload['password']

            user_info = get_user_by_username_and_password(username, password)

            if (not user_info):
                return {'code': 401, 'message': 'Invalid username or password'}

            # TODO: Add OTP verification

            access_token = create_access_token(
                identity=username,
                expires_delta=datetime.timedelta(hours=24),
                additional_claims={
                    'roles': [roles.as_dict()['name'] for roles in user_info.user_roles],
                    'username': username,
                    'user_id': user_info.id
                }
            )

            return {
                'code': SUCCESS_CODE,
                'message': SUCCESS_MESSAGE,
                'jwt': access_token
            }
        
        except ValidationError as e:
            return {'code': VALIDATION_ERROR_CODE, 'message': VALIDATION_ERROR_MESSAGE}

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/add', methods=['POST'])
class AddUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_user_payload())
    @ns.response(SUCCESS_CODE, INSERT_SUCCESS_MESSAGE, add_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def post(self, jwt_data):
        try:
            validator = AddUserValidator()
            payload = validator.load(request.get_json())

            user_id = add_user(payload)

            return {'code': SUCCESS_CODE, 'message': INSERT_SUCCESS_MESSAGE}
        
        except ValidationError as e:
            return {
                'code': VALIDATION_ERROR_CODE, 
                'message': VALIDATION_ERROR_MESSAGE,
                'errors': e.normalized_messages()
            }

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/update', methods=['PATCH'])
class UpdateUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*update_user_payload())
    @ns.response(SUCCESS_CODE, UPDATE_SUCCESS_MESSAGE, update_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def patch(self, jwt_data):
        try:
            validator = UpdateUserValidator()
            payload = validator.load(request.get_json())

            updated = update_user(payload)

            if not updated:
                return {'code': VALIDATION_ERROR_CODE, 'message': UPDATE_ERROR_MESSAGE}

            return {'code': SUCCESS_CODE, 'message': UPDATE_SUCCESS_MESSAGE}
        
        except ValidationError as e:
            return {'code': VALIDATION_ERROR_CODE, 'message': VALIDATION_ERROR_MESSAGE}

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get', methods=['GET'])
class GetUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*get_user_payload())
    @ns.response(SUCCESS_CODE, GET_SUCCESS_MESSAGE, get_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def get(self, jwt_data):
        try:
            validator = GetUserValidator()
            arguments = validator.load(request.args.to_dict())

            user_info = get_user_by_id(arguments['id'])

            return {
                'code': SUCCESS_CODE,
                'message': GET_SUCCESS_MESSAGE,
                'data': user_info.as_dict()
            }
        
        except ValidationError as e:
            return {'code': VALIDATION_ERROR_CODE, 'message': VALIDATION_ERROR_MESSAGE}

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get-all', methods=['GET'])
class GetAllUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.response(SUCCESS_CODE, GET_ALL_SUCCESS_MESSAGE, get_user_list_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def get(self, jwt_data):
        try:
            users_list = get_user_list()

            return {
                'code': SUCCESS_CODE,
                'message': GET_ALL_SUCCESS_MESSAGE,
                'data': [user.as_dict() for user in users_list]
            }
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/delete', methods=['DELETE'])
class DeleteUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*delete_user_payload())
    @ns.response(SUCCESS_CODE, DELETE_SUCCESS_MESSAGE, delete_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def delete(self, jwt_data):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}
