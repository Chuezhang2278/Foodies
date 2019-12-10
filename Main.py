from Employee import Manager, Cook, Delivery, Salesperson
from Food import Food
from User import Member, VIP, Guest
from Supplies import Supplies
from Order import Order
import random

# Employee
def addDeliveryPerson(employee):
    DeliveryPeople.append(employee)
    print("Added " + employee.getFirst() + " to DeliveryPeople")

def addCook(employee):
    Cooks.append(employee)
    print("Added " + employee.getFirst() + " to Cooks")

def addSalesperson(employee):
    Sales.append(employee)
    print("Added " + employee.getFirst() + " to Sales")

def findCook(name):
    for i in range(len(Cooks)):
        if(Cooks[i].getFirst() == name):
            print('Cook ' + Cooks[i].getFirst() + ' has been found')
            return Cooks[i]

def printCooks():
    print("Printing list of Cooks...")
    if(len(Cooks) == 0):
        print("\tCooks is empty")
    else:
        print('\tCooks: ', end='')
        for i in range(len(Cooks)):
            print(Cooks[i].getFirst(), end=' ')
        print('')

def checkLaidOff(Delivery):
    if Delivery.getWarnings() > 2:
        print(Delivery.getFirst() + " has been laid off")
        DeliveryPeople.remove(Delivery)
# Food
def addMenuItem(food):
    Menu.append(food)
    print("Added " + food.getName() + " to Foods")

def printMenu():
    print("Printing list of Foods...")
    if(len(Menu) == 0):
        print("\tFoods is empty")
    else:
        for i in range(len(Menu)):
            print('\t' + Menu[i].getCate(), Menu[i].getFood_name(), Menu[i].getSpice())

# User

def getUserSize():
    return len(User)

def removeMember(user):
    User.remove(user)
    print("Removed " + user.getFirst() + " from VIP")

def findUser(name):
    for i in range(len(User)):
        if(User[i].getFirst() == name):
            print('Member ' + user[i].getFirst() + ' has been found')
            return User[i]

def promoteVIP(name):
    for i in range(len(User)):
        if(User[i].getFirst() == name):
            print(User[i].getFirst() + " found, promoting to VIP")
            para1 = User[i].getFirst()
            para2 = User[i].getLast()
            para3 = User[i].getUser()
            para4 = User[i].getEmail()
            para5 = User[i].getPass()
            removeMember(User[i])
            new = VIP(para1, para2, para3, para4, para5)
            addUser(new)
            break

    self.order.append(Food)
    self.order.append(Price)

def addCurrentUser(name):
    CurrentUser.append(name)

def addCurrentCart(name):
    CurrentCart.append(name)

def currentCartSize():
    return len(CurrentCart)*2

def addEmployee(name):
    Employee.append(name)

def addUser(user):
    User.append(user)

def sortMenu(): #Bubble sort algorithm for most relevant items, May change for only top 3
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(Menu)-1):
            if(Menu[i].getSold() < Menu[i+1].getSold()):
                Menu[i], Menu[i+1] = Menu[i+1], Menu[i]

def printMenu():
    for i in range(len(Menu)):
        print(Menu[i].getName())

# Salesperson
# For each supplier they will have an array of different supplies in them.
def addSupplies(Supplies):
    SuppliesList.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List")

def addSupplies1(Supplies):
    SuppliesList1.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 1")

def addSupplies2(Supplies):
    SuppliesList2.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 2")

def addSupplies3(Supplies):
    SuppliesList3.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 3")

def addCurrentCart_SalesPerson(Supplies):
    CurrentCart_SalesPerson.append(Supplies)

# Customer Checking Out Stuff
def addOrder2(Name, CurrentCart):
    Orders.append(Order(Name, CurrentCart))
    CurrentCart.clear()



#====For_Storage====
Orders = []
DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
User = []
Employee = []
CurrentUser = []
CurrentCart = []
SuppliesList=[]
SuppliesList1 = []
SuppliesList2 = []
SuppliesList3 = []
CurrentCart_SalesPerson=[]
#====For_Storage====#

################################################### TESTING BELOW #################################################################
# Foods
foodTest1 = Food('Chicken', 12.99, 'Entrees', True, 100, 2, 4)
foodTest2 = Food('Fish', 10.99, 'Entrees', False, 500, 3, 5)
foodTest3 = Food('Duck', 9.49, 'Entrees', False, 122, 5, 6)
foodTest4 = Food('Dog', 20.99, 'Entrees', True, 5, 5, 7)

# Cart

# addOrder()

# Cook
John = Cook('John','john', 'test')
Jim = Cook('Jim', 'jim', 'test')

# Manager
manager = Manager('y','y','y')

# Salesperson
Anderson = Salesperson('Anderson','anderson1','password',1000.00,'restaurantname') #sales person example
Patrick = Salesperson('Patrick','patrick','password',1000.00,'restaurantname') #sales person example

# Users
deliveryBot = Delivery('Delivery Bot','u','p','City College of New York')
deliveryBot2 = Delivery('Delivery Bot 2','u2','p2','JFK Airport')
void = Guest('void1','void2')
eric = Member('eric','test2','t','t','t','Coney Island')
chue = VIP('chue','bloo','blee','blee','blop','Empire State Building')

addDeliveryPerson(deliveryBot)
deliveryBot.setRating(1)
deliveryBot.setRating(2)
deliveryBot.setRating(1)
deliveryBot.setRating(4)
deliveryBot.setRating(5)
checkLaidOff(deliveryBot)
deliveryBot2.setRating(1)
deliveryBot2.startNewOrder(Order(chue, CurrentCart))
deliveryBot.startNewOrder(Order(eric, CurrentCart))


# Define some supplies
#### reminder to maybe add randomnized quality
Meat = Supplies('Meat','Good', 24.99)
Fish = Supplies('Fish', 'Good', 31.99)
Vegetables = Supplies('Vegetables', 'Good', 9.99)
Flour = Supplies('Flour', 'Good', 5.99)
Yeast = Supplies('Yeast', 'Good', 6.99)
Salt = Supplies('Salt', 'Good', 3.99)
Spices = Supplies('Spices', 'Good', 15.99)
Sugar = Supplies('Sugar', 'Good', 4.99)
Egg = Supplies('Egg', 'Good', 5.99)
Dairy = Supplies('Dairy', 'Good', 8.99)

addSupplies(Meat)
addSupplies(Fish)
addSupplies(Vegetables)
addSupplies(Flour)
addSupplies(Yeast)
addSupplies(Salt)
addSupplies(Spices)
addSupplies(Sugar)
addSupplies(Egg)
addSupplies(Dairy)

random_quality = ['Bad', 'Good', 'Best']


# Add the Supplies into each supplier inventory with them each having random qualities
for i in range(0, 9):
    rand_int1 = random.randint(0, 2)
    rand_int2 = random.randint(0, 2)
    rand_int3 = random.randint(0, 2)

    addSupplies1(Supplies(SuppliesList[i].getName(), random_quality[rand_int1], SuppliesList[i].getPrice()))
    addSupplies2(Supplies(SuppliesList[i].getName(), random_quality[rand_int2], SuppliesList[i].getPrice()))
    addSupplies3(Supplies(SuppliesList[i].getName(), random_quality[rand_int3], SuppliesList[i].getPrice()))

addUser(void)
addUser(chue)
addUser(eric)
addUser(John)
addUser(Jim)
addUser(manager)
addUser(Anderson)
addUser(Patrick)
addUser(deliveryBot)
addUser(deliveryBot2)

addMenuItem(foodTest1)
addMenuItem(foodTest2)
addMenuItem(foodTest3)
addMenuItem(foodTest4)
