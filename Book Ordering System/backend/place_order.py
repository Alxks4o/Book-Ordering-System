import pickle
import os

'''
Order class to handle book orders, including calculating total price, updating stock, and storing order details. 
'''

class Order:

    '''
    Initializes an Order object with customer and book details.
    '''
    def __init__(self, book_id, customer_id, fname, lname, address, book_title, book_author, email, quantity, shipping, urgent_shipping):

        #setting up file path for storing order data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        
        # orders file path
        self.orders_file_path = os.path.join(base_dir, "data", "orders.pkl")

        # books file path
        self.books_file_path = os.path.join(base_dir, "data", "books.pkl")

        # initializing order attributes
        self.__order_id = self.nextID()
        self._customer_firstname = fname
        self._customer_lastname = lname
        self._address = address
        self._book_title = book_title
        self._book_author = book_author
        self.__book_id = book_id
        self.__customer_id = customer_id
        self._email = email
        self._quantity = quantity
        self._shipping = shipping
        self._urgent_shipping = urgent_shipping
        self._total_price = 0

    
    '''
    Getters and Setters for order_id, book_id, and customer_id
    '''

    # Order ID

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = order_id
    

    # Book ID

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id


    # Customer ID

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id


    '''
    Method to get the next available order ID, by checking the existing orders file.
    '''
    def nextID(self):
        #check if orders file exists and get the last order ID
        if self.checkFileExists(self.orders_file_path):
            with open(self.orders_file_path, "rb") as f: # open in read binary mode
                order = pickle.load(f)
                if order:
                    return order[-1]["order_id"] + 1 # increment last order ID and add 1 to it 
                
        return 0 # if no orders exist, start from 0

    '''
    Method to check if a file exists at the given path.
    '''
    def checkFileExists(self, path):
        return os.path.isfile(path)




    '''
    Method to calculate the total price of the order, including shipping costs.
    '''

    def calculateTotalPrice(self, unit_price):

        if self._shipping and not self._urgent_shipping: # standard shipping
            price = unit_price 
            quantity = int(self._quantity)
            self._total_price = (price * quantity) + 2.00 # adds 2 for standard shipping

        elif self._shipping and self._urgent_shipping: # urgent shipping
            price = unit_price 
            quantity = int(self._quantity)
            self._total_price = (price * quantity) + 5.00 # adds 5 for urgent shipping

        else: # no shipping
            price = unit_price
            quantity = int(self._quantity)
            self._total_price = price * quantity # no shipping cost added
        
    '''
    Method to retrieve existing orders from the orders file.
    '''

    def getOrders(self):
        if self.checkFileExists(self.orders_file_path): # check if orders file exists
            with open(self.orders_file_path, "rb") as f:
                orders = pickle.load(f)
                return orders # return list of orders
            
        return [] # return empty list if no orders exist
    

    '''
    Method to update the stock quantity of the ordered book in the books file.
    '''

    def updateQuantity(self):
        
        # read existing books from books file
        with open(self.books_file_path, "rb") as f:
            books = pickle.load(f)
        
        # update the quantity of the ordered book
        for book in books:
            if book["ID"] == int(self.__book_id): # match book ID

                if int(self._quantity) > book["quantity"]: # check if enough stock is available
                    return False
                
                book["quantity"] -= int(self._quantity) # reduce stock by ordered quantity
        
        with open(self.books_file_path, "wb") as f:
            pickle.dump(books, f) # write updated books back to file
        
        return True # return True if stock updated successfully
     
        
    '''
    Main method to place the order, update stock, and store order details.
    '''
    def placeOrder(self):

        # Check if stock is sufficient before placing the order
        if not self.updateQuantity():
            return "Order failed due to insufficient stock."

        # Create order dictionary to store order details
        order = {
            "order_id": self.__order_id,
            "customer_fname": self._customer_firstname,
            "customer_lname": self._customer_lastname,
            "address": self._address,
            "book_id": self.__book_id,
            "customer_id": self.__customer_id,
            "book_title": self._book_title,
            "book_author": self._book_author,
            "email": self._email,
            "quantity": self._quantity,
            "shipping": self._shipping,
            "total_price": self._total_price
        }
        
        # Read existing orders, append the new order, and write back to file

        if self.checkFileExists(self.orders_file_path):
            with open(self.orders_file_path, "rb") as f:
                data = pickle.load(f) # load existing orders
        else:
            data = [] # initialize empty list if no orders exist
        
        data.append(order) # add new order to list

        with open(self.orders_file_path, "wb") as f:
            pickle.dump(data, f) # write updated orders back to file

        return "Order placed successfully!" # return success message
