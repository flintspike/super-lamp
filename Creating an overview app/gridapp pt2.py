import fs
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('grid maker extreme')
window.geometry('400x300')

#text
title_label = ttk.Label(master = window, text = 'grid maker extreme', font = ("system", "36", "bold"))
title_label.pack()

#input
input_frame_x = ttk.Frame(master = window)
entry_x = ttk.Entry(master = input_frame_x)
button_x = ttk.Button(master = input_frame_x, text = 'Convert')

entry_x.pack(side = 'left')
button_x.pack(side = 'right')
input_frame_x.pack(pady = 20)

input_frame_y = ttk.Frame(master = window)
entry_y = ttk.Entry(master = input_frame_y)
button_y = ttk.Button(master = input_frame_y, text = 'Convert')

entry_y.pack(side = 'left')
button_y.pack(side = 'right')
input_frame_y.pack()

output_label = ttk.Label(master = window, text = 'Output')
output_label.pack()


window.mainloop()