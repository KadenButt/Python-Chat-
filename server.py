import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.165"
##SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
g_msg = []
g_msg_ip = []
g_recived_msg = []
connected_devices = []

def remove_seen_msg(g_msg_seen, device_connected):
    for x  in g_msg_seen[:]:
        if len(x) == device_connected:
            g_msg_seen.remove(x)
    return g_msg_seen

def send_all(ip):
    i =0
    msg_delete = []
    l_msg_ip = g_msg_ip
    ##finds messages for deletion
    for x in l_msg_ip[:]:
        ##mesages that user has sent them selfs for one they have already seen
        if x == ip or ip in g_recived_msg[i]:
            msg_delete.append(g_recived_msg[i])
        else:
            g_recived_msg[i].append(ip)
        i += 1
    ##deletes the messages
    for x in msg_delete[:]:
        l_msg_ip.remove(x)
    return(l_msg_ip)



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    ##list with all connected devices
    connected_devices.append(addr[0])
    connected = True
    while connected:
        ##header
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            ##reciving message
            msg = conn.recv(msg_length).decode(FORMAT)


            ##gloable send
            g_msg.append(msg)
            g_recived_msg.append([])
            g_msg_ip.append(addr[0])

            ##deal with send other users messagea
            print(g_msg)
            print(g_msg_ip)
            print(g_recived_msg)


            ##deals with user disconnecting
            if msg == DISCONNECT_MESSAGE:
                connected_devices.remove(addr[0])
                print(connected_devices)
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()