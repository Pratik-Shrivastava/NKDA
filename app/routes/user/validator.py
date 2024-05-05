from app.enum.user_role_enum import USER_ROLE
from marshmallow import Schema, fields, validate, ValidationError, validates, validates_schema

import re


class LoginValidator(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class AddUserValidator(Schema):
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    gender = fields.String(required=True)
    active = fields.Boolean(required=True)
    date_of_join = fields.Integer(required=True)
    roles = fields.List(
        fields.String(
            required=True,
            validate=validate.OneOf(USER_ROLE.get_list())
        )
    )

    @validates_schema
    def validate(self, data, **kwargs):
        errors = {}

        mobile_pattern = r"^[0-9]{10}$"
        if not re.match(mobile_pattern, data['phone']):
            errors['phone'] = 'Invalid phone number'

        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, data['email']):
            errors['email'] = 'Invalid email address'

        if len(data['password'].strip()) > 32 or len(data['password'].strip()) < 6:
            errors['password'] = 'Password should be between 6 and 32 characters'

        if len(data['roles']) < 1:
            errors['roles'] = 'roles cannot be empty'

        if errors:
            raise ValidationError(errors)


class UpdateUserValidator(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String()
    last_name = fields.String()
    password = fields.String()
    phone = fields.String()
    gender = fields.String()
    active = fields.Boolean()
    date_of_join = fields.Integer()

    @validates_schema
    def validate(self, data, **kwargs):
        errors = {}

        mobile_pattern = r"^[0-9]{10}$"
        if not re.match(mobile_pattern, data['phone']):
            errors['phone'] = 'Invalid phone number'

        if len(data['password'].strip()) > 32 or len(data['password'].strip()) < 6:
            errors['password'] = 'Password should be between 6 and 32 characters'

        if errors:
            raise ValidationError(errors)


class GetUserValidator(Schema):
    id = fields.Integer(required=True)
