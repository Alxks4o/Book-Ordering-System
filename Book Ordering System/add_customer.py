import os
import pickle 

class Person:
    
    def __init__(self, firstName, lastName, email):
        self._firstName = firstName
        self._lastName = lastName
        self.__email = email


class Customer(Person):

    def __init__(self, firstName, lastName, email):
        super().__init__(firstName, lastName, email)
        self.__customerID = 0

    def checkFileExists(self, filepath):
        return os.path.isfile(filepath)
    
    
    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value


    @property
    def sname(self):
        return self._sname

    @sname.setter
    def sname(self, value):
        self._sname = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


    @property
    def customerid(self):
        return self._customerid

    def createUser(self):
        
        if self.checkFileExists() != True:
            
