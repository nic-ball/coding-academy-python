from tkinter import *
from tkinter.messagebox import *

def fun(e):
    showinfo('My Box', 'Event is generated')

root = Tk()
root.title('My Events')
root.geometry('600x400')

e = Entry(root, bg='red', fg='black')
e.place(x=100, y=100, width=200, height=50)
e.bind('<KeyPress>', fun)

# Can use <Button>, <Enter> and many more to bind the functions

root.mainloop()
