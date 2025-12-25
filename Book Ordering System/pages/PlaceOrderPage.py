import tkinter as tk

class PlaceOrderPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        tk.Label(self, text="Place Order",font=("Arial", 25, "bold"), bg="#e9bb8d") \
        .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))
        

        tk.Label(self, text=("Books"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
        .grid(row=1, column=0, padx=30, pady=(20, 10))

        book_listbox = tk.Listbox(self, font=("Arial", 15), height=6, width=30)
        book_listbox.grid(row=2, column=0, padx=30, pady=10, sticky='w')

        quantity_label = tk.Label(self, text="Quantity", font=("Arial", 15), bg="#e9bb8d")
        quantity_label.grid(row=3, column=0, padx=30, pady=10, sticky='w', columnspan=2)

        quantity_entry = tk.Entry(self, font=("Arial", 15), width=10)
        quantity_entry.grid(row=4, column=0, padx=30, pady=10, sticky='w')

        place_order_button = tk.Button(self, text="Place Order", font=("Arial", 15), bg="#ffd3ad", height=2, width=15)
        place_order_button.grid(row=5, column=0, columnspan=2, pady=30, sticky="w", padx=30)





        tk.Label(self, text=("Customers"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
        .grid(row=1, column=1, padx=30, pady=(20, 10))

        customer_listbox = tk.Listbox(self, font=("Arial", 15), height=6, width=50)
        customer_listbox.grid(row=2, column=1, padx=30, pady=10, sticky='e')


