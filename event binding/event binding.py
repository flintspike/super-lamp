import tkinter as tk
from tkinter import ttk

def get_pos(event):
	print(f'x{event.x} y{event.y}')

#window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button (text = 'button')
btn.pack()

#events

# btn.bind('<Alt-KeyPress-a>', lambda event: print('trigger'))
# window.bind('<Motion>', get_pos)
# window.bind('<KeyPress>', lambda event: print(f'{event.char} was pressed'))

entry.bind('<Shift-MouseWheel>', lambda event: print('entry box selected'))




window.mainloop()