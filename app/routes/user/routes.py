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
from app.decorators.sanitizer import sanitized
from app.enum.user_role_enum import USER_ROLE
from app.routes import api

from app.routes.user.payload import *
from app.routes.user.response import *
from app.routes.user.dao_service import *
from app.routes.user.validator import *
from app.utils.api_response import prepare_api_response
from app.utils.get_my_ip import get_my_ip


logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1].replace('_', '-'),
    description='API connected to user module',
    ordered=False
)


@ns.route('/login', methods=['POST'])
class Login(Resource):

    @ns.expect(*login_payload())
    @ns.response(*login_response())
    @sanitized()
    def post(self):
        try:
            validator = LoginValidator()
            payload: dict = validator.load(request.get_json())

            username: str = payload['username']
            password: str = payload['password']

            user_info: ORM.User | None =\
                get_user_by_username_and_password(username, password)

            if (not user_info):
                return prepare_api_response(401, 'Invalid username or password')

            access_token: str = create_access_token(
                identity=username,
                expires_delta=datetime.timedelta(hours=24),
                additional_claims={
                    'roles': [roles.as_dict()['name'] for roles in user_info.user_roles],
                    'user_name': f'{user_info.first_name} {user_info.last_name}',
                    'user_id': user_info.id,
                    'ip_address': get_my_ip(request)
                }
            )

            return prepare_api_response(
                SUCCESS_CODE,
                SUCCESS_MESSAGE,
                data={'jwt': access_token}
            )

        except ValidationError as e:
            return prepare_api_response(
                VALIDATION_ERROR_CODE,
                VALIDATION_ERROR_MESSAGE,
                error=e.normalized_messages()
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/add', methods=['POST'])
class AddUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_user_payload())
    @ns.response(*add_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def post(self, jwt_data):
        try:
            validator = AddUserValidator()
            payload: dict = validator.load(request.get_json())

            user_id: int = add_user(payload)

            return prepare_api_response(SUCCESS_CODE, INSERT_SUCCESS_MESSAGE)

        except ValidationError as e:
            return prepare_api_response(
                VALIDATION_ERROR_CODE,
                VALIDATION_ERROR_MESSAGE,
                error=e.normalized_messages()
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/update', methods=['PATCH'])
class UpdateUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*update_user_payload())
    @ns.response(*update_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def patch(self, jwt_data):
        try:
            validator = UpdateUserValidator()
            payload: dict = validator.load(request.get_json())

            updated: bool = update_user(payload)

            if not updated:
                return prepare_api_response(
                    VALIDATION_ERROR_CODE, UPDATE_ERROR_MESSAGE)

            return prepare_api_response(SUCCESS_CODE, UPDATE_SUCCESS_MESSAGE)

        except ValidationError as e:
            return prepare_api_response(
                VALIDATION_ERROR_CODE,
                VALIDATION_ERROR_MESSAGE,
                error=e.normalized_messages()
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/get', methods=['GET'])
class GetUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*get_user_payload())
    @ns.response(*get_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def get(self, jwt_data):
        try:
            validator = GetUserValidator()
            arguments: dict = validator.load(request.args.to_dict())

            user_info: ORM.User | None = get_user_by_id(arguments['id'])

            return prepare_api_response(
                SUCCESS_CODE,
                GET_SUCCESS_MESSAGE,
                data=user_info.as_dict()
            )

        except ValidationError as e:
            return prepare_api_response(
                VALIDATION_ERROR_CODE,
                VALIDATION_ERROR_MESSAGE,
                error=e.normalized_messages()
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/get-all', methods=['GET'])
class GetAllUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.response(*get_user_list_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def get(self, jwt_data):
        try:
            users_list = get_user_list()

            return prepare_api_response(
                SUCCESS_CODE,
                GET_ALL_SUCCESS_MESSAGE,
                data=[user.as_dict() for user in users_list]
            )
        
        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/delete', methods=['DELETE'])
class DeleteUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*delete_user_payload())
    @ns.response(*delete_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def delete(self, jwt_data):
        try:
            pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))
