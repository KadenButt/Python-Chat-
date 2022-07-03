from tkinter import *
from functions import *


userinfo = "logindetails"

##adds window
root = Tk()
root.title("Login Page")
##get the passwords and usersnames
login_info = Read_To_Txt(userinfo)
main_menu = False


# main page
def chat_screen():
    chat_screen = Tk()
    chat_screen.title("Chat Screen")
    chat_screen.mainloop()


# delets login page and opens main page
def enter_button():

    if Login_Checker(username_entry, password_entry, login_info, ):
        root.destroy()
        chat_screen()

    password_entry.delete(0, END)


# login page
# creating widgets
username_lable = Label(root, text="Username")
username_entry = Entry(root)
password_lable = Label(root, text="Password")
password_entry = Entry(root)
enter = Button(root, text="Enter", command=enter_button)

##placing widgets
username_lable.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_lable.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
enter.grid(row=2, column=0)
root.mainloop()

##starts loop
