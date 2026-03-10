from tkinter import *
from tkinter.messagebox import *

def fun(e):
    showinfo('Student Record Save', 'Event is generated')

root = Tk()
root.title = ('My Events')
root.geometry('600x400')

# Entry 1
Label(root, text='name').pack()
e= Entry(root).pack()

# Entry 2
Label(root, text='age').pack()
e1 = Entry(root).pack()

# Entry 3
Label(root, text='course').pack()
e2 = Entry(root).pack()

# Button widget
b = Button(root, text="Save").pack(pady=10)

root.bind_all('<Control-s>', fun)

root.mainloop()
