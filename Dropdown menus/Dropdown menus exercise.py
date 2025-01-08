import tkinter as tk
from tkinter import ttk

#print command
def printer(text):
	print(text)

#make window
window = tk.Tk()
window.geometry('300x450')

#make list and variable
spinlist = ('A','B','C','D','E')
textvar = tk.StringVar(value = spinlist[0])

#make spinbox
spinbox = ttk.Spinbox(window, values = spinlist, textvariable = textvar)

#print event
spinbox.bind('<<Decrement>>', lambda event: print(textvar.get()))

spinbox.pack()

#mainloop
window.mainloop()