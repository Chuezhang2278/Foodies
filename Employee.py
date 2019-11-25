import googlemaps, polyline, GoogleMapParser as Parser
from Food import Food
from datetime import datetime

class Employee():
    def __init__(self, first_name, username, password):
        self.first_name = first_name.title()
        self.username = username
        self.password = password

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

class Delivery(Employee):
    def __init__(self, first_name, username, password, address):
        super().__init__(first_name, username, password)
        self.step_by_step = []
        self.decoded = []
        self.gmaps = googlemaps.Client(key='API key here')
        self.geocode_result = self.gmaps.geocode(address)
        self.now = datetime.now()
        # using my parser to get google formatted address, returns a better formatted address for use
        self.address = Parser.get_formatted_address(self.geocode_result)
        # using my own parser to parse longtitude and latitude from google
        self.x = Parser.get_lat(self.geocode_result)
        self.y = Parser.get_long(self.geocode_result)

        # temporary create_direction_result here for testing
        self.create_direction_result("Grand St, Manhattan, NY")

    def create_direction_result(self, end_address):
        print("---------------------------------------------------------------------------------\nto: " + end_address)
        self.directions_result = self.gmaps.directions(self.address, end_address, departure_time=self.now)
        self.duration_to_address = Parser.get_duration(self.directions_result)
        self.distance_to_address = Parser.get_distance(self.directions_result)
        self.step_by_step = Parser.get_step_by_step_directions(self.directions_result)
        self.polylines = Parser.get_polyline(self.directions_result)
        self.decoded = Parser.decode_polyline(self.polylines)
        # self.convert_decoded_to_javascript_format()

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

class Cook(Employee):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 10

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
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 20
        self.budget = 600

class Manager(Employee):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 250
        self.budget = 1000

# DeliveryGuy = Delivery("Jia Ming", "jma8774", "jma8774", "160 Convent Ave, New York, NY 10031")
