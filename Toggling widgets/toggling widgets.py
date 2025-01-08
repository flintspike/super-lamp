import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('300x300')
window.title('Toggling')

#command
def toggle_label_place():
	global label_vis
	if label_vis == True:
		label_vis = False
		label.place_forget()
	else:
		label_vis = True
		label.place(relx = 0.5, rely = 0.5, width = 100, height = 100, anchor = 'center')


#place
button = ttk.Button(window, text = 'Toggle Label', command = toggle_label_place)
button.place(relx = 1, rely = 0.5, anchor = 'e')

label_vis = True
label = ttk.Label(window, text = 'Label', background = 'darkgoldenrod1', anchor = 'center')
label.place(relx = 0.5, rely = 0.5, width = 100, height = 100, anchor = 'center')

#GRID
window.columnconfigure((0,1,2,3,4,5), uniform = 'a', weight = 1)
window.rowconfigure((0,1,2,3,4,5), uniform = 'a', weight = 1)

#GRID TOGGLE
visibility = {'glabel1': True, 'glabel2': True, 'glabel3': True}
placement = {'glabel1': 0, 'glabel2': 2, 'glabel3': 4}

def toggle_grid_label(label, var_name):
	global visibility
	global placement
	if visibility[var_name] == True:
		label.grid_forget()
		visibility[var_name] = False
	else:
		label.grid(row = 5, column = placement[var_name] , columns = 2, sticky = 'nswe')
		visibility[var_name] = True


#BUTTONS
gbutton1 = ttk.Button(window, text = 'Toggle 1', command = lambda: toggle_grid_label(glabel1, 'glabel1'))
gbutton1.grid(row = 0, column = 0 , columns = 2, sticky = 'nswe')
gbutton2 = ttk.Button(window, text = 'Toggle 2', command = lambda: toggle_grid_label(glabel2, 'glabel2'))
gbutton2.grid(row = 0, column = 2 , columns = 2, sticky = 'nswe')
gbutton3 = ttk.Button(window, text = 'Toggle 3', command = lambda: toggle_grid_label(glabel3, 'glabel3'))
gbutton3.grid(row = 0, column = 4 , columns = 2, sticky = 'nswe')

#LABELS
glabel1 = ttk.Label(window, text = 'G-label 1', background = 'darkorange1', anchor = 'center')
glabel1.grid(row = 5, column = 0 , columns = 2, sticky = 'nswe')
glabel2 = ttk.Label(window, text = 'G-label 2', background = 'orangered2', anchor = 'center')
glabel2.grid(row = 5, column = 2 , columns = 2, sticky = 'nswe')
glabel3 = ttk.Label(window, text = 'G-label 3', background = 'red', anchor = 'center')
glabel3.grid(row = 5, column = 4 , columns = 2, sticky = 'nswe')

#run
window.mainloop()