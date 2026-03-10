from tkinter import *
import tkinter as tk
 
root = Tk()
root.geometry("650x400")
root.title("Temperature Comfort Checker")
root.resizable(False, False)
root.configure(bg='grey')
root.attributes('-alpha', 1.00)
 
def check_name_was_entered():
    if root.name.get() == "":
        root.label.config(text="Please enter your name!")
    else:
        root.label.config(text=f"Welcome:, {root.name.get()}! Adjust the thermostat slider to check your comfort level.")
        root.check_button.config(command=check_comfort)
 
def check_comfort():
    temperature = root.thermostat_slider.get()
    if temperature < 18:
        root.label.config(text="It's too cold! Please increase the temperature.")
        root.configure(bg='snow')
        root.label.config(bg='snow')
        root.thermostat_slider.config(bg='snow')
    elif 18 <= temperature <= 24:
        root.label.config(text="The temperature is comfortable!")
        root.configure(bg='lightblue')
        root.label.config(bg='lightblue')
        root.thermostat_slider.config(bg='lightblue')
    else:
        root.label.config(text="It's too hot! Please decrease the temperature.")
        root.configure(bg='firebrick3')
        root.label.config(bg='firebrick3')
        root.thermostat_slider.config(bg='firebrick3')
 
def reset_values():
    root.name.delete(0, END)
    root.thermostat_slider.set(0)
    root.label.config(text="Welcome, please enter your name below:")
    root.configure(bg='grey')
    root.label.config(bg='grey')
    root.thermostat_slider.config(bg='grey')
 
root.label = Label(root, text="Welcome, please enter your name below:", font=("Arial", 12), bg='grey')
root.label.pack(pady=10)
 
root.name = Entry(root, width=30)
root.name.pack(pady=0)
 
root.thermostat_slider = Scale(root, from_=0, to=30, orient=HORIZONTAL, bg='grey', label="Thermostat Temperature (°C)", length=300)
root.thermostat_slider.pack(pady=20)
 
root.check_button = Button(root, text="Check Comfort", command=check_name_was_entered)
root.check_button.pack(pady=10)
 
root.reset_button = Button(root, text="Reset", command=reset_values)
root.reset_button.pack(pady=10)
 
root.mainloop()
