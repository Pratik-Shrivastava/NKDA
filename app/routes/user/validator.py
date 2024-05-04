from app.enum.user_role_enum import USER_ROLE
from werkzeug.datastructures import ImmutableMultiDict


def validate_login_payload(payload: dict) -> tuple[bool, str]:

    if (not payload.get('username')):
        return False, 'Username is required'

    if (not payload.get('password')):
        return False, 'Password is required'

    return True, ''


def validate_add_user_payload(payload: dict) -> tuple[bool, str]:

    if (not payload.get('username')):
        return False, 'Username is required'

    if (not payload.get('first_name')):
        return False, 'First name is required'

    if (not payload.get('last_name')):
        return False, 'Last name is required'

    if (not payload.get('password')):
        return False, 'Password is required'

    if (not payload.get('phone')):
        return False, 'Phone is required'

    if (not payload.get('email')):
        return False, 'Email is required'

    if (not payload.get('gender')):
        return False, 'Gender is required'

    if (not payload.get('active')):
        return False, 'Active is required'

    if (not payload.get('date_of_join')):
        return False, 'Date of join is required'

    if (not payload.get('roles')):
        return False, 'Roles are required'

    if not any(role in payload.get('roles') for role in USER_ROLE.get_list()):
        return False, 'Invalid roles'

    return True, ''


def validate_update_user_payload(payload: dict) -> tuple[bool, str]:

    if (not payload.get('id')):
        return False, 'id is required'

    return validate_add_user_payload(payload)


def validate_get_user_payload(args: dict) -> tuple[bool, str]:

    if (not args.get('id')):
        return False, 'id is required'

    return True, ''