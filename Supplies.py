
#supplies class for both the cook and salesperson
class Supplies():
    def __init__(self, name, quality, price, quantity): #price entered is the default price for "Good" Quality inventory
        self.name = name
        self.quality = quality
        self.quantity = quantity

        if quality=='Bad': #if quality is bad then cut default price by 50%
            self.price = price * .50
        elif quality=='Best': #if quality is the best than increase by 120%
            self.price = price * 1.20
        else: #if quality is neither bad or best than it is just the default price
            self.price=price


    #getters
    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    # Update the price if the price changes or if quality is changed
    def updatePrice(self):
        if self.quality=='Bad': #if quality is bad then cut default price by 50%
            self.price = self.price * .50
        elif self.quality=='Best': #if quality is the best than increase by 120%
            self.price = self.price * 1.20
        else: #if quality is neither bad or best than it is just the default price
            self.price=self.price

    def changePrice(self,price):
        self.price=price
        self.updatePrice()

    def changeQuality(self, quality):
        self.quality=quality
        self.updatePrice()

    def changeQuantity(self, quantity):
        self.quantity=quantity