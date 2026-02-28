amount = int(input("Enter amount to withdraw: "))
if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount should be multiple of 100")

else:
    print("\nDenominations:")
    d500 = amount // 500
    amount = amount % 500

    d200 = amount // 200
    amount = amount % 200

    d100 = amount // 100
    amount = amount % 100

    if d500 > 0:
        print("500 x", d500)

    if d200 > 0:
        print("200 x", d200)

    if d100 > 0:
        print("100 x", d100)
