from tkinter import *
from tkinter import ttk, filedialog, messagebox

class logPage:
    _username = StringVar()
    _password = StringVar()

    def __init__(self,parent):
        self._parent = parent
        self._mainframe = ttk.Frame(self._parent,padding = '5 5 5 5')
        ## mainframe
        self._mainframe.grid(row = 0 , column = 0 , sticky = (E,W,N,S))

        ## userfield
        self._username_field = ttk.LabelFrame(self._mainframe,
                                          text = 'Username', padding = '5 5 5 5')
        self._username_field.grid(row = 0 , column = 0,
                                  sticky = (E,W,N,S))

        self._user_Entry = ttk.Entry(self._username_field,width = 20 ,
                                     textvariable = logPage._username)
        self._user_Entry.grid(row = 0 , column = 0, sticky = (W,E))

        self._password_field = ttk.LabelFrame(self._mainframe,text = 'Password'
                                          ,padding = '5 5 5 5')
        self._password_field.grid(row = 1, column = 0,sticky = (W,E))
        self._password_Entry = ttk.Entry(self._password_field,width = 20,
                                         textvariable = logPage._password)
        self._password_Entry.grid(row = 0 , column = 0 , sticky = (W,E))






if __name__ == '__main__':
    root = Tk()
    logPage(root)
    root.mainloop()

