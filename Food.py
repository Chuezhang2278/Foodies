class Food():
    def __init__(self, name, price, cate, spicy, quantity, quality, sold):
        self.name = name
        self.price = price
        self.cate = cate
        self.spicy = spicy
        self.quantity = quantity
        # quality rated from 1 to 5
        self.quality = quality
        self.sold = sold

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

    def setQuality(self, quality):
        self.quality = quality

    def setQuantity(self, quantity):
        self.quantity = quantity
    
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
