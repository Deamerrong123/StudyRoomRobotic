from tkinter import *
from tkinter import ttk, filedialog, messagebox
# from Log import *
from Log import Loger


class logPage:
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'
    Room = [
        'Room 1', 'Room 2','Room 3','Room 4','Room 5','Room 6'
    ]
    From = [
        12,13,14,15,16,17,18,19
    ]
    To = [

    ]

    def __init__(self):
        self._parent = Tk()
        self._mainframe = ttk.Frame(self._parent,padding = '5 5 5 5')
        ## mainframe
        self._mainframe.grid(row = 0 , column = 0 , sticky = (E,W,N,S))

        ## userfield
        self._user_frame = ttk.Frame(self._mainframe, padding = '5 5 5 5')
        self._user_frame.grid(row = 0 , column = 0)
        self._username_field = ttk.LabelFrame(self._user_frame,
                                          text = 'Username', padding = '5 5 5 5')
        self._username_field.grid(row = 0 , column = 0,
                                  sticky = (E,W,N,S))
        self._username = StringVar()

        self._username_Entry = ttk.Entry(self._username_field,width = 20 ,
                                     textvariable = self._username)
        self._username_Entry.grid(row = 0 , column = 0, sticky = (W,E))

        self._password = StringVar()
        self._password_field = ttk.LabelFrame(self._user_frame, text = 'Password',padding = '5 5 5 5')
        self._password_field.grid(row = 1, column = 0, sticky = (W,E))
        self._password_Entry = ttk.Entry(self._password_field,width = 20,
                                         textvariable = self._password)
        self._password_Entry.grid(row = 0 , column = 0 , sticky = (W,E))


        ## Dropdown mune
        self._dropMenu = ttk.Frame(self._mainframe).grid(row = 0, column = 1 , padx = 5)
        self._RoomSele = ttk.Label(self._dropMenu,text = 'Room :').grid(row = 0 , column = 0, padx = 2)
        self._CbBox = ttk.Combobox(self._dropMenu,width = 15,values = self.Room).grid(row = 0, column = 1, padx = 1)

        ## login button
        self._log_btn = ttk.Button(
            self._mainframe,text = 'Login!', command = self._log
        )
        self._log_btn.grid(row = 2,column = 1,sticky = E , padx = 5 , pady = 3)

        ## State Frame
        self._status_frame = ttk.Frame(
            self._parent, relief='sunken', padding='5 5 5 5'
        )
        self._status_frame.grid(row=1, column=0, sticky=(E, W, S))
        self._status_msg = StringVar()
        self._status_msg.set('Type Username and Password ... ')
        self._status = ttk.Label(
            self._status_frame, textvariable=self._status_msg, anchor=W)
        self._status.grid(row=0, column=0, sticky=(E, W))



        ## mainWin mainloop
        self._parent.mainloop()



    def _log(self):
        ## determine the username and passward is correct,
        ## and it has the authority to assess
        messagebox.showinfo(message = 'logging ... ')
        loger = Loger(logPage.URL,self._getUsername(),self._getPassword())
        loger.log()



    def _getUsername(self):
        return self._username.get()

    def _getPassword(self):
        return self._password.get()








#
# if __name__ == '__main__':
#     root = Tk()
#     logPage(root)
#     root.mainloop()

