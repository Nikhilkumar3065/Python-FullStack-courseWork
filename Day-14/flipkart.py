class flipkart:
    
    discount = 10

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount
        print(f'{cls.discount} is your discount')

    def userinfo(self,name,phoneno):
        self.name = name
        self.phoneno = phoneno
        print(f'username: {self.name}')
        print(f'phoneno: {self.phoneno}')

    @staticmethod
    def banner():
        print("welcome to flipkart\n10% discount is going shop now")
        

Nikhil = flipkart()
Nikhil.userinfo('Nikhil',12345678)
Nikhil.updatediscount(40)
flipkart.updatediscount(30)
Nikhil.banner()
flipkart.banner()
