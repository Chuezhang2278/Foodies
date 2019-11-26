from Employee import Manager, Cook, Delivery
from Food import Food
from User import Member, VIP, Guest

# Employee
def addDeliveryPerson(employee):
    DeliveryPeople.append(employee)
    print("Added " + employee.getFirst() + " to DeliveryPeople")

def addCook(employee):
    Cooks.append(employee)
    print("Added " + employee.getFirst() + " to Cooks")

def addSalesperson(employee):
    Sales.append(employee)
    print("Added " + sales.getFirst() + " to Sales")

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
def getCustomerSize():
    return len(Customer)

def addCustomer(customer):
    Customer.append(customer)
    print("Added " + customer.getFirst() + " to Members")

def removeMember(customer):
    Customer.remove(customer)
    print("Removed " + customer.getFirst() + " from VIP")

def findCustomer(name):
    for i in range(len(Customer)):
        if(Customer[i].getFirst() == name):
            print('Member ' + Customer[i].getFirst() + ' has been found')
            return Customer[i]

def promoteVIP(name):
    for i in range(len(Customer)):
        if(Customer[i].getFirst() == name):
            print(Customer[i].getFirst() + " found, promoting to VIP")
            para1 = Customer[i].getFirst()
            para2 = Customer[i].getLast()
            para3 = Customer[i].getUser()
            para4 = Customer[i].getEmail()
            para5 = Customer[i].getPass()
            removeMember(Customer[i])
            new = VIP(para1, para2, para3, para4, para5)
            addCustomer(new)
            break
#NEEDS REWORKINg, DO LATER
''' 
def printAllCustomer():
    print("Printing list of Members and VIPMembers...")
    if(len(Customer) == 0):
        print("\tMembers is empty")
    else:
        print("\tMembers: ", end='')
        for i in range(len(Customer)):
            print(Customer[i].getFirst(), end=' ')
        print('')
    if(len(Customer) == 0):
        print("\tVIPMembers is empty")
    else:
        print("\tVIP Members: ", end='')
        for i in range(len(Customer)):
            print(Customer[i].getFirst(), end=' ')
        print('')
'''
def addCurrentUser(name):
    CurrentUser.append(name)
    
DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
Customer = []
CurrentUser = []



# Testing Employee.py
#print("TESTING EMPLOYEE.PY:")
John = Cook('John','Username', 'test')
addCook(John)
# findCook("John")
# printCooks()
# DeliveryGuy = Delivery("Jia Ming", "jma8774", "jma8774", "160 Convent Ave, New York, NY 10031")

# Testing Food.py
#print("\nTESTING FOOD.PY:")
Chicken = Food('Chicken', 12.99, 'Entree', True, 100, 2)
addMenuItem(Chicken)
Fish = Food('Fish', 10.99, 'Entree', True, 500, 3)
addMenuItem(Fish)
Duck = Food('Duck', 9.49, 'Entree', True, 122, 5)
addMenuItem(Duck)
Dog = Food('Dog', 20.99, 'Entree', True, 5, 5)
addMenuItem(Dog)
#printMenu()

# Testing User.py
#print("\nTESTING USER.PY:")
void = Guest('t')
eric = Member('eric','test2','t','t','t')
chue = VIP('chue','bloo','blee','blee','blop')
addCustomer(chue)
addCustomer(eric)
#printAllMembers()
# removed 'Eric' who was originally a Member, and moved him to VIPMembers
#promoteVIP('eric'.title())
#printAllMembers()
