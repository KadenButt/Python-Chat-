import socket
import threading


HEADER = 64
PORT = 5050
##SERVER = "127.0.1.1"
SERVER = "192.168.1.165"
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

READY_TO_RECIVE = False

def recivce():
    print(client.recv(20480).decode(FORMAT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER -len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    message = input("user: ")

    thread1 = threading.Thread(target=send, args=(message,))
    thread1.start()

    thread2 = threading.Thread(target=recivce())
    thread2.start()

    if message == "EXIT":
        send(DISCONNET_MESSAGE)
        exit("[CONNECTION STATUS] disconnected")