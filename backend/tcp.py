import socket 
import threading
import json

import service as s

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(s.ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]}:{addr[1]} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(s.HEADER).decode(s.FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(s.FORMAT)
            if msg == s.DISCONNECT_MESSAGE:
                connected = False
            else:
                print(f"[NEW MESSAGE] Message from {addr[0]}:{addr[1]}: {msg}")
                connected = s.convert_to_json(msg, conn)
                conn.send(f"Msg {msg} received".encode(s.FORMAT))

    print(f"[DISCONNECT] {addr[0]}:{addr[1]}")
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {s.SERVER}")
    while True:
        conn, addr = server.accept()
        print(type(conn))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()