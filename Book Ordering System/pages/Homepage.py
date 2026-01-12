import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        # Title
        tk.Label(
            self,
            text="Welcome back!",
            font=("Arial", 28, "bold"),
            bg="#e9bb8d"
        ).pack(anchor='center', pady=(75,40))

        # Subtitle
        tk.Label(
            self,
            text="Use the navigation menu on the left to get started.",
            font=("Arial", 16),
            bg="#e9bb8d"
        ).pack(anchor='center')

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
        ).pack(anchor='center')