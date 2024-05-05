from functools import wraps
from flask import request

from app.utils.sanitizer import sanitize

def sanitized():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arguments = request.args.to_dict()
            request.args = sanitize(arguments)
            try:
                payload = request.get_json()
                request.json = sanitize(payload)
            except Exception as e:
                payload = request.form.to_dict()
                request.form = sanitize(payload)

            return func(*args, **kwargs)
        return wrapper
    return decorator