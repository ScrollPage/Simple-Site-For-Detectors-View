import django
import socket
import json

from asgiref.sync import sync_to_async

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from data.models import Data

@sync_to_async
def split_json_and_create_data(data):
    data['detector'] = get_object_or_404(Detector, id=data.pop('id'))
    DetectorData.objects.create(**data)

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def create_data(data: dict, connected: bool=True) -> bool:
    try:
        instance = Data.objects.create(**data)
    except (django.db.IntegrityError, TypeError) as err:
        print(f'[ERROR] {err}')
        connected = False
    else:
        print(f'[SUCCESS] Instance {instance} created')
    finally:
        return connected

def convert_to_json(msg: str, conn: socket.socket, connected: bool=True) -> bool:
    try:
        data = json.loads(msg)
    except json.JSONDecodeError:
        connected = False
        conn.send("Bad msg format".encode(FORMAT))
        print(f'[ERROR] Could not convert message: {msg} to a JSON')  
        data = {}
    else:
        connected = create_data(data)
    finally:
        return connected