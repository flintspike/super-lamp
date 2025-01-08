import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


#window
window = tk.Tk()

scale_int = tk.IntVar(value = 50)
scale = ttk.Scale(
	window, 
	command = lambda value: print(scale_int.get()), 
	from_ = 100, 
	to = 0,
	length = 200,
	orient = 'vertical',
	variable = scale_int)
scale.pack()

progess = ttk.Progressbar(
	window,
	variable = scale_int
	)
progess.pack()

scrolledtext = scrolledtext.ScrolledText(window)
scrolledtext.pack()

window.mainloop()