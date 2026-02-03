data = {
'sathvik':{'status':True,'python':100,'mysql':99,'skills':60},
'Ravi':{'status':True,'python':50,'mysql':69,'skills':40},
'dilip':{'status':False,'python':70,'mysql':39,'skills':40},
'nikhil':{'status':True,'python':90,'mysql':89,'skills':70}}

user = input("Enter the student name:")
if user in data:
    if data[user]['status']:
        sum = data[user]['python']+data[user]['mysql']+data[user]['skills']
        avg = sum/3
        if avg>80:
            print(f"congrats {user}!!\nyou got 'A' grade")
        elif avg>60:
            print(f"better luck {user}!!\nyou got 'b' grade")
        elif avg>40:
            print(f"need improvement {user}!!\nyou got 'c' grade")
        else:
            print(f"{user} ,failed in exams.\nBring your parents")
    else:
        print(f"{user} did not write any exams.")
else:
    print(f"{user} not found")
    
