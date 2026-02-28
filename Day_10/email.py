'''
accounts = {}

for i in range(5):
    print(f"\nRegistration {i+1}")
    
    email = input("Enter email: ")
    password = input("Enter password: ")


    if email in accounts:
        print("Email already existed!")
    else:
        accounts[email] = password
        print("Account created successfully!")

print("\n---- Registered Accounts ----")
for email in accounts:
    print(email)
'''
data= {
    'qwerty@gmail.com':'1234'
    'jkif@gmail.com':'7890'
    'zxvccvb@gmail.com':'30655'
    'mnbvc@gmail.com':'inko'
}
int('1.Register')
int('2.login')
ch=int(input("Entervyour choice:"))
ch==1:
    email=input("enter the email")
    pwd = input("enetr the pwd")
    if email in data:
        print(f"register - failed\n{email} is alreday exist")
    else:
        data[email]=pwd
        print("register successfull")
ch==2:
    email=input("enter the email")
    pwd = input("enetr the pwd")
    if email in data:
        print(f"register - failed\n{email} is alreday exist")
    else:
        data[email]=pwd
        print("register successfull")

       
