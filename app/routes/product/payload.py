from flask_restx import fields
from app.enum.user_role_enum import USER_ROLE
from app.routes import api

def add_product_payload() -> list:

    payload = api.model('addProduct Payload', {
        'product_name': fields.String,
        'product_description': fields.String,
        'product_price': fields.Float,
        'created_by': fields.String
    })
    
    return [payload]


def update_product_payload() -> list:

    payload = api.model('updateProduct Payload' , {
        'product_id':fields.Integer,
        'product_name': fields.String,
        'product_description': fields.String,
        'product_price': fields.Float,
        'updated_by': fields.String    
    })

    return [payload]

def get_product_payload() -> list:

    parser = api.parser()
    parser.add_argument('id', type=int, location='args')

    return [parser]


def delete_product_payload() -> list:

    parser = api.parser()
    parser.add_argument('id', type=int, location='args')

    return [parser]
    

