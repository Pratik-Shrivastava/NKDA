from datetime import datetime
from functools import wraps

from flask import request
from flask_jwt_extended import decode_token


def is_authorized(required_roles_enum: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                token = request.headers.get('Authorization').split('Bearer ')[1]
                jwt_data = decode_token(token)
                roles: list = jwt_data.get('roles', [])
                exp: int = jwt_data['exp']
                current_time: datetime = datetime.now()

                required_roles_list: list = [e.value for e in required_roles_enum]
                
                if not any(role in roles for role in required_roles_list):
                    return {'code': 403, 'message': 'Insufficient privileges'}

                if current_time > datetime.fromtimestamp(exp):
                    return {'code': 401, 'message': 'Token has expired'}

                return func(*args, **kwargs, jwt_data=jwt_data)
            except Exception as e:
                return {'code': 401, 'message': str(e)}
        return wrapper
    return decorator
