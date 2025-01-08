import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('500x500')
window.title('Combining Layouts')
window.minsize(600,600)

menu_frame = tk.Frame(window)
main_frame = tk.Frame(window)

#main place layout
menu_frame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)

#CREATE LEFT SIDE
def Left():
	#menu widgets
	button1 = ttk.Button(menu_frame, text = 'Button1')
	button2 = ttk.Button(menu_frame, text = 'Button2')
	button3 = ttk.Button(menu_frame, text = 'Button3')

	slider1 = ttk.Scale(menu_frame, orient = 'vertical')
	slider2 = ttk.Scale(menu_frame, orient = 'vertical')

	toggle_frame = ttk.Frame(menu_frame)
	menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'Check 1')
	menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'Check 2')

	entry = ttk.Entry(menu_frame)

	#menu layout
	menu_frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
	menu_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

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
	
Left()

#CREATE MIDDLE/RIGHT SIDE
def Right():
	entry_frame1 = ttk.Frame(main_frame)
	main_label1 = ttk.Label(entry_frame1, text = 'Label ', background = 'cyan2')
	main_button1 = ttk.Button(entry_frame1, text = 'Button 1')

	entry_frame2 = ttk.Frame(main_frame)
	main_label2 = ttk.Label(entry_frame2, text = 'Label ', background = 'violetred2')
	main_button2 = ttk.Button(entry_frame2, text = 'Button 2')

	entry_frame1.pack(side = 'left', expand = True, fill = 'both', padx = 3, pady = 3)
	entry_frame2.pack(side = 'left', expand = True, fill = 'both', padx = 3, pady = 3)

	main_label1.pack(expand = True, fill = 'both', padx = 5)
	main_label2.pack(expand = True, fill = 'both', padx = 5)
	main_button1.pack(expand = True, fill = 'both', pady = 10)
	main_button2.pack(expand = True, fill = 'both', pady = 10)
Right()

#run
window.mainloop()