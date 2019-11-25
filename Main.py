from Employee import Manager, Cook, Delivery
from Food import Food
from User import Member, VIP

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
def getMemberSize():
    return len(Members)

def getVIPsize():
    return len(VIPMembers)

def addMember(member):
    Members.append(member)
    print("Added " + member.getFirst() + " to Members")

def removeMember(member):
    Members.remove(member)
    print("Removed " + member.getFirst() + " from Members")

def addVIP(VIP):
    VIPMembers.append(VIP)
    print("Added " + VIP.getFirst() + " to VIPMembers")

def findMember(name):
    for i in range(len(Members)):
        if(Members[i].getFirst() == name):
            print('Member ' + Member[i].getFirst() + ' has been found')
            return Members[i]

def findVIP(name):
    for i in range(len(VIP)):
        if(VIP[i].getFirst() == name):
            print('VIP ' + VIP[i].getFirst() + ' has been found')
            return VIP[i]

def promoteVIP(name):
    for i in range(len(Members)):
        if(Members[i].getFirst() == name):
            print(Members[i].getFirst() + " found, promoting to VIP")
            para1 = Members[i].getFirst()
            para2 = Members[i].getLast()
            para3 = Members[i].getUser()
            para4 = Members[i].getEmail()
            para5 = Members[i].getPass()
            removeMember(Members[i])
            new = VIP(para1, para2, para3, para4, para5)
            addVIP(new)
            break

def printAllMembers():
    print("Printing list of Members and VIPMembers...")
    if(len(Members) == 0):
        print("\tMembers is empty")
    else:
        print("\tMembers: ", end='')
        for i in range(len(Members)):
            print(Members[i].getFirst(), end=' ')
        print('')
    if(len(VIPMembers) == 0):
        print("\tVIPMembers is empty")
    else:
        print("\tVIP Members: ", end='')
        for i in range(len(VIPMembers)):
            print(VIPMembers[i].getFirst(), end=' ')
        print('')


DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
Members = []
VIPMembers = []


# Testing Employee.py
#print("TESTING EMPLOYEE.PY:")
John = Cook('John','Username', 'test')
addCook(John)
# findCook("John")
# printCooks()
# DeliveryGuy = Delivery("Jia Ming", "jma8774", "jma8774", "160 Convent Ave, New York, NY 10031")

# Testing Food.py
#print("\nTESTING FOOD.PY:")
Chicken = Food('Chicken', 10, 'Entree', True, 100, 2)
addMenuItem(Chicken)
Fish = Food('Fish', 10, 'Entree', True, 500, 3)
addMenuItem(Fish)
Duck = Food('Duck', 10, 'Entree', True, 122, 5)
addMenuItem(Duck)
Dog = Food('Dog', 10, 'Entree', True, 5, 5)
addMenuItem(Dog)
#printMenu()

# Testing User.py
#print("\nTESTING USER.PY:")
eric = Member('eric','test2','t','t','t')
chue = VIP('chue','bloo','blee','blop','t')
addMember(eric)
addVIP(chue)
#printAllMembers()
# removed 'Eric' who was originally a Member, and moved him to VIPMembers
promoteVIP('eric'.title())
#printAllMembers()
