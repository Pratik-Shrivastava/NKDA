from app.app_config.response_code import *
from app.app_config.response_message import *


SWAG_AUTH: dict = {
    'Authorization': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

SWAG_VERSION: str = '3.0'
SWAG_TITLE: str = 'NKDA API'
SWAG_DESCRIPTION: str = 'Powered by DC Comics Universe'
SWAG_DOC_URL: str = '/swagger-ui/'
SWAG_BASE_URL: str = '/nkda/v1'
SECURITY: list = ['Authorization']
