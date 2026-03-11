Monthlysalary = int(input("Monthly salary: "))
ExistingLoanAmount = int(input("Existing Loan Amount: "))
CreditScore = int(input("Credit Score: "))
if Monthlysalary > 30000 and CreditScore > 700 and ExistingLoanAmount < 50000:
    print("Eligible")
else:
    print("Not Eligible")
