
#supplies class for both the cook and salesperson
class Supplies():
    def __init__(self, name, quality, price): #price entered is the default price for "Good" Quality inventory
        self.name = name
        self.quality = quality
        self.quantity=0
        self.deal_of_the_day_boolean = False

        if quality=='Bad': #if quality is bad then cut default price by 50%
            self.price = price * .50
            self.price = round(self.price, 2)
        elif quality=='Best': #if quality is the best than increase by 120%
            self.price = price * 1.20
            self.price = round(self.price, 2)
        else: #if quality is neither bad or best than it is just the default price
            self.price = round(price, 2)



    #setters
    def setQuantity(self, quantity):
        self.quantity = quantity

    def setPrice(self, price):
        self.price = round(price, 2)

    #set the supply as the deal of the day
    def setDealOfTheDay(self):
        self.deal_of_the_day_boolean = True

    #getters
    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    #used to determine if this supply is a deal of the day
    def isDealOfTheDay(self):
        return self.deal_of_the_day_boolean

    # Update the price if the price changes or if quality is changed
    def updatePrice(self):
        if self.quality=='Bad': #if quality is bad then cut default price by 50%
            self.price = self.price * .50
            self.price = round(self.price, 2)
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





