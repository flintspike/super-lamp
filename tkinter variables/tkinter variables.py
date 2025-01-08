import tkinter as tk
from tkinter import ttk

def button_func():
	print(string_var.get())
	string_var.set('( ͡° ͜ʖ ͡°)')

#make window
window = tk.Tk()
window.title('( ͡° ͜ʖ ͡°)')
window.geometry('210x100')

#tkinter variable

string_var = tk.StringVar()

#make objects
display = ttk.Label(master = window, text = '( ͡° ͜ʖ ͡°)', textvariable = string_var)
display.pack(pady = 5)

entry = ttk.Entry(master = window, text = '( ͡° ͜ʖ ͡°)', textvariable = string_var)
entry.pack(pady = 5)

send_button = ttk.Button(master = window, text = '( ͡° ͜ʖ ͡°)', command = button_func)
send_button.pack(pady = 5)

#run window

window.mainloop()