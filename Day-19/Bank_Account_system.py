class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("\nAmount Deposited:", amount)
        print("Current Balance:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("\nAmount Withdrawn:", amount)
            print("Current Balance:", self.__balance)
        else:
            print("\nInsufficient Balance")

    def get_balance(self):
        return self.__balance


balance = int(input("Enter Initial Balance: "))
account = BankAccount(balance)

deposit_amount = int(input("Enter Deposit Amount: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter Withdraw Amount: "))
account.withdraw(withdraw_amount)
