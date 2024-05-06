from datetime import datetime
from app import db

class Product(db.Model):
    '''
    ORM class for Product
    '''
    __tablename__ = 'product'

    product_id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    product_name = db.Column(
        db.String(255),
        nullable=False
    )

    product_description = db.Column(
        db.Text
    )

    product_price = db.Column(
        db.Float,
        nullable=False
    )
    
    created_at = db.Column(
        db.DATETIME,
        default=datetime.now
    )

    created_by = db.Column(
        db.String(255),
        nullable = False
    )

    updated_at = db.Column(
        db.DATETIME,
        onupdate=datetime.now
    )

    updated_by = db.Column(
        db.String(255),
        nullable = False
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
