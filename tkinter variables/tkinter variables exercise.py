import fs
import tkinter as tk
from tkinter import ttk

# make window
window = tk.Tk()
window.geometry('250x100')

# make string var
variable = tk.StringVar()
variable.set('test')

# make 2 entry fields
entry1 = ttk.Entry(master = window, textvariable = variable)
entry2 = ttk.Entry(master = window, textvariable = variable)

# make one label
label = tk.Label(master = window, textvariable = variable)

# run
entry1.pack()
entry2.pack()
label.pack()

window.mainloop()