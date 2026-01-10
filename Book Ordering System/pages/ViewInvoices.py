import tkinter as tk
from tkinter import ttk

from backend.place_order import Order
from backend.add_book import Book

class ViewInvoices(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        tk.Label(self, text="View Invoices",font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))
        
        invoices_frame = tk.Frame(self, bg="#e9bb8d")
        invoices_frame.grid(row=2, column=0, padx=30, pady=10, sticky='w')


        '''
        Setting a placeholder for the searchbar
        '''

        placeholder = "Enter order ID" # placeholder value
        

        def set_placeholder(e=None):
            if search_bar.get() == "": # searchbar is empty
                search_bar.insert(0, placeholder) # insert placeholder
                search_bar.config(fg="grey") # set to grey

        
        def clear_placeholder(e=None):
            if search_bar.get() == placeholder: # searchbar has been clicked
                search_bar.delete(0, tk.END) # clear placeholder
                search_bar.config(fg="black") # set to black
            
        

        search_bar = tk.Entry(invoices_frame, width=20, font=('Arial', 18))
        search_bar.grid(row=0, column=0, padx=(0, 10), pady=10, sticky = 'w')

        set_placeholder()

        search_bar.bind("<FocusIn>", clear_placeholder) # User clicks on searchbar
        search_bar.bind("<FocusOut>", set_placeholder) # User clicks off searchbar




        invoices_tree = ttk.Treeview(
            invoices_frame,
            columns=("order_id", "customer_name", "email", "address", "book_title", "book_author", "quantity", "shipping_cost", "shipping_type", "total_price"),
            show="headings",
            height=15
        )

        invoices_tree.heading("order_id", text="Order ID")
        invoices_tree.heading("customer_name", text="Customer Name")
        invoices_tree.heading("email", text="Email")
        invoices_tree.heading("address", text="Address")
        invoices_tree.heading("book_title", text="Book Title")
        invoices_tree.heading("book_author", text="Book Author")
        invoices_tree.heading("quantity", text="Quantity")
        invoices_tree.heading("shipping_cost", text="Shipping Cost")
        invoices_tree.heading("shipping_type", text="Shipping Type")
        invoices_tree.heading("total_price", text="Total Price")

        invoices_tree.column("order_id", width=80, anchor="center")
        invoices_tree.column("customer_name", width=150, anchor="center")
        invoices_tree.column("email", width=200, anchor="center")
        invoices_tree.column("address", width=200, anchor="center")
        invoices_tree.column("book_title", width=150, anchor="center")
        invoices_tree.column("book_author", width=150, anchor="center")
        invoices_tree.column("quantity", width=80, anchor="center")
        invoices_tree.column("shipping_cost", width=100, anchor="center")
        invoices_tree.column("shipping_type", width=120, anchor="center")
        invoices_tree.column("total_price", width=100, anchor="center")

        y_scroll = ttk.Scrollbar(
            invoices_frame,
            orient="vertical",
            command=invoices_tree.yview
        )
        invoices_tree.configure(yscrollcommand=y_scroll.set)

        x_scroll = ttk.Scrollbar(invoices_frame, orient='horizontal', command=invoices_tree.xview)
        invoices_tree.configure(xscrollcommand=x_scroll.set)

        invoices_tree.grid(row=1 , column=0, columnspan=2, sticky='nesw')
        y_scroll.grid(row=1, column=2, sticky='ns')
        x_scroll.grid(row=2, column=0, columnspan=2, sticky='ew')


            

        self.invoiceObj = Order(None, None, None, None, None, None, None, None, None, None, None)

        self.bookObj = Book("", "", "", 0, 0) 
        
        def getBookPrice(selected_book):
            # Fetch book price from the books list
            books = self.bookObj.getBooks()
            book_price = 0
            book_id = selected_book['book_id']

            for book in books:
                if book["ID"] == int(book_id): # match book ID
                    book_price = book["price"] # get price
                    return book_price
                

        def get_shipping_type(invoice):
            book_price = getBookPrice(invoice) # get price of the book from invoice 

            # Calculation to see if shipping is standard or urgent 
            standard_calc = (invoice['total_price'] - 2) / invoice['quantity'] # standard 
            urgent_calc = (invoice['total_price'] - 5) / invoice['quantity'] # urgent

            if  invoice['shipping'] and standard_calc ==  book_price: # standard shipping
                return "Standard"
            elif invoice['shipping'] and urgent_calc == book_price: # urgent shipping
                return "Urgent"
            else: #no shipping
                return "No Shipping" 
            
            

        def clearTree():
            for item in invoices_tree.get_children():
                invoices_tree.delete(item)

        
        def searchInvoices():
            entry = search_bar.get().strip()

            latest_invoices = self.invoiceObj.getOrders()

            if entry == placeholder or entry == "":
                refreshTreeView(latest_invoices)
                return
            
            try:
                target_id = int(entry)
            except ValueError:
                refreshTreeView(latest_invoices)
                return
            
            matches = []
            for invoice in latest_invoices:
                if int(invoice['order_id']) == target_id:
                    matches.append(invoice)

            clearTree()

            refreshTreeView(matches)


        def validate_search_input(*args):
            entry = search_bar.get().strip()
            if entry.isdigit():
                search_btn.config(state="normal")
            else:
                search_btn.config(state="disabled")

        search_btn = tk.Button(invoices_frame, text="Search", font=('Arial', 12), bg= "#ffd3ad", fg ="#000000", command=searchInvoices)
        search_btn.grid(row=0, column=0, padx=278, pady=10, sticky='w')

        search_bar.bind("<KeyRelease>", validate_search_input)
        validate_search_input()

        def refreshTreeView(invoices):
            try:
                clearTree()
                for invoice in invoices:
                    shipping_cost = 0
                    shipping_type = get_shipping_type(invoice)

                    if shipping_type == "Standard":
                        shipping_cost = 2
                    elif shipping_type == "Urgent":
                        shipping_cost = 5
                    else:
                        shipping_cost = 0

                    invoices_tree.insert(
                        "",
                        tk.END,
                        values=(
                            invoice["order_id"],
                            f"{invoice['customer_fname']} {invoice['customer_lname']}",
                            invoice["email"],
                            invoice["address"],
                            invoice["book_title"],
                            invoice["book_author"],
                            invoice["quantity"],
                            f"£{shipping_cost:.2f}",
                            shipping_type,
                            f"£{invoice['total_price']:.2f}"
                        )
                    )
            except Exception as e:
                pass

        def refreshInvoices():
            latest_invoices = self.invoiceObj.getOrders()
            refreshTreeView(latest_invoices)
            if len(latest_invoices) == 0:
                refresh_button.config(state="disabled")
            else:
                refresh_button.config(state="normal")
        

        #Place Order Button
        refresh_button = tk.Button(self, text="Refresh", font=("Arial", 15), bg="#ffd3ad", height=2, width=14)
        refresh_button.grid(row=7, column=0, columnspan=2, pady=30, sticky="w", padx=30)

        refreshInvoices()
        
        refresh_button.configure(command=refreshInvoices)
        
            