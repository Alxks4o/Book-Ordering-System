import tkinter as tk
from tkinter import ttk
from backend.add_customer import Customer

class AddCustomerPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5e6c8")

        #Setting up tabs
        style = ttk.Style()
        style.configure('TNotebook', background='#f5e6c8', borderwidth=0)
        style.configure('TNotebook.Tab', background='#ffd3ad', font=('Arial', 15), padding=10)

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        # Create a tab for adding customers
        add_customer_tab = tk.Frame(notebook, bg="#f5e6c8")
        notebook.add(add_customer_tab, text="Add Customer")

        tk.Label(add_customer_tab, text="Add Customer", font=("Arial", 25, "bold"), bg="#f5e6c8")\
            .grid(row=0, column=0, columnspan=2, pady=(40, 20))

        # First Name Label
        tk.Label(add_customer_tab, text="First Name", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=1, column=0, sticky="w", padx=50, pady=10)

        self.first_name_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.first_name_entry.grid(row=2, column=0, padx=50, pady=10)

        # Last Name Label
        tk.Label(add_customer_tab, text="Last Name", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=3, column=0, sticky="w", padx=50, pady=10)

        self.last_name_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.last_name_entry.grid(row=4, column=0, padx=50, pady=10)

        # Email Label
        tk.Label(add_customer_tab, text="Email", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=5, column=0, sticky="w", padx=50, pady=10)

        self.email_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.email_entry.grid(row=6, column=0, padx=50, pady=10)

        # Address Label
        tk.Label(add_customer_tab, text="Address", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=7, column=0, sticky="w", padx=50, pady=10)

        self.address_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.address_entry.grid(row=8, column=0, padx=50, pady=10)

        # Message Label
        self.message_label = tk.Label(add_customer_tab, text="", font=("Arial", 12), bg="#f5e6c8")
        self.message_label.grid(row=9, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(add_customer_tab, text="Add Customer", font=("Arial", 15), command=self.addCustomerFunc)\
            .grid(row=10, column=0, sticky="nws", padx=50, pady=20)

        tk.Button(add_customer_tab, text="Clear", font=("Arial", 15), command=self.clearEntries)\
            .grid(row=10, column=0, sticky="nes", padx=50, pady=20)

        add_book_tab = tk.Frame(notebook, bg="#f5e6c8")
        notebook.add(add_book_tab, text="Add Book")

        # Add Book Tab Content
        tk.Label(add_book_tab, text="Add Book",font=("Arial", 25, "bold"), bg="#f5e6c8") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))

    def clearEntries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def addCustomerFunc(self):
        firstName = self.first_name_entry.get().strip()
        lastName = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not firstName or not lastName or not email:
            self.message_label.config(text="All fields are required.", fg="red")
            return

        user = Customer(firstName, lastName, email, address)
        user.createUser()

        self.message_label.config(text="Customer added successfully!", fg="green")
        self.clearEntries()