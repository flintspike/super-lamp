import tkinter as tk
from tkinter import ttk

#window setup

window = tk.Tk()
window.title('buttons')
window.geometry('220x160')

#make button
def butt_func():#unsed, replaced by lambda
	print('*click*') #

texty = tk.StringVar(value = 'Click here') #creates a variable with a default assignment of 'click here'

button1 = ttk.Button(window, command = lambda: print('*click*'), textvariable = texty)
button1.pack()

#check buttons
check1_var = tk.IntVar(value = 0)

check1 = ttk.Checkbutton(window, 
	text = 'checkbox 1', 
	command = lambda: print(check1_var.get()),
	variable = check1_var,
	)
check1.pack()

#radio buttons

radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window,
 text = 'bump it',
 value = 'bump',
 variable = radio_var,
 command = lambda: print(radio_var.get()),
 )
radio1.pack()

radio2 = ttk.Radiobutton(window,
 text = 'jump it',
 value = 'jump',
 variable = radio_var,
 command = lambda: print(radio_var.get()),
 )
radio2.pack()

#second radio buttons

button_set2 = ttk.Frame(window)

radio_var2 = tk.StringVar()

radio_set2_label = ttk.Label(button_set2, text = 'set 2')
radio_set2_label.pack()

radio3 = ttk.Radiobutton(button_set2, text = 'bump it',
 value = 'dump',
 variable = radio_var2,
 command = lambda : print(radio_var2.get()),
 )
radio3.pack()

radio4 = ttk.Radiobutton(button_set2, text = 'jump it',
 value = 'pump',
 variable = radio_var2,
 command = lambda : print(radio_var2.get()),
 )
radio4.pack()

button_set2.pack()

#run
window.mainloop()