'''
import csv
def palindrome(num):
    temp=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        return "palindrome"
    else:
        return "not a palindrome"
n=int(input("enter the number:"))
print(palindrome(n))

with open("palindrome.csv","r")as file:
    reader=csv.DictReader(file)
    print(reader)
    for row in reader:
        if palindrome(int(row['input'])) == row['output']:
            print("test case is passed for",row['input'])
        else:
            print("test case failed for",row['input'])
'''
import csv

def ispalindrom(n):
    rev = n[::-1]
    if n == rev:
        return "palindrom"
    else:
        return "not a palindrom"


with open("palindrome.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        num = row['input']
        result = ispalindrom(num)

        if result == "palindrom":
            print(num, "Test Case Passed")
        else:
            print(num, "Test Case Failed")
