import csv
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
with open("facttc.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if factorial(int(row['input']))==int(row['output']):
            print('Test case is passed for',row['input'])
        else:
            print('Test case is failed for',row['input'])
            
