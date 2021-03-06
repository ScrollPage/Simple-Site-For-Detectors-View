import paho.mqtt.client as mqtt
from loguru import logger
import asyncio

from service import SERVER, PORT


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

client.connect(SERVER, PORT, 60)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client.loop_forever())
    asyncio.get_event_loop().run_forever()
