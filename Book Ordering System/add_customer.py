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
        self.__customerID = self.nextID("customers.pkl")

    def checkFileExists(self, filepath):
        return os.path.isfile(filepath)
    

    def nextID(self, filepath):
        if self.checkFileExists(filepath):
            with open(filepath, 'rb') as f:
                loaded_customers = pickle.load(f)

                if loaded_customers:


                    # Get last customer
                    last_customer = loaded_customers[-1]

                    # If it's a dict
                    if isinstance(last_customer, dict):
                        return last_customer["ID"] + 1
                    else:
                        return last_customer.ID + 1

        # If file doesn't exist or is empty
        return 0

    def createUser(self):
        user = {
            "ID": self.__customerID,
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
        

fname = input("Enter fname: ") 
lname = input("Enter lname: ")
email = input("Enter email: ")

user1 = Customer(fname, lname, email)
user1.createUser()


with open('customers.pkl', 'rb') as f:
     user_from_file = pickle.load(f)

for user in user_from_file:
    print(f"ID: {user["ID"]}, First name: {user["first_name"]}, Last Name: {user["last_name"]}, Email: {user["email"]}")