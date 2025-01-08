import tkinter as tk
from tkinter import ttk

#make window:

window = tk.Tk()
window.geometry('230x150')
window.title('cheese')

#radiobuttons

radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window, text = 'A', value = 'A', variable = radio_var, command = lambda : print(check_var.get()))
radio2 = ttk.Radiobutton(window, text = 'B', value = 'B', variable = radio_var, command = lambda : print(check_var.get()))

#checkbutton and checkbutton title

check_var = tk.BooleanVar()

checktitle = ttk.Label(window, text = 'Check button:')
check = ttk.Checkbutton(window, text = 'Checkers', variable = check_var, command = lambda : print(radio_var.get()))


#run
radio1.pack()
radio2.pack()
checktitle.pack()
check.pack()

window.mainloop()