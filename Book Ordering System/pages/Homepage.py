import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5e6c8")

        tk.Label(self, text="Welcome to the Book Ordering System", 
                 font=("Arial", 25, "bold"), bg="#f5e6c8")