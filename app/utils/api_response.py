# from flask_restx import fields
from app.routes import api
from flask_restx import fields


def prepare_swagger_response(
    code: int,
    message: str,
    model_name: str = '',
    data: any = None
) -> dict:
    response: dict = {
        'code': fields.Integer(default=code),
        'message': fields.String(default=message)
    }

    if (data is not None):
        response['data'] = data

    return [code, message, api.model(model_name, response)]
