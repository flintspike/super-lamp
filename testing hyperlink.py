import tkinter as tk
import webbrowser

def open_url(event):
    webbrowser.open("https://www.example.com")

root = tk.Tk()
root.title("Hyperlink in Text Widget")

# Create a Text widget
text_widget = tk.Text(root, wrap="word", height=5, width=50)
text_widget.pack(pady=20)

# Insert the body of text
text_widget.insert("1.0", "Here is a larger body of text, and you can ")

# Insert the hyperlink text
start_index = text_widget.index("end")
text_widget.insert("end", "click here")
end_index = text_widget.index("end")

# Continue with more text
text_widget.insert("end", " to visit the website.")

# Make the hyperlink text blue and underlined
text_widget.tag_add("hyperlink", start_index, end_index)
text_widget.tag_config(
    "hyperlink", foreground="blue", underline=True, font=("Arial", 12)
)

# Bind the hyperlink text to a callback
text_widget.tag_bind("hyperlink", "<Button-1>", open_url)

# Disable editing of the Text widget
text_widget.config(state="disabled")

root.mainloop()