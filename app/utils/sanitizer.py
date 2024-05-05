import bleach


def sanitize(data: dict) -> dict:
    if data:
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = bleach.clean(value)
            elif isinstance(value, dict):
                data[key] = sanitize(value)
    return data
