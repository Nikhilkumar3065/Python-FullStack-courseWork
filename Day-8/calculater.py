def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div (a,b):
    return a/b
def mod(a,b):
    return a%b
exp = input("enter the exp:")
for i in exp:
    if i=='+':
        a,b= exp.split('+')
        print(add(int(a),int(b)))
    elif i=='-':
        a,b= exp.split('-')
        print(sub(int(a),int(b)))
    elif i=='*':
        a,b= exp.split('*')
        print(mul(int(a),int(b)))
    elif i=='/':
        a,b= exp.split('/')
        print(div(int(a),int(b)))
    elif i=='%':
        a,b= exp.split('%')
        print(mod(int(a),int(b)))
        
                 
    
