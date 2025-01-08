import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('combo and spin')

#Combobox
items = ("Ice cream", "Pizza", "Broccoli")
food = tk.StringVar(value = 'select')
combo = ttk.Combobox(window, textvariable = food)
combo['value'] = items
combo.pack()

#Combo events
combo.bind('<<ComboboxSelected>>', lambda event : combolabel.configure(text = food.get()))

#Combolabel
combolabel = ttk.Label(window, text = 'none')
combolabel.pack()

#Spinbox
spinboxlist = ('111','222','333','444','555')
spinvar = tk.StringVar(value = 'select')
spinbox = ttk.Spinbox(window, from_ = 2, to = 20, increment = 2, textvariable = spinvar)
spinbox.pack()

spinbox.bind('<<Increment>>', lambda event : spinboxlabel.configure(text = spinvar.get()))
spinbox.bind('<<Decrement>>', lambda event : spinboxlabel.configure(text = spinvar.get()))

spinboxlabel = ttk.Label(window, text = 'spin')
spinboxlabel.pack()

#run
window.mainloop()