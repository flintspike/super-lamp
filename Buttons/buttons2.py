import tkinter as tk
from tkinter import ttk

def button1func():
	print(stringvar.get())

# window
window = tk.Tk()
window.geometry('400x300')
window.title('Buttons 2')

# button
stringvar = tk.StringVar(value = 'Chicken Butt.')
button1 = ttk.Button(window, 
	text = 'Guess what.',
	command = button1func
	)
button1.pack()

# check
checkvar = tk.StringVar(value = 'Check box is unticked.')
check = ttk.Checkbutton(window,
	text = 'Check box 1',
	command = lambda: print(checkvar.get()),
	variable = checkvar,
	onvalue = 'Check box is ticked.',
	offvalue = 'Check box is unticked.',
	)
check.pack()

# radio buttons
radiovar = tk.StringVar(value = 'Value 1')
def radiofunc():
	print(radiovar.get())
radio1 = ttk.Radiobutton(window, 
	text = 'Radio 1', 
	variable = radiovar, 
	value = 'Value 1', 
	command = radiofunc
)
radio2 = ttk.Radiobutton(window, 
	text = 'Radio 2', 
	variable = radiovar, 
	value = 'Value 2', 
	command = radiofunc
)

radio1.pack()
radio2.pack()

#run
window.mainloop()