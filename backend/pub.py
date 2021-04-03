import paho.mqtt.client as mqtt
from loguru import logger
from service import SERVER, PORT

def on_connect(client, userdata, flags, rc):
    logger.info(f'Connected with result code {rc}')

def on_publish(client, userdata, mid):
    logger.info(f'Published {mid}')

client = mqtt.Client()
client.on_publish = on_publish
client.on_connect = on_connect
client.connect(SERVER, PORT, 60)

while True:
    client.publish('data', input())