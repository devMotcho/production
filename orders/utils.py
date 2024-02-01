import uuid, base64


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code