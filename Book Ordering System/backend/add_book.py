#importing necessary modules
import os
import pickle 


'''
Stock Class - parent class for Book class which holds common attributes for stock items
'''

class Stock:
    
    #setting up attributes
    def __init__(self, title, author, isbn,price):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = price

    
    #Getters and Setters - to access and modify protected attributes
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title.strip()

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author.strip()
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn.strip()

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
    


'''
Book Class - child class of Stock, represents a book in the inventory
'''

class Book(Stock):

    #setting up attributes
    def __init__(self, title, author, isbn, price, quantity):
        super().__init__(title, author, isbn, price)

        #setting up file path for storing book data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.file_path = os.path.join(base_dir, "data", "books.pkl")

        self.__bookID = self.nextID() # Assigning a unique book ID
        self.__quantity = quantity # Quantity of the book in stock

    
    #Getters and Setters - to access and modify private attributes
    @property
    def bookID(self):
        return self.__bookID
    
    @bookID.setter
    def bookID(self, bookID):
        self.__bookID = bookID

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    #helper method to check if the data file exists
    def checkFileExists(self):
        return os.path.isfile(self.file_path)

    #method to generate the next unique book ID
    def nextID(self):
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                book = pickle.load(f)
                if book:
                    return book[-1]["ID"] + 1
        return 0

    def getBooks(self):
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                books = pickle.load(f)
                return books
        return []

    #method to create and save a new book record
    def createBook(self):
        data_valid = False

        #validating price and quantity inputs
        try:
            int(self.price)
            data_valid = True
        except:
            return "Price must be a number!"
        
        
        try:
            int(self.quantity)
            data_valid = True
        except:
            return "Quantity must be an integer!"

        if  data_valid:          
            book = {
                "ID": self.bookID,
                "title": self.title,
                "author": self.author,
                "isbn": self.isbn,
                "price": float(self.price),
                "quantity": int(self.quantity)
            }

            if self.checkFileExists():
                with open(self.file_path, "rb") as f:
                    data = pickle.load(f)

                if not isinstance(data, list):
                    data = []
            else:
                data = []

            data.append(book)

            with open(self.file_path, "wb") as f:
                pickle.dump(data, f)

            return "Book added successfully!"



# TESTING 

# title = input("Enter title: ") 
# author = input("Enter author: ")
# isbn = input("Enter isbn: ")
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))

# book1 = Book(title, author, isbn, price, quantity)
# book1.createBook()


# with open(book1.file_path, 'rb') as f:
#      book_from_file = pickle.load(f)

# for book in book_from_file:
#     print(f"ID: {book["ID"]}, Title: {book["title"]}, Author: {book["author"]}, ISBN: {book["isbn"]}, Price: {book["price"]}, Quantity: {book["quantity"]}")