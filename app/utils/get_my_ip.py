from flask import Request


def get_my_ip(request: Request) -> str:
    ip_address: str = request.environ.get('HTTP_X_FORWARDED_FOR')
    if ip_address is None:
        ip_address = request.environ['REMOTE_ADDR']
    return ip_address