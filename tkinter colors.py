import tkinter as tk
from tkinter import ttk

# Organized colors list
color_categories = {
    "Whites and Off-Whites": [
        "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen",
        "antique white", "papaya whip", "blanched almond", "bisque", "peach puff",
        "navajo white", "lemon chiffon", "mint cream", "azure", "alice blue", "lavender",
        "lavender blush", "misty rose", "snow"
    ],
    "Grays": [
        "gray", "gray1", "gray2", "gray3", "gray4", "gray5", "gray6", "gray7", "gray8", "gray9",
        "gray10", "gray11", "gray12", "gray13", "gray14", "gray15", "gray16", "gray17", "gray18",
        "gray19", "gray20", "gray21", "gray22", "gray23", "gray24", "gray25", "gray26", "gray27",
        "gray28", "gray29", "gray30", "gray31", "gray32", "gray33", "gray34", "gray35", "gray36",
        "gray37", "gray38", "gray39", "gray40", "gray41", "gray42", "gray43", "gray44", "gray45",
        "gray46", "gray47", "gray48", "gray49", "gray50", "gray51", "gray52", "gray53", "gray54",
        "gray55", "gray56", "gray57", "gray58", "gray59", "gray60", "gray61", "gray62", "gray63",
        "gray64", "gray65", "gray66", "gray67", "gray68", "gray69", "gray70", "gray71", "gray72",
        "gray73", "gray74", "gray75", "gray76", "gray77", "gray78", "gray79", "gray80", "gray81",
        "gray82", "gray83", "gray84", "gray85", "gray86", "gray87", "gray88", "gray89", "gray90",
        "gray91", "gray92", "gray93", "gray94", "gray95", "gray96", "gray97", "gray98", "gray99"
    ],
    "Blues": [
        "blue", "light blue", "sky blue", "deep sky blue", "dodger blue", "royal blue",
        "medium blue", "slate blue", "light slate blue", "medium slate blue",
        "dark slate blue", "steel blue", "light steel blue", "powder blue", "cadet blue"
    ],
    "Greens": [
        "green", "lawn green", "lime green", "pale green", "spring green", "medium spring green",
        "sea green", "medium sea green", "dark sea green", "forest green", "dark green",
        "yellow green", "olive drab", "chartreuse"
    ],
    "Yellows and Golds": [
        "yellow", "light yellow", "light goldenrod yellow", "lemon chiffon", "goldenrod",
        "dark goldenrod", "gold"
    ],
    "Reds and Oranges": [
        "red", "light coral", "coral", "tomato", "orange red", "dark orange", "orange", "salmon",
        "light salmon", "dark salmon"
    ],
    "Pinks and Purples": [
        "pink", "light pink", "hot pink", "deep pink", "medium violet red", "pale violet red",
        "orchid", "violet red", "medium orchid", "dark orchid", "medium purple", "purple",
        "blue violet", "dark violet", "thistle"
    ],
    "Browns and Tans": [
        "brown", "rosy brown", "saddle brown", "sienna", "peru", "sandy brown", "burlywood",
        "tan", "wheat", "khaki", "dark khaki"
    ],
    "Miscellaneous": [
        "cyan", "light cyan", "turquoise", "medium turquoise", "dark turquoise",
        "pale turquoise", "light sky blue", "slate gray"
    ]
}

# Create the main application window
root = tk.Tk()
root.title("Organized Tkinter Colors")

# Create a scrollbar for the canvas
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Add color labels by categories
for category, colors in color_categories.items():
    # Add category label
    category_label = ttk.Label(scrollable_frame, text=category, font=("Arial", 12, "bold"))
    category_label.pack(anchor="w", pady=(10, 0))

    # Add color boxes
    for color in colors:
        frame = ttk.Frame(scrollable_frame)
        frame.pack(fill="x", padx=10, pady=2)

        color_label = ttk.Label(frame, text=color, background=color, width=20)
        color_label.pack(side="left")

        name_label = ttk.Label(frame, text=color, anchor="w")
        name_label.pack(side="left", padx=10)

# Layout scrollbar and canvas
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the Tkinter main loop
root.mainloop()
