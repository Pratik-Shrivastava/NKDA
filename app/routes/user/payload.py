from flask_restx import fields
from app.enum.user_role_enum import USER_ROLE
from app.routes import api


def login_payload() -> list:

    payload = api.model('login Payload', {
        'username': fields.String,
        'password': fields.String
    })

    return [payload]


def add_user_payload() -> list:

    payload = api.model('addUser Payload', {
        'username': fields.String,
        'first_name': fields.String,
        'last_name': fields.String,
        'password': fields.String,
        'phone': fields.String,
        'email': fields.String,
        'gender': fields.String,
        'active': fields.Boolean,
        'date_of_join': fields.Integer(description='date in epoch format'),
        'roles': fields.List(
            fields.String(
                default=USER_ROLE.USER.value,
                description=f'available roles: {",".join(USER_ROLE.get_list())}'
            )
        )
    })

    return [payload]


def update_user_payload() -> list:

    payload = api.model('updateUser Payload', {
        'id': fields.Integer,
        'first_name': fields.String,
        'last_name': fields.String,
        'password': fields.String,
        'phone': fields.String,
        'gender': fields.String,
        'active': fields.Boolean,
        'date_of_join': fields.Integer(description='date in epoch format')
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
