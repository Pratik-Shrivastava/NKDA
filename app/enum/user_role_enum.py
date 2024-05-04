from enum import Enum


class USER_ROLE(Enum):
    ADMIN: str = 'ADMIN'
    USER: str = 'USER'
    CHEIF_ENGINEER: str = 'CHEIF_ENGINEER'
    EXECUTIVE_ENGINEER: str = 'EXECUTIVE_ENGINEER'
    ASSISTANT_ENGINEER: str = 'ASSISTANT_ENGINEER'

    @staticmethod
    def get_list() -> list:
        return [e.value for e in USER_ROLE]
