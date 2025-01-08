from tkinter import Tk
from tkinter import Label
window = Tk()
window.title('You just lost')
window.geometry('250x50')
label = Label(window, text = 'The Game', font = 'Arial 30 bold')
label.pack()
window.mainloop()