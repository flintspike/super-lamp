import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Stacking Widgets')
window.geometry('400x400')

#widgets
#labels
label1 = ttk.Label(window, text = 'Label1', background = 'royal blue', anchor = 'center')
label2 = ttk.Label(window, text = 'Label2', background = 'darkorchid2', anchor = 'center')
label3 = ttk.Label(window, text = 'Label3', background = 'firebrick3', anchor = 'center')

#buttons
buttonframe = ttk.Frame()
button1 = ttk.Button(buttonframe, text = 'Raise Label 1', command = lambda: label1.lift())
button2 = ttk.Button(buttonframe, text = 'Raise Label 2', command = lambda: label2.lift())
button3 = ttk.Button(buttonframe, text = 'Raise Label 3', command = lambda: label3.lift())

#layout
label1.place(x = 200-55, y = 200-55, width = 200, height = 200, anchor = 'center')
label2.place(x = 200, y = 200, width = 200, height = 200, anchor = 'center')
label3.place(x = 200+55, y = 200+55, width = 200, height = 200, anchor = 'center')
buttonframe.place(relx = 1, rely = 1, anchor = 'se')
button1.pack(side = 'left')
button2.pack(side = 'left')
button3.pack(side = 'left')


#run
window.mainloop()