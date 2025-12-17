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

        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self.file_path = os.path.join(base_dir, "data", "customers.pkl")

        self.__customerID = self.nextID()
        

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
            print(f"ID: {user["ID"]}, First name: {user["first_name"]}, Last Name: {user["last_name"]}, Email: {user["email"]}")

    def createUser(self):
        user = {
            "ID": self.__customerID,
            "first_name": self._firstName,
            "last_name": self._lastName,
            "email": self._email
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

# user1 = Customer(fname, lname, email)
# user1.createUser()


# with open(, 'rb') as f:
#      user_from_file = pickle.load(f)

# for user in user_from_file:
#     print(f"ID: {user["ID"]}, First name: {user["first_name"]}, Last Name: {user["last_name"]}, Email: {user["email"]}")

customer = Customer(" "," "," ")
customer.read_file()