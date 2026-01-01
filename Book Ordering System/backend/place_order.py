import pickle
import os


class Order:

    def __init__(self, book_id, customer_id, fname, lname, book_title, book_author, email, quantity):
        #setting up file path for storing order data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.file_path = os.path.join(base_dir, "data", "orders.pkl")

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
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                order = pickle.load(f)
                if order:
                    return order[-1]["order_id"] + 1
        return 0

    #helper method to check if the data file exists
    def checkFileExists(self):
        return os.path.isfile(self.file_path)

    def calculateTotalPrice(self, unit_price):
        price = unit_price
        quantity = int(self._quantity)
        self._total_price = price * quantity
        
    
    def getOrders(self):
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                orders = pickle.load(f)
                return orders
        return []

    def placeOrder(self):
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

        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
        else:
            data = []
        
        data.append(order)

        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)
        
        print(self.getOrders())
        return "Order placed successfully!"
    




