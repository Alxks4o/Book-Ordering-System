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
    
    # Title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title.strip()

    # Author

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author.strip()

    # ISBN

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn.strip()

    # Price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
    
class ID:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self._file_path = os.path.join(base_dir, "data", "books.pkl")

        self.__bookID = self.__nextID()

    @property
    def bookID(self):
        return self.__bookID
    
    @bookID.setter
    def bookID(self, bookID):
        self.__bookID = bookID


    #helper method to check if the data file exists
    def __checkFileExists(self):
        return os.path.isfile(self._file_path) 


    #method to generate the next unique book ID
    def __nextID(self):
        try:        
            if self.__checkFileExists(): # checking if file exists
                with open(self._file_path, "rb") as f:
                    book = pickle.load(f) # loading existing book data
                    if book:
                        return book[-1]["ID"] + 1 # generating next ID based on last record
            return 0 # starting ID from 0 if no records exist
        except:
            return 0 # in case of any error, start ID from 0
        


        
'''
Book Class - child class of Stock, represents a book in the inventory. Handles book-specific attributes and methods for managing book records.
'''

class Book(Stock, ID):

    def __init__(self, title, author, isbn, price, quantity):
        Stock.__init__(self, title, author, isbn, price)
        ID.__init__(self)

        base_dir = os.path.dirname(os.path.dirname(__file__))
        self._file_path = os.path.join(base_dir, "data", "books.pkl")

        self.__quantity = quantity
    
    
    # Getters and Setters - to access and modify private attributes

    # Quantity

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity


    #helper method to check if the data file exists
    def __checkFileExists(self):
        return os.path.isfile(self._file_path) 



    def getBooks(self):
        if not self.__checkFileExists(): # checking if file exists
            return [] # returning empty list if no file
        try:
            with open(self._file_path, "rb") as f: # loading existing book data
                books = pickle.load(f) 
            
            if isinstance(books, list): # checking if data is in list format
                return books # returning list of books
            else:
                return [] # returning empty list if data is not in expected format
            
        except Exception:
            return [] # returning empty list in case of any error

    '''
    Function for validating book data
    '''
    def _validateBookData(self):
        # check data is valid
        try:
            float(self.price)
            int(self.quantity)
            return True # dadta is valid
        except:
            return False # data is invalid


    '''
    Main method to create and save a new book record, returns success or error message.
    '''
    def createBook(self):
        #validating price and quantity inputs
        if not self._validateBookData():
            return "Invalid Book Data"
        

        # If all data is valid, proceed to create and save the book record

        # Build book dictionary
        book = {
            "ID": self.bookID,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": float(self.price),
            "quantity": int(self.quantity)
        }


        # Load existing data or create a new list 

        if self.__checkFileExists():
            with open(self._file_path, "rb") as f: # loading existing book data
                data = pickle.load(f)

            if not isinstance(data, list): # checking if data is in list format
                data = []
        else:
            data = [] # initializing empty list if file does not exist

        
        # add new book 

        data.append(book) 

        # saving book to file
        
        with open(self._file_path, "wb") as f:
            pickle.dump(data, f) 

        return "Book added successfully!" # success message



