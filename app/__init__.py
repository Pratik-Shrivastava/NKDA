from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from jwt import PyJWTError
from app.app_config.config import DB_URI, JWT_SECRET_KEY
from flask_jwt_extended import JWTManager

# importing routes
from app import routes

# instantiating required classes
app: Flask = Flask(__name__)

cors: CORS = CORS(app, resources={r"/*": {"origins": "*"}})

# db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db: SQLAlchemy = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(routes.blueprint)
app.config['RESTX_MASK_SWAGGER'] = False

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({'code': 401, 'message': 'Missing or invalid token'}), 401