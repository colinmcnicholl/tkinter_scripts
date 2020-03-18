from tkinter import *       # tkinter is the standard binding to Tk
from tkinter import ttk     # ttk is Python's binding to the newer "themed widgets" added to Tk in 8.5


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass
        
root = Tk()                                             # set up the main window
root.title('Feet to Meters')                            # give it a title

mainframe = ttk.Frame(root, padding='3 3 12 12')        # create the frame widget and 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # place it in the main window
root.columnconfigure(0, weight=1)                       # if the main window is resized
root.rowconfigure(0, weight=10)                         # the frame should expand to take up the extra space

feet = StringVar()      # global variable "feet". Option "textvariable" when creating entry is specified as "feet".  Anytime the entry changes, Tk will automatically update the global variable "feet".
meters = StringVar()    # global variable "meters".  Option "textvariable" when creating Label is specified as "meters".

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)                               # create as instances of Tk's themed widget classes 1st of 3 main widgets, entry widget where we type number of feet
feet_entry.grid(column=2, row=1, stick=(W, E))                                              # place the entry widget, anchor it to both left and right side of cell.

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))              # create 2nd of 3 main widgets, the label where we put the resulting number of meters
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=3, sticky=W)  # create 3rd of 3 main widgets, the calculate button that we press to perform the calculation

ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky=W)                           # create and place static text label
ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text='meters').grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)               # walk through each of the widgets that are children of our content frame
                                                                                            # add a little padding around each.
feet_entry.focus()                      # cursor starts in the entry field, so user doesn't have to click in it before starting to type.
root.bind('<Return>', calculate)        # if the user presses the Return key (Enter on Windows) anywhere within the root window, call our calculate routine,
                                        # the same as if the user pressed the Calculate button.

root.mainloop()
