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

        invoices_tree = ttk.Treeview(
            invoices_frame,
            columns=("order_id", "customer_name", "address", "book_title", "book_author", "quantity", "shipping_cost", "shipping_type", "total_price"),
            show="headings",
            height=15
        )

        invoices_tree.heading("order_id", text="Order ID")
        invoices_tree.heading("customer_name", text="Customer Name")
        invoices_tree.heading("address", text="Address")
        invoices_tree.heading("book_title", text="Book Title")
        invoices_tree.heading("book_author", text="Book Author")
        invoices_tree.heading("quantity", text="Quantity")
        invoices_tree.heading("shipping_cost", text="Shipping Cost")
        invoices_tree.heading("shipping_type", text="Shipping Type")
        invoices_tree.heading("total_price", text="Total Price")

        invoices_tree.column("order_id", width=80, anchor="center")
        invoices_tree.column("customer_name", width=150, anchor="center")
        invoices_tree.column("address", width=200, anchor="center")
        invoices_tree.column("book_title", width=150, anchor="center")
        invoices_tree.column("book_author", width=150, anchor="center")
        invoices_tree.column("quantity", width=80, anchor="center")
        invoices_tree.column("shipping_cost", width=100, anchor="center")
        invoices_tree.column("shipping_type", width=120, anchor="center")
        invoices_tree.column("total_price", width=100, anchor="center")

        invoice_scroll = ttk.Scrollbar(
            invoices_frame,
            orient="vertical",
            command=invoices_tree.yview
        )
        invoices_tree.configure(yscrollcommand=invoice_scroll.set)
        invoice_scroll.pack(side="right", fill="y")

            

        self.invoiceObj = Order(None, None, None, None, None, None, None, None, None, None, None)

        self.bookObj = Book("", "", "", 0, 0) 
        
        def getBookPrice(x):
            # Fetch book price from the books list
            books = self.bookObj.getBooks()
            book_price = 0
            book_id = x['book_id']

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
            

            
        invoices = self.invoiceObj.getOrders()
        try:
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
                        invoice["address"],
                        invoice["book_title"],
                        invoice["book_author"],
                        invoice["quantity"],
                        f"£{shipping_cost:.2f}",
                        shipping_type,
                        f"£{invoice['total_price']:.2f}"
                    )
                )
        except:
            pass
        
        invoices_tree.pack()
