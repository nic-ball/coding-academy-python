### A cinema is creating a small ticket calculator for customers.
# Customers can:
# Enter their name
# Select their age using a slider
# Choose if they want Popcorn
# Click a button to calculate ticket price
# The program should display a message with the total price.
from tkinter import *
import tkinter as tk

win = tk.Tk()
win.geometry("300x750")
win.title("Ticket Price Calculator")
win.configure(bg="grey")

win.label = tk.Label(win, text="Hi, please enter your name: ")
win.label.pack(pady=10)

win.name = tk.Entry(win, width=20)
win.name.pack(pady=20)

win.age_scale = tk.Scale(win, from_=1, to=114, orient=HORIZONTAL, bg="grey", label="Choose Your age", length=200)
win.age_scale.pack(pady=20)

win.wants_popcorn = tk.Checkbutton(win, text="Price of Popcorn £3 - Add to Cart").pack()

b = tk.Button(win, text="Check Prices")
b.pack()


result = tk.Label

def calculate_price():
    name = name.get()
    age = age_scale.get()

    price = 10

    if age < 12:
        price = 5
        if popcorn.get()
            price += 3

win.mainloop()
