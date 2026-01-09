import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        # Title
        tk.Label(
            self,
            text="Welcome to the Book Ordering System",
            font=("Arial", 28, "bold"),
            bg="#e9bb8d"
        ).grid(row=0, column=0, padx=30, pady=(60, 20))

        # Subtitle
        tk.Label(
            self,
            text="Use the navigation menu on the left to get started.",
            font=("Arial", 16),
            bg="#e9bb8d"
        ).grid(row=1, column=0, padx=30, pady=10)

        # Description / Instructions
        instructions = (
            "• Add new customers to the system\n"
            "• Add books to your inventory\n"
            "• Place orders for any customer\n"
            "• View all invoices and search by order ID\n\n"
            "Everything you need is just one click away."
        )

        tk.Label(
            self,
            text=instructions,
            font=("Arial", 14),
            bg="#e9bb8d",
            justify="left"
        ).grid(row=2, column=0, padx=30, pady=20)