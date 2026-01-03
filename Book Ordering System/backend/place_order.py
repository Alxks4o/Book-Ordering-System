import pickle
import os


class Order:

    def __init__(self, book_id, customer_id, fname, lname, book_title, book_author, email, quantity):
        #setting up file path for storing order data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.orders_file_path = os.path.join(base_dir, "data", "orders.pkl")
        self.books_file_path = os.path.join(base_dir, "data", "books.pkl")

        self.__order_id = self.nextID()
        self._customer_firstname = fname
        self._customer_lastname = lname
        self._book_title = book_title
        self._book_author = book_author
        self.__book_id = book_id
        self.__customer_id = customer_id
        self._email = email
        self._quantity = quantity
        self._total_price = 0

        
    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = order_id
    

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id

    
    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    #method to generate the next unique order ID
    def nextID(self):
        if self.checkFileExists(self.orders_file_path):
            with open(self.orders_file_path, "rb") as f:
                order = pickle.load(f)
                if order:
                    return order[-1]["order_id"] + 1
        return 0

    #helper method to check if the data file exists
    def checkFileExists(self, path):
        return os.path.isfile(path)

    def calculateTotalPrice(self, unit_price):
        price = unit_price
        quantity = int(self._quantity)
        self._total_price = price * quantity
        
    
    def getOrders(self):
        if self.checkFileExists(self.orders_file_path):
            with open(self.orders_file_path, "rb") as f:
                orders = pickle.load(f)
                return orders
        return []
    

    def updateQuantity(self):
        book_selected = {}
        
        if self.checkFileExists(self.books_file_path):
            with open(self.books_file_path, "rb") as f:
                books = pickle.load(f)
            
        for book in books:
            if book["ID"] == self.__book_id:
                book_selected = book
                break

        if int(self._quantity) > book_selected["quantity"] :
            print("Insufficient stock for the order.")
            print(f"Available stock: {book_selected['quantity']}, Requested: {self._quantity}")
        else:            
            new_book = book_selected["quantity"] - int(self._quantity)
            with open(self.books_file_path, "wb") as f:
                pickle.dump(new_book, f)
           
            print(f"Updated stock for book ID {self.__book_id}: {new_book} remaining.")
            return True
                            
            
            
                

            



    def placeOrder(self):

        if not self.updateQuantity():
            return "Order failed due to insufficient stock."
    
        order = {
            "order_id": self.__order_id,
            "customer_fname": self._customer_firstname,
            "customer_lname": self._customer_lastname,
            "book_title": self._book_title,
            "book_author": self._book_author,
            "email": self._email,
            "quantity": self._quantity,
            "total_price": self._total_price
        }
        

        if self.checkFileExists(self.orders_file_path):
            with open(self.orders_file_path, "rb") as f:
                data = pickle.load(f)
        else:
            data = []
        
        data.append(order)

        with open(self.orders_file_path, "wb") as f:
            pickle.dump(data, f)

        return "Order placed successfully!"
