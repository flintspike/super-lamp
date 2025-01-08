import tkinter as tk
from tkinter import ttk

def buttfunc():
	print(entry.get())
	label['text'] = entry.get()
	button.configure(state = 'disabled')
	entry.configure(state = 'disabled')
	button2.configure(state = 'enabled')

def reset():
	label.configure(text = 'some text')
	entry.configure(state = 'enabled')
	button.configure(state = 'enabled')
	button2.configure(state = 'disabled')

#make the window
window = tk.Tk()
window.title('Settings and Getting Data')
window.geometry('800x600')

#label
label = ttk.Label(text = 'here is the label')
label.pack()
#entry
entry = ttk.Entry()
entry.pack()

#frame
buttonholder = ttk.Frame()

#button
button = ttk.Button(master = buttonholder, text = 'button', command = buttfunc)
button.pack(side = 'left')
#button 2
button2 = ttk.Button(master = buttonholder, text = 'reset', command = reset, state = 'disabled')
button2.pack(side = 'left')

buttonholder.pack()

#run
window.mainloop()