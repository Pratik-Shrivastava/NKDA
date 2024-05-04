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
    @ns.response(SUCCESS_CODE, SUCCESS_MESSGAE, login_response())
    def post(self):
        try:
            payload = request.get_json()
            valid, validation_message = validate_login_payload(payload)

            if not valid:
                return {'code': 400, 'message': validation_message}

            username: str = payload.get('username')
            password: str = payload.get('password')

            user_info = get_user_by_username_and_password(username, password)

            if (not user_info):
                return {'code': 401, 'message': 'Invalid username or password'}

            # TODO: Add OTP verification

            access_token = create_access_token(
                identity=username,
                expires_delta=datetime.timedelta(hours=24),
                additional_claims={
                    'roles': [roles.as_dict()['name'] for roles in user_info.user_roles],
                    'username': username
                }
            )

            return {
                'code': SUCCESS_CODE,
                'message': SUCCESS_MESSGAE,
                'jwt': access_token
            }

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
            payload = request.get_json()
            valid, validation_message = validate_add_user_payload(payload)

            if not valid:
                return {'code': 400, 'message': validation_message}

            user_id = add_user(payload)

            # TODO: send email

            return {'code': SUCCESS_CODE, 'message': INSERT_SUCCESS_MESSGAE}

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/update', methods=['PATCH'])
class UpdateUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*update_user_payload())
    @ns.response(SUCCESS_CODE, UPDATE_SUCCESS_MESSGAE, update_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def patch(self, jwt_data):
        try:
            payload = request.get_json()
            valid, validation_message = validate_update_user_payload(payload)

            if not valid:
                return {'code': 400, 'message': validation_message}

            updated = update_user(payload)

            if not updated:
                return {'code': 400, 'message': UPDATE_ERROR_MESSGAE}

            return {'code': SUCCESS_CODE, 'message': UPDATE_SUCCESS_MESSGAE}

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get', methods=['GET'])
class GetUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*get_user_payload())
    @ns.response(SUCCESS_CODE, GET_SUCCESS_MESSGAE, get_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def get(self, jwt_data):
        try:
            arguments = request.args
            valid, validation_message = validate_get_user_payload(arguments)

            if not valid:
                return {'code': 400, 'message': validation_message}

            user_info = get_user_by_id(arguments.get('id'))

            return {
                'code': SUCCESS_CODE,
                'message': GET_SUCCESS_MESSGAE,
                'data': user_info.as_dict()
            }

        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/get-all', methods=['GET'])
class GetAllUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.response(SUCCESS_CODE, GET_ALL_SUCCESS_MESSGAE, get_user_list_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def get(self, jwt_data):
        try:
            users_list = get_user_list()

            return {
                'code': SUCCESS_CODE,
                'message': GET_ALL_SUCCESS_MESSGAE,
                'data': [user.as_dict() for user in users_list]
            }
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}


@ns.route('/delete', methods=['DELETE'])
class DeleteUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*delete_user_payload())
    @ns.response(SUCCESS_CODE, DELETE_SUCCESS_MESSGAE, delete_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def delete(self, jwt_data):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return {'code': EXCEPTION_CODE, 'message': str(e)}
