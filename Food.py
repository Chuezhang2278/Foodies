class Food():
    def __init__(self, name, price, cate, spicy):
        self.name = name
        self.price = price
        self.cate = cate
        self.spicy = spicy
        self.Menu = []
    
    def addMenu(self,Food):
        self.Menu.append(Food)
    
    def getFood_name(self):
        return self.name
    
    def getFood_price(self):
        return self.price
    
    def getCate(self):
        return self.cate

    def getSpice(self):
        return self.spicy
    
    def getMenuSize(self):
        return len(MainMenu.Menu)
    
    def PrintMenu(self):
        for i in range(MainMenu.getMenuSize()):
            print(MainMenu.Menu[i].getCate(), MainMenu.Menu[i].getFood_name(), MainMenu.Menu[i].getSpice())

MainMenu = Food('Test',1,'1',True)
Chicken = Food('Chicken', 10, 'Entree', True)
MainMenu.addMenu(Chicken)
Fish = Food('Fish', 10, 'Entree', True)
MainMenu.addMenu(Fish)
Duck = Food('Duck', 10, 'Entree', True)
MainMenu.addMenu(Duck)
Dog = Food('Dog', 10, 'Entree', True)
MainMenu.addMenu(Dog)