import tkinter as root

##adds window
window = root.Tk()
window.title("Login Page")


##login page
##creating widgets
username_lable = root.Label(text="Username" )
username_entry = root.Entry()
password_lable = root.Label(text="Password" )
password_entry = root.Entry(show="*")
enter = root.Button(text="Enter")

##placing widgets
username_lable.grid(row=0,column=0)
username_entry.grid(row=0,column=1)
password_lable.grid(row=1,column=0)
password_entry.grid(row=1,column=1)
enter.grid(row=2,column=0)



##starts loop
root.mainloop()
