import tkinter as tk
from tkinter import ttk

#importing backend modules
from backend.add_book import Book
from backend.add_customer import Customer
from backend.place_order import Order

'''
PlaceOrderPage Class - page for placing book orders for customers by selecting from a book from the inventory and a customer from the customer list
'''

class PlaceOrderPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")


        tk.Label(self, text="Place Order", font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2, padx=30, pady=(40, 20))


        #Books Section

        tk.Label(self, text=("Books"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
            .grid(row=1, column=0, padx=30, pady=(20, 10))

        books_frame = tk.Frame(self, bg="#e9bb8d")
        books_frame.grid(row=2, column=0, padx=30, pady=10, sticky='w')

        books_tree = ttk.Treeview(
            books_frame,
            columns=("id", "title", "author"),
            show="headings",
            height=8
        )
        books_tree.heading("id", text="ID")
        books_tree.heading("title", text="Title")
        books_tree.heading("author", text="Author")
        books_tree.column("id", width=60, anchor="center")
        books_tree.column("title", width=220, anchor="w")
        books_tree.column("author", width=160, anchor="w")
        books_tree.grid(row=0, column=0, sticky="nsew")

        books_scroll = ttk.Scrollbar(books_frame, orient="vertical", command=books_tree.yview)
        books_tree.configure(yscrollcommand=books_scroll.set)
        books_scroll.grid(row=0, column=1, sticky="ns")

        quantity_label = tk.Label(self, text="Quantity", font=("Arial", 15), bg="#e9bb8d")
        quantity_label.grid(row=3, column=0, padx=30, pady=10, sticky='w', columnspan=2)

        quantity_entry = tk.Entry(self, font=("Arial", 15), width=10)
        quantity_entry.grid(row=4, column=0, padx=30, pady=10, sticky='w')

        place_order_button = tk.Button(self, text="Place Order", font=("Arial", 15), bg="#ffd3ad", height=2, width=15)
        place_order_button.grid(row=5, column=0, columnspan=2, pady=30, sticky="w", padx=30)

        

        #Customers Section

        tk.Label(self, text=("Customers"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
            .grid(row=1, column=1, padx=30, pady=(20, 10))

        customers_frame = tk.Frame(self, bg="#e9bb8d")
        customers_frame.grid(row=2, column=1, padx=30, pady=10, sticky='e')

        customers_tree = ttk.Treeview(
            customers_frame,
            columns=("id", "name", "email"),
            show="headings",
            height=8
        )
        customers_tree.heading("id", text="ID")
        customers_tree.heading("name", text="Name")
        customers_tree.heading("email", text="Email")
        customers_tree.column("id", width=60, anchor="center")
        customers_tree.column("name", width=220, anchor="w")
        customers_tree.column("email", width=220, anchor="w")
        customers_tree.grid(row=0, column=0, sticky="nsew")

        customers_scroll = ttk.Scrollbar(customers_frame, orient="vertical", command=customers_tree.yview)
        customers_tree.configure(yscrollcommand=customers_scroll.set)
        customers_scroll.grid(row=0, column=1, sticky="ns")


        #Populating the book tables
        self.bookObj = Book("", "", "", 0, 0)
        books = self.bookObj.getBooks()
        for book in books:
            books_tree.insert("", tk.END, values=(book["ID"], book["title"], book["author"]))

        #Populating the customer table
        self.customerObj = Customer("", "", "", "")
        customers = self.customerObj.getCustomers()
        for customer in customers:
            full_name = f'{customer["first_name"]} {customer["last_name"]}'
            customers_tree.insert("", tk.END, values=(customer["ID"], full_name, customer["email"]))


        # Place Order Button Functionality
        def place_order():
            book_sel = books_tree.focus()
            cust_sel = customers_tree.focus()
            qty_text = quantity_entry.get().strip()

            if not book_sel or not cust_sel:
                # tk.messagebox.showerror("Missing selection", "Please select a book and a customer.")
                return

            if not qty_text.isdigit() or int(qty_text) <= 0:
                # tk.messagebox.showerror("Invalid quantity", "Please enter a valid positive quantity.")
                return

            book_vals = books_tree.item(book_sel)["values"]
            cust_vals = customers_tree.item(cust_sel)["values"]

            book_id = book_vals[0]
            customer_id = cust_vals[0]
            customer_firstname = cust_vals[1].split(" ")[0]
            customer_lastname = cust_vals[1].split(" ")[1]
            email = cust_vals[2]
            book_title = book_vals[1]
            book_author = book_vals[2]
            quantity = int(qty_text)

            book_price = 0
            for book in books:
                if book["ID"] == book_id:
                    book_price = book["price"]
                    break

            # print(book_vals)
            # print(cust_vals)
            orderObj = Order(book_id, customer_id, customer_firstname, customer_lastname, book_title, book_author, email, quantity)
            orderObj.calculateTotalPrice(book_price) 
            result = orderObj.placeOrder()

            if result == "Order placed successfully!":
                print(result)
                # tk.messagebox.showinfo("Success", result)
            else:
                # tk.messagebox.showerror("Error", result)
                print("Error placing order.")

            quantity_entry.delete(0, tk.END)

        place_order_button.configure(command=place_order)
