from tkinter import *
from tkinter.messagebox import *

def fun(e):
    showinfo('My Box', 'Event is generated')

root = Tk()
root.title = ('My Events')
root.geometry('600x400')

e= Entry(root, bg='black', fg='grey')
e.place(x=100, y=100, width=200, height=50)

e1 = Entry(root, bg='black', fg='grey')
e1.place(x=100, y=100, width=200, height=50)

root.bind_class('Entry', '<Button-1>', fun)

root.mainloop()
