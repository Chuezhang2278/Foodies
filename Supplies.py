
#supplies class for both the cook and salesperson
class Supplies():
    def __init__(self, name, quality, price): #price entered is the default price for "Good" Quality inventory
        self.name = name
        self.quality = quality
        self.quantity=0

        if quality=='Bad': #if quality is bad then cut default price by 50%
            self.price = price * .50
            self.price = round(self.price, 2)
        elif quality=='Best': #if quality is the best than increase by 120%
            self.price = price * 1.20
            self.price = round(self.price, 2)
        else: #if quality is neither bad or best than it is just the default price
            self.price = round(price, 2)



    #setters
    def setQuantity(self,quantity):
        self.quantity = quantity

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
            self.priec = round(self.price, 2)
        elif self.quality=='Best': #if quality is the best than increase by 120%
            self.price = self.price * 1.20
            self.price = round(self.price, 2)
        else: #if quality is neither bad or best than it is just the default price
            self.price=round(self.price,2)

    def changePrice(self,price):
        self.price=round(price, 2)
        self.updatePrice()

    def changeQuality(self, quality):
        self.quality=quality
        self.updatePrice()





