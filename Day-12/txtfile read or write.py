'''
file = open('sample.txt','r')
content1  = file.read()
file.seek(0)
content2  = file.readline()   {read mode}
file.seek(0)
content3  = file.readlines()

print(content1,content2,content3,sep='\n\n')
file.close()
output:
names------------------
Nikhil
saaketh
shanmuka


names------------------


['names------------------\n', 'Nikhil\n', 'saaketh\n', 'shanmuka\n']
--------------------------------------------------------------------------------------------
with open('sample.txt','w,r,a') as file:
    file.write('')         
----------------------------------------------------------
file = open('samples.txt','w')       {creates new file and if file exist it rewrite the text}
file.write("Hello world")               {write mode}

file.close()
--------------------------------------------------------------------------------------------
file = open('samples.txt','a')
file.write("\n WELCOME to python class")     {append}     {it will not rewrite the file
                                                           it will add the text into file}
file.close()
--------------------------------------------------------------------------------------------
file = open('samples.txt','r') as file:
    file.write("\n WELCOME to python class")
--------------------------------------------------------------------------------------------
file = open('samples.txt','a+')         {append and write} {r+ read and write
                                                                   w+ write and read}
file.write("\n FIle operations")
file.seek(0)
print(file.read())
file.close()
--------------------------------------------------------------------------
'''
with open('sample.txt','r+') as file:
    file.write("\n File operations")
    file.seek(0)
    print(file.read())
    







































