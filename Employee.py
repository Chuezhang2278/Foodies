import googlemaps, polyline, GoogleMapParser as Parser
from Food import Food
from datetime import datetime

class Employee():
    def __init__(self, first_name, username, password):
        self.first_name = first_name.title()
        self.username = username
        self.password = password

    def getPass(self):
        return self.password

    def getType(self):
        return self.user_type

    def getFirst(self):
        return self.first_name

    def getUser(self):
        return self.username

    def getSalary(self):
        return self.salary

    def getBudget(self):
        return self.budget

    def increaseSalary(self):
        self.salary = self.salary * 1.1
        return self.salary

    def getRating(self):
        if len(self.rating) == 0:
            return -1
        sum = 0
        for i in self.rating:
            sum += i
        return sum / len(self.rating)

    def setRating(self, value):
        self.rating.append(value)
        print(self.first_name + " received a new rating of " + str(value))
        if len(self.rating) > 2:
            last_three = [self.rating[len(self.rating) - 1], self.rating[len(self.rating) - 2], self.rating[len(self.rating) - 3]]
            sum = 0
            for i in last_three:
                sum += i
            avg = sum / 3
            print("The last 3 rating average is " + str(avg))
            if avg < 2:
                self.warning += 1
                print(self.first_name + " has been issued a warning, he/she has " + str(self.warning) + " warnings")

    def getLast3Rating(self):
        last_3 = []
        if len(self.rating) > 3:
            for i in range(len(self.rating) - 3, len(self.rating)):
                last_3.append(self.rating[i])
        else:
            for i in range(len(self.rating)):
                last_3.append(self.rating[i])
        return last_3

    def getWarnings(self):
        return self.warning


class Delivery(Employee):
    def __init__(self, first_name, username, password, address):
        super().__init__(first_name, username, password)
        self.bidded = False
        self.user_type = 3
        self.warning = 0
        self.rating = []
        self.currentOrder = None
        self.step_by_step = []
        self.decoded = []
        self.gmaps = Parser.gmaps
        self.geocode_result = self.gmaps.geocode(address)
        self.now = datetime.now()
        # using my parser to get google formatted address, returns a better formatted address for use
        print("\n\ninitializing Delivery person " + self.first_name + "'s address...")
        self.address = Parser.get_formatted_address(self.geocode_result)
        # using my own parser to parse longtitude and latitude from google
        self.x = Parser.get_lat(self.geocode_result)
        self.y = Parser.get_long(self.geocode_result)
        # temporary create_direction_result here for testing
        # self.create_direction_result("Grand St, Manhattan, NY")

    def create_direction_result(self, end_address):
        print("\ncollecting google maps directions and information for delivery person " + self.first_name + " to " + end_address + "... ")
        self.directions_result = self.gmaps.directions(self.address, end_address, departure_time=self.now)
        self.duration_to_address = Parser.get_duration(self.directions_result)
        self.distance_to_address = Parser.get_distance(self.directions_result)
        self.step_by_step = Parser.get_step_by_step_directions(self.directions_result)

        # ended up not needing the polyline coordinates
        # self.polylines = Parser.get_polyline(self.directions_result)
        # self.decoded = Parser.decode_polyline(self.polylines)
        # self.convert_decoded_to_javascript_format()

    def startNewOrder(self, Order):
        self.currentOrder = Order
        self.bidded = False
        self.create_direction_result(self.currentOrder.getCustomer().getAddress())

    def get_duration_to_address(self):
        return self.duration_to_address

    def get_distance_to_address(self):
        return self.distance_to_address

    def get_step_by_step(self):
        return self.step_by_step

    def convert_decoded_to_javascript_format(self):
        for i in range(len(self.decoded)):
            for j in range(len(self.decoded[i])):
                self.decoded[i][j] = str(self.decoded[i][j]).replace('(', '{lat:')
                self.decoded[i][j] = str(self.decoded[i][j]).replace(', ', ', lng:')
                print(str(self.decoded[i][j]).replace(')', '},'))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAddress(self):
        return self.address

    def getCustomerAddress(self):
        return self.currentOrder.getCustomer().getAddress()

    def getCustomer(self):
        return self.currentOrder.getCustomer()

    def getOrder(self):
        return self.currentOrder

    def resetOrder(self):
        self.currentOrder = None

    def getBidded(self):
        return self.bidded

    def setBidded(self, bool):
        self.bidded = bool

class Cook(Employee):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 10
        self.user_type = 4
        self.rating = []

    def addFood(menuList, Food):
        menuList.append(Food)

    def removeFood(menuList, name):
        for i in range(len(menuList)):
            if menuList[i].getName() == name:
                menuList.remove(menuList[i])

    def changeFoodQuantity(menuList, name, quantity):
        for i in range(len(menuList)):
            if menuList[i].getName() == name:
                menuList[i].setQuantity(quantity)

    def changeFoodQuality(menuList, name, quality):
        for i in range(len(menuList)):
            if menuList[i].getName() == name:
                menuList[i].setQuality(quality)

class Salesperson(Employee):
    def __init__(self,first_name, username, password, budget, restaurant):
        super().__init__(first_name,username,password)
        self.user_type = 5
        self.salary = 20
        self.budget = budget
        self.restaurant=restaurant
        self.rating = [5,4]


    def getRestaurant(self):

        return self.restaurant

class Manager(Employee):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.user_type = 6
        self.salary = 250
        self.budget = 1000
