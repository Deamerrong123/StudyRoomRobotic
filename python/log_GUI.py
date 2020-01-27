from tkinter import *
from tkinter import ttk, filedialog, messagebox
from time import time
from datetime import date,datetime
from Log import *
import sys


class logPage:

    Room = list()
    Room_dic = {
        '4-8 People':[342,346,348,347,446,447,448,542,546,547],
        '2-3 People':[350,351,352,353,354,355,356,357,450,451,452,453,454,455,550,551,552],
        'Technology Room':[1,2,3,4,5,6],
        }
    Type =[
         '4-8 People','2-3 People' ,'Technology Room'
    ]
    From = [
       '10:00','10:30','11:00','11:30', '12:00','12:30','13:00','13:30','14:00','14:30',
        '15:00','15:30','16:00','16:30','17:00','17:30',
        '18:00','18:30','19:00','19:30'
    ]

    T = datetime(date.today().year,\
                 date.today().month,date.today().day).timestamp()+(60*60*24)
##    T = datetime(date.today().year,\
##                 date.today().month,date.today().day+1).timestamp()
    
    Mode = [
        ('Demo','d'),
        ('Actual','a'),
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
        
        self._RatioFrame  = ttk.LabelFrame(self._user_frame,padding = '2 2 2 2')
        self._RatioFrame.grid(row = 2, column = 0)
        self._Choice = IntVar()
        R1 = ttk.Radiobutton(self._RatioFrame,text = 'Demo',variable = self._Choice,value = 0)
        R1.grid(row = 0, column = 0, sticky = (W,N))
        R2 = ttk.Radiobutton(self._RatioFrame, text = 'Actual',variable = self._Choice,value = 1)
        R2.grid(row = 0 , column = 1, stick = (W,N))
        


        ## Dropdown mune
        self._dropMenu = ttk.Frame(self._mainframe)
        self._dropMenu.grid(row = 0, column = 1)
        ## Type of Study room
        self._RoomType = ttk.Label(self._dropMenu,text = 'Type :')
        self._RoomType.grid(row = 0 , column = 0, padx = 2,sticky = (W,S,N))
        self._RoomTypeCbBox = ttk.Combobox(self._dropMenu,width = 7,\
                                           values = logPage.Type,postcommand=self._RoomList)
        self._RoomTypeCbBox.grid(row = 1, column = 0, padx = 1, sticky = (E,S,N))
        self._RoomTypeCbBox.set(logPage.Type[2])
        

        ## Specify the Room number after fixing the type.
        #logPage.Room = self._RoomList(self._RoomTypeCbBox.get())
        ## Room number

        ##self._RoomCbBox.set(logPage.Room[0])

        ## Specify the time for section one
        self._Sec1Lab = ttk.Label(self._dropMenu,text = 'Section 1 :')
        self._Sec1Lab.grid(row = 0, column = 1 , padx = 2 , sticky = (W,S,N))
        self._Sec1CbBox = ttk.Combobox(self._dropMenu,width = 7, values = logPage.From)
        self._Sec1CbBox.grid(row = 1 , column = 1,sticky = (E,S,N))
        self._Sec1CbBox.set(logPage.From[1])

##        self._Fromsplit = self._FromCbBox.get().split(':')
##        self.ToMenu = [
##            str(int(self._Fromsplit[0])+1)+':'+self._Fromsplit[1],
##            str(int(self._Fromsplit[0]) + 2) + ':' + self._Fromsplit[1],
##        ]
        self._Sec2Lab = ttk.Label(self._dropMenu,text = 'Section 2 :')
        self._Sec2Lab.grid(row = 2, column = 1 , padx = 2 , sticky = (W,S,N))
        self._Sec2CbBox = ttk.Combobox(self._dropMenu,width = 7, values = logPage.From)
        self._Sec2CbBox.grid(row = 3 , column = 1,sticky = (E,S,N))

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



        self._parent.mainloop()

    def _RoomList(self):
        logPage.Room = logPage.Room_dic[self._RoomTypeCbBox.get()]
        self._RoomLab = ttk.Label(self._dropMenu,text = 'Room :')
        self._RoomLab.grid(row = 2 , column = 0, padx = 2,sticky = (W,S,N))
        self._RoomCbBox = ttk.Combobox(self._dropMenu,width = 7,values = logPage.Room)
        self._RoomCbBox.grid(row = 3, column = 0, padx = 1, sticky = (E,S,N))
        


    def _log(self):
        if self._Choice.get():
            timeToSleep = logPage.T
        else:
            timeToSleep = 10 + time()
        self._status_msg.set('It is {} and room {}'.format(self._RoomTypeCbBox.get(),self._RoomCbBox.get()))
        print('It is {} and room {}'.format(self._RoomTypeCbBox.get(),self._RoomCbBox.get()))
        try:
            Double_log(
                self._username.get(),self._password.get(),self._RoomTypeCbBox.current(),\
                self._RoomCbBox.current(),self._Sec1CbBox.get(),self._Sec2CbBox.get(),timeToSleep
                )
            messagebox.showinfo(message = 'Account comfirmed!')
        except Exception as e:
            messagebox.showerror(message = str(e))
        finally:
            sys.exit()



