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

from app.routes.product.payload import *
from app.routes.product.response import *
from app.routes.product.dao_service import *
from app.routes.product.validator import *
from app.utils.api_response import prepare_api_response


logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1].replace('_', '-'),
    description='API connected to product module',
    ordered=False
)


@ns.route('/add', methods=['POST'])
class AddProduct(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_product_payload())
    @ns.response(*add_product_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def post(self, jwt_data):
        try:
            validator = AddProductValidator()
            payload: dict = validator.load(request.get_json())

            product_id: int = add_product(payload)

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
class UpdateProduct(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*update_product_payload())
    @ns.response(*update_product_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def patch(self, jwt_data):
        try:
            validator = UpdateProductValidator()
            payload: dict = validator.load(request.get_json())

            updated: bool = update_product(payload)

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
class GetProduct(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*get_product_payload())
    @ns.response(*get_product_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def get(self, jwt_data):
        try:
            validator = GetProductValidator()
            arguments: dict = validator.load(request.args.to_dict())

            product_info: Product | None = get_product_by_id(arguments['id'])

            return prepare_api_response(
                SUCCESS_CODE,
                GET_SUCCESS_MESSAGE,
                data=product_info.as_dict()
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
class GetAllProduct(Resource):

    @ns.doc(security=SECURITY)
    @ns.response(*get_product_list_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def get(self, jwt_data):
        try:
            products_list = get_product_list()

            return prepare_api_response(
                SUCCESS_CODE,
                GET_ALL_SUCCESS_MESSAGE,
                data=[product.as_dict() for product in products_list]
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))


@ns.route('/delete', methods=['DELETE'])
class DeleteProduct(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*delete_product_payload())
    @ns.response(*delete_product_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    @sanitized()
    def delete(self, jwt_data):
        try:
            product_id: int = request.args.get('product_id')

            deleted = delete_product(product_id)

            if not deleted:
                return prepare_api_response(EXCEPTION_CODE, DELETE_ERROR_MESSAGE)
            
            return prepare_api_response(SUCCESS_CODE, DELETE_SUCCESS_MESSAGE)
        
        except Exception as e:
            logger.error(traceback.format_exc())
            return prepare_api_response(EXCEPTION_CODE, str(e))