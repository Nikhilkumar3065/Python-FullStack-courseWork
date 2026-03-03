class Hotstar:
    def __init__(self,username):
        print(f'hey {username}, Welcome to the HOTSTAR')
    def playvideo(self):
        print("ads will be run")
        print("Quality is low")
        print("no Download")
    def search(self):
        print("You can search for program")
    def watchlist(self):
        print("You can add the watchlist")
    def notifications(self):
        print("You can get notifications")
    def login(self):
        print("You can login")
        
class premiumHotstar(Hotstar):
    def __init__(self,username):
        print(f'hey {username}, Welcome to the Premium HOTSTAR')
    def playvideo(self):
        print("ads will not be run")
        print("Quality is High")
        print("You can Download")

Nikhil = Hotstar("Nikhil")
Nikhil.playvideo()
Nikhil.search()
Nikhil.watchlist()
Nikhil.notifications()
Nikhil.login()
saaketh = premiumHotstar("saaketh")
saaketh.playvideo()
saaketh.search()
saaketh.watchlist()
saaketh.notifications()
saaketh.login()
