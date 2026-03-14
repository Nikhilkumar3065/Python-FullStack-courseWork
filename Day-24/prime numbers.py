'''
n = int(input("Enter the numbers:"))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number")
'''
import csv
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "not a prime number"
    return "prime number"

with open("primetc.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if isprime(int(row['input'])) == row['output']:
            print(row['input'],"Test case PASSED")
        else:
            print(row['input'],"Test case FAILED")
            
