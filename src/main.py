"""

This module handles the graphical user interface using Tkinter, featuring
a fall-inspired pastel palette and high-readability text settings.
"""

import tkinter as tk
from tkinter import messagebox
import random
from connection_generator import ConnectionsEngine

# --- Configuration Constants (Fall & Pastel Palette) ---
# Category Colors: Late Warm Green, Blue, Yellow, Purple (Pastel Tones)
COLORS = ["#D1E8E2", "#D1D9E8", "#F7E7CE", "#E1D1E8"] 
COLOR_BOX_DEFAULT = "#F0EAD6"  # Egg Shell
COLOR_BOX_SELECTED = "#D3D3D3" # Light Gray
COLOR_TEXT_DARK = "#2C2C2C"    # Soft charcoal for better readability
COLOR_TEXT_SELECTED = "#000000"

FONT_BOX = ("Segoe UI", 10, "bold") # Clean, modern font
FONT_TITLE = ("Segoe UI", 13, "bold")

class ConnectionBox(tk.Label):
    """
    Custom UI Element representing a single word box.
    """
    def __init__(self, master, word, category_data, on_click_callback):
        super().__init__(master, text=word.upper(), font=FONT_BOX, 
                         bg=COLOR_BOX_DEFAULT, fg=COLOR_TEXT_DARK,
                         relief="flat", bd=0, width=14, height=3, cursor="hand2")
        self.word = word
        self.category_data = category_data
        self.callback = on_click_callback
        self.selected = False
        
        # Border effect via highlightthickness for a modern look
        self.config(highlightbackground="#E0D8C3", highlightthickness=1)
        self.bind("<Button-1>", lambda e: self.callback(self))

    def toggle(self):
        """Switches the box between Egg Shell and Light Gray."""
        self.selected = not self.selected
        if self.selected:
            self.config(bg=COLOR_BOX_SELECTED, fg=COLOR_TEXT_SELECTED, 
                        highlightbackground="#BDBDBD")
        else:
            self.config(bg=COLOR_BOX_DEFAULT, fg=COLOR_TEXT_DARK, 
                        highlightbackground="#E0D8C3")

class ConnectionsGame:
    """
    Main Application class featuring logic-UI coordination.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Connections: Autumn Edition")
        self.root.configure(bg="#FAF9F6") # Off-white background
        self.engine = ConnectionsEngine()
        self.selected_boxes = []
        self.solved_count = 0
        
        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        """Initializes layout frames with soft padding."""
        self.header_frame = tk.Frame(self.root, bg="#FAF9F6")
        self.header_frame.pack(pady=20)
        
        self.grid_frame = tk.Frame(self.root, bg="#FAF9F6")
        self.grid_frame.pack(pady=10, padx=20)
        
        btn_frame = tk.Frame(self.root, bg="#FAF9F6")
        btn_frame.pack(pady=30)
        
        # Styled Buttons
        style = {"relief": "flat", "padx": 15, "pady": 5, "font": ("Segoe UI", 9)}
        tk.Button(btn_frame, text="Shuffle", command=self.shuffle_words, **style).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Submit", command=self.submit_guess, bg="#2C2C2C", fg="white", **style).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Reset", command=self.reset_game, **style).pack(side="left", padx=10)
        
        self.root.bind('<Return>', lambda e: self.submit_guess())

    def reset_game(self):
        """Resets game and fetches new puzzle from engine."""
        self.solved_count = 0
        for widget in self.header_frame.winfo_children():
            widget.destroy()
        
        # Logic Case: Get 4 categories from the JSON engine
        self.puzzle_data = self.engine.get_new_puzzle()
        self.all_word_objects = []
        
        for i, cat in enumerate(self.puzzle_data):
            for word in cat['words']:
                self.all_word_objects.append({
                    "word": word, 
                    "cat": cat, 
                    "color": COLORS[i]
                })
        self.shuffle_words()

    def shuffle_words(self):
        """Randomizes position of remaining words."""
        random.shuffle(self.all_word_objects)
        self.render_grid()

    def render_grid(self):
        """Redraws the grid using the 'Egg Shell' default state."""
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.selected_boxes = []
        
        for i, obj in enumerate(self.all_word_objects):
            box = ConnectionBox(self.grid_frame, obj['word'], obj['cat'], self.handle_click)
            box.grid(row=i//4, column=i%4, padx=6, pady=6)

    def handle_click(self, box):
        """Selection logic."""
        if box.selected:
            box.toggle()
            self.selected_boxes.remove(box)
        elif len(self.selected_boxes) < 4:
            box.toggle()
            self.selected_boxes.append(box)

    def submit_guess(self):
        """Validates selection and handles feedback cases."""
        if len(self.selected_boxes) != 4:
            return
        
        category_names = [b.category_data['name'] for b in self.selected_boxes]
        
        if len(set(category_names)) == 1:
            self.mark_solved(self.selected_boxes[0].category_data)
        else:
            most_common = max(set(category_names), key=category_names.count)
            correct_count = category_names.count(most_common)
            
            if correct_count == 3:
                messagebox.showinfo("Hint", "One off!")
            elif correct_count == 2:
                messagebox.showinfo("Hint", "2 off")
            else:
                messagebox.showinfo("Hint", "Try again")

    def mark_solved(self, cat):
        """Displays the category in its pastel banner."""
        color = COLORS[self.solved_count]
        
        # Banner for solved category
        banner = tk.Label(self.header_frame, 
                          text=f"{cat['name'].upper()}\n{', '.join(cat['words']).upper()}", 
                          bg=color, fg=COLOR_TEXT_DARK, font=FONT_TITLE, 
                          width=45, pady=10, relief="flat")
        banner.pack(pady=4)
        
        self.all_word_objects = [o for o in self.all_word_objects if o['word'] not in cat['words']]
        self.solved_count += 1
        self.render_grid()
        
        if self.solved_count == 4:
            messagebox.showinfo("Success", "Puzzle Solved!")

if __name__ == "__main__":
    root = tk.Tk()
    ConnectionsGame(root)
    root.mainloop()