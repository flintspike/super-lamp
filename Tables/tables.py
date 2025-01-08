import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('eksel')
window.geometry('660x300')

#data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

#treeview

table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'first name')
table.heading('last', text = 'surname')
table.heading('email', text = 'email address')
table.pack()

#table.insert(parent = '', index = 0, values = ('john', 'doe', 'johndoe@email.com'))
for i in range(100):
	f = choice(first_names)
	l = choice(last_names)
	e = f'{f}.{l}@warnermusic.com'
	entry = (f, l, e)
	table.insert(parent = '', index = i, values = entry)

table.insert(parent = '', index = 2, values = ('xxx','xxx','zzz'))
table.insert(parent = '', index = 2, values = ('uuu','vvv','www'))
table.insert(parent = '', index = tk.END, values = ('LAST','INDEX','Func'))

#events
def item_select(_):
	for i in table.selection():
		print(table.item(i)['values'])

def delete_items(_):
	for i in table.selection():
		print(f'{table.item(i)['values']} deleted')
		table.delete(i)


table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)


window.mainloop()