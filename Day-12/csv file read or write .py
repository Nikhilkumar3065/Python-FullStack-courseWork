'''
import csv
with open('rough.csv','r') as file:
    content = csv.reader(file)            {read the xl sheet}
    for i in content:
        print(i)
--------------------------------------------------------
ids
1
2
3
import csv
with open('rough.csv','r') as file:
    content = csv.reader(file)          
    for row in content:
        print(row[0])
-----------------------------------

ids	names	course
1	nikhil	pfs
2	saaketh	jfs
3	shanmukha	ds
5	sapnil	da
import csv
with open('rough.csv','a', newline='\n') as file:
    data =csv.writer(file)
    data.writerow(["5","sapnil","da"])
----------------------------------------------------
import csv
with open('product.csv','w', newline='\n') as file:
    data =csv.writer(file)
    data.writerow(["id","product","price"])
    data.writerow(["1","laptop","13000"])               #{write}
    data.writerow(["2","mouse","23444"])
    data.writerow(["3","charger","4343"])
    data.writerow(["4","iphone","3343"])
---------------------------------------------------------------
'''
import csv
with open('product.csv','r') as file:
    content = csv.reader(file)          
    for row in content:
        print(row)

