from django.conf import settings

import os
import sys
import asyncio
from asyncio.exceptions import IncompleteReadError
import json
import time
from loguru import logger

from hbmqtt.broker import Broker
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0

from service import split_json_and_create_data

# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <lvl>{message}</lvl>")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

broker = Broker(settings.MQTT_CONFIG)

async def start_broker():
    logger.info('Started!')
    await broker.start()

# async def broker_get_message():
#     client = MQTTClient()
#     # await client.connect('mqtt://127.0.0.1:1883/')
#     # await client.subscribe([('data', QOS_0)])
#     logger.info('Started!')
#     try: 
#         for i in range(1, 100):
#             message = await client.deliver_message()
#             packet = message.publish_packet
#             payload = str(packet.payload.data.decode('utf-8'))
#             logger.info(f'Got message {payload}')
#     except ClientException as ce:
#         logger.error(f'Client exception {ce}')
#     except IncompleteReadError:
#         pass


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_broker())
    # asyncio.get_event_loop().run_until_complete(broker_get_message())
    asyncio.get_event_loop().run_forever()
