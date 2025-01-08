import tkinter as tk
from tkinter import ttk

#main window
root = tk.Tk()

#get screen center before starting
halfw = root.winfo_screenwidth()/2
halfh = root.winfo_screenheight()/2
windoww = 300
windowh = 300
startw = int(halfw - windoww/2)
starth = int(halfh - windowh/2)

#set window start
root.title('Working with Windows')
root.geometry(f'{windoww}x{windowh}+{startw}+{starth}')
root.iconbitmap('yaboi.ico')

#attributes
root.attributes('-alpha', 0.7)
root.attributes('-topmost', False)


#size properties
root.minsize(250,250)
root.maxsize(800,600)
root.resizable(True,True)
root.overrideredirect(False)
grip = ttk.Sizegrip(root)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

#security even
root.bind('<Y>', lambda event : root.quit())

#primary container
window = ttk.Frame(root)
window.pack(fill = 'both')

#screen properties
print(window.winfo_screenwidth())

root.mainloop()

