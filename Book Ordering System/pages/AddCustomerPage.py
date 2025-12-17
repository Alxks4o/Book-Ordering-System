import tkinter as tk
from backend.add_customer import Customer

class AddCustomerPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5e6c8")

        tk.Label(self, text="Add Customer", font=("Arial", 25, "bold"), bg="#f5e6c8")\
            .grid(row=0, column=0, columnspan=2, pady=(40, 20))

        # First Name Label
        tk.Label(self, text="First Name", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=1, column=0, sticky="w", padx=50, pady=10)

        self.first_name_entry = tk.Entry(self, font=("Arial", 15))
        self.first_name_entry.grid(row=2, column=0, padx=50, pady=10)

        # Last Name Label
        tk.Label(self, text="Last Name", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=3, column=0, sticky="w", padx=50, pady=10)

        self.last_name_entry = tk.Entry(self, font=("Arial", 15))
        self.last_name_entry.grid(row=4, column=0, padx=50, pady=10)

        # Email Label
        tk.Label(self, text="Email", font=("Arial", 15), bg="#f5e6c8")\
            .grid(row=5, column=0, sticky="w", padx=50, pady=10)

        self.email_entry = tk.Entry(self, font=("Arial", 15))
        self.email_entry.grid(row=6, column=0, padx=50, pady=10)

        # Message Label
        self.message_label = tk.Label(self, text="", font=("Arial", 12), bg="#f5e6c8")
        self.message_label.grid(row=7, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(self, text="Add Customer", font=("Arial", 15), command=self.addCustomerFunc)\
            .grid(row=8, column=0, sticky="nws", padx=50, pady=20)

        tk.Button(self, text="Clear", font=("Arial", 15), command=self.clearEntries)\
            .grid(row=8, column=0, sticky="nes", padx=50, pady=20)

    def clearEntries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def addCustomerFunc(self):
        firstName = self.first_name_entry.get().strip()
        lastName = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not firstName or not lastName or not email:
            self.message_label.config(text="All fields are required.", fg="red")
            return

        user = Customer(firstName, lastName, email)
        user.createUser()

        self.message_label.config(text="Customer added successfully!", fg="green")
        self.clearEntries()