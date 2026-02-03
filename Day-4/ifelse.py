products = ['shirts','paints','shoes','laptop']
search = input("Enter the item:")
if search in products:
    print(f"{search} is found!!\nGo and Shop now!!!!")
else:
    print(f"{search} Not Found!!!!!!!\nLook for other items")
