from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
import string

# FUNCTİON

def button_click():

    try:
        password_range = int(entry_label.get())
        if password_range < 1:
            messagebox.showerror("Error", "Please enter a number greater than 1")
        character_set = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(character_set) for i in range(password_range))
        result_label.config(text="Password: " + password)
    except:
        messagebox.showerror("Error", "Please enter a number")

# Uİ

window = tk.Tk()
window.title('Password Creator')
window.geometry('410x480')

# LABEL
info_label = tk.Label(window, text='How many digits is the password?', font=('Arial', 16))
info_label.pack(padx=5, pady=5)

# ENTRY

entry_label = tk.Entry(window, font=('Arial', 16), width=8)
entry_label.pack(padx=5, pady=10)

# BUTTON

my_button = tk.Button(window, text='Give Password', font=('Arial', 16), command=button_click)
my_button.pack(padx=5, pady=15)

# RESULT LABEL

result_label = Label(window, font=('Arial', 16))
result_label.pack(padx=5, pady=20)

photo = PhotoImage(file="password2.png")
canvas = tk.Canvas(window, width=200, height=200)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.pack(padx=5, pady=25)



window.mainloop()
