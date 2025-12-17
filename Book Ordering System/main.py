import tkinter as tk
from backend.add_customer import Customer
import pages.AddCustomerPage as AddCustomer

def showFrame(frame):
    frame.tkraise()

#creating window
window = tk.Tk()

#setting window size
window.geometry("800x500")
window.minsize(800, 600)

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


'''
NAVIGATION
'''

navigation = tk.Frame(window, bg='#ffe9d6')
navigation.grid(row=0, column=0, sticky='ns')



#buttons quick design 
button_style = {
    "font": ("Arial", 14),
    "height": 2,
    "width": 14,
    "bg": "#ffd3ad"
}

#HOME PAGE
homeButton = tk.Button(
    navigation,
    **button_style,
    text= "Home",
    command=lambda: showFrame(home)
).pack(fill='x')


#button for adding customers 
addCustomerButton = tk.Button(
    navigation,
    **button_style,
    text= "Add Customer",
    command=lambda: showFrame(addCustomer)
).pack(fill='x')


#button for adding books
addBookButton = tk.Button(
    navigation,
    **button_style,
    text= "Add Book",
    command=lambda: showFrame(addBook)
).pack(fill='x')


#button for placing orders 
placeOrderButton = tk.Button(
    navigation,
    **button_style,
    text= "Place Order",
    command=lambda: showFrame(placeOrder)
).pack(fill='x')


#button for viewing invoices 
viewInvoicesButton = tk.Button(
    navigation,
    **button_style,
    text= "View Invoices",
    command=lambda: showFrame(viewInvoices)
).pack(fill='x')


#Button for searching through invoices 
searchInvoicesButton = tk.Button(
    navigation,
    **button_style,
    text= "Search Invoices",
    command=lambda: showFrame(searchInvoices)
).pack(fill='x')



'''
FRAMES
'''

#Dashboard buttons frame
main = tk.Frame(window, bg="#f5e6c8")
main.grid(row=0, column=1, sticky='nsew')


home = tk.Frame(main, bg="#f5e6c8")
home.grid(row=0, column=0, sticky='nsew')

tk.Label(home, text="Welcome to Book Management", font="Arial, 20", bg="#f5e6c8").pack(padx=100, pady=40, anchor='center', expand=True)

addCustomer = AddCustomer.AddCustomerPage(main)
addCustomer.grid(row=0, column=0, sticky="nsew")


addBook = tk.Frame(main, bg="#f5e6c8")
addBook.grid(row=0, column=0, sticky='nsew')

tk.Label(addBook, text="Add Book", font="Arial, 20", bg="#f5e6c8").pack(padx=100, pady=40, anchor='center', expand=True)



placeOrder = tk.Frame(main, bg="#f5e6c8")
placeOrder.grid(row=0, column=0, sticky='nsew')

tk.Label(placeOrder, text="Place Order", font="Arial, 20", bg="#f5e6c8").pack(padx=100, pady=40, anchor='center', expand=True)




viewInvoices = tk.Frame(main, bg="#f5e6c8")
viewInvoices.grid(row=0, column=0, sticky='nsew')

tk.Label(viewInvoices, text="View Invoices", font="Arial, 20", bg="#f5e6c8").pack(padx=100, pady=40, anchor='center', expand=True)



searchInvoices = tk.Frame(main, bg="#f5e6c8")
searchInvoices.grid(row=0, column=0, sticky='nsew')

tk.Label( searchInvoices, text="Search Invoices", font="Arial, 20", bg="#f5e6c8").pack(padx=100, pady=40, anchor='center', expand=True)



showFrame(addCustomer)

window.mainloop()