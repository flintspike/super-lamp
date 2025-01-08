import tkinter as tk
from tkinter import ttk

def create_segment(parent, labeltext, buttontext):
	frame = ttk.Frame(parent)
	frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
	frame.rowconfigure(0, weight = 1, uniform = 'a')

	label = ttk.Label(frame, text = labeltext, anchor = 'center', )
	button = ttk.Button(frame, text = buttontext)

	label.grid(row = 0, column = 0, sticky='nswe', padx = 5, pady = 5)
	button.grid(row = 0, column = 1, sticky='nswe', padx = 5, pady = 5)
	return frame

class Segment(ttk.Frame):
	def create_segment(self,parent, buttontext, labeltext, labelcolor):
		frame = ttk.Frame(parent)
		label = ttk.Label(frame, text = buttontext, background = labelcolor, anchor = 'center')
		button = ttk.Button(frame, text = buttontext)

		label.pack(side = 'top', expand = True, fill = 'both', anchor = 'center')
		button.pack(side = 'top', expand = True, fill = 'both', pady = 5)

		return frame

	def __init__(self, parent, labeltext, buttontext, color):
		super().__init__(parent)

		#grid layout
		self.rowconfigure(0, weight = 1, uniform = 'a')
		self.columnconfigure((0,1,2), weight = 1, uniform = 'a')

		#internal items label and button
		ttk.Label(self, text = labeltext, anchor = 'center').grid(row = 0, column = 0, sticky = 'nwse', padx = 5, pady = 5)
		ttk.Button(self, text = buttontext).grid(row = 0, column = 1, sticky = 'nwse', padx = 5, pady = 5)

		self.create_segment(self, 'one2', 'two2', labelcolor = color).grid(row = 0, column = 2, pady = 5, padx = 5, sticky = 'nwse')

		self.pack(expand = True, fill = 'both')

#WINDOW
window = tk.Tk()
window.geometry('400x600')
window.title('Custom Widgets')

#widgets

Segment(window, 'one', 'one', 'maroon')
Segment(window, 'two', 'two', 'goldenrod')
Segment(window, 'three', 'three', 'chartreuse')
Segment(window, 'four', 'four', 'red3')
Segment(window, 'five', 'five', 'slateblue')
# create_segment(window, labeltext = 'six', buttontext = 'six').pack(expand = True, fill = 'both')

window.mainloop()