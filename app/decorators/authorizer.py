from datetime import datetime
from functools import wraps

from flask import request
from flask_jwt_extended import decode_token

from app.app_config.config import SENSITIVE_FIELDS
from app.enum.user_role_enum import USER_ROLE
from app.utils.api_response import prepare_api_response
from app.utils.entry_log import create_entry_log
from app.utils.get_my_ip import get_my_ip

import copy

def encode_payload(payload):
    if payload:
        for key, value in payload.items():
            if isinstance(value, str):
                if key in SENSITIVE_FIELDS:
                    payload[key] = '**********'
            elif isinstance(value, dict):
                payload[key] = encode_payload(value)
    return payload


def is_authorized(required_roles_enum: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                token = request.headers.get('Authorization').split('Bearer ')[1]
                jwt_data = decode_token(token)
                user_name = jwt_data.get('user_name')
                user_id = jwt_data.get('user_id')
                roles: list = jwt_data.get('roles', [])
                exp: int = jwt_data['exp']
                current_time: datetime = datetime.now()

                required_roles_list: list = [e.value for e in required_roles_enum]

                if len(required_roles_list) == 0:
                    required_roles_list = USER_ROLE.get_list()
                
                if not any(role in roles for role in required_roles_list):
                    return prepare_api_response(403, 'Insufficient privileges')

                if current_time > datetime.fromtimestamp(exp):
                    return prepare_api_response(401, 'Token expired')
                
                arguments = request.args.to_dict()
                try:
                    payload = request.get_json()
                except Exception as e:
                    payload = request.form.to_dict()

                create_entry_log(
                    user_id=user_id,
                    user_name=user_name,
                    ip_address=get_my_ip(request),
                    endpoint=request.path,
                    method=request.method,
                    request_payload=encode_payload(copy.deepcopy(payload)),
                    query_params=encode_payload(copy.deepcopy(arguments))
                )

                return func(*args, **kwargs, jwt_data=jwt_data)
            except Exception as e:
                return prepare_api_response(500, str(e))
        return wrapper
    return decorator
