import paho.mqtt.client as mqtt
from loguru import logger

def on_connect(client, userdata, flags, rc):
    logger.info(f'Connected with result code {rc}')

def on_publish(client, userdata, mid):
    logger.info(f'Published {mid}')

client = mqtt.Client()
client.on_publish = on_publish
client.on_connect = on_connect
client.connect('127.0.0.1', 1883)

while True:
    client.publish('data', input())