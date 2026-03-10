from tkinter import *
root = Tk()
Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
Entry(root).grid(row=0, column=1)
Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
Entry(root).grid(row=1, column=1)
Button(root, text="Login").grid(row=2, column=0, columnspan=2)
root.mainloop()
