import tkinter as tk
from tkinter import ttk
import time
import threading

from Xlib.protocol.rq import TextElements16

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x800")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, ChatPage):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Waiting For Connection!!!", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        t1 = threading.Thread(target=self.connection, args=(controller,))
        t1.start()

    def connection(self, controller):
        time.sleep(1)
        controller.show_frame(ChatPage)
        print("change")





# second window frame page1
class ChatPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        screen = ttk.Label(self, background="black", foreground="green", text="")
        msg_input = ttk.Entry(self)
        send_message = ttk.Button(self, text="send", )

        screen.place(x=0, y=0, width=1000, height=750)
        msg_input.place(x=0, y=750, width=950, height=50)
        send_message.place(x=950, y=750, width=50, height=50)



# Driver Code
app = tkinterApp()
app.mainloop()
