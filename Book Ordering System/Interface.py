import tkinter as tk
from tkinter import messagebox


#creating window
window = tk.Tk()

#setting window size
window.geometry("800x500")
window.minsize(800, 600)


#creating canvas for notepad background
canvas = tk.Canvas(window, bg="#f5e6c8", highlightthickness=0)
canvas.pack(fill="both", expand=True)

#drawing notepad lines
def draw_notepad_lines(event=None):
    canvas.delete("lines")
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    for i in range(0, width, 40):
        canvas.create_line(i, 0, i, height, fill="#e0d4b8", tags="lines")
canvas.bind("<Configure>", draw_notepad_lines)


#add customer form
def open_add_customer_form():
    form = tk.Toplevel(window)
    form.title("Add Customer")
    form.geometry("400x300")
    form.resizable(False, False)

    tk.Label(form, text="Customer Name").pack()
    tk.Entry(form).pack()

    tk.Label(form, text="Email").pack()
    tk.Entry(form).pack()

    tk.Button(form, text="Save").pack(pady=10)

#title at the top of the page 
title = tk.Label(
    canvas,
    text="Book Ordering System",
    font=("Arial", 28, "bold"),
    bg="#f5e6c8"
)
title.pack(padx=40, pady=50)

#Dashboard buttons frame
mainPageFrame = tk.Frame(canvas, bg="#f5e6c8")
mainPageFrame.pack()

#buttons quick design 
button_style = {
    "font": ("Arial", 14),
    "height": 2,
    "width": 20,
    "bg": "#ffe9d6"
}

#button for adding customers 
addCustomerButton = tk.Button(
    mainPageFrame,
    text= "Add Customer",
    **button_style,
    command=open_add_customer_form
)

#button for adding books
addBookButton = tk.Button(
    mainPageFrame,
    text= "Add Book",
    **button_style
)

#button for placing orders 
placeOrderButton = tk.Button(
    mainPageFrame,
    text= "Place Order",
    **button_style
)

#button for viewing invoices 
viewInvoicesButton = tk.Button(
    mainPageFrame,
    text= "View Invoices",
    **button_style
)

#Button for searching through invoices 
searchInvoicesButton = tk.Button(
    mainPageFrame,
    text= "Search Invoices",
    **button_style
)

#placing buttons on the grid
addCustomerButton.grid(row=1, column=1, sticky="nsew", padx=40, pady=10)
addBookButton.grid(row=2, column=1, sticky="nsew", padx=40, pady=10)
placeOrderButton.grid(row=3, column=1, sticky="nsew", padx=40, pady=10)
viewInvoicesButton.grid(row=4, column=1, sticky="nsew", padx=40, pady=10)
searchInvoicesButton.grid(row=5, column=1, sticky="nsew", padx=40, pady=10)

window.mainloop()