import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x400')
root.title('PACK')

mainframe = ttk.Frame(root)



top = ttk.Frame(mainframe)
top.pack(expand = True, fill = 'both')
red = ttk.Label(top, text = 'red', background = 'red')
red.pack(side = 'left', expand = True, fill = 'both')

bot = ttk.Frame(mainframe)
bot.pack(expand = True, fill = 'both')

botl = ttk.Frame(bot)
botl.pack(expand = True, fill = 'both', side = 'left')
blue = ttk.Label(botl, text = 'blue', background = 'blue')
blue.pack(side = 'left', expand = True, fill = 'both')

botr = ttk.Frame(bot)
botr.pack(expand = False, fill = 'both', side = 'left')


botrt = ttk.Frame(botr)
botrt.pack(expand = True, fill = 'both')
green = ttk.Label(botrt, text = 'last of the labels', background = 'green')
green.pack(expand = True, fill = 'both')

botrb = ttk.Frame(botr)
botrb.pack(expand = True, fill = 'both')
button = ttk.Button(botrb, text = 'button')
button.pack(expand = True, fill = 'both')

mainframe.pack(expand = True, fill = 'both')
root.mainloop()