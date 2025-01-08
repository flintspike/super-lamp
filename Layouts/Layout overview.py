import tkinter as tk
from tkinter import ttk

#window properties
root = tk.Tk()
root.title('Layout overview')
root.geometry('600x400+-400+-1000')

#widgets
label1 = ttk.Label(root, text = 'Label 1 (pack)', background = 'red')
label2 = ttk.Label(root, text = 'Label 2 (pack)', background = 'green')
label3 = ttk.Label(root, text = 'Label 3 (grid)', background = 'blue')
label4 = ttk.Label(root, text = 'Label 4 (place)', background = 'white')
label5 = ttk.Label(root, text = 'Label 5 (rel place)', background = 'pink')

# pack
label1.pack(side = 'right', expand = True, fill = 'both')
label2.pack(side = 'right')

# # grid
# root.columnconfigure(0, weight = 1)
# root.columnconfigure(1, weight = 1)
# root.columnconfigure(2, weight = 1)
# root.columnconfigure(3, weight = 1)
# root.columnconfigure(4, weight = 2)
# root.rowconfigure(0,weight = 2)
# root.rowconfigure(1,weight = 1)
# root.rowconfigure(2,weight = 1)
# label3.grid(row = 1, column = 3, sticky = 'nsew')

#place (in pixels)
label4.place(x = 90, y = 50, width = 200, height = 50)

label5.place(relx = 0.5, rely = 0.1)

#run
root.mainloop()











