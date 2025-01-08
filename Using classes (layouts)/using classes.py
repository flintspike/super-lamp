import tkinter as tk
from tkinter import ttk

class App(tk.Tk, ):
	def __init__(self, geometry, title, minsize):

		#MAIN SETUP
		super().__init__()
		self.geometry(f'{geometry[0]}x{geometry[1]}')
		self.title(title)
		self.minsize(minsize[0], minsize[1])

		#WIDGETS
		self.menu = Menu(self)
		self.primary = Primary(self)


		self.mainloop()
class Menu(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

		self.create_widgets()
	def create_widgets(self):
		#create widgets
		button1 = ttk.Button(self, text = 'Button1')
		button2 = ttk.Button(self, text = 'Button2')
		button3 = ttk.Button(self, text = 'Button3')

		slider1 = ttk.Scale(self, orient = 'vertical')
		slider2 = ttk.Scale(self, orient = 'vertical')

		toggle_frame = ttk.Frame(self)
		menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'Check 1')
		menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'Check 2')

		entry = ttk.Entry(self)

		#menu layout
		self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
		self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

		button1.grid(row = 0, column = 0, columns = 2, sticky = 'nswe')
		button2.grid(row = 0, column = 2, sticky = 'nswe')
		button3.grid(row = 1, column = 0, columns = 3, sticky = 'nswe')

		slider1.grid(row = 2, column = 0, rows = 2, sticky = 'nswe')
		slider2.grid(row = 2, column = 2, rows = 2, sticky = 'nswe')

		#toggle layout
		toggle_frame.grid(row = 4, column = 0, columns = 3, sticky = 'nswe')
		menu_toggle1.pack(side = 'left', expand = True)
		menu_toggle2.pack(side = 'left', expand = True)

		#entry layout
		entry.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')
class Primary(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
		self.one = Entry_Frame(self, buttontext = 'one', labeltext = 'one', labelcolor = 'slateblue3')
		self.two = Entry_Frame(self, buttontext = 'two', labeltext = 'two', labelcolor = 'purple3')
		self.three = Entry_Frame(self, buttontext = 'three', labeltext = 'three', labelcolor = 'darkorchid1')
class Entry_Frame(ttk.Frame):
	def __init__(self, parent, buttontext, labeltext, labelcolor):
		super().__init__(parent)

		main_label = ttk.Label(self, text = labeltext, background = labelcolor, anchor = 'center')
		main_button = ttk.Button(self, text = buttontext)

		main_label.pack(expand = True, fill = 'both', padx = 5)
		main_button.pack(expand = True, fill = 'both', pady = 10)

		self.pack(side = 'left', expand = True, fill = 'both', padx = 3, pady = 3)

App(geometry = (400,400), title = 'App', minsize = (200,200))