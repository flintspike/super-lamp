import tkinter as tk
from tkinter import ttk

brush_size = 2
def paint(x,y):
	canvas.create_oval((x,y,x,y), width = brush_size)

def sizer(event):
	global brush_size
	print(event)
	if event.delta > 0:
		if brush_size > 0:
			brush_size += 1
	else:
		if brush_size > 0:
			brush_size -= 1

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

#canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# canvas.create_rectangle((10,10,110,110), fill = 'yellow', width = 3, dash = (15,2), outline = 'magenta')
# canvas.create_line((10,10,60,60), width = 3)
# canvas.create_oval((20,20,100,100), width = 2, dash = (5,4))
# # canvas.create_polygon((16,60,45,20,90,70))
# canvas.create_arc((10,10,60,60))

# canvas.create_text((22,120), text = 'hello')

# canvas.create_window((50,100), window = ttk.Label(window, text = 'boombas'))

#paint
canvas.bind('<B1-Motion>', lambda event: paint(event.x, event.y))

#size adjustment
canvas.bind('<MouseWheel>', lambda event: sizer(event))

window.mainloop()