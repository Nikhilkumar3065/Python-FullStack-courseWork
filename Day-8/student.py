n = int(input("Enter the number of students: "))
names = []
gpas = []
for i in range(n):
    name = input("Enter the name: ")
    gpa = float(input("Enter the GPAS: "))
    
    names.append(name)
    gpas.append(gpa)
print(f'{names.ljust(15)}')
for i in range(len(names)):
    print(names[i],gpas[i])


