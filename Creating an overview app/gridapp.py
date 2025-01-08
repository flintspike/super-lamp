import fs
import tkinter as tk
from tkinter import ttk
#makes a square of numbers



def entry_confirmation():

	#checks if input is an int and prompt again if it is not
	def int_check(num): 
		try: 
			num = int(num)
			return(num)
		except ValueError:
			result('Only use integers')

	#check X first
	if type(int_check(entry_x.get())) == int:
		x = int(entry_x.get())

		#then check y
		if type(int_check(entry_y.get())) == int:
			y = int(entry_y.get())

			
			result(make_grid(x,y))

def make_grid(x_val, y_val):
	all_nums = [num for num in range(0, (x_val*y_val))]
	grid = [all_nums[i:i + x_val] for i in range(0, len(all_nums), x_val)]
	

	max_len = len(str(grid[-1][-1]))
	for i in range(len(grid)):        # Iterate over rows using indices
		for j in range(len(grid[i])):  # Iterate over elements using indices
			grid[i][j] = str((grid[i][j])+1).zfill(max_len)  # Update each element with zero-padded string and add 1
	for line in grid: print(line)
	return grid


	# total = x_val * y_val
	# rows = [[x for x in range(x_val * y,((x_val * y))+x_val+1)] for y in range(1,y_val+1)]###YOU ARE TRYING TO FIGURE THIS PART OUT
	# for row in rows: print(row)

#output
output_label = None
def result(output):
	global output_label
	if output_label:
		output_label.destroy()
	output = '\n'.join([' '.join(row) for row in output])
	output_label = ttk.Label(master = window, text = output, font = ("system", "14"))
	output_label.pack()	

#window
window = tk.Tk()
window.title('grid maker extreme')
window.geometry('400x300')

#text
title_label = ttk.Label(master = window, text = 'grid maker extreme', font = ("system", "36", "bold"))
title_label.pack()

#input X
input_frame_x = ttk.Frame(master = window)
entry_x = ttk.Entry(master = input_frame_x)
entry_x.pack(side = 'left')
input_frame_x.pack(pady = 20)

#input Y
input_frame_y = ttk.Frame(master = window)
entry_y = ttk.Entry(master = input_frame_y)
entry_y.pack(side = 'left')
input_frame_y.pack()


#go button
go_frame = ttk.Frame(master = window)
go_button = ttk.Button(master = go_frame, text = 'Gridify', command = entry_confirmation)
go_frame.pack(pady = 60)
go_button.pack()


window.mainloop()

