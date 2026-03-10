from tkinter import *
from tkinter.messagebox import *

def fun(e):
    showinfo('My Box', 'Event is generated')

def fun1(e):
    showinfo('My box', e)

root = Tk()
root.title('My Events')
root.geometry('600x400')

e = Entry(root, bg='grey', fg='black')
e.place(x=100, y=100, width=200, height=50)

e.bind('<Button-1>', fun)
e.bind('<KeyPress>', fun1, add='+')

root.mainloop()
