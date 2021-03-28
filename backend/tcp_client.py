import socket

import service as s

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(s.ADDR)

def send(msg: str):
    message = msg.encode(s.FORMAT)
    client.send(message)
    print(client.recv(2048).decode(s.FORMAT))

send('{"lightning": 12.3, "humidity": 10.12, "temp": 12}')

send(s.DISCONNECT_MESSAGE)
