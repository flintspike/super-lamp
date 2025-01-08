import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Pack Parenting')
root.geometry('300x400')

first = ttk.Label(text = 'First Label', background = 'red')
second = ttk.Label(text = 'Second Label', background = 'blue')
third = ttk.Label(text = 'Another label', background = 'green')

frame = ttk.Frame()

button1 = ttk.Button(frame, text = 'Button 1')
fourth = ttk.Label(frame, text = 'Last of the labels', background = 'orange')
button2 = ttk.Button(frame, text = 'Button 2')

frame2 = ttk.Frame(frame)

button3 = ttk.Button(frame2, text = 'Button 3')
button4 = ttk.Button(frame2, text = 'Button 4')
button5 = ttk.Button(frame2, text = 'Button 5')

first.pack(side = 'top', expand = True, fill = 'both')
second.pack(side = 'top', expand = True, fill = 'both')
third.pack(side = 'top', expand = True, padx = 10, pady = 10)

frame.pack(expand = True, fill = 'both', padx = 10, pady = 10)

button1.pack(side = 'left', expand = True, fill = 'both')
fourth.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')

frame2.pack(side = 'left', expand = True, fill = 'both')

button3.pack(side = 'top', expand = True, fill = 'both')
button4.pack(side = 'top', expand = True, fill = 'both')
button5.pack(side = 'top', expand = True, fill = 'both')

root.mainloop()