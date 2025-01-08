import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.geometry('300x300')
window.title('Toggling')

# Track visibility state
label_visibility = True

def toggle_label_place():
    """Toggle the placement of the standalone label."""
    global label_visibility
    if label_visibility:
        label.place_forget()
    else:
        label.place(relx=0.5, rely=0.5, width=100, height=100, anchor='center')
    label_visibility = not label_visibility

# Create a toggle button for the standalone label
button = ttk.Button(window, text='Toggle Label', command=toggle_label_place)
button.place(relx=1, rely=0.5, anchor='e')

# Create the standalone label
label = ttk.Label(window, text='Label', background='darkgoldenrod1', anchor='center')
label.place(relx=0.5, rely=0.5, width=100, height=100, anchor='center')

# Configure the grid layout
for i in range(6):
    window.columnconfigure(i, uniform='a', weight=1)
    window.rowconfigure(i, uniform='a', weight=1)

# Track visibility and placement for grid labels
labels = {}
visibility = {}

# Define the toggle function for grid labels
def toggle_grid_label(label_name):
    """Toggle the grid visibility of a label."""
    label, placement = labels[label_name]
    if visibility[label_name]:
        label.grid_forget()
    else:
        label.grid(row=5, column=placement, columnspan=2, sticky='nswe')
    visibility[label_name] = not visibility[label_name]

# Create grid buttons and labels
placements = {'glabel1': 0, 'glabel2': 2, 'glabel3': 4}
colors = {'glabel1': 'darkorange1', 'glabel2': 'orangered2', 'glabel3': 'red'}

for name, placement in placements.items():
    visibility[name] = True

    # Create the label
    label = ttk.Label(window, text=f'G-label {name[-1]}', background=colors[name], anchor='center')
    label.grid(row=5, column=placement, columnspan=2, sticky='nswe')
    labels[name] = (label, placement)

    # Create the button
    button = ttk.Button(window, text=f'Toggle {name[-1]}', command=lambda n=name: toggle_grid_label(n))
    button.grid(row=0, column=placement, columnspan=2, sticky='nswe')

# Run the application
window.mainloop()
