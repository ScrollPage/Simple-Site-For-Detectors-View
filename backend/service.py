import django
import json
import socket


from asgiref.sync import sync_to_async

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from data.models import Data

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def create_data(data, connected=True):
    try:
        instance = Data.objects.create(**data)
    except TypeError as err:
        print(f'[ERROR] {err}')
        connected = False
    except django.db.IntegrityError as err:
        print(f'[ERROR] {err}')
        connected = False
    else:
        print(f'[SUCCESS] Instance {instance} created')
    finally:
        return connected

def convert_to_json(msg, conn, connected=True):
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