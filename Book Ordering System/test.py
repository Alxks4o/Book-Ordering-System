
class Person:

    def __init__(self, address):
        self.__address = address

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address): 
        self.__address = address


class Customer(Person):

    def __init__(self, address):
        super().__init__(address)

    def printAddress(self):
        print(f"Address: {self.address}")

    def setAddress(self):
        new_address = input("Enter new address: ")
        self.address = Person.address(new_address)