import tkinter as tk
from tkinter import ttk

def button_off_func():

	#update label
	input_ = entry.get()
	label['text'] = input_
	entry['state'] = 'disabled'
	button_off['state'] = 'disabled'
	button_on['state'] = 'enabled'

def button_on_func():
	label['text'] = 'This is some text'
	entry['state'] = 'enabled'
	button_on['state'] = 'disabled'
	button_off['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Get Set Radio')
window.geometry('250x100')

label = ttk.Label(master = window, text = 'This is some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button_frame = tk.Frame()

button_off = ttk.Button(master = button_frame, text = 'one butten', command = button_off_func)
button_off.pack(side = 'left')

button_on = ttk.Button(master = button_frame, text = 'reset', command = button_on_func, state = 'disabled')
button_on.pack(side = 'left')

button_frame.pack()

#run
window.mainloop()