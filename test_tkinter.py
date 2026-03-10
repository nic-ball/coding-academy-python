import tkinter as tk
root = tk.Tk()

#Set Window title
root.title("My First Tkinter App")
#Set window size
root.geometry("600x400+100-50")
root.resizable(False, True)
root.attributes('-alpha', 0.25)

root.mainloop()
