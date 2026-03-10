import tkinter as tk
from tkinter import messagebox

# Function to show message box
def show_message():
    messagebox.showinfo("Hello", "Hi Nic, hope everything is good today")

# Create the main window
root = tk.Tk()
root.title("Messagebox example")

# Create a button to trigger the message box
button = tk.Button(root, text="Click ME!", command=show_message)
button.pack(pady=20)

# Run App
root.mainloop()
