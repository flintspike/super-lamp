import tkinter as tk
from tkinter import ttk

def butt_func(entry_string):
	print('button was pressed')
	print(entry_var.get())

#### make window ####
window = tk.Tk()
window.title('buttons with arguments')
window.geometry('300x200')

####widgets####
###top border###
top_border = ttk.Frame()
top_border.pack(pady = 10)
###entry###
##entry var
entry_var = tk.StringVar(value = 'text')
entry = ttk.Entry(window, textvariable = entry_var)
entry.pack(pady = 5)
###button###
button = ttk.Button(window, text = 'GO', command = lambda: butt_func(entry_var))
button.pack()




window.mainloop()