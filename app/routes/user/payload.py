from flask_restx import fields
from app.routes import api


def login_payload() -> list:

    payload = api.model('login Payload', {
        'username': fields.String,
        'password': fields.String
    })

    return [payload]


def add_user_payload() -> list:

    payload = api.model('addUser Payload', {
        'first_name': fields.String,
        'last_name': fields.String
    })

    return [payload]


def update_user_payload() -> list:

    payload = api.model('updateUser Payload', {
        'id': fields.Integer,
        'first_name': fields.String,
        'last_name': fields.String
    })

    return [payload]


def get_user_payload() -> list:

    parser = api.parser()
    parser.add_argument('id', type=int, location='args')

    return [parser]


def delete_user_payload() -> list:

    parser = api.parser()
    parser.add_argument('id', type=int, location='args')

    return [parser]
