import tkinter as tk
from tkinter import ttk

#window details
window  = tk.Tk()
window.title('Grid')
window.geometry('600x400')

#Widgets Shelf
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
label4 = ttk.Label(window, text = 'Label 4', background = 'tan')

button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')

entry = ttk.Entry(window)

#Grid properties

window.columnconfigure((0,1,2), weight = 1, uniform = 'a')
window.columnconfigure(3, weight = 3, uniform = 'a')

window.rowconfigure((0,1,2), weight = 1)
window.rowconfigure(3, weight = 3)

#placing widgets
label1.grid( column = 0, row = 0, sticky = 'nswe')
label2.grid( column = 1, row = 1, columns = 2, sticky = 'nswe')
label3.grid( column = 2, row = 2, sticky = 'nswe')
label4.grid( column = 3, row = 3, sticky = 'nswe')

button1.grid(column = 2, row = 1, rows = 2 , sticky = 'nsew', pady = 10, padx = 10)

button2.grid(row = 3, column = 3, sticky = 'se', padx = 2, pady = 2)

#run
window.mainloop()