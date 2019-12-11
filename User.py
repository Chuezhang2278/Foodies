import googlemaps
import GoogleMapParser as Parser
import Main


class User():
    def __init__(self, first_name, last_name, username, password, email, address):
        self.first_name = first_name.title()  # First name
        self.last_name = last_name.title()  # Last name
        self.username = username  # User name
        self.email = email  # Email
        self.password = password  # Password
        self.deliveryPerson = None
        self.cookPerson = None
        self.rating = []

        print("\ninitializing User " + self.first_name + "'s address...")
        self.gmaps = Parser.gmaps
        self.geocode_result = self.gmaps.geocode(address)
        # using my parser to get google formatted address, returns a better formatted address for use
        self.address = Parser.get_formatted_address(self.geocode_result)

    def setDelivery(self, Delivery):
        self.deliveryPerson = Delivery

    def setCook(self, Cook):
        self.cookPerson = Cook

    def confirmDelivery(self):
        self.confirm = True

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

    def setAddress(self, Address):
        self.address = Address

    def addUserOrder(self, Food):
        self.order.append(Food)

    def removeUserOrder(self, index):
        self.order.pop(index)

    def printOrderSize(self):
        return len(self.order)



    def printOrder(self):
        i = 0
        while (i < (len(self.order))):
            print(self.order[i].getName())
            i += 1

    def getRating(self):
        if len(self.rating) == 0:
            return -1
        sum = 0
        for i in self.rating:
            sum += i
        return sum / len(self.rating)

    def setRating(self, value):
        self.rating.append(value)

    # need to do this function, so that when delivery guy gives a rating, this will decide if the user will get promoted/demoted
    def checkPromotion(self):
        sum = 0
        for i in self.getLast3Rating():
            sum += i
        if sum != 0:
            avg = sum / len(self.getLast3Rating())
        if avg != 0 and len(self.getLast3Rating()) == 3:
            if avg > 4:
                self.user_type = 2  # become VIP
                self.discount = 0.75
            elif avg < 2 and avg > 1:
                self.user_type = 0  # become GUEST
                self.discount = 1
            else:
                print(self.first_name + " has been blacklisted")
                Main.removeUser(self)
                Main.addBlacklist(self)

    def getLast3Rating(self):
        last_3 = []
        if len(self.rating) > 3:
            for i in range(len(self.rating) - 3, len(self.rating)):
                last_3.append(self.rating[i])
        else:
            for i in range(len(self.rating)):
                last_3.append(self.rating[i])
        return last_3


class Guest(User):
    def __init__(self, username, password):
        self.first_name = "guest"
        self.username = username
        self.password = password
        self.discount = 1
        self.user_type = 0
        self.order = []
        self.confirm = False
        self.address = None


class Member(User):  # Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name, last_name, username, password, email, address)
        self.discount = 0.85
        self.user_type = 1
        self.order = []
        self.confirm = False


class VIP(User):  # Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name, last_name, username, password, email, address)
        self.discount = 0.75
        self.user_type = 2
        self.order = []
        self.confirm = False


class SignUp(User): #Inherits VIP methods as well as user, polymorphism
    def __init__(self, first_name, last_name, username, password, email, address):
        super().__init__(first_name,last_name,username, password, email, address)
