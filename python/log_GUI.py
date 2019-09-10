from tkinter import *
from tkinter import ttk, filedialog, messagebox

class logPage:
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

        ## radiofield
        self._Radioframe = ttk.Labelframe(self._mainframe, text = 'Option')
        self._Radioframe.grid(row = 0 , column = 1, sticky = (N,S,W,E))
        self._choice_lbl = ttk.Label(
            self._Radioframe, text="Pick your Option"
        )
        self._choice_lbl.grid(row=0, column=0, padx=5, pady=3, sticky = W)
        self._Opt_ = StringVar()
        self._Op1 = ttk.Radiobutton(
            self._Radioframe,text = 'Room 4,\nfrom 15:30 - 17:30',variable = self._Opt_,
            value = 'Op1'
        )
        self._Op1.grid(row = 1, column = 0, pady = 1)
        self._Op2 = ttk.Radiobutton(
            self._Radioframe,text = 'Room 4,\nfrom 17:30 - 19:30' ,
            variable = self._Opt_, value = 'Op2'
        )
        self._Op2.grid(row = 2 , column = 0 , sticky = E,pady = 1)
        self._Op3 = ttk.Radiobutton(
            self._Radioframe, text = 'Room 4,\n from 12:30 - 14:30',
            variable = self._Opt_ , value = 'Op3'
        )
        self._Op3.grid(row = 3 , column = 0, sticky = E , pady = 1 )

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

    def _getUsername(self):
        return self._username

    def _getPassword(self):
        return self._password








#
# if __name__ == '__main__':
#     root = Tk()
#     logPage(root)
#     root.mainloop()

