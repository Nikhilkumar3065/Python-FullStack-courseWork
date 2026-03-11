store = {
    "apple": 50,
    "banana": 20,
    "milk": 40,
    "bread": 30,
    "eggs": 60
}


cart = {}

while True:
    print("\n------ MENU ------")
    print("1. View Store Items")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        print("\nAvailable Items:")
        for item, price in store.items():
            print(f"{item} - ₹{price}")

    elif choice == "2":
        item = input("Enter item name to add: ").lower()
        if item in store:
            cart[item] = store[item]
            print(f"{item} added to cart.")
        else:
            print("Item not available!")

   
    elif choice == "3":
        item = input("Enter item name to remove: ").lower()
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print("Item not in cart!")

  
    elif choice == "4":
        print("\nYour Cart:")
        total = 0
        if cart:
            for item, price in cart.items():
                print(f"{item} - ₹{price}")
                total += price
            print(f"Total Amount: ₹{total}")
        else:
            print("Cart is empty!")

 
    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Try again.")
