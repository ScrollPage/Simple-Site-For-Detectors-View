import paho.mqtt.client as mqtt
from loguru import logger

import time
import sys

# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <lvl>{message}</lvl>")

def on_connect(client, userdata, flags, rc):
    logger.info(f'Connected with result code {rc}')
    topic = 'data'
    client.subscribe("data", qos=0)
    logger.info(f'Subscribed to a topic {topic}')

def on_disconnect(client, userdata, rc):
    if rc != 0:
        logger.error('Unexpected MQTT disconnection. Will auto-reconnect')
        client.reconnect()

def on_message(client, userdata, msg):
    logger.info(f"New message: {msg.payload.decode('utf-8')}, topic: {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
# client.on_log = on_log

client.connect("127.0.0.1", 1883, 60)

while True:
    client.loop_forever()
