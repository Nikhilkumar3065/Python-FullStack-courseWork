from abc import ABC,abstractmethod    #abstract base class (abc)

class BankAccount(ABC):
    def checkbalance(self):
        print("You can check your BALANCE------")

    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh per day")
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimted deposit")
    def withdraw(self):
        print("unlimited withdraw ")

class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20,000 to 1 lakh you can withdraw perday")

class PensionAccount(BankAccount):
    def deposit(self):
        print("No deposit")
    def withdraw(self):
        print("40k per day")

print("--------Saaketh----------")
saaketh = SavingAccount()
saaketh.checkbalance()
saaketh.deposit()
saaketh.withdraw()

print("--------Nikhil----------")
nikhil = CurrentAccount()
nikhil.checkbalance()
nikhil.deposit()
nikhil.withdraw()

print("--------Abhi-Sweety----------")
abhi_sweety = JointAccount()
abhi_sweety.checkbalance()
abhi_sweety.deposit()
abhi_sweety.withdraw()

print("--------Shanmuk----------")
shanmuk = SalaryAccount()
shanmuk.checkbalance()
shanmuk.deposit()
shanmuk.withdraw()

print("--------Sapnil----------")
sapnil = PensionAccount()
sapnil.checkbalance()
sapnil.deposit()
sapnil.withdraw()
