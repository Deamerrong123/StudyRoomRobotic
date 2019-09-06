import tkinter

window = tkinter.Tk()
##label = tkinter.Label(window,text = 'This is out label.')
##label.pack()
##label.config(text = 'Second label')
##

##data = tkinter.StringVar()
##data.set('Data to display')
##label = tkinter.Label(window,textvariable = data)
##label.pack()
##

##frame = tkinter.Tk()
##frame = tkinter.Frame(window)
##frame.pack()
##
##first = tkinter.Label(frame,text = 'First label')
##first.pack()
##second = tkinter.Label(frame,text = 'Second label')
##second.pack()
##third = tkinter.Label(frame,text = 'Third label')
##third.pack()
##

##frame = tkinter.Frame(window)
##frame.pack()
##frame2 = tkinter.Frame(window,borderwidth = 4 , relief = tkinter.GROOVE)
##frame2.pack()
##first = tkinter.Label(frame,text = 'First label')
##first.pack()
##second = tkinter.Label(frame2,text = 'Second label')
##second.pack()
##third = tkinter.Label(frame2,text = 'Third label')
##third.pack()
##

##frame = tkinter.Frame(window)
##frame.pack()
##var = tkinter.StringVar()
##label = tkinter.Label(frame,textvariable = var)
##label.pack()
##entry = tkinter.Entry(frame,textvariable = var)
##entry.pack()
##

#### The controller
##def click(var,value):
##    var.set(var.get()+value)
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    ## THe model.
##    counter = tkinter.IntVar()
##    counter.set(0)
##    ## The views.
##    frame = tkinter.Frame(window)
##    frame.pack()
##
##    button = tkinter.Button(frame,text = 'Down',command = lambda: click(counter,-1))
##    button.pack()
##
##    button = tkinter.Button(frame,text = 'Up' , command = lambda: click(counter,1))
##    button.pack()
##
##    label = tkinter.Label(frame,textvariable = counter)
##    label.pack()
##
##    window.mainloop()
##

#### Laying out the Widgets
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame,text = 'Name : ')
# label.pack(side = 'left')
label.grid(row = 0,column = 0)

entry = tkinter.Entry(frame)
# entry.pack(side = 'left')
entry.grid(row = 1, column =1)


    
window.mainloop()

