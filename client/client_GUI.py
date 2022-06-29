import tkinter as root
from functions import *
userinfo = "logindetails"


##adds window
window = root.Tk()
window.title("Login Page")

login_info = Read_To_Txt(userinfo)
main_menu = False

def chat_screen():
    pass

def EnterButton():
    window.quit()
    main_menu = Login_Checker(username_entry, password_entry, login_info, )
    print(main_menu)

##login page
##creating widgets
username_lable = root.Label(text="Username" )
username_entry = root.Entry()
password_lable = root.Label(text="Password" )
password_entry = root.Entry()
enter = root.Button(text="Enter", command=EnterButton)

##placing widgets
username_lable.grid(row=0,column=0)
username_entry.grid(row=0,column=1)
password_lable.grid(row=1,column=0)
password_entry.grid(row=1,column=1)
enter.grid(row=2,column=0)
root.mainloop()



##starts loop



