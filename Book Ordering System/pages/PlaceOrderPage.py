import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#importing backend modules
from backend.add_book import Book
from backend.add_customer import Customer
from backend.place_order import Order

'''
PlaceOrderPage Class - page for placing book orders for customers by selecting from a book from the inventory and a customer from the customer list,
and specifying the quantity to order. It also includes options for shipping and urgent shipping.
'''

class PlaceOrderPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")


        tk.Label(self, text="Place Order", font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2, padx=30, pady=(40, 20), sticky='w')


        #Books Section
        tk.Label(self, text=("Books"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
            .grid(row=1, column=0, padx=30, pady=(20, 10), sticky='w')

        
        '''
        Books Table - for showing the books available in the inventory
        '''

        # Book frame 
        books_frame = tk.Frame(self, bg="#e9bb8d")
        books_frame.grid(row=2, column=0, padx=30, pady=10, sticky='nesw')

        books_tree = ttk.Treeview(
            books_frame,
            columns=("id", "title", "author", "price", "quantity"),
            show="headings",
            height=8
        )

        #Headings
        books_tree.heading("id", text="ID")
        books_tree.heading("title", text="Title")
        books_tree.heading("author", text="Author")
        books_tree.heading("price", text="Price")
        books_tree.heading("quantity", text="Quantity")

        #Column configurations
        books_tree.column("id", width=60, anchor="center")
        books_tree.column("title", width=200, anchor="center")
        books_tree.column("author", width=200, anchor="center")
        books_tree.column("price", width=100, anchor="center")
        books_tree.column("quantity", width=100, anchor="center")

        #Placing the table
        books_tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbar for the books table
        books_scroll = ttk.Scrollbar(books_frame, orient="vertical", command=books_tree.yview)
        books_tree.configure(yscrollcommand=books_scroll.set)
        books_scroll.grid(row=0, column=1, sticky="ns")

        #Quantity Label 
        quantity_label = tk.Label(self, text="Quantity", font=("Arial", 15), bg="#e9bb8d")
        quantity_label.grid(row=5, column=0, padx=30, pady=10, sticky='w', columnspan=2)

        #Quantity Entry
        quantity_entry = tk.Entry(self, font=("Arial", 15), width=10)
        quantity_entry.grid(row=6, column=0, padx=30, pady=10, sticky='w')
        
        '''
        Shipping Options - Checkbuttons for selecting shipping and urgent shipping options to make sure
        the buttons appear and disappear correctly based on user interaction
        '''
        def on_shipping_toggle():
            if self.shipping_var.get():
                # Show urgent shipping checkbox and place order button below it
                urgent_shipping_checkbox.grid(row=7, column=0, padx=250, pady=10, sticky='w')  
            else:
                # Hide urgent shipping checkbox and move place order button up
                urgent_shipping_checkbox.grid_remove()
                place_order_button.grid(row=8, column=0, columnspan=2, pady=30, sticky="w", padx=30)
                refresh_button.grid(row=8, column=0, columnspan=2, pady=30, sticky="w", padx=220)



        #Shipping Checkbuttons Setup         
        self.shipping_var = tk.BooleanVar(value=False)
        shipping_checkbox= tk.Checkbutton(
            self,
            text="Shipping (+£2.00)",
            font=("Arial", 12),
            bg="#ffd3ad",
            indicatoron=False,
            width=22,
            selectcolor="#ffb36c",
            relief="raised",
            variable=self.shipping_var,
            onvalue=True,
            offvalue=False,
            command=on_shipping_toggle
        )
        shipping_checkbox.grid(row=7, column=0, padx=30, pady=10, sticky='w')

        # Urgent Shipping Checkbutton Setup
        self.urgent_shipping_var = tk.BooleanVar(value=False)
        urgent_shipping_checkbox = tk.Checkbutton(
            self,
            text="Urgent Shipping (+£3.00)",
            font=("Arial", 12),
            bg="#ffd3ad",
            indicatoron=False,
            width=22,
            selectcolor="#ffb36c",
            relief="raised",
            variable=self.urgent_shipping_var,
            onvalue=True,
            offvalue=False
        )

        #Place Order Button
        place_order_button = tk.Button(self, text="Place Order", font=("Arial", 15), bg="#ffd3ad", height=2, width=14, state="disabled") 
        place_order_button.grid(row=8, column=0, columnspan=2, pady=30, sticky="w", padx=30)

        # Refresh Button
        refresh_button = tk.Button(self, text="Refresh", font=("Arial", 15), bg="#ffd3ad", height=2, width=14)
        refresh_button.grid(row=8, column=0, columnspan=2, pady=30, sticky="w", padx=220)

        

        '''
        Customers Section - for selecting the customer placing the order
        '''

        # Customers Label        
        tk.Label(self, text=("Customers"), font=("Arial", 20, "bold"), bg="#e9bb8d") \
            .grid(row=3, column=0, padx=30, pady=(20, 10), sticky='w')
        
        # Customer frame
        customers_frame = tk.Frame(self, bg="#e9bb8d")
        customers_frame.grid(row=4, column=0, padx=30, pady=10, sticky='nesw')

        customers_tree = ttk.Treeview(
            customers_frame,
            columns=("id", "name", "email", "address"),
            show="headings",
            height=8
        )

        # Table Headings
        customers_tree.heading("id", text="ID")
        customers_tree.heading("name", text="Name")
        customers_tree.heading("email", text="Email")
        customers_tree.heading("address", text="Address")

        # Column configurations
        customers_tree.column("id", width=60, anchor="center")
        customers_tree.column("name", width=220, anchor="center")
        customers_tree.column("email", width=180, anchor="center")
        customers_tree.column("address", width=200, anchor="center")
        customers_tree.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar for the customers table
        customers_scroll = ttk.Scrollbar(customers_frame, orient="vertical", command=customers_tree.yview)
        customers_tree.configure(yscrollcommand=customers_scroll.set)
        customers_scroll.grid(row=0, column=1, sticky="ns")

        self.bookObj = Book("", "", "", 0, 0)
        books = self.bookObj.getBooks()
        
        
        '''
        Function for disabling and enabling Place Order button
        '''
        def validate_order_ready(*args):
            book_sel = books_tree.focus()
            cust_sel = customers_tree.focus()
            qty_text = quantity_entry.get().strip()

            # Check all conditions
            if book_sel and cust_sel and qty_text.isdigit() and int(qty_text) > 0:
                place_order_button.config(state="normal")
            else:
                place_order_button.config(state="disabled")


        # Bind events to enable/disable the Place Order button
        books_tree.bind("<<TreeviewSelect>>", validate_order_ready)
        customers_tree.bind("<<TreeviewSelect>>", validate_order_ready)
        quantity_entry.bind("<KeyRelease>", validate_order_ready)


        self.customerObj = Customer("", "", "", "")

        def clearTree(table_name):
            for item in table_name.get_children():
                table_name.delete(item)

        '''
        Populating the Books Table - fetching books from the database and inserting them into the books table
        '''
        def populateBooks():
            latest_books = self.bookObj.getBooks()

            clearTree(books_tree)

            try:
                for book in latest_books:
                    books_tree.insert("", tk.END, values=(book["ID"], book["title"], book["author"], f"£{book["price"]:.2f}", book["quantity"]))
            except Exception:
                pass
        
        populateBooks()

        
        '''
        Populating the Customers Table - fetching customers from the database and inserting them into the customers table
        '''
        def populateCustomers():
            latest_customer = self.customerObj.getCustomers()

            clearTree(customers_tree)

            for customer in latest_customer:
                full_name = f'{customer["first_name"]} {customer["last_name"]}' # concatenate first and last name
                customers_tree.insert("", tk.END, values=(customer["ID"], full_name, customer["email"], customer["address"]))

        populateCustomers()


        def refreshAll():
            populateCustomers()
            populateBooks()

        
        '''
        Function to show the invoice in a new window after placing an order successfully
        '''
        def show_invoice(orderObj, first, last, address, title, author, qty, use_shipping, urgent_shipping):
            
            # Create a new window for the invoice
            win = tk.Toplevel()
            win.title("Invoice")
            win.geometry("500x550")
            # win.iconbitmap()
            win.resizable(False, False)
            win.configure(bg="#ececec")
            


            '''
            Displaying the invoice details
            '''
            tk.Label(win, text="Order Confirmation", font=("Arial", 18, "bold"), bg="#ececec").pack(pady=10)
            tk.Label(win, text=(100*"-"), font=("Arial", 18, "bold"), bg="#ececec").pack(pady=10)
            tk.Label(win, text=f"Order ID: {orderObj.order_id}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Customer: {first} {last}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Address: {address}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Book: {title} — {author}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Label(win, text=f"Quantity: {qty}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)

            # Display shipping costs if applicable
            if use_shipping and not urgent_shipping:
                # shipping only
                tk.Label(win, text=f"Subtotal: £{((orderObj.total_price)-2):.2f}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
                tk.Label(win, text=f"Shipping: £2.00", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20) 
            elif use_shipping and urgent_shipping:
                # urgent shipping
                tk.Label(win, text=f"Subtotal: £{((orderObj.total_price)-5):.2f}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
                tk.Label(win, text=f"Shipping: £5.00", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)

            tk.Label(win, text=f"Total Price: £{orderObj.total_price:.2f}", font=("Arial", 15), bg="#ececec").pack(anchor="w", padx=20)
            tk.Button(win, text="Close", width=20, height=2, font=("Arial", 15), bg="#7b7b7b", command=win.destroy).pack(pady=50)

        def getBookPrice(bookID):
            refreshAll()
            self.bookObj = Book("", "", "", 0, 0)
            latest_books = self.bookObj.getBooks()

            for book in latest_books:
                if book["ID"] == int(bookID):
                    try:
                        return float(book["price"])
                    except (ValueError, TypeError):
                        return None  # or raise a custom error

            return None  # book not found

        '''
        Function to handle placing an order when the "Place Order" button is clicked, including input validation and order processing. 
        '''
        def place_order():
            
            # Get selected book, customer, quantity, and shipping options
            book_sel = books_tree.focus()
            cust_sel = customers_tree.focus()
            qty_text = quantity_entry.get().strip()
            shipping = self.shipping_var.get()
            urgent_shipping = self.urgent_shipping_var.get()

            # Input validation if no book or customer is selected or quantity is invalid
            if not book_sel or not cust_sel:
                # Show error message if no book or customer is selected
                messagebox.showerror("Missing selection", "Please select a book and a customer.")
                return
            
            if not qty_text.isdigit() or int(qty_text) <= 0:
                # Show error message if quantity is not a valid positive integer
                messagebox.showerror("Invalid quantity", "Please enter a valid positive quantity.")
                return

            # Extracting values from the selected book and customer
            book_vals = books_tree.item(book_sel)["values"]
            cust_vals = customers_tree.item(cust_sel)["values"]

            # Getting customer values from the selected customer
            customer_id = cust_vals[0]
            customer_firstname = cust_vals[1].split(" ")[0]
            customer_lastname = cust_vals[1].split(" ")[1]
            address = cust_vals[3]
            email = cust_vals[2]

            # Getting book values from the selected book
            book_id = book_vals[0]
            book_title = book_vals[1]
            book_author = book_vals[2]

            # Getting quantity as an integer
            quantity = int(qty_text)

            book_price = getBookPrice(book_id)

            # Creating an Order object and placing the order
            orderObj = Order(book_id, customer_id, customer_firstname, customer_lastname, address, book_title, book_author, email, quantity, shipping, urgent_shipping)
            result = orderObj.placeOrder(book_price)  # place the order

            # Handling the result of the order placement
            if result == "Order placed successfully!":
                # Order placed successfully, show invoice
                show_invoice(orderObj, customer_firstname, customer_lastname, address, book_title, book_author, quantity, shipping, urgent_shipping)

            elif result == "Order failed due to insufficient stock.":
                # Show error message for insufficient stock if quantity exceeds available stock
                messagebox.showerror("Insufficient Stock", "Order failed due to insufficient stock.")
            
            # Clear the quantity entry field after placing the order
            populateBooks()
            quantity_entry.delete(0, tk.END)
    
        place_order_button.configure(command=place_order)
        refresh_button.configure(command=refreshAll)
