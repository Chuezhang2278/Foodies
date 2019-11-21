class User():
    def __init__(self, first_name, last_name, username, password, email):    
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        self.Members = []
        self.VIP = []
    
    def addMember(self,Member): 
        self.Members.append(Member)
    
    def removeMember(self,Member):
        self.Members.remove(Member)
    
    def addVIP(self,VIP):
        self.VIP.append(VIP)

    def findMember(self, name):
        for i in range(0, len(self.Members)):
            if(Customer.Members[i].getFirst() == name):
                return (Customer.Members[i].getFirst())

    def findVIP(self, name):
        for i in range(0, len(self.VIP)):
            if(Customer.VIP[i].getFirst() == name):
                return (Customer.VIP[i].getFirst())

    def getsize(self):
        return len(self.Members)

    def get_discount(self):
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
    
    def getDiscount(self):
        return self.discount 
    
    def promoteVIP(self,name):
        for i in range(0, len(self.Members)):
            if(Customer.Members[i].getFirst() == name):
                para1 = Customer.Members[i].getFirst()
                para2 = Customer.Members[i].getLast()
                para3 = Customer.Members[i].getUser()
                para4 = Customer.Members[i].getEmail()
                para5 = Customer.Members[i].getPass()

        New = VIP(para1,para2,para3,para4,para5)
        Customer.addVIP(New)

class Member(User): 
    def __init__(self, first_name, last_name, username, password, email):
        super().__init__(first_name, last_name, username, password, email)
        self.discount = 0.85
        self.user_type = 1

class VIP(User): #Inherits VIP methods as well as user, polymorphism 
    def __init__(self, first_name, last_name, username, password, email):
        super().__init__(first_name,last_name,username, password, email)
        self.discount = 0.75
        self.user_type = 2

Customer = User('t','t','t','t','t')
eric = Member('eric','test2','t','t','t')
eric2 = VIP('Blah','bloo','blee','blop','t')
Customer.addMember(eric)
Customer.addVIP(eric2)
Customer.promoteVIP('Eric')