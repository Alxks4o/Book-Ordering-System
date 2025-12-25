import tkinter as tk

class SearchInvoices(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        tk.Label(self, text="Search Invoices",font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))