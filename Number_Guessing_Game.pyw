from tkinter import *
from random import randint
from tkinter import messagebox
from tkinter import Menu
import tkinter as tk

window = Tk()
window.title("Python GUI Guessing Game")
window.geometry('400x100+450+300')
window.resizable(0, 0)
tries = 0

def number_choice(event):
    ("callback when the player has entered a number.")
    number_choice = int(response.get())
    response.delete(0, tk.END)
    proposal["text"] = number_choice
    if secret_number > number_choice:
        result["text"] = ("The number is bigger")
    elif secret_number < number_choice:
        result["text"] = ("The number is smaller")
    else:
        lbl_response.destroy()
        response.destroy()
        proposal.grid_forget()
        proposal.grid(row=1, column=0)
        result.grid_forget()
        result.grid(row=1, column=1)
        result.config(text= "Well done. You found the number!", font=("", 12), fg="green")

def score():
    response.focus_set()
    tries += 1
    triesLabel.config(text = "Tries: " + str(tries))

root = tk.Tk()
root.geometry('580x100+350+450')
root.resizable(0, 0)
title = tk.Label(root, text="Guess the Number", font=("", 16), fg=("brown"))
title.grid(row=0, columnspan=2, pady=8)

secret_number = randint(0, 100) + 1

lbl = Label(window, text="Welcome!", font=("Calibri", 20))
lbl.grid(column=0, row=0)

lbl = Label(window, text="Enter Username:", font=("Arial Bold", 12))
lbl.grid(column=0, row=1)
text = Entry(window, width=15)
text.grid(column=2, row=1)
lbl_response = tk.Label(root, text="WELCOME " + text.get() + "!" + ". Choose a number between 1 and 100:")
lbl_response.grid(row=2, column=0, pady=5, padx=5)
   
def clicked():
    lbl_response = tk.Label(root, text="WELCOME " + text.get() + "!" + ". Choose a number between 1 and 100:")
    lbl_response.grid(row=2, column=0, pady=5, padx=5)
    
btn = Button(window, text="Click here", command=clicked)
btn.grid(column=3, row=1)

response = tk.Entry(root)
response.grid(row=1, column=1, pady=5, padx=5)
response.bind("<Return>", number_choice)
response.focus_set()

proposal = tk.Label(root, text="")
proposal.grid(row=2, column=0, pady=5, padx=5)

result = tk.Label(root, text="")
result.grid(row=2, column=1, pady=5, padx=5)

root.mainloop()
window.mainloop()


