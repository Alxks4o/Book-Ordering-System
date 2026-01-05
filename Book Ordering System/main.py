import tkinter as tk

#importing backend modules
from backend.add_customer import Customer

#importing pages
import pages.AddPage as AddCustomer
import pages.Homepage as HomepageFunc
import pages.PlaceOrderPage as PlaceOrderFunc
import pages.ViewInvoices as ViewInvoicesFunc
import pages.SearchInvoices as SearchInvoicesFunc

# Function to switch frames
def showFrame(frame):
    frame.tkraise()

#creating window
window = tk.Tk()

#setting window size
window.geometry("1000x900")
window.minsize(1000, 900)

#setting window grid configuration
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


'''
NAVIGATION - This is where the navigation buttons will go
'''

#navigation frame
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
    text= "Add",
    command=lambda: showFrame(add)
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
FRAMES - This is where the content of each page will go
'''

#Dashboard window frame
main = tk.Frame(window, bg="#e9bb8d")
main.grid(row=0, column=1, sticky='nsew')


#home page frame
home = HomepageFunc.HomePage(main)
home.grid(row=0, column=0, sticky='nsew')


#add customer page frame
add = AddCustomer.AddPage(main)
add.grid(row=0, column=0, sticky="nsew")


#place order page frame
placeOrder = PlaceOrderFunc.PlaceOrderPage(main)
placeOrder.grid(row=0, column=0, sticky='nsew')


#view invoices page frame
viewInvoices = ViewInvoicesFunc.ViewInvoices(main)
viewInvoices.grid(row=0, column=0, sticky='nsew')


#search invoices page frame
searchInvoices = SearchInvoicesFunc.SearchInvoices(main)
searchInvoices.grid(row=0, column=0, sticky='nsew')


#show home page by default
showFrame(viewInvoices)


#running the window
window.mainloop()