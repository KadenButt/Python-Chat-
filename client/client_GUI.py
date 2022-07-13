from tkinter import *
from functions import *
import socket
import multiprocessing

root = Tk()
root.title("Test chat")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
        self.hello(master)
        self.myButton = Button(master, text="Click me", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you")

    def hello(self, master):
        print("hello")
        master.after(0,lambda: self.hello(master,))

e = Elder(root)
root.mainloop()