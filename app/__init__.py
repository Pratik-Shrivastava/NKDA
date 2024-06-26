from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.app_config.config import DB_URI, JWT_SECRET_KEY
from flask_jwt_extended import JWTManager


# instantiating required classes
app: Flask = Flask(__name__)

cors: CORS = CORS(app, resources={r"/*": {"origins": "*"}})

# db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db: SQLAlchemy = SQLAlchemy(app)
jwt = JWTManager(app)


from app import routes

# registering routes for each sub-folder in routes
app.register_blueprint(routes.blueprint)
app.config['RESTX_MASK_SWAGGER'] = False

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return {'code': 401, 'message': 'Missing or invalid token'}