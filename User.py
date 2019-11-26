import googlemaps
import GoogleMapParser as Parser

class User():
    def __init__(self, first_name, last_name, username, password, email, address):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password

        print("\ninitializing User address...")
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

class Guest(User):
    def __init__(self, void):
        self.discount = 1
        self.user_type = 1

class Member(User):
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name, last_name, username, password, email, address)
        self.discount = 0.85
        self.user_type = 1

class VIP(User): #Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name,last_name,username, password, email, address)
        self.discount = 0.75
        self.user_type = 2

# MOVED TO MAIN.PY
# Customer = User('t','t','t','t','t')
# eric = Member('eric','test2','t','t','t')
# eric2 = VIP('Blah','bloo','blee','blop','t')
# Customer.addMember(eric)
# Customer.addVIP(eric2)
# Customer.promoteVIP('Eric')
