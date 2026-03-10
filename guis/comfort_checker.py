from tkinter import *

win = Tk()
win.geometry("650x400")
win.title("Comfort Checker")
win.configure(bg="grey")
win.attributes('-alpha', 0.25)

bg = PhotoImage(file="home.png")
bg_label = Label(win, image = bg)
bg_label.place(x = 0, y = 0, relwidth=1, relheight=1)

def was_name_entered():
    if win.name.get() == "":
        win.label.config(text="Please enter your name: ")
    else:
        win.label.config(text=f"Hello, {win.name.get()}! Move the slider to set the temperature")
        win.check_button.config(command=check_comfort)

def check_comfort():
    temp = win.thermostat_slider.get()
    if temp < 18:
        win.label.config(text="It is Freezing, you need to increase the heat")
        win.configure(bg="snow")
        win.label.config(bg="snow")
        win.thermostat_slider.config(bg="snow")
    elif 18 <= temp <= 24:
        win.label.config(text="The temperature is comfortable")
        win.configure(bg="yellow")
        win.label.config(bg="yellow")
        win.thermostat_slider.config(bg="yellow")
    else:
        win.label.config(text="It's too hot! Turn down the heat")
        win.configure(bg="red")
        win.label.config(bg="red")
        win.thermostat_slider.config(bg="red")

def reset_values():
    win.name.delete(0, END)
    win.thermostat_slider.set(0)
    win.label.config(text="Hi, please enter your name: " )
    win.configure(bg="grey")
    win.label.config(bg="grey")
    win.thermostat_slider(bg="grey")

win.label = Label(win, text="HI, please enter your name: ")
win.label.pack(pady=10)

win.name = Entry(win, width=30)
win.name.pack(pady=20)

win.thermostat_slider = Scale(win, from_=0, to=30, orient=HORIZONTAL, bg="grey", label="Thermostat Temp (°C)", length=300)
win.thermostat_slider.pack(pady=20)

win.check_button = Button(win, text="Check Comfort", command=was_name_entered)
win.check_button.pack(pady=10)

win.reset_button = Button(win, text="reset", command=reset_values)
win.reset_button.pack(pady=10)

win.mainloop()
