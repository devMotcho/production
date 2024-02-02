import uuid, base64

#my imports
from human.models import Client, Profile


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code

def get_client_from_id(val):
    client = Client.objects.get(id=val)
    return client

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman