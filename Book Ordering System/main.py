import tkinter as tk
import os

#importing backend modules
from backend.add_customer import Customer

#importing pages
import pages.AddPage as AddCustomer
import pages.Homepage as HomepageFunc
import pages.PlaceOrderPage as PlaceOrderFunc
import pages.ViewInvoices as ViewInvoicesFunc


# setting up file path 
current_dir = os.path.dirname(__file__)

# logo filepath
window_logo_filepath = os.path.join(current_dir, "assets", "window-logo.ico")

nav_logo_filepath = os.path.join(current_dir, "assets", "nav-logo.png")


# Function to switch frames
def showFrame(frame):
    frame.tkraise()

#creating window
window = tk.Tk()

#setting window size
window.geometry("1000x900")
window.minsize(1000, 900)
window.iconbitmap(window_logo_filepath) # setting logo
window.title("Book Ordering System")

#setting window grid configuration
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


'''
NAVIGATION - This is where the navigation buttons will go
'''

#navigation frame
navigation = tk.Frame(window, bg='#ffe9d6')
navigation.grid(row=0, column=0, sticky='ns')

nav_logo = tk.PhotoImage(file=nav_logo_filepath).subsample(4, 4) # logo size

# logo style 
logo_label = tk.Label(navigation, image=nav_logo, bg="#ffe9d6")
logo_label.image = nav_logo
logo_label.pack(side="bottom", pady=20)

nav_label = tk.Label(navigation, text="Book Ordering System", font=("Arial", 22, "bold"), bg="#ffe9d6", fg="#202020"
).pack(fill='x', padx=15, pady=(10,50))


#buttons quick design 
button_style = {
    "font": ("Arial", 14, "bold"),
    "height": 2,
    "width": 14,
    "bg": "#ffd3ad",
    "fg": "#202020"
}

#HOME PAGE
homeButton = tk.Button(
    navigation,
    **button_style,
    text= "Home",
    command=lambda: showFrame(home)
).pack(fill='x', padx=15, pady=8)


#button for adding customers 
addCustomerButton = tk.Button(
    navigation,
    **button_style,
    text= "Add",
    command=lambda: showFrame(add)
).pack(fill='x', padx=15, pady=8)


#button for placing orders 
placeOrderButton = tk.Button(
    navigation,
    **button_style,
    text= "Place Order",
    command=lambda: showFrame(placeOrder)
).pack(fill='x', padx=15, pady=8)


#button for viewing invoices 
viewInvoicesButton = tk.Button(
    navigation,
    **button_style,
    text= "View Invoices",
    command=lambda: showFrame(viewInvoices)
).pack(fill='x', padx=15, pady=8)



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



#show home page by default
showFrame(home)


#running the window
window.mainloop()