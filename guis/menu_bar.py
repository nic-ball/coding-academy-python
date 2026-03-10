from tkinter import *
from tkinter.ttk import *

def my_handler():
    text1.insert(1.0, 'Hello World!')

# Create Tkinter Window
root = Tk()
root.title('Simple Menu Demo')

# Function to open a new window
def open_new_window():
    new_window = Toplevel(root)
    new_window.title('New Window')
    new_window.geometry('500x300')

    lbl = Label(new_window, text='This is a NEW Window....', font=('monospace', 14))
    lbl.pack(pady=20)

    text2 = Text(new_window)
    text2.pack(fill=BOTH, expand=True)
    text2.insert(1.0, 'Text inside the new window...')

text1 = Text(root)
text1.pack(fill=BOTH, expand=True)

# Create menubar
menubar = Menu(root)

# Add file menu and commands
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=my_handler)
file_menu.add_command(label='Open', command=open_new_window) # Opens new window
file_menu.add_command(label='Save', command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Add Options menu
options_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_radiobutton(label='Option 1')
options_menu.add_checkbutton(label='Option 2')
options_menu.add_checkbutton(label='Option 3')

# Add a Help Menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=None)

# Display Menu
root.config(menu=menubar)

root.mainloop()
