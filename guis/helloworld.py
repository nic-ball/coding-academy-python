import tkinter as tk

win = tk.Tk()
win.geometry('900x600+600-70')
win.title('hello world')
win.attributes('-alpha', 0.25)
tk.Entry(win).pack()
def change_text():
    label.config(text="Clicked Enter!" )
    print("clicked")
label = tk.Label(win, text="Hello World")
label.pack()
b = tk.Button(win, text="Enter", command=change_text)
b.pack()
c = tk.Radiobutton(win, text="agree")
c.pack()

win.mainloop()
