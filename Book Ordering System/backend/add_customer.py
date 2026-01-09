
#importing necessary modules
import os
import pickle 

'''
Person Class - parent class for Customer class which holds common attributes for a person
'''
class Person:
    
    #setting up attributes
    def __init__(self, firstName, lastName, email, address):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._address = address

    #Getters and Setters - to access and modify protected attributes

    # First Name
    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName.strip()


    # Last Name
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName.strip()

    # Email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email.strip()

    # Address
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address.strip()


'''
Customer Class - child class of Person which holds attributes and methods specific to customers. 
For managing customer records including creating new customers and checking for existing emails.
'''

class Customer(Person):

    #setting up attributes
    def __init__(self, firstName, lastName, email, address):
        super().__init__(firstName, lastName, email, address)

        # Setting up the file path for storing customer data
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        self._file_path = os.path.join(base_dir, "data", "customers.pkl") # data file path

        self.__customerID = self.__nextID() # Assigning a unique customer ID
    

    #Getters and Setters - to access and modify private attributes
    
    # Customer ID
    @property
    def customerID(self):
        return self.__customerID
    
    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID
        

    #helper method to check if the data file exists
    def __checkFileExists(self):
        return os.path.isfile(self._file_path)


    #method to generate the next unique customer ID
    def __nextID(self):
        if self.__checkFileExists():
            with open(self._file_path, "rb") as f: # opening file in read binary mode
                customers = pickle.load(f) # loading existing customer data
                if customers:
                    return customers[-1]["ID"] + 1 # incrementing the last ID by 1
        return 0 # starting ID from 0 if no file exists
    

    # method to retrieve all customers from the data file
    def getCustomers(self):
        if self.__checkFileExists():
            with open(self._file_path, "rb") as f:
                customers = pickle.load(f)
                return customers # returning the list of customers
        return [] # returning empty list if no file exists


    #method to check if an email already exists in the records
    def _checkEmailExists(self):
        if self.__checkFileExists():
            with open(self._file_path, "rb") as f: # opening file in read binary mode
                customers = pickle.load(f)
                for customer in customers: # iterating through existing customers
                    if customer["email"].lower() == self.email.lower(): # case-insensitive email check
                        return True # email exists
        return False # email does not exist


    '''
    Function for validating customer data entries    
    '''
    def _validateCustomerData(self):

        if not self.firstName.strip(): 
            return "First name cannot be empty" # first name empty
        if not self.lastName.strip():
            return "Last name cannot be empty" # last name empty 
        if "@" not in self.email or "." not in self.email:
            return "Email must contain '@' and '.'" # invalid email format
        if not self.address.strip():
            return "Address cannot be empty" # address empty
        return True

    '''
    Main method to create and save a new customer record, ensuring no duplicate emails.
    '''
    def createUser(self):

        # validate customer data before creating customer 
        validation = self._validateCustomerData()
        if validation is not True:
            return validation # returns message

        # checking for existing email
        if self._checkEmailExists():
            return "Email already exists" # returning error message if email exists
        
        # preparing customer data for saving
        user = {
            "ID": self.customerID,
            "first_name": self._firstName,
            "last_name": self._lastName,
            "email": self._email,
            "address": self._address
        }
        
        # loading existing data or initializing new list
        if self.__checkFileExists():
            with open(self._file_path, "rb") as f:
                data = pickle.load(f) 

            if not isinstance(data, list): # ensuring data is a list
                data = [] # initializing empty list if data is not in expected format
        else:
            data = [] # initializing empty list if file does not exist

        data.append(user) # adding new user to data list

        with open(self._file_path, "wb") as f:
            pickle.dump(data, f) # saving updated data back to file

        return "Customer added successfully!" # success message


