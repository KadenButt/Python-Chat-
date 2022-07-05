from tkinter import *
from functions import *
import socket
import threading



HEADER = 64
PORT = 5050
SERVER = "192.168.1.165"
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

READY_TO_RECIVE = False


userinfo = "logindetails"


##get the passwords and usersnames
login_info = Read_To_Txt(userinfo)
main_menu = False

def recivce():
    print()

def send(message_box):
    msg = message_box.get()
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER -len(send_length))
    client.send(send_length)
    client.send(message)
    message_box.delete(0, END)

def display_reviced_text(screen):
    chat_list = []
    while True:
        chat_list.append(client.recv(20480).decode(FORMAT)+ "\n")
        if len(chat_list)>42:
            chat_list.pop(1)
        screen.config(text=" ".join(chat_list))


# main page
def chat_screen():
    chat_screen = Tk()
    chat_screen.title("Chat Screen")
    chat_screen.geometry("1000x800")



    screen = Label(chat_screen,bg="black", fg="green",text="Hello there",anchor=SW)
    msg_input = Entry(chat_screen)
    send_message = Button(chat_screen, text="Send",command=lambda: send(msg_input,))

    screen.place(x=0, y=0, width=1000, height=750)
    msg_input.place(x=0, y=750, width=950, height=50)
    send_message.place(x=950, y=750, width=50, height=50)

    thread1 = threading.Thread(target=display_reviced_text, args=(screen,))
    thread1.start()

    chat_screen.mainloop()


# delets login page and opens main page
def enter_button():
    if Login_Checker(username_entry, password_entry, login_info, ):
        root.destroy()
        chat_screen()

    password_entry.delete(0, END)

##adds window
root = Tk()
root.title("Login Page")

# login page
#creating widgets
username_lable = Label(root, text="Username")
username_entry = Entry(root)
password_lable = Label(root, text="Password")
password_entry = Entry(root, show="*")
enter = Button(root, text="Enter", command=enter_button)

##placing widgets
username_lable.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_lable.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
enter.grid(row=2, column=0)
root.mainloop()

#starts loop
chat_screen()