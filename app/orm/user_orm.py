from datetime import datetime
from app import db


class User(db.Model):
    '''
    ORM class for NKDA User
    '''
    __tablename__ = 'nkda_user'

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    date_of_join = db.Column(db.BigInteger, nullable=False)
    
    created_at = db.Column(db.DATETIME, default=datetime.now)
    updated_at = db.Column(db.DATETIME, onupdate=datetime.now)

    user_roles = db.relationship('UserRole', backref=db.backref('user_role'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
