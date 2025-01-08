import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Event binding exercise')
window.geometry('300x250')

text = ttk.Entry()
text.pack()

text.bind('<Shift-MouseWheel>', lambda event: print('mousewheel'))

window.mainloop()