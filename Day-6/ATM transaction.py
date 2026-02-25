'''
# ATM Simulation with Exception Handling

accounts = {
    "1001": 5000,
    "1002": 8000
}

transactions = [200, 500, 1000]


while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    # 1. ZeroDivisionError
    if choice == "1":
        try:
            total = sum(transactions)
            count = int(input("Enter number of transactions: "))
            average = total / count
            print("Average Transaction:", average)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    # 2. ValueError
    elif choice == "2":
        try:
            amount = int(input("Enter withdrawal amount: "))
            print("Withdrawal Successful:", amount)
        except ValueError:
            print("Error: Invalid input! Enter numbers only.")

    # 3. TypeError
    elif choice == "3":
        try:
            amount = input("Enter deposit amount: ")
            result = amount + 100   # causes TypeError
            print(result)
        except TypeError:
            print("Error: Invalid data type for deposit.")

    # 4. IndexError
    elif choice == "4":
        try:
            index = int(input("Enter transaction index: "))
            print("Transaction:", transactions[index])
        except IndexError:
            print("Error: Transaction not found!")

    # 5. KeyError
    elif choice == "5":
        try:
            acc_no = input("Enter account number: ")
            print("Balance:", accounts[acc_no])
        except KeyError:
            print("Error: Account does not exist!")

    # 6. FileNotFoundError
    elif choice == "6":
        try:
            file = open("transaction_log.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("Error: Transaction log file not found!")

    # Exit
    elif choice == "7":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid Option! Please select 1-7.")
'''
def zero_division_error_case():
    try:
        transactions = []  
        average_transaction = sum(transactions) / len(transactions)
        print("Average Transaction:", average_transaction)
    except ZeroDivisionError:
        print("Error: Cannot calculate average transaction because there are no transactions.")

def value_error_case():
    try:
        
        withdrawal_amount = int("abc")  
        print("Withdrawing:", withdrawal_amount)
    except ValueError:
        print("Error: Invalid value entered. Please enter a numeric amount.")

def type_error_case():
    try:
       
        balance = 500
        deposit_amount = "100"  
        new_balance = balance + deposit_amount  
        print("New Balance:", new_balance)
    except TypeError:
        print("Error: Incompatible data types. Cannot add string to an integer.")

def index_error_case():
    try:
        transaction_history = [200, -150, 300]
        print("Last transaction:", transaction_history[5])
    except IndexError:
        print("Error: Trying to access a transaction that does not exist.")

def key_error_case():
    try:
        accounts = {"12345": {"pin": "1111", "balance": 1000}}
        account_number = "67890"  
        print("Account Balance:", accounts[account_number]["balance"])  
    except KeyError:
        print("Error: Account number not found.")

def file_not_found_error_case():
    try:
        with open("transaction_log.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("Error: Transaction log file not found.")



while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    if choice == "1":
        zero_division_error_case()
    elif choice == "2":
        value_error_case()
    elif choice == "3":
        type_error_case()
    elif choice == "4":
        index_error_case()
    elif choice == "5":
        key_error_case()
    elif choice == "6":
        file_not_found_error_case()
    elif choice == "7":
        print("Exiting the ATM Simulation. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid choice.")

