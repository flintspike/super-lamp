import tkinter as tk
from tkinter import ttk

def printer():
	print('The button was pressed')

## create a window##

# main window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master = window, text = 'this is a test')
label.pack()

## create widgets ##

# text box
text = tk.Text(master = window)
text.pack()

# line text entry
entry = tk.Entry(master = window)
entry.pack()

# button
button = ttk.Button(master = window, text = 'A button', command = printer)
button.pack()

# run
window.mainloop()
print('hello')