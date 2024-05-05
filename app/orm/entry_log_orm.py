import time
from app import db


class EntryLog(db.Model):
    '''
    ORM class for Entry Log
    '''
    __tablename__ = 'entry_log'

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

    username = db.Column(
        db.String(80),
        db.ForeignKey('nkda_user.username', ondelete='CASCADE'),
        nullable=False
    )

    endpoint = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    request_payload = db.Column(db.JSON)
    query_params = db.Column(db.JSON)
    created_at = db.Column(db.BigInteger, default=int(time.time() * 1000))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}