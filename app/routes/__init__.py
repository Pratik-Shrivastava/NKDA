from flask_restx import Api
import importlib
import werkzeug
import flask
import os

from app.app_config.swagger_config import *

werkzeug.cached_property = werkzeug.utils.cached_property

blueprint: flask.Blueprint = flask.Blueprint(
    name='api',
    import_name=__name__,
    url_prefix=SWAG_BASE_URL
)

api: Api = Api(
    app=blueprint,
    version=SWAG_VERSION,
    title=SWAG_TITLE,
    description=SWAG_DESCRIPTION,
    authorizations=SWAG_AUTH,
    doc=SWAG_DOC_URL
)

# from app.routes.user import sub_routes
current_dir: str = os.path.dirname(__file__)
for subdir in os.listdir(current_dir):
    if os.path.isdir(os.path.join(current_dir, subdir)) and not subdir.startswith('__'):
        module_name: str = f'app.routes.{subdir}.routes'
        module = importlib.import_module(module_name)
