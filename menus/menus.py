import tkinter as tk
from tkinter import ttk

#window properites
window = tk.Tk()
window.title('Menus R Us')
window.geometry('600x400')
window.pack_propagate(0)

#Menus
menu = tk.Menu(window, tearoff = False)

#sub menu
file = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = 'File', menu = file)

# save = tk.Menu(file)
def save(): print('saved')
def open_(): print('open')
def new(): print('new')
file.add_command(label = 'Save', command = save)
file.add_command(label = 'New', command = new)
file.add_command(label = 'Open', command = open_)

#help menu
def help_func(): print('made by sas')
help_ = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = 'Help', menu = help_)
help_.add_command(label = 'about', command = help_func)

window.configure(menu = menu)

#run
window.mainloop()