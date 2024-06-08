import tkinter as tk
import time
from tkinter import PhotoImage


def update():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)

    current_date = time.strftime("%B %d, %Y")
    date_label.config(text=current_date)

    current_day = time.strftime("%A")
    day_label.config(text=current_day)

    # Making a recursive call every 1000ms
    root.after(1000, update)


# Setting up the root   -->
root = tk.Tk()
icon = PhotoImage(file="ClockIcon.png")
root.iconphoto(False, icon)
root.title("Clock")
root.geometry("300x200")
root.resizable(False, False)
root.configure(bg="black")


# Labels setup   -->
time_label = tk.Label(root, font=("Angkor", 40), fg="red", bg="black")
time_label.pack()

date_label = tk.Label(root, font=("Bahnschrift", 20), fg="white", bg="black")
date_label.pack()

day_label = tk.Label(root, font=("Bahnschrift", 20), fg="white", bg="black")
day_label.pack()


# Updating the app  -->
update()
root.mainloop()
