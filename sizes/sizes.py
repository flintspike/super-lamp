import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Sizes')
window.geometry('300x300')

Label1 = ttk.Label(window, text = 'label', background = 'mediumorchid1',  anchor = 'center')
Label2 = ttk.Label(window, text = 'label', background = 'firebrick1',  anchor = 'center')
Label3 = ttk.Label(window, text = 'label', background = 'green2',  anchor = 'center')
Label4 = ttk.Label(window, text = 'label', background = 'deepskyblue',  anchor = 'center')

# #pack
# Label1.pack(fill = 'both', expand = 'True')
# Label2.pack(fill = 'both', expand = 'True')

window.columnconfigure((0,1), weight = 1, uniform = 'a')
window.rowconfigure((0,1), weight = 1, uniform = 'a')

Label1.grid(row = 0, column = 1, sticky = 'nswe', padx = 3, pady = 3)
Label2.grid(row = 1, column = 0, sticky = 'nswe', padx = 3, pady = 3)
Label3.grid(row = 1, column = 1, sticky = 'nswe', padx = 3, pady = 3)
Label4.grid(row = 0, column = 0, sticky = 'nswe', padx = 3, pady = 3)


window.mainloop()