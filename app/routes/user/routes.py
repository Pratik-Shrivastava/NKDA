import os
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.app_config.config import get_logger
from app.app_config.response_code import *
from app.app_config.response_message import *
from app.app_config.swagger_config import SECURITY
from app.routes import api

from app.routes.user.payload import *
from app.routes.user.response import *
from app.routes.user.service import *

logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1],
    description='API connected to user module',
    ordered=False
)


@ns.route('/login', methods=['POST'])
class Login(Resource):
    
    @ns.expect(*login_payload())
    @ns.response(SUCCESS_CODE, SUCCESS_MESSGAE, login_response())
    def post(self):
        try:
            pass
        except Exception as e:
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500


@ns.route('/add', methods=['POST'])
class AddUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_user_payload())
    @ns.response(SUCCESS_CODE, INSERT_SUCCESS_MESSGAE, add_user_response())
    @jwt_required()
    def post(self):
        try:
            pass
        except Exception as e:
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500


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
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500


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
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500


@ns.route('/get-all', methods=['GET'])
class GetAllUser(Resource):
    
    @ns.doc(security=SECURITY)
    @ns.response(SUCCESS_CODE, GET_ALL_SUCCESS_MESSGAE, get_user_list_response())
    @jwt_required()
    def get(self):
        try:
            pass
        except Exception as e:
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500


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
            logger.error(e)
            return jsonify({'code': EXCEPTION_CODE, 'message': str(e)}), 500
