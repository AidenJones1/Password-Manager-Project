import tkinter as tk

def center_window(window: tk.Tk):
    """Start the window at center screen."""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def visual_grid(parent, rows: int, cols: int):
    """Provide a visual representation of how the grid is laid out."""
    for y in range(rows):
        for x in range(cols):
            label = tk.Label(parent)
            label.config(text = f"({y},{x})", borderwidth = 1, relief = "solid")
            label.grid(row = y, column = x, sticky = "nsew")