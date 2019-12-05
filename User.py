import googlemaps
import GoogleMapParser as Parser

class User():
    def __init__(self, first_name, last_name, username, password, email, address):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        
        print("\ninitializing User " + self.first_name + "'s address...")
        self.gmaps = Parser.gmaps
        self.geocode_result = self.gmaps.geocode(address)
        # using my parser to get google formatted address, returns a better formatted address for use
        self.address = Parser.get_formatted_address(self.geocode_result)

    def getDiscount(self):
        return self.discount

    def getFirst(self):
        return self.first_name

    def getLast(self):
        return self.last_name

    def getUser(self):
        return self.username

    def getPass(self):
        return self.password

    def getEmail(self):
        return self.email

    def getType(self):
        return self.user_type

    def getAddress(self):
        return self.address

    def addOrder(self,Food,Price):
        self.order.append(Food)
        self.order.append(Price)
        
    def removeOrder(self,Food,Price):
        self.order.remove(Food)
        self.order.remove(Price)
    
    def printOrder(self):
        i=0
        while (i < (len(self.order))):
            print(self.order[i] + " " + str(self.order[i+1]))
            i += 2
        
class Guest(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.discount = 1
        self.user_type = 0
        self.order = []

class Member(User): #Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name, last_name, username, password, email, address)
        self.discount = 0.85
        self.user_type = 1
        self.order = []
        
class VIP(User): #Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name,last_name,username, password, email, address)
        self.discount = 0.75
        self.user_type = 2
        self.order = []

