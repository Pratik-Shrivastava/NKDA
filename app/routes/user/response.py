from app.app_config.response_code import SUCCESS_CODE
from app.app_config.response_message import *
from app.routes import api
from flask_restx import fields

USER_RESPONSE_MODEL: any = api.model('user', {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String
})


def login_response() -> any:
    return api.model('login Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=SUCCESS_MESSGAE),
        'jwt': fields.String
    })


def add_user_response() -> any:
    return api.model('addUser Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=INSERT_SUCCESS_MESSGAE)
    })


def update_user_response() -> any:
    return api.model('updateUser Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=UPDATE_SUCCESS_MESSGAE)
    })


def get_user_response() -> any:
    return api.model('updateUser Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=GET_SUCCESS_MESSGAE),
        'data': fields.Nested(USER_RESPONSE_MODEL)
    })


def get_user_list_response() -> any:
    return api.model('updateUser Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=GET_ALL_SUCCESS_MESSGAE),
        'data': fields.List(fields.Nested(USER_RESPONSE_MODEL))
    })


def delete_user_response() -> any:
    return api.model('deleteUser Response', {
        'code': fields.Integer(default=SUCCESS_CODE),
        'message': fields.String(default=DELETE_SUCCESS_MESSGAE),
    })
