from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        P = float(principal.get())
        R = float(rate.get())
        n = float(compound_periods.get())
        t = float(time.get())
        A = P * (1 + ((R / 100) / n))**(n * t)
        accrued_amount.set(A)
    except ValueError:
        pass
        
root = Tk()
root.title('Coumpound Interest Calculator')

mainframe = ttk.Frame(root, padding='3 3 12 12')        # create the frame widget and 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # place it in the main window
root.columnconfigure(0, weight=1)                       # if the main window is resized
root.rowconfigure(0, weight=10)                         # the frame should expand to take up the extra space

principal = StringVar()
rate = StringVar()
compound_periods = StringVar()
time = StringVar()
accrued_amount = StringVar()

principal_entry = ttk.Entry(mainframe, width=10, textvariable=principal)
principal_entry.grid(column=1, row=2, sticky=(W, E))
rate_entry = ttk.Entry(mainframe, width=10, textvariable=rate)
rate_entry.grid(column=1, row=3, sticky=(W, E))
time_entry = ttk.Entry(mainframe, width=10, textvariable=time)
time_entry.grid(column=1, row=5)

ttk.Label(mainframe, text='Calculate:').grid(column=0, row=0, sticky=(W, E))
ttk.Label(mainframe, text='Where: A = P(1 + r/n)**nt').grid(column=0, row=1, sticky=(W, E))
ttk.Label(mainframe, text='Principal (P): £').grid(column=0, row=2, sticky=(W, E))
ttk.Label(mainframe, text='Rate (R): %').grid(column=0, row=3, sticky=(W, E))
ttk.Label(mainframe, text='Compound (n):').grid(column=0, row=4, sticky=(W, E))
ttk.Label(mainframe, text='Time (t in years):').grid(column=0, row=5, sticky=(W, E))

calculations = ttk.Combobox(mainframe)
calculations['values'] = ('Total P + I(A)', 'Principal (P)', 'Rate (R)', 'Time (T)')
calculations.grid(column=1, row=0)
periods = ttk.Combobox(mainframe)
periods['values'] = ('Continuously', 'Daily (365/yr)', 'Daily (360/Yr)', 'Weekly (52/Yr)', 'Bi-Weekly (26/Yr)', 'Semi-Monthly (24/Yr)', 'Monthly (12/Yr)', 'Bi-Monthly (6/Yr)', 'Quarterly (4/Yr)', 'Semi-Annually (2/Yr)', 'Annually (1/Yr)')
periods.grid(column=1, row=4)

ttk.Button(mainframe, text='Clear').grid(column=0, row=6, sticky=W)
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=1, row=6, sticky=E)

text = Text(mainframe, width=40, height=10)
text.grid(column=0, row=7, columnspan=2)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

principal_entry.focus()

root.bind('<Return>', calculate) 

root.mainloop()
