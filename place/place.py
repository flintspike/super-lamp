import tkinter as tk
from tkinter import ttk

#window properties
root = tk.Tk()
root.geometry('400x600')
root.title('Place')

label1 = tk.Label(root, text = 'Label 1', background = 'red')
label2 = tk.Label(root, text = 'Label 2', background = 'orange')
label3 = tk.Label(root, text = 'Label 3', background = 'violet')

button1 = ttk.Button(root, text = 'Button 1')

#layout

label1.place(x = 0, y = 0, width = 50, height = 50)
label3.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = 'center')

#RUN
root.mainloop()