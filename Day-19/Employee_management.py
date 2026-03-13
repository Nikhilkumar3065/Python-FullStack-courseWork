class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):

    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.20


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
salary = int(input("Enter Salary: "))
dept = input("Enter Department: ")

emp = Employee(emp_id, name, salary)
mgr = Manager(emp_id, name, salary, dept)

print("\nEmployee Bonus (10%):", int(emp.calculate_bonus()))

print("\nManager Details:")
print("Department:", mgr.department)
print("Manager Bonus (20%):", int(mgr.calculate_bonus()))
