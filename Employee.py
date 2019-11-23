import googlemaps, json, GoogleMapParser as Parser
from datetime import datetime

class Admin():
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

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def increaseSalary(self):
        return (self.salary + (self.salary * .10))

class Delivery(Admin):
    def __init__(self, first_name, username, password, address):
        super().__init__(first_name, username, password)
        self.step_by_step = []
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
        self.create_direction_result("Boulder, CO 80309")

    def create_direction_result(self, end_address):
        print("---------------------------------------------------------------------------------\nto: " + end_address)
        self.directions_result = self.gmaps.directions(self.address, end_address, departure_time=self.now)
        self.duration_to_address = Parser.get_duration(self.directions_result)
        self.distance_to_address = Parser.get_distance(self.directions_result)
        self.step_by_step = Parser.get_step_by_step_directions(self.directions_result)

    def get_duration_to_address(self):
        return self.duration_to_address

    def get_distance_to_address(self):
        return self.distance_to_address

    def get_step_by_step(self):
        return self.step_by_step


class Cook(Admin):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 10

class Sales(Admin):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 20
        self.budget = 600
