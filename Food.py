class Food():
    def __init__(self, name, price, cate, spicy):
        self.name = name
        self.price = price
        self.cate = cate
        self.spicy = spicy

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCate(self):
        return self.cate

    def getSpice(self):
        return self.spicy

# MOVED TO MAIN FILE
# MainMenu = Food('Test',1,'1',True)
# Chicken = Food('Chicken', 10, 'Entree', True)
# MainMenu.addMenu(Chicken)
# Fish = Food('Fish', 10, 'Entree', True)
# MainMenu.addMenu(Fish)
# Duck = Food('Duck', 10, 'Entree', True)
# MainMenu.addMenu(Duck)
# Dog = Food('Dog', 10, 'Entree', True)
# MainMenu.addMenu(Dog)
