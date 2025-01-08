import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, start_size):
		super().__init__()
		self.title('Responsive Layout')
		self.geometry(f'{start_size[0]}x{start_size[1]}')
		self.frame = ttk.Frame(self)
		self.frame.pack(expand = True, fill = 'both')
		SizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout, 1200: self.create_large_layout})
		# self.bind('<Configure>', lambda event: print(event))

		self.mainloop()

	def create_small_layout(self):
		print('small_layout')
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)

		ttk.Label(self.frame, text = 'Label 1', background = 'maroon1').pack(expand = True, fill = 'both')
		ttk.Label(self.frame, text = 'Label 2', background = 'deeppink2').pack(expand = True, fill = 'both')
		ttk.Label(self.frame, text = 'Label 3', background = 'mediumvioletred').pack(expand = True, fill = 'both')
		ttk.Label(self.frame, text = 'Label 4', background = 'purple').pack(expand = True, fill = 'both')

		self.frame.pack(expand = True, fill = 'both')

	def create_medium_layout(self):
		print('medium_layout')
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)
		self.frame.columnconfigure((0,1), weight = 1, uniform = 'a')
		self.frame.rowconfigure((0,1), weight = 1, uniform = 'a')

		ttk.Label(self.frame, text = 'Label 1', background = 'maroon1').grid(column = 0, row = 0, sticky = 'nswe')
		ttk.Label(self.frame, text = 'Label 2', background = 'deeppink2').grid(column = 1, row = 0, sticky = 'nswe')
		ttk.Label(self.frame, text = 'Label 3', background = 'mediumvioletred').grid(column = 0, row = 1, sticky = 'nswe')
		ttk.Label(self.frame, text = 'Label 4', background = 'purple').grid(column = 1, row = 1, sticky = 'nswe')

		self.frame.pack(expand = True, fill = 'both')

	def create_large_layout(self):
		print('large_layout')
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)

		ttk.Label(self.frame, text = 'Label 1', background = 'maroon1').pack(expand = True, fill = 'both', side = 'left')
		ttk.Label(self.frame, text = 'Label 2', background = 'deeppink2').pack(expand = True, fill = 'both', side = 'left')
		ttk.Label(self.frame, text = 'Label 3', background = 'mediumvioletred').pack(expand = True, fill = 'both', side = 'left')
		ttk.Label(self.frame, text = 'Label 4', background = 'purple').pack(expand = True, fill = 'both', side = 'left')
		self.frame.pack(expand = True, fill = 'both')

class SizeNotifier:
	def __init__(self, window, size_dict):
		self.window = window
		self.size_dict = {key: value for key, value in sorted(size_dict.items())}
		self.window.bind('<Configure>', lambda event: self.check_size(event))
		self.current_min_size = None
		self.window.update()


		min_width = list(self.size_dict)[0]
		min_height = self.window.winfo_height()
		self.window.minsize(min_width,min_height)

	def check_size(self, event):
		if event.widget == self.window:
			width = event.width
			checked_size = None

			for min_size in self.size_dict:
				delta = width - min_size
				if delta >= 0:
					checked_size = min_size
			if checked_size != self.current_min_size:
				self.current_min_size = checked_size
				self.size_dict[self.current_min_size]()


app = App((400,300))