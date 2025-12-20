import os
import pickle 


class Person:
    
    def __init__(self, firstName, lastName, email, address):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._address = address


    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName.strip()

    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName.strip()

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email.strip()

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address.strip()


class Customer(Person):

    def __init__(self, firstName, lastName, email, address):
        super().__init__(firstName, lastName, email, address)

        # Setting up the file path for storing customer data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.file_path = os.path.join(base_dir, "data", "customers.pkl") # data file path

        self.__customerID = self.nextID() # Assigning a unique customer ID
    
    @property
    def customerID(self):
        return self.__customerID
    
    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID
        

    def checkFileExists(self):
        return os.path.isfile(self.file_path)

    def nextID(self):
        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                customers = pickle.load(f)
                if customers:
                    return customers[-1]["ID"] + 1
        return 0

    def read_file(self):
        with open(self.file_path, 'rb') as f:
            user_from_file = pickle.load(f)

        for user in user_from_file:
            print(f"ID: {user["ID"]}, First name: {user["first_name"]}, Last Name: {user["last_name"]}, Email: {user["email"]}, Address: {user["address"]}")

    def createUser(self):
        user = {
            "ID": self.customerID,
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.email,
            "address": self.address
        }

        if self.checkFileExists():
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
        else:
            data = []

        data.append(user)

        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)

        return "User created successfully!"



# TESTING 

# fname = input("Enter fname: ") 
# lname = input("Enter lname: ")
# email = input("Enter email: ")
# address = input("Enter address: ")

# user1 = Customer(fname, lname, email, address)
# user1.createUser()


# with open(user1.file_path, 'rb') as f:
#      user_from_file = pickle.load(f)

# for user in user_from_file:
#     print(f"ID: {user["ID"]}, First name: {user["first_name"]}, Last Name: {user["last_name"]}, Email: {user["email"]}")
#     print(f"Address: {user["address"]}")