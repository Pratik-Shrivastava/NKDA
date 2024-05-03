from app import db
from app.orm import BaseModel


class User(BaseModel):
    '''
    ORM class for User
    '''
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    username = db.Column(db.String(80), unique=True, nullable=False)
    fist_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    date_of_join = db.Column(db.Date, nullable=False)
    
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())
