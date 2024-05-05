from typing import List
from app import orm as ORM
from app import db


def get_user_by_username_and_password(username: str, password: str) -> ORM.User | None:
    return ORM.User.query.filter_by(username=username, password=password).first()


def add_user(user: dict) -> int | None:
    try:
        existing_user: ORM.User | None = ORM.User.query.\
            filter_by(username=user.get('username')).first()
        
        if existing_user:
            raise Exception('username already exists')

        user_model = ORM.User(
            username=user.get('username'),
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            password=user.get('password'), #TODO: hash password
            phone=user.get('phone'),
            email=user.get('email'),    #TODO: encrypt email
            gender=user.get('gender'),
            active=user.get('active'),
            date_of_join=user.get('date_of_join')
        )

        db.session.add(user_model)
        db.session.flush([user_model])

        for role in user.get('roles'):
            db.session.add(
                ORM.UserRole(
                    user_id=user_model.id,
                    name=role
                )
            )

        db.session.commit()
        return user_model.id

    except Exception as e:
        db.session.rollback()
        raise e
    

def get_user_by_id(id: int) -> ORM.User | None:
    return ORM.User.query.filter_by(id=id).first()


def get_user_list() -> List[ORM.User] | list:
    return ORM.User.query.all()


def update_user(user: dict) -> bool:
    try:
        user_info = get_user_by_id(user.get('id'))

        if user_info is None:
            return False

        user_info.first_name = user.get('first_name')
        user_info.last_name = user.get('last_name')
        user_info.password = user.get('password') #TODO: hash password
        user_info.phone = user.get('phone')
        user_info.gender = user.get('gender')
        user_info.active = user.get('active')
        user_info.date_of_join = user.get('date_of_join')

        db.session.commit()
        return True

    except Exception as e:
        db.session.rollback()
        raise e