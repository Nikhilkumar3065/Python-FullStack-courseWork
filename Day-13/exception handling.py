'''
if a>10:
    print()
else:
    print()
NameError: name 'a' is not defined
------------------------------------------------------------
try:
    if a>10:      #check the error
        print("good")
except NameError:
    print('a is not defined')    #if there is error handle the error
else:
    print('no error')     #no error it finaly works
finally:
    print("End of the block")   #it will execute everytime
#output:
#a is not defined
#End of the block
------------------------------------------------------
try:
    'a'+10
       #check the error
except NameError:
    print('a is not defined')    #if there is error handle the error
except ValueError:
    print('Enter the requested data type')
except TypeError:
    print('Data types are different')
except ZeroDivisionError:
    print('can not divide with zero')
except IndexError:
    print('the index is not present')
except KeyError:
    print('Key is not present')

else:
    print('no error')     #no error it finaly works
finally:
    print("End of the block")
-----------------------------------------------------
try:
    a=a+'8'
    print(a[9])
except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f'Error Occured: {e}')
else:
    print('No Errors')
finally:
    print("End of the Block")
----------------------------------------------------------------------------
try:
    a=int(input())
    print(a)
except Exception as e:         #just give exception it will handle all type of errors
    print(f'Error Occured: {e}')
else:
    print('No Errors')
finally:
    print("End of the Block")
-------------------------------------------------
'''
try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive value")#raise is used for rasing error explesitly
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No Errors')
finally:
    print("End of the Block")


































