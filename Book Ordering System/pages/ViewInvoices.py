import tkinter as tk
from tkinter import ttk

from backend.place_order import Order
from backend.add_book import Book

class ViewInvoices(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e9bb8d")

        tk.Label(self, text="View Invoices",font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))
        

        # Frame for the invoices 
        invoices_frame = tk.Frame(self, bg="#e9bb8d")
        invoices_frame.grid(row=2, column=0, padx=30, pady=10, sticky='w')


        
        
        placeholder = "Enter order ID" # placeholder value for search bar

        '''
        Function for setting placeholdder when user hasn't clicked on input field 
        '''
        def set_placeholder(e=None):
            if search_bar.get() == "": # searchbar is empty
                search_bar.insert(0, placeholder) # insert placeholder
                search_bar.config(fg="grey") # set to grey

        '''
        Function for clearing placeholdder when user clicks on input field 
        '''
        def clear_placeholder(e=None):
            if search_bar.get() == placeholder: # searchbar has been clicked
                search_bar.delete(0, tk.END) # clear placeholder
                search_bar.config(fg="black") # set to black
            
        
        # Search bar entry 
        search_bar = tk.Entry(invoices_frame, width=20, font=('Arial', 18))
        search_bar.grid(row=0, column=0, padx=(0, 10), pady=10, sticky = 'w')

        set_placeholder()

        search_bar.bind("<FocusIn>", clear_placeholder) # User clicks on searchbar
        search_bar.bind("<FocusOut>", set_placeholder) # User clicks off searchbar



        # setting up treeview for invoices 
        invoices_tree = ttk.Treeview(
            invoices_frame,
            columns=("order_id", "customer_name", "email", "address", "book_title", "book_author", "quantity", "shipping_type", "total_price"),
            show="headings",
            height=35
        )


        # HEADINGS # 

        invoices_tree.heading("order_id", text="Order ID")
        invoices_tree.heading("customer_name", text="Customer Name")
        invoices_tree.heading("email", text="Email")
        invoices_tree.heading("address", text="Address")
        invoices_tree.heading("book_title", text="Book Title")
        invoices_tree.heading("book_author", text="Book Author")
        invoices_tree.heading("quantity", text="Quantity")
        invoices_tree.heading("shipping_type", text="Shipping Type")
        invoices_tree.heading("total_price", text="Total Price")


        
        # COLUMNS #

        invoices_tree.column("order_id", width=80, anchor="center")
        invoices_tree.column("customer_name", width=150, anchor="center")
        invoices_tree.column("email", width=150, anchor="center")
        invoices_tree.column("address", width=150, anchor="center")
        invoices_tree.column("book_title", width=150, anchor="center")
        invoices_tree.column("book_author", width=150, anchor="center")
        invoices_tree.column("quantity", width=80, anchor="center")
        invoices_tree.column("shipping_type", width=120, anchor="center")
        invoices_tree.column("total_price", width=70, anchor="center")


        # Scroll bar configuration 
        y_scroll = ttk.Scrollbar(
            invoices_frame,
            orient="vertical",
            command=invoices_tree.yview
        )
        invoices_tree.configure(yscrollcommand=y_scroll.set)

        invoices_tree.grid(row=1 , column=0, columnspan=2, sticky='nesw')
        y_scroll.grid(row=1, column=2, sticky='ns')


            
        # setting up the Order object for retrieving the orders from file
        self.invoiceObj = Order(None, None, None, None, None, None, None, None, None, None, None)
        
        #setting up book object for getting book data 
        self.bookObj = Book("", "", "", 0, 0) 
        
        '''
        Function for getting each book price
        '''
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
            
            

        # deletes the values inside the table
        def clearTree():
            for item in invoices_tree.get_children():
                invoices_tree.delete(item)

        '''
        Function which will run when value is entered inside the search bar and the search button is clicked.
        '''
        def searchInvoices():
            entry = search_bar.get().strip() # get entry

            latest_invoices = self.invoiceObj.getOrders() # get latest orders/invoices

            if entry == placeholder or entry == "": # validate data
                refreshTreeView(latest_invoices) 
                return
            
            try:
                target_id = int(entry) # validating entry is int
            except ValueError:
                refreshTreeView(latest_invoices)
                return
            
            matches = []
            for invoice in latest_invoices: # get invoices
                if int(invoice['order_id']) == target_id: # match search bar entry with database ID 
                    matches.append(invoice) # add invoice if match

            clearTree()

            refreshTreeView(matches)

        # validation for search bar 
        def validate_search_input(*args):
            entry = search_bar.get().strip()
            if entry.isdigit():
                search_btn.config(state="normal") # entry valid
            else:
                search_btn.config(state="disabled") # entry invalid 

        # Search button
        search_btn = tk.Button(invoices_frame, text="Search", font=('Arial', 12), bg= "#ffd3ad", fg ="#000000", command=searchInvoices)
        search_btn.grid(row=0, column=0, padx=278, pady=10, sticky='w')

        search_bar.bind("<KeyRelease>", validate_search_input) # check search bar when key is released
        validate_search_input()

        '''
        Function which reloads all of the invoices inside the table including latest orders
        '''
        def refreshTreeView(invoices):
            try:
                clearTree() # clear table
                for invoice in invoices:
                    shipping_type = get_shipping_type(invoice) 

                    # layout of values being enterd inside of the treeview 
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
                            shipping_type,
                            f"£{invoice['total_price']:.2f}"
                        )
                    )
            except Exception as e:
                pass
        
        '''
        Function which loads latest orders/invoices in the table (used for the refresh button)
        '''
        def refreshInvoices():
            latest_invoices = self.invoiceObj.getOrders() # get latest orders
            refreshTreeView(latest_invoices) 
            if len(latest_invoices) == 0:
                refresh_button.config(state="disabled") # no invoices, disable refresh button 
            else:
                refresh_button.config(state="normal") # invoices exist, enable refresh button 
        

        #Place Order Button
        refresh_button = tk.Button(self, text="Refresh", font=("Arial", 15), bg="#ffd3ad", height=2, width=14)
        refresh_button.grid(row=7, column=0, columnspan=2, pady=30, sticky="w", padx=30)

        refreshInvoices()
        
        refresh_button.configure(command=refreshInvoices)
        
            