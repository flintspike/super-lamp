import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('256x256')
window.title('Menus II')

# menu
menu = tk.Menu()
window.configure(menu = menu)

def File_func():
	print('File')
File = tk.Menu(menu, tearoff = False)
File.add_command(label = 'New', command = lambda : print('New'))
File.add_command(label = 'Open', command = lambda : print('Open'))
File.add_separator()
File.add_command(label = 'Save', command = lambda : print('Save'))
File.add_command(label = 'Save as...', command = lambda : print('Save as'))
menu.add_cascade(label = 'File', menu = File, )

def Edit_func():
	print('Edit')
Edit = tk.Menu(menu, tearoff = False)
Edit.add_command(label = 'Edit Function', command = Edit_func)
menu.add_cascade(label = 'Edit', menu = Edit, )

def Preferences_func():
	print('Preferences')
Preferences = tk.Menu(menu, tearoff = False)
Preferences.add_command(label = 'Preferences Function', command = Preferences_func)

darkmode = tk.StringVar(value = 'off')
Preferences.add_checkbutton(
	label = 'Dark Mode', 
	onvalue = 'on', 
	offvalue = 'off', 
	variable = darkmode, 
	command = lambda: print(darkmode.get())
	)
Preferences.add_command(
	label = 'Dark Checker',
	command = lambda: print('Dark mode is '+str(darkmode.get())+'.')
	)
menu.add_cascade(label = 'Preferences', menu = Preferences, )

def Help_func():
	print('Help')
Help = tk.Menu(menu, tearoff = False)
Help.add_command(label = 'Help Function', command = Help_func)
menu.add_cascade(label = 'Help', menu = Help, )

About = tk.Menu(Help, tearoff = False)
About.add_command(label = 'Made by: Sascha Ellis')
Help.add_cascade(label = 'About', menu =About)

window.mainloop()