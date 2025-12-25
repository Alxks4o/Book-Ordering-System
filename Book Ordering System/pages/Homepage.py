import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        tk.Label(self, text="Welcome to the Book Ordering System",font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))