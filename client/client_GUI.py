from tkinter import *
from functions import *
import socket
from threading import Thread

root = Tk()
root.title("Chat Screen")
root.geometry("1000x800")

HEADER = 64
PORT = 5050
SERVER = "192.168.1.165"
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

READY_TO_RECIVE = False
chat_list = []


class Main_Screen:
    def __init__(self, master):
        screen = Label(master, bg="black", fg="green", text="", anchor=SW)
        msg_input = Entry(master)
        send_message = Button(master, text="Send",command=lambda: self.send_msg(msg_input,))

        screen.place(x=0, y=0, width=1000, height=750)
        msg_input.place(x=0, y=750, width=950, height=50)
        send_message.place(x=950, y=750, width=50, height=50)
        t1 = Thread(target=self.display_receviced_msg, args=(master,screen))
        t1.start()

    def send_msg(self, input_widget):
        msg = input_widget.get()
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        input_widget.delete(0, END)

    def display_receviced_msg(self, master, screen):
        chat_list.append(client.recv(20480).decode(FORMAT)+ "\n")
        if len(chat_list) > 42:
                chat_list.pop(1)
        screen.config(text=" ".join(chat_list))
        master.after(2000,lambda: self.test(master,screen))

    def test(self,master,screen):
        t1 = Thread(target=self.display_receviced_msg, args=(master,screen))
        t1.start()


e = Main_Screen(root)
root.mainloop()