from app import db


class UserRole(db.Model):
    '''
    ORM class for User Role
    '''
    __tablename__ = 'user_role'

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey('nkda_user.id', ondelete='CASCADE'),
        nullable=False
    )
    name = db.Column(db.String(80), nullable=False)

    created_at = db.Column(db.BigInteger, default=db.func.now())
    updated_at = db.Column(db.BigInteger, onupdate=db.func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
