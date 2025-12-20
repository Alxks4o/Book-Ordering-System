import tkinter as tk

class AddBookPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5e6c8")

        tk.Label(self, text="Add Book",font=("Arial", 25, "bold"), bg="#f5e6c8") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))