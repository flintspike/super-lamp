import tkinter as tk
import ttkbootstrap as ttk

def convert():
	c = inputtext.get()
	f = c*(9/5) + 32
	outputstring.set(str(f))

# poopass window ########################
window1 = ttk.Window(themename = 'darkly')
window1.title('C2F')
window1.geometry('400x300')

# title
titlelabel = tk.Label(
	master = window1, 
	text = 'C2F', 
	font = 'Arial 32'
	)
titlelabel.pack()

# text box and button
textandbutton = ttk.Frame(master = window1)
inputtext = tk.IntVar()
inputbox = tk.Entry(
	master = textandbutton,
	textvariable = inputtext)
button = tk.Button(
	master = textandbutton, 
	text = 'convert', 
	command = convert
	)

inputbox.pack(side = 'left', padx = 15)
button.pack(side = 'left')
textandbutton.pack(pady = 15)

#output

outputstring = tk.StringVar()
output = ttk.Label(
	master = window1, 
	text = 'Output', 
	font = 'Times 28', 
	textvariable = outputstring
	)
output.pack()

#run window1
window1.mainloop()