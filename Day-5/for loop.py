'''
#LIST...
products = ['Butter','Tea powder','Milk','Sugar']
for product in products:
    print(f"{product}-Add to CART | Add to FAV | Buy now!!")
33
#tuple...    
sizes = ('s','l','xl','xxl','xxxl')
for s in sizes:
    print(s)

#set...
followers = {'nikhil','saaketh','sapnil','shanmuk'}
for i in followers:
    print(f'{i}-|follow back | remove| message|')

#dict
data={
    'nikhil': ['c','python','java','js'],
    'saaketh': ['p','pythonfs','javafs','js']}
for i in data:
    print(f"{i}:{data[i]}")
    
#string
s='python programming'
for i in s:
    print(i)

#range(start,stop+1,step)=range(0,n,1)
for i in range(2,101,2): #even number 
    print(i)
    
for i in range(1,100,2): #odd number
    print(i)
    
for i in range(10,0,-1): #reverse the number 10-1 
    print(i)
    
n = int(input("Enter the number:"))
print(f'{n}-Table')
for i in range(1,11,): 
    print(f'{n}*{i}={n*i}') #multiplication Table
    
# break
for i in range(1,100):
    if i==45:
        break    #break the number that is given
    print(i)
'''    
#continue
for i in range(1,10):
    if i==5:
        continue    #skip the given number and continue
    print(i)



