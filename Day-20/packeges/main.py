from product import Product
from order import Order
from utils import generate_order_id

name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

p = Product(name, price)

print("\nProduct Created:", p.name)

order = Order(p, quantity)

print("Order Created Successfully")

order_id = generate_order_id()

print("Generated Order ID:", order_id)
print("Total Amount:", order.total_price())
