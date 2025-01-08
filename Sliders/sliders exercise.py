import tkinter as tk
from tkinter import ttk

#variable

#window
window = tk.Tk()
window.title('progress exercise')
window.geometry('250x250')

#vertical holder
frame = tk.Frame(window)

#slider
var = tk.IntVar()
slider = ttk.Scale(
	frame,
	from_ = 100,
	to = 0,
	variable = var,
	orient = 'vertical',
	length = 200
	)
slider.pack(side = 'left')
#bar
bar = ttk.Progressbar(
	frame,
	variable = var,
	orient = 'vertical',
	length = 200
	)
bar.pack(side = 'left')
bar.start()
#label
label = tk.Label(
	window,
	textvariable = var
	)
label.pack()

frame.pack()

window.mainloop()