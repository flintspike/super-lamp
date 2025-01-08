import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Taaaabs')
window.geometry('600x400')

notebook = ttk.Notebook(window)

#tab 1
tab1 = ttk.Frame(notebook, width = 580, height = 370)
tab1.pack_propagate(0)
textvar = tk.StringVar(value = 'this is tab 1')
label1 = ttk.Label(tab1, text = 'this button does nothing', textvariable = textvar)
label1.pack()
button1 = ttk.Button(tab1, text = 'button1')
button1.pack()

#tab2
tab2 = ttk.Frame(notebook, width = 580, height = 370)
tab2.pack_propagate(0)
label2 = ttk.Label(tab2, text = 'this is tab 2')
label2.pack()
button2 = ttk.Button(tab2, text = 'button2')
button2.pack()

#tab3
tab3 = ttk.Frame(window)
tab3.pack_propagate(0)
t3f = ttk.Frame(tab3)
t3l = ttk.Label(tab3, text = 'this is tab 3')
t3b1 = ttk.Button(t3f, text = 't3b1', command = lambda : textvar.set('t3b1 was pressed'))
t3b2 = ttk.Button(t3f, text = 't3b2', command = lambda : textvar.set('t3b2 was pressed'))
t3b1.pack(side = 'left')
t3b2.pack(side = 'left')
t3f.pack()
tab3.pack()

notebook.add(tab1, text = 'tab1')
notebook.add(tab2, text = 'tab2')
notebook.add(tab3, text = 'tab3')

notebook.pack()

window.mainloop()