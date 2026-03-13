class Product:

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_details(self):
        print("Product Details:")
        print("ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount
        print("\nAfter", percent, "% Discount:")
        print("Updated Price:", int(self.price))

    def update_stock(self, quantity):
        self.stock += quantity
        print("\nAfter Stock Update:")
        print("Updated Stock:", self.stock)


pid = int(input("Enter Product ID: "))
name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
stock = int(input("Enter Stock: "))

p = Product(pid, name, price, stock)

p.display_details()

percent = int(input("Enter Discount Percentage: "))
p.apply_discount(percent)

qty = int(input("Enter Quantity to Update Stock: "))
p.update_stock(qty)
