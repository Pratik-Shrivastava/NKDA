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
SWAG_TITLE: str = 'Data History API'
SWAG_DESCRIPTION: str = 'Powered by Dibwas Websoft Technologies LLP'
SWAG_DOC_URL: str = '/swagger-ui/'
SWAG_BASE_URL: str = '/nkda/v1'
SECURITY: list = ['Authorization']

RESPONSE = {
    SUCCESS_CODE: SUCCESS_MESSGAE,
    UN_AUTHORIZED_CODE: UNAUTHORISED_MESSGAE,
    VALIDATION_ERROR_CODE: VALIDATION_ERROR_MESSGAE,
    EXCEPTION_CODE: EXCEPTION_MESSGAE
}
