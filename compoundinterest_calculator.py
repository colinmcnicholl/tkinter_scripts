from tkinter import *
from tkinter import ttk


compound_periods_values = ('Daily (365/yr)', 'Daily (360/Yr)',
                           'Weekly (52/Yr)', 'Bi-Weekly (26/Yr)',
                           'Semi-Monthly (24/Yr)', 'Monthly (12/Yr)',
                           'Bi-Monthly (6/Yr)', 'Quarterly (4/Yr)',
                           'Semi-Annually (2/Yr)', 'Annually (1/Yr)')
compound_periods_n = (365, 360, 52, 26, 24, 12, 6, 4, 2, 1)

def calculate(*args):
    compound_period_n = periods.get()
    ndx = compound_periods_values.index(compound_period_n)
    n = compound_periods_n[ndx]
    try:
        P = float(principal.get())
        R = float(rate.get())
        t = float(time.get())
        A = round((P * (1 + ((R / 100) / n))**(n * t)), 2)
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
compound_periods = StringVar(value=compound_periods_values)
time = StringVar()
accrued_amount = StringVar()

principal_entry = ttk.Entry(mainframe, width=10, textvariable=principal)
principal_entry.grid(column=1, row=2, sticky=(W, E))
rate_entry = ttk.Entry(mainframe, width=10, textvariable=rate)
rate_entry.grid(column=1, row=3, sticky=(W, E))
time_entry = ttk.Entry(mainframe, width=10, textvariable=time)
time_entry.grid(column=1, row=5)

ttk.Label(mainframe, text='Calculate:').grid(column=0, row=0, sticky = E)
ttk.Label(mainframe, text='Where: A = P(1 + r/n)**nt').grid(column=0, row=1, sticky=(W, E))
ttk.Label(mainframe, text='Principal (P): £').grid(column=0, row=2, sticky = E)
ttk.Label(mainframe, text='Rate (R): %').grid(column=0, row=3, sticky = E)
ttk.Label(mainframe, text='Compound (n):').grid(column=0, row=4, sticky = E)
ttk.Label(mainframe, text='Time (t in years):').grid(column=0, row=5, sticky = E)

calculations = ttk.Combobox(mainframe)
calculations['values'] = ('Total P + I(A)', 'Principal (P)', 'Rate (R)', 'Time (T)')
calculations.grid(column=1, row=0)
periods = ttk.Combobox(mainframe)
periods['values'] = compound_periods_values
periods.grid(column=1, row=4)

ttk.Button(mainframe, text='Clear').grid(column=0, row=6, sticky=W)
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=1, row=6, sticky=E)

ttk.Label(mainframe, text='Answer: £').grid(column=0, row=7, sticky = E)
ttk.Label(mainframe, textvariable=accrued_amount).grid(column=1, row=7, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

principal_entry.focus()

root.bind('<Return>', calculate) 

root.mainloop()
