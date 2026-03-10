import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Tk example")
root.configure(background="yellow")
root.minsize(200, 200)
root.geometry("300x300+50+50")

#Create 2 labels
tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text=" - Maya Angelou").pack()

#Display an image
image = Image.open(file="025.gif")
img = image.resize((150, 150))
my_img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=my_img)
label.pack()

root.mainloop()
