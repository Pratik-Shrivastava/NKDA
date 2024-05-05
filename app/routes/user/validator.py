from app.enum.user_role_enum import USER_ROLE
from marshmallow import Schema, fields, validate


class LoginValidator(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class AddUserValidator(Schema):
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=32))
    phone = fields.String(required=True, validate=validate.Regexp(r'^[0-9]{10}$'))
    email = fields.String(required=True, validate=validate.Email())
    gender = fields.String(required=True)
    active = fields.Boolean(required=True)
    date_of_join = fields.Integer(required=True)
    roles = fields.List(
        fields.String(
            required=True,
            validate=validate.OneOf(USER_ROLE.get_list()),
        ),
        required=True,
        validate=validate.Length(min=1),
    )


class UpdateUserValidator(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=1))
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=32))
    phone = fields.String(required=True, validate=validate.Regexp(r'^[0-9]{10}$'))
    gender = fields.String(required=True)
    active = fields.Boolean(required=True)
    date_of_join = fields.Integer(required=True)


class GetUserValidator(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=1))
