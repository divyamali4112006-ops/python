import tkinter as tk
from tkinter import messagebox

# Products
products = {
    1: ("Laptop", 50000),
    2: ("Headphones", 2000),
    3: ("Mouse", 800),
    4: ("Keyboard", 1500)
}

cart = {}

# Functions
def add_to_cart(pid):
    cart[pid] = cart.get(pid, 0) + 1
    messagebox.showinfo("Cart", "Item added to cart")

def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Shopping Cart")

    total = 0
    row = 0
    for pid, qty in cart.items():
        name, price = products[pid]
        cost = price * qty
        total += cost

        tk.Label(cart_window, text=f"{name} x {qty} = ₹{cost}").grid(row=row, column=0)
        row += 1

    tk.Label(cart_window, text=f"Total: ₹{total}", font=("Arial", 12, "bold")).grid(row=row, column=0)
    tk.Button(cart_window, text="Checkout", command=lambda: checkout(total)).grid(row=row+1, column=0)

def checkout(total):
    pin = "1234"  # Secure PIN simulation
    pin_entered = pin_entry.get()

    if pin_entered == pin:
        messagebox.showinfo("Payment", "Payment Successful ")
        cart.clear()
    else:
        messagebox.showerror("Payment", "Payment Failed ")

# Main Window
root = tk.Tk()
root.title("E-Commerce Shopping Cart")
root.geometry("400x400")

tk.Label(root, text="Product Listings", font=("Arial", 14, "bold")).pack()

# Product Buttons
for pid, details in products.items():
    name, price = details
    tk.Button(
        root,
        text=f"{name} - ₹{price}",
        command=lambda pid=pid: add_to_cart(pid)
    ).pack(pady=5)

tk.Button(root, text="View Cart", bg="lightblue", command=view_cart).pack(pady=10)

tk.Label(root, text="Enter PIN for Payment:").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

root.mainloop()
