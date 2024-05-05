from app.app_config.response_code import SUCCESS_CODE
from app.app_config.response_message import *
from app.routes import api
from flask_restx import fields

from app.utils.api_response import prepare_swagger_response

USER_RESPONSE_MODEL: any = api.model('user', {
    'id': fields.Integer,
    'username': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'password': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'gender': fields.String,
    'active': fields.Boolean,
    'date_of_join': fields.Integer(description='date in epoch format'),
    'roles': fields.List(fields.String)
})

JWT_RESPONSE_MODEL: any = api.model('jwt Data', {
    'jwt': fields.String
})


def login_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=SUCCESS_MESSAGE,
        model_name='login Response',
        data=fields.Nested(JWT_RESPONSE_MODEL)
    )


def add_user_response() -> any:

    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=INSERT_SUCCESS_MESSAGE,
        model_name='addUser Response'
    )


def update_user_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=UPDATE_SUCCESS_MESSAGE,
        model_name='updateUser Response'
    )


def get_user_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=GET_SUCCESS_MESSAGE,
        model_name='getUser Response',
        data=fields.Nested(USER_RESPONSE_MODEL)
    )


def get_user_list_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=GET_ALL_SUCCESS_MESSAGE,
        model_name='getUserList Response',
        data=fields.List(fields.Nested(USER_RESPONSE_MODEL))
    )


def delete_user_response() -> any:
    return prepare_swagger_response(
        code=SUCCESS_CODE,
        message=DELETE_SUCCESS_MESSAGE,
        model_name='deleteUser Response'
    )
