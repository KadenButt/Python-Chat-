from tkinter import *
from functions import *
import socket
import multiprocessing

root = Tk()
root.title("Chat Screen")
root.geometry("1000x800")

chat_list = []


class Elder:
    def __init__(self, master):
        screen = Label(master, bg="black", fg="green", text="", anchor=SW)
        msg_input = Entry(master)
        send_message = Button(master, text="Send")

        screen.place(x=0, y=0, width=1000, height=750)
        msg_input.place(x=0, y=750, width=950, height=50)
        send_message.place(x=950, y=750, width=50, height=50)

        self.hello(master,screen)

    def hello(self, master, screen):
        chat_list.append("test")
        if len(chat_list) > 42:
                chat_list.pop(1)
        screen.config(text=" ".join(chat_list))
        master.after(500,lambda: self.hello(master,screen))

e = Elder(root)
root.mainloop()