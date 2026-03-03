class snapchat:
    def __init__(self,username,password,friends):
        self.username = username      #public
        self.__password = password    #__ private
        self._friends = friends       #_ protected

    def getpassword(self):          #we need call  private inside the class
        return self.__password
    def setpassword(self,new_password):    #to modify private
        self.__password = new_password
    @property                #decorater
    def oprfriends(self):
        return self._friends
    @oprfriends.setter
    def oprfriends(self,newfriend):
        self._friends.append(newfriend)

nikhil = snapchat('nikhil','1234',['saaketh','shanmuka'])
print(f'Name Before modification: {nikhil.username}')
nikhil.username = 'Nikhil kumar'
print(f'Name after modification: {nikhil.username}')
#private 
print(f'password Before modification: {nikhil.getpassword()}')
nikhil.setpassword('8@3849')
print(f'password after modification: {nikhil.getpassword()}')

print(f'Name Before modification: {nikhil.oprfriends}')
nikhil.oprfriends = 'abhinandhan'
print(f'password after modification: {nikhil.oprfriends}')



