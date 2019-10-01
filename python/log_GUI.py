from tkinter import *
from tkinter import ttk, filedialog, messagebox
from time import sleep,time
from datetime import date,datetime
# from Log import *
from Log import Loger


class logPage:
    
    Room = [
        'Room 1', 'Room 2','Room 3','Room 4','Room 5','Room 6'
    ]
    From = [
        '12:00','12:30','13:00','13:30','14:00','14:30',
        '15:00','15:30','16:00','16:30','17:00','17:30',
        '18:00','18:30','19:00','19:30'
    ]

    T = datetime(date.today().year,\
                 date.today().month,date.today().day).timestamp()+(60*60*24)


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
        self._username.set('Username')

        self._username_Entry = ttk.Entry(self._username_field,width = 20 ,
                                     textvariable = self._username)
        self._username_Entry.grid(row = 0 , column = 0, sticky = (W,E))

        self._password = StringVar()
        self._password.set('Password')
        self._password_field = ttk.LabelFrame(self._user_frame, text = 'Password',padding = '5 5 5 5')
        self._password_field.grid(row = 1, column = 0, sticky = (W,E))
        self._password_Entry = ttk.Entry(self._password_field,width = 20,
                                         textvariable = self._password)
        self._password_Entry.grid(row = 0 , column = 0 , sticky = (W,E))


        ## Dropdown mune
        self._dropMenu = ttk.Frame(self._mainframe)
        self._dropMenu.grid(row = 0, column = 1)
        self._RoomLab = ttk.Label(self._dropMenu,text = 'Room :')
        self._RoomLab.grid(row = 0 , column = 0, padx = 2,sticky = (W,S,N))
        self._RoomCbBox = ttk.Combobox(self._dropMenu,width = 7,values = self.Room)
        self._RoomCbBox.grid(row = 1, column = 0, padx = 1, sticky = (E,S,N))
        self._RoomCbBox.set(logPage.Room[4])
        self._FromLab = ttk.Label(self._dropMenu,text = 'From :')
        self._FromLab.grid(row = 2, column = 0 , padx = 2 , sticky = (W,S,N))
        self._FromCbBox = ttk.Combobox(self._dropMenu,width = 7, values = logPage.From)
        self._FromCbBox.grid(row = 3 , column = 0,sticky = (E,S,N))
        self._FromCbBox.set(logPage.From[1])

        self._Fromsplit = self._FromCbBox.get().split(':')
        self.ToMenu = [
            str(int(self._Fromsplit[0])+1)+':'+self._Fromsplit[1],
            str(int(self._Fromsplit[0]) + 2) + ':' + self._Fromsplit[1],
        ]
        self._ToLab = ttk.Label(self._dropMenu,text = 'To :')
        self._ToLab.grid(row = 4, column = 0 , padx = 2 , sticky = (W,S,N))
        self._ToCbBox = ttk.Combobox(self._dropMenu,width = 7, values = self.ToMenu)
        self._ToCbBox.grid(row = 5 , column = 0,sticky = (E,S,N))

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
        loger = Loger()
        self._dt = logPage.T - time()
        self._status_msg.set('It is about to act in {} second'.format(self._dt))
        #sleep(self._dt)
        sleep(5)
        try:
            
            
            sleep(.500)
            loger.ReserseRoom(self._RoomCbBox.get(),self._FromCbBox.get())
            messagebox.showinfo(message = 'Account comfirmed!')
        except Exception as e:
            messagebox.showerror(message = str(e))
        finally:
            pass



