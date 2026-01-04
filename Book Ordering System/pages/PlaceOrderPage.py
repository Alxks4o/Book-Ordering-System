import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
            .grid(row=0, column=0, columnspan=2, padx=30, pady=(40, 20), sticky='w')


        #Books Section

        tk.Label(self, text=("Books"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
            .grid(row=1, column=0, padx=30, pady=(20, 10))

        books_frame = tk.Frame(self, bg="#e9bb8d")
        books_frame.grid(row=2, column=0, padx=30, pady=10, sticky='w')

        books_tree = ttk.Treeview(
            books_frame,
            columns=("id", "title", "author", "quantity"),
            show="headings",
            height=8
        )

        books_tree.heading("id", text="ID")
        books_tree.heading("title", text="Title")
        books_tree.heading("author", text="Author")
        books_tree.heading("quantity", text="Quantity")

        books_tree.column("id", width=60, anchor="center")
        books_tree.column("title", width=220, anchor="w")
        books_tree.column("author", width=160, anchor="w")
        books_tree.column("quantity", width=100, anchor="w")

        books_tree.grid(row=0, column=0, sticky="nsew")

        books_scroll = ttk.Scrollbar(books_frame, orient="vertical", command=books_tree.yview)
        books_tree.configure(yscrollcommand=books_scroll.set)
        books_scroll.grid(row=0, column=1, sticky="ns")

        quantity_label = tk.Label(self, text="Quantity", font=("Arial", 15), bg="#e9bb8d")
        quantity_label.grid(row=3, column=0, padx=30, pady=10, sticky='w', columnspan=2)

        quantity_entry = tk.Entry(self, font=("Arial", 15), width=10)
        quantity_entry.grid(row=4, column=0, padx=30, pady=10, sticky='w')
        
        self.shipping_var = tk.BooleanVar(value=False)
        shipping_checkbox= tk.Checkbutton(
            self,
            text="Shipping (+£5.00)",
            font=("Arial", 12),
            bg="#ffd3ad",
            indicatoron=False,
            width=18,
            selectcolor="#94ff8a",
            relief="raised",
            variable=self.shipping_var,
            onvalue=True,
            offvalue=False
        )
        shipping_checkbox.grid(row=6, column=0, padx=30, pady=10, sticky='w')

        place_order_button = tk.Button(self, text="Place Order", font=("Arial", 15), bg="#ffd3ad", height=2, width=15)
        place_order_button.grid(row=7, column=0, columnspan=2, pady=30, sticky="w", padx=30)

        

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
        try:
            for book in books:
                books_tree.insert("", tk.END, values=(book["ID"], book["title"], book["author"], book["quantity"]))
        except:
            pass

        
        #Populating the customer table
        self.customerObj = Customer("", "", "", "")
        customers = self.customerObj.getCustomers()
        for customer in customers:
            full_name = f'{customer["first_name"]} {customer["last_name"]}'
            customers_tree.insert("", tk.END, values=(customer["ID"], full_name, customer["email"]))

        # Function to show invoice in a new window
        def show_invoice(orderObj, first, last, title, author, qty, use_shipping):
            win = tk.Toplevel()
            win.title("Invoice")
            win.geometry("400x450")
            win.resizable(False, False)
            win.configure(bg="#ececec")
            



            tk.Label(win, text="Order Confirmation", font=("Arial", 18, "bold"), bg="#ececec").pack(pady=10)
            tk.Label(win, text=(100*"-"), font=("Arial", 18, "bold"), bg="#ececec").pack(pady=10)
            tk.Label(win, text=f"Order ID: {orderObj.order_id}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Customer: {first} {last}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Book: {title} — {author}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Quantity: {qty}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            if use_shipping:
                tk.Label(win, text=f"Shipping: £5.00", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Total Price: £{orderObj._total_price:.2f}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Button(win, text="OK", width=20, height=2, font=("Arial", 15), bg="#7b7b7b", command=win.destroy).pack(pady=50)


        # Place Order Button Functionality
        def place_order():
            book_sel = books_tree.focus()
            cust_sel = customers_tree.focus()
            qty_text = quantity_entry.get().strip()
            shipping = self.shipping_var.get()


            if not book_sel or not cust_sel:
                messagebox.showerror("Missing selection", "Please select a book and a customer.")
                return

            if not qty_text.isdigit() or int(qty_text) <= 0:
                messagebox.showerror("Invalid quantity", "Please enter a valid positive quantity.")
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
                if book["ID"] == int(book_id):
                    book_price = book["price"]
                    break


            orderObj = Order(book_id, customer_id, customer_firstname, customer_lastname, book_title, book_author, email, quantity, shipping)
            orderObj.calculateTotalPrice(book_price) 
            result = orderObj.placeOrder()


            if result == "Order placed successfully!":
                show_invoice(orderObj, customer_firstname, customer_lastname, book_title, book_author, quantity, shipping)
            elif result == "Order failed due to insufficient stock.":
                messagebox.showerror("Insufficient Stock", "Order failed due to insufficient stock.")
            
            quantity_entry.delete(0, tk.END)

        place_order_button.configure(command=place_order)
