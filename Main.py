from Employee import Manager, Cook, Delivery, Salesperson
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
    
 #====For_Storage====#   
DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
User = []
Employee = []
CurrentUser = []
CurrentCart = []
#====For_Storage====#


Chicken = Food('Chicken', 12.99, 'Entree', True, 100, 2, 4)
Fish = Food('Fish', 10.99, 'Entree', True, 500, 3, 5)
Duck = Food('Duck', 9.49, 'Entree', True, 122, 5, 6)
Dog = Food('Dog', 20.99, 'Entree', True, 5, 5, 7)
John = Cook('John','Username', 'test')
manager = Manager('y','y','y')
saleguy = Salesperson('x','x','x')
deli = Delivery('z','z','z','z')
void = Guest('void1','void2')
eric = Member('eric','test2','t','t','t','t')
chue = VIP('chue','bloo','blee','blee','blop','t')

addUser(void)
addUser(chue)
addUser(eric)
addUser(John)
addUser(manager)
addUser(saleguy)
addUser(deli)
addMenuItem(Duck)
addMenuItem(Dog)
addMenuItem(Fish)
addMenuItem(Chicken)

 