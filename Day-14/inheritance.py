class InstagramV1:                            #parent class
    def __init__(self,username):
        self.username = username
        print(f"Heyy {self.username},Welcome to Instagram!!!!!!!")

    def reels(self):
        print("You can upload and scroll reels")

    def posts(self):
        print("You can upload Your posts")



class InstagramV2(InstagramV1):                    #childclass(parentclass)

    def __init__(self,username):
        super().__init__(username)

    
    def story(self):
        print("You can upload Your Story")



class InstagramV3(InstagramV2):                #multilevelinheritance

    def __init__(self,username):
        super().__init__(username)

    
    def note(self):
        print("You can ADD Your note")
    
        
class Live:
    def launchLIVE(self):
        print("You can start Instagram LIVE")
    
class Verification:                                  #multipleinheritance
    def Verify(self):
        print("You can make your ACCOUNT VERIFIED for better feature")
    
class InstagramV4(InstagramV3,Live,Verification):
    def __init__(self,username):
        super().__init__(username)

class creator(InstagramV4):
    def __init__(self,username):
        super().__init__(username)

    def insights(self):
        print("You can check your insights")

class business(InstagramV4):
    def __init__(self,username):
        super().__init__(username)
    def buttons(self):
        print("You can CONTACT them and CALL")

        
Nikhil = InstagramV4('Nikhil')
Nikhil.reels()
Nikhil.posts()
Nikhil.story()
Nikhil.note()
Nikhil.launchLIVE()
Nikhil.Verify()
Nikhil.insights()
Nikhil.buttons()        
        
