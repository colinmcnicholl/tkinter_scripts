import tkinter as tk
from random import randint


def roll_dice():
    value = randint(1, 6)
    lbl_value['text'] = f'{value}'


window = tk.Tk()

window.columnconfigure(0, minsize=50, weight=1)
window.rowconfigure([0, 1], minsize=50, weight=1)

btn_roll = tk.Button(master=window, text='Roll', command=roll_dice)
btn_roll.grid(row=0, column = 0, sticky='nsew')

lbl_value = tk.Label(master=window, text='')
lbl_value.grid(row=1, column=0)

window.mainloop()