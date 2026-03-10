from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

def my_handler():
    text1.insert(1.0, 'Hello World!')

# Create Tkinter Window
root = Tk()
root.title('Simple Menu Demo')

# Function to open a new window
def login_window():
    login_window = Toplevel(root)
    login_window.title('Login')
    login_window.geometry('500x300')

    try:
        size = (100, 150)
        # Load and resize image
        with Image.open('nicthedev.png') as avatar:
            avatar.thumbnail(size)
            avatar.save('nic_thumbnail.png')
            img = avatar.thumbnail(size)
            img_label = Label(login_window, image=img)
            img_label.pack(pady=20)

    except Exception as e:
        print('Error Loading Image....', e)
        Label(login_window, text='Image not found!').pack()

    # Username and Password
    Label(login_window, text='username').pack(pady=3)
    username_entry = Entry(login_window)
    username_entry.pack(pady=3)

    Label(login_window, text='password').pack(pady=3)
    password_entry = Entry(login_window)
    password_entry.pack(pady=3)

    login_button = Button(login_window, text='login', command=lambda: verify_login(username_entry, password_entry))
    login_button.pack(pady=3)

def verify_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == '1234':
        login_window.destroy()
        login_window()

    else:
        exit
        

    # lbl = Label(login_window, text='This is a NEW Window....', font=('monospace', 14))
    # lbl.pack(pady=20)

    # text2 = Text(login_window)
    # text2.pack(fill=BOTH, expand=True)
    # text2.insert(1.0, 'Text inside the new window...')

text1 = Text(root)
text1.pack(fill=BOTH, expand=True)

# Create menubar
menubar = Menu(root)

# Add file menu and commands
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=my_handler)
file_menu.add_command(label='Open', command=login_window) # Opens new window
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
