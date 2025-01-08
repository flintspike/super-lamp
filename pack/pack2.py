import tkinter as tk
from tkinter import ttk

#window
root = tk.Tk()
root.title('Pack 2')
root.geometry('300x450')

#widgets
label1 = ttk.Label(root, text = 'Label 1', background = 'red')
label2 = ttk.Label(root, text = 'Label 2', background = 'blue')
label3 = ttk.Label(root, text = 'Label 3', background = 'green')
button = ttk.Button(root, text = 'Button')

label1.pack(side = 'top', expand = True, fill = 'both', pady = 5, padx = 5)
label2.pack(side = 'left', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')

#run
root.mainloop()