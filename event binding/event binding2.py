import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.geometry('256x256')
window.title('Event 2')

# widgets
##text
text = tk.Text(width = 22, height = 10)
text.pack(pady = 6)

##entry
entry = ttk.Entry()
entry.pack(pady = 10)

##button
button = ttk.Button(text = 'Button')
button.pack()

# events
window.bind('<Control-KeyPress-w>', lambda event: print('Event', event))

entry.bind('<FocusIn>', lambda event: print('entry was selected'))


# main loop
window.mainloop()