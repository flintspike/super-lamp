import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('pump dish it')
window.geometry('250x50')

##############variables##############
stringvar = tk.StringVar(value = 'test')
#####################################

label = ttk.Label(textvariable = stringvar)
label.pack()

################FRAME################
entryframe = ttk.Frame()

entry = ttk.Entry(master = entryframe, textvariable = stringvar)
entry.pack(side = 'left')

button = ttk.Button(master = entryframe, text = 'Next', command = lambda: print(stringvar.get()))
button.pack(side = 'left')

entryframe.pack()
################FRAME################

window.mainloop()