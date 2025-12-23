import tkinter as tk
from tkinter import ttk
from backend.add_customer import Customer
from backend.add_book import Book

class AddPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5e6c8")

        #Setting up tabs
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TNotebook', background="#e9bb8d", borderwidth=0, padding=40)
        style.configure('TNotebook.Tab', background='#f5e6c8', font=('Arial', 15), padding=10)
        style.map(
            'TNotebook.Tab',
            background=[('selected', "#fed8c0")],
            foreground=[('selected', 'black')]                  
                  )  
        
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)



        '''
        
        TAB FOR ADDING CUSTOMERS

        '''


        # Create a tab for adding customers
        add_customer_tab = tk.Frame(notebook, bg="#e9bb8d", bd=0, highlightthickness=0)
        notebook.add(add_customer_tab, text="Add Customer")

        tk.Label(add_customer_tab, text="Add Customer", font=("Arial", 25, "bold"), bg="#e9bb8d")\
            .grid(row=0, column=0, columnspan=2, pady=(40, 20))

        # First Name Label
        tk.Label(add_customer_tab, text="First Name", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=1, column=0, sticky="w", padx=50, pady=10)

        self.first_name_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.first_name_entry.grid(row=2, column=0, padx=50, pady=10)

        # Last Name Label
        tk.Label(add_customer_tab, text="Last Name", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=3, column=0, columnspan=2, sticky="w", padx=50, pady=10)

        self.last_name_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.last_name_entry.grid(row=4, column=0, padx=50, pady=10)

        # Email Label
        tk.Label(add_customer_tab, text="Email", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=5, column=0, sticky="w", padx=50, pady=10)

        self.email_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.email_entry.grid(row=6, column=0, padx=50, pady=10)

        # Address Label
        tk.Label(add_customer_tab, text="Address", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=7, column=0, sticky="w", padx=50, pady=10)

        self.address_entry = tk.Entry(add_customer_tab, font=("Arial", 15))
        self.address_entry.grid(row=8, column=0, padx=50, pady=10)

        # Message Label
        self.message_label_user = tk.Label(add_customer_tab, text="", font=("Arial", 12), bg="#e9bb8d")
        self.message_label_user.grid(row=9, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(add_customer_tab, text="Add Customer", font=("Arial", 15), command=self.addCustomerFunc)\
            .grid(row=10, column=0, sticky="nws", padx=50, pady=20)

        tk.Button(add_customer_tab, text="Clear", font=("Arial", 15), command=self.clearEntries)\
            .grid(row=10, column=0, sticky="nes", padx=50, pady=20)



        '''
        
        TAB FOR ADDING BOOKS
        
        '''

        add_book_tab = tk.Frame(notebook, bg="#e9bb8d", bd=0, highlightthickness=0)
        notebook.add(add_book_tab, text="Add Book")

        # Add Book Tab Content
        tk.Label(add_book_tab, text="Add Book",font=("Arial", 25, "bold"), bg="#e9bb8d") \
            .grid(row=0, column=0, columnspan=2,padx=30, pady=(40, 20))

        # Title Label
        tk.Label(add_book_tab, text="Title", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=1, column=0, sticky="w", padx=50, pady=10)

        self.title_entry = tk.Entry(add_book_tab, font=("Arial", 15))
        self.title_entry.grid(row=2, column=0, padx=50, pady=10)

        # Author Label
        tk.Label(add_book_tab, text="Author", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=3, column=0, sticky="w", padx=50, pady=10)

        self.author_entry = tk.Entry(add_book_tab, font=("Arial", 15))
        self.author_entry.grid(row=4, column=0, padx=50, pady=10)

        # ISBN Label
        tk.Label(add_book_tab, text="ISBN", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=5, column=0, sticky="w", padx=50, pady=10)

        self.isbn_entry = tk.Entry(add_book_tab, font=("Arial", 15))
        self.isbn_entry.grid(row=6, column=0, padx=50, pady=10)

        # Price Label
        tk.Label(add_book_tab, text="Price", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=7, column=0, sticky="w", padx=50, pady=10)

        self.price_entry = tk.Entry(add_book_tab, font=("Arial", 15))
        self.price_entry.grid(row=8, column=0, padx=50, pady=10)

        # Quantity Label
        tk.Label(add_book_tab, text="Quantity", font=("Arial", 15), bg="#e9bb8d")\
            .grid(row=9, column=0, sticky="w", padx=50, pady=10)

        self.quantity_entry = tk.Entry(add_book_tab, font=("Arial", 15))
        self.quantity_entry.grid(row=10, column=0, padx=50, pady=10)

        # Message Label
        self.message_label_book = tk.Label(add_book_tab, text="", font=("Arial", 12), bg="#e9bb8d")
        self.message_label_book.grid(row=11, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(add_book_tab, text="Add Book", font=("Arial", 15), command=self.addBookFunc)\
            .grid(row=12, column=0, sticky="nws", padx=50, pady=20)
        tk.Button(add_book_tab, text="Clear", font=("Arial", 15), command=self.clearEntries)\
            .grid(row=12, column=0, sticky="nes", padx=50, pady=20)

    def clearEntries(self, *args):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def addBookFunc(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        price = self.price_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not title or not author or not isbn or not price or not quantity:
            self.message_label_book.config(text="All fields are required.", fg="red")
            return
        
        book = Book(title, author, isbn, price, quantity)
        book.createBook()

        if book.createBook() != "Book added successfully!":
            self.message_label_book.config(text=book.createBook(), fg="red")
        else:
            self.message_label_book.config(text=book.createBook(), fg="green")
            self.clearEntries(title, author, isbn, price, quantity)


    def addCustomerFunc(self):
        firstName = self.first_name_entry.get().strip()
        lastName = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not firstName or not lastName or not email or not address:
            self.message_label_user.config(text="All fields are required.", fg="red")
            return

        user = Customer(firstName, lastName, email, address)
        user.createUser()
        print(user.createUser())

        if user.createUser() != "Customer added successfully!":
            self.message_label_user.config(text=user.createUser(), fg="red")
        else:
            self.message_label_user.config(text=user.createUser(), fg="green")
            self.clearEntries(firstName, lastName, email, address)
            print("Customer added successfully!")