class Food():
    def __init__(self, name, price, cate, spicy):
        self.name = name
        self.price = price
        self.cate = cate
        self.spicy = spicy
        self.quantity = 0
        # quality rated from 1 to 5
        self.quality = 0
        self.sold = 0

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCate(self):
        return self.cate

    def getSpice(self):
        return self.spicy

    def getQuantity(self):
        return self.quantity

    def getQuality(self):
        return self.quality
    
    def setPrice(self, value):
        self.price = value

    def setQuality(self, quality):
        self.quality = quality

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setSold(self, amount):
        self.sold += amount

    def getSold(self):
        return self.sold

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
