class Admin():
    def __init__(self, first_name, username, password):
        self.first_name = first_name.title()
        self.username = username
        self.password = password
        self.Delivery = []
        self.Cook = []
        self.Sales = []

    def __DeliveryAdd(self, Delivery):
        self.Delivery.append(Delivery)
        
    def CookAdd(self, Cook):
        self.Cook.append(Cook)

    def SalesAdd(self, Sales):
        self.Sales.append(Sales)

    def getFirst(self):
        return self.first_name
    
    def getUser(self):
        return self.username

    def getSalary(self):
        return self.salary
    
    def getBudget(self):
        return self.budget

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def increaseSalary(self):
        return (self.salary + (self.salary * .10))
    
    def FindCook(self,name):
        for i in range(len(Admin.Cook)):
            if(Admin.Cook[i].getFirst() == name):
                return (Admin.Cook[i].getFirst() + ' found')

class Delivery(Admin):
    def __init__(self, first_name, username, password, x, y,):
        super().__init__(first_name,username,password)
        self.x = x
        self.y = y

class Cook(Admin):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)  
        self.salary = 10

class Sales(Admin):
    def __init__(self,first_name, username, password):
        super().__init__(first_name,username,password)
        self.salary = 20
        self.budget = 600

Admin = Admin('t','t','t')
John = Cook('John','Username', 'test')
Admin.CookAdd(John)

#print(Admin.FindCook('John'))
#for i in range(len(Admin.Cook)):
#    print(Admin.Cook[i].increaseSalary())



