from tkinter import *
import socket

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
        ##displays screen widgets
        screen = Label(master, bg="black", fg="green", text="", anchor=SW)
        msg_input = Entry(master)
        send_message = Button(master, text="Send",command=lambda: self.input_button_press(msg_input,))

        screen.place(x=0, y=0, width=1000, height=750)
        msg_input.place(x=0, y=750, width=950, height=50)
        send_message.place(x=950, y=750, width=50, height=50)
        self.display_receviced_msg(master,screen)

    def input_button_press(self, input_widget):
        msg = input_widget.get()
        self.send_msg(msg)
        input_widget.delete(0, END)


##sends msg to server
    def send_msg(self, msg):
        msg += "\n"
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

##dispays msg from server to label called "screen"
    def display_receviced_msg(self, master, screen):
        self.send_msg("[INCOMEING MESSAGE]")
        chat_list.append(client.recv(20480).decode(FORMAT)+ "\n")
        if len(chat_list) > 42:
                chat_list.pop(1)
        screen.config(text=" ".join(chat_list))
        ##calls function start_threading after 2 seeconds
        master.after(2000,lambda: self.display_receviced_msg(master,screen))




e = Main_Screen(root)
root.mainloop()