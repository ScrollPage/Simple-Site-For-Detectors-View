import django

from asgiref.sync import sync_to_async

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from data.models import Data

@sync_to_async
def split_json_and_create_data(data):
    Data.objects.create(**data)