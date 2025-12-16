import os
import pickle 

class Person:
    
    def __init__(self, firstName, lastName, email):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email


class Customer(Person):

    def __init__(self, firstName, lastName, email):
        super().__init__(firstName, lastName, email)
        self.__customerID = 0

    def checkFileExists(self, filepath):
        return os.path.isfile(filepath)
    

    @property
    def userID(self):
        return self.__customerID

    @userID.setter
    def userID(self, value):
        self.__customerID= value

    def nextID(self, filepath):
        if self.checkFileExists(filepath) == True:
            with open(filepath, 'rb') as f:
                loaded_customers = pickle.load(f)
        
        return loaded_customers


    def createUser(self):
        user = {
            "ID":self.nextID(),
            'first_name': self._firstName,
            'last_name': self._lastName,
            'email': self._email
        }


        if self.checkFileExists('customers.pkl') == True:
            with open('customers.pkl', 'rb') as f:
                data = pickle.load(f)
        else:
            data = []

        data.append(user)

        with open('customers.pkl', 'wb') as f:
            pickle.dump(data, f)
        

# fname = input("Enter fname: ") 
# lname = input("Enter lname: ")
# email = input("Enter email: ")

# user1 = Customer(fname, lname, email)
# user1.createUser()


# with open('customers.pkl', 'rb') as f:
#      user_from_file = pickle.load(f)

# print(user_from_file)
