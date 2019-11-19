class User():
    def __init__(self, first_name,last_name,username,email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.members = []
    
    def add(self,Member): #TESTING
        self.members.append(Member)
    
    def getsize(self):
        return len(self.members)
    
    def getfirst(self):
        return self.first_name
    
    def getlast(self):
        return self.last_name
    
    def getuser(self):
        return self.username
    
    def getemail(self):
        return self.email

class Member(User): #Inherits Users methods but not admins
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name,last_name,username,email)
        self.discount = 0.85
        self.user_type1 = 'Member'
        self.mem = []

    def get_discount(self):
        print(self.discount)
    
    def get_user_type(self):
        print(self.user_type1)

class VIP(Member): #Inherits VIP methods as well as user, polymorphism 
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name,last_name,username,email)
        self.user_type2 = 'VIP'
    
    def get_discount(self):
        return print(self.user_type2)

temp = User('a','b','c','d')



        






