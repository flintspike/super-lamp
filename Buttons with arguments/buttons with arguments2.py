import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('buttons with arguments')
window.geometry('200x200')

textvar = tk.StringVar(value = 'hello')

entry = ttk.Entry(window,
	textvariable = textvar
	)

entry.pack()

def printer(text):
	print(text)

button = ttk.Button(window,
	text = 'printer',
	command = lambda:printer(textvar.get())
	)

button.pack()

window.mainloop()