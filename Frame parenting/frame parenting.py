import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x400')
window.title('Frames and parenting')

#label frame
labelframe = ttk.Frame(window)

label1frame = ttk.Frame(labelframe)
label2frame = ttk.Frame(labelframe)

label2 = ttk.Label(labelframe, text = 'frame1')
label2.pack(side = 'left')

label3= ttk.Label(labelframe, text = 'frame2')
label3.pack(side = 'right')

labelframe.pack(side = 'top')
#frame


frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)

label = ttk.Label(frame, text = 'label in frame')
label.pack(side = 'top')

button = ttk.Button(frame, text = 'button')
button.pack(side= 'left')
button2 = ttk.Button(frame, text = 'button2')
button2.pack(side ='right')


#frame2
frame2 = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame2.pack_propagate(False)
textlabel = ttk.Label(frame2, text = 'frame 2 text label')
textlabel.pack()
entry = tk.Text(frame2, height = 8)
entry.pack()
entry.insert(tk.END, 'hello')
f2button = ttk.Button(frame2, text = 'button2')
f2button.pack(side = 'bottom')


frame.pack(side = 'left')
frame2.pack(side = 'right')

#mainloop
window.mainloop()