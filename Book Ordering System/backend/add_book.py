import os
import pickle 


class Stock:
    
    def __init__(self, title, author, isbn,price):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = price

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
    


class Book(Stock):

    def __init__(self, title, author, isbn, price, quantity):
        super().__init__(title, author, isbn, price)

        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.file_path = os.path.join(base_dir, "data", "books.pkl")

        self.__bookID = self.nextID()
        self.__quantity = quantity


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


    def checkFileExists(self):
        return os.path.isfile(self.file_path)

    def nextID(self):
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                book = pickle.load(f)
                if book:
                    return book[-1]["ID"] + 1
        return 0


    def createBook(self):
        book = {
            "ID": self.bookID,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity
        }

        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
        else:
            data = []

        data.append(book)

        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)

        return "Book added successfully!"



# TESTING 

title = input("Enter title: ") 
author = input("Enter author: ")
isbn = input("Enter isbn: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

book1 = Book(title, author, isbn, price, quantity)
book1.createBook()


with open(book1.file_path, 'rb') as f:
     book_from_file = pickle.load(f)

for book in book_from_file:
    print(f"ID: {book["ID"]}, Title: {book["title"]}, Author: {book["author"]}, ISBN: {book["isbn"]}, Price: {book["price"]}, Quantity: {book["quantity"]}")