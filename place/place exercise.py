import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('hello')
window.geometry('300x300')

label = tk.Label(window, background = 'tan')
label.place(relx = 0.5, rely = 0.5, relwidth = 0.5, height = 200, anchor = 'center')

window.mainloop()