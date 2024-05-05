from app import db
from app.orm import *


def create_entry_log(
    user_id: int,
    username: str,
    endpoint: str,
    method: str,
    request_payload: dict,
    query_params: dict
) -> None:
    
    try:
        entry_log = EntryLog(
            user_id=user_id,
            username=username,
            endpoint=endpoint,
            method=method,
            request_payload=request_payload,
            query_params=query_params
        )
        db.session.add(entry_log)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
