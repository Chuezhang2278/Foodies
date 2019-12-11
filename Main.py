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
            removeUser(User[i])
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
    return len(CurrentCart)

def addEmployee(name):
    Employee.append(name)

def addUser(user):
    User.append(user)

def removeUser(user):
    User.remove(user)
    print("Removed " + user.getFirst() + " from VIP")

def addBlacklist(user):
    Blacklist.append(user)
    print("Added " + user.getFirst() + " to Blacklist")

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

def printCurrentCart():
    for i in range(len(CurrentCart)):
        print(CurrentCart[i].getCate())

# Customer Checking Out Stuff
def addOrder2(Order):
    Orders.append(Order)

# def addOrder2(Order):
#     Orders.append(Order)

def addOrderHistoy(Order):
    OrderHistory.append(Order)

def addPendingOrder(Order):
    PendingOrders.append(Order)
    #Order.getCart().clear()

def addCookSupplies(Supplies):
    CartSupplies_ForCook.append(Supplies)

# Thread
threadKill = False

#====For_Storage====
PendingOrders = []
Orders = []
OrderHistory = []
DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
User = []
Blacklist = []
Employee = []
CurrentUser = []
CurrentCart = []
SuppliesList=[]
SuppliesList1 = []
SuppliesList2 = []
SuppliesList3 = []
CurrentCart_SalesPerson = []
CartSupplies_ForCook = []
Complaint = []
#====For_Storage====#

################################################### TESTING BELOW #################################################################
# Foods
foodTest1 = Food('Chicken', 12.99, 'Entrees', True)
foodTest2 = Food('Fish', 10.99, 'Entrees', False)
foodTest3 = Food('Duck', 9.49, 'Entrees', False)
foodTest4 = Food('Dog', 20.99, 'Entrees', True)

# Cart

# addOrder()

# Cook
John = Cook('John','john', 'test')
Jim = Cook('Jim', 'jim', 'test')

# Manager
manager = Manager('y','y','y')

# Salesperson
Anderson = Salesperson('Anderson','anderson1','password',1000.00,'Foodies') #sales person example
Patrick = Salesperson('Patrick','patrick','password',1000.00,'Foodies') #sales person example

# Users
deliveryJiaMing = Delivery('Jia Ming Ma','u','p','City College of New York')
deliveryBot2 = Delivery('Auto Bidding Bot','u2','p2','JFK Airport')
void = Guest('void1','void2')
eric = Member('eric','test2','t','t','t','Coney Island')
jd = Member('jd','test2','t','t','t','Bronx Zoo')
wilson = Member('wilson','test2','t','t','t','Flushing Ave, NY')
chue = VIP('chue','bloo','blee','blee','blop','Empire State Building')

addDeliveryPerson(deliveryJiaMing)
deliveryJiaMing.setRating(1)
deliveryJiaMing.setRating(2)
deliveryJiaMing.setRating(1)
deliveryJiaMing.setRating(4)
deliveryJiaMing.setRating(5)
checkLaidOff(deliveryJiaMing)
deliveryBot2.setRating(1)
# deliveryBot2.startNewOrder(Order(chue, CurrentCart))
# deliveryBot.startNewOrder(Order(eric, CurrentCart))


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


# Give cook default inventory
defaultMeat = Supplies('Meat','Best', 24.99)
defaultMeat.setQuantity(25)
defaultFish = Supplies('Fish', 'Best', 31.99)
defaultFish.setQuantity(25)
defaultVegetables = Supplies('Vegetables', 'Best', 9.99)
defaultVegetables.setQuantity(25)
defaultFlour = Supplies('Flour', 'Best', 5.99)
defaultFlour.setQuantity(25)
defaultYeast = Supplies('Yeast', 'Best', 6.99)
defaultYeast.setQuantity(25)
defaultSalt = Supplies('Salt', 'Best', 3.99)
defaultSalt.setQuantity(25)
defaultSpices = Supplies('Spices', 'Best', 15.99)
defaultSpices.setQuantity(25)
defaultSugar = Supplies('Sugar', 'Best', 4.99)
defaultSugar.setQuantity(25)
defaultEgg = Supplies('Egg', 'Best', 5.99)
defaultEgg.setQuantity(25)
defaultDairy = Supplies('Dairy', 'Best', 8.99)
defaultDairy.setQuantity(25)

addCookSupplies(defaultMeat)
addCookSupplies(defaultFish)
addCookSupplies(defaultVegetables)
addCookSupplies(defaultFlour)
addCookSupplies(defaultYeast)
addCookSupplies(defaultSalt)
addCookSupplies(defaultSpices)
addCookSupplies(defaultSugar)
addCookSupplies(defaultEgg)
addCookSupplies(defaultDairy)

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
for i in range(len(SuppliesList)):
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
addUser(deliveryJiaMing)
addUser(deliveryBot2)

foodTest5 = Food('Eel', 5.99, 'Entrees', False)

foodTest1.setSold(3)
foodTest2.setSold(2)
foodTest3.setSold(6)
foodTest4.setSold(7)
foodTest5.setSold(5)

addMenuItem(foodTest1)
addMenuItem(foodTest2)
addMenuItem(foodTest3)
addMenuItem(foodTest4)
addMenuItem(foodTest5)
