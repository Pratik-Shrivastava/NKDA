from app.app_config.response_code import SUCCESS_CODE
from app.app_config.response_message import *
from app.routes import api
from flask_restx import fields

from app.utils.api_response import prepare_swagger_response

PRODUCT_RESPONSE_MODEL: any = api.model('user', {
    'id': fields.Integer,
    'product_name': fields.String,
    'product_description':fields.String,
    'product_price':fields.Float,
    'created_by':fields.String,
})

JWT_RESPONSE_MODEL: any = api.model('jwt Data', {
    'jwt': fields.String
})


def add_product_response() -> any:

    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=INSERT_SUCCESS_MESSAGE,
        model_name='addProduct Response'
    )


def update_product_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=UPDATE_SUCCESS_MESSAGE,
        model_name='updateProduct Response'
    )


def get_product_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=GET_SUCCESS_MESSAGE,
        model_name='getProduct Response',
        data=fields.Nested(PRODUCT_RESPONSE_MODEL)
    )


def get_product_list_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=GET_ALL_SUCCESS_MESSAGE,
        model_name='getProductList Response',
        data=fields.List(fields.Nested(PRODUCT_RESPONSE_MODEL))
    )


def delete_product_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=DELETE_SUCCESS_MESSAGE,
        model_name='deleteProduct Response'
    )
