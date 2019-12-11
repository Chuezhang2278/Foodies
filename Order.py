from threading import Thread
from time import sleep
from User import VIP, Member, Guest
from Food import Food
from Employee import Delivery
from datetime import datetime
import random
import sys, random, Main

class Order():
    def __init__(self, User, cart):
        # User is a User object and cart is a List of Food objects
        self.window = None
        self.killThread = False
        self.Id = self.generateId()
        self.customer = User
        self.delivery = None
        self.cook = None
        self.cart = cart
        # prices are in dollars
        self.totalCost = 0
        for i in range(len(self.cart)):
            self.totalCost += self.cart[i].getPrice()
        self.startingBid = 10 + (.13 * self.totalCost)
        self.currentBid = self.startingBid
        self.autoWin = 5
        self.bidCompleted = False
        # time is in seconds
        self.time = 60
        self.timerStarted = False

        # print("\n\norder started...")
        # print("startingBid: 10 + (.2 * " + str(self.totalCost) + ") = $" + str(self.startingBid))
        # print("currentBid: $" + str(self.currentBid))
        # print("autoWin: $" + str(self.autoWin))

    def bidComplete(self):
        self.bidCompleted = True
        self.time = 0
        if self.window != None:
            now = datetime.now().strftime("%H:%M:%S")
            self.window.addHistory("[" + str(now) + "] " + self.delivery.getFirst() + " won the bidding, please press back to see your new order!")
        Main.Orders.remove(self)
        self.delivery.startNewOrder(self)

    def bid(self, Delivery, bidAmount):
        # Delivery is a Delivery object
        now = datetime.now().strftime("%H:%M:%S")

        if bidAmount < 0:
            self.window.addHistory("[" + str(now) + "] " + Delivery.getFirst() + "'s bid failed, must bid positive amount")
            return

        if self.bidCompleted == False and self.delivery != Delivery:
            if bidAmount < self.currentBid:
                if self.delivery != None:
                    self.delivery.setBidded(False)
                self.delivery = Delivery
                self.delivery.setBidded(True)
                self.currentBid = bidAmount
                if bidAmount <= self.autoWin:
                    self.window.addHistory("[" + str(now) + "] " + self.delivery.getFirst() + " bidded $" + format(bidAmount, '.2f') + ", which is the auto win amount.")
                    self.bidComplete()
                    # bot simulation instant delivery for TESTING
                    if self.delivery == Main.deliveryBot2:
                        self.orderCompleted()
                elif self.timerStarted == False:
                    self.window.addHistory("[" + str(now) + "] " + self.delivery.getFirst() + " bidded $" + format(bidAmount, '.2f') + ".")
                    self.window.addHistory("[" + str(now) + "] Timer started!")
                    self.timeThread = Thread(target=self.startTimer)
                    self.timeThread.start()
                else:
                    self.window.addHistory("[" + str(now) + "] " + self.delivery.getFirst() + " bidded $" + format(bidAmount, '.2f') + ".")
            else:
                self.window.addHistory("[" + str(now) + "] " + Delivery.getFirst() + "'s bid failed, amount bid is higher than current bid.")
        else:
            self.window.addHistory("[" + str(now) + "] " + Delivery.getFirst() + "'s bid failed, you can't bid against yourself.")

    def startTimer(self):
        bot_bid = False
        if random.uniform(0, 1) > 0.3:
            bot_bid = True
        self.timerStarted = True
        for i in range(60):
            if self.bidCompleted == True or self.killThread:
                break
            if self.time > 0:
                self.time -= 1
            if i % 5 == 0 and bot_bid == True and self.delivery != Main.deliveryBot2:
                self.bid(Main.deliveryBot2, self.currentBid - 1)
            if self.window != None:
                self.window.updateSecondScene()
            sleep(1)
        if self.killThread:
            print("Order timer thread killed")
        elif self.bidCompleted == False:
            if self.window != None:
                now = datetime.now().strftime("%H:%M:%S")
                self.window.addHistory("[" + str(now) + "] Time's up!")
            self.bidComplete()
            # bot simulation instant delivery for TESTING
            if self.delivery == Main.deliveryBot2:
                self.orderCompleted()

    def getCustomer(self):
        return self.customer

    def getTime(self):
        min = int(self.time / 60)
        sec = self.time % 60
        if sec > 9:
            return str(min) + ":" + str(sec)
        else:
            return str(min) + ":0" + str(sec)

    def setKillThread(self, bool):
        self.killThread = bool

    def getTotalCost(self):
        return self.totalCost

    def getId(self):
        return self.Id

    def getStartingBid(self):
        return self.startingBid

    def getCurrentBid(self):
        return self.currentBid

    def setWindow(self, window):
        self.window = window

    def getAutoWin(self):
        return self.autoWin

    def generateId(self):
        Id = 0
        for i in range(8):
            Id += random.randint(0, 9) * (10**i)
        Id = str(Id)
        while len(Id) < 8:
            Id = "0" + Id
        return Id

    def orderCompleted(self):
        self.timeCompleted = datetime.now().strftime("%H:%M:%S")
        Main.addOrderHistoy(self)
        print("OrderHistoy length is now " + str(len(Main.OrderHistory)) + " and orderID " + self.Id + " has been put into OrderHistory")

    def getTimeCompleted(self):
        return self.timeCompleted

    def getCook(self):
        return self.cook

    def getUser(self):
        return self.customer

    def setCook(self, Cook):
        self.cook = Cook

    def getCart(self):
        return self.cart


# customer = Member("Jia Ming", "Ma", "jma8774", "password", "jma8774@bths.edu", "2369 W 11th St, NY")
# chue = Delivery("Chue", "chue1", "password", "City College of New York")
# eric = Delivery("Eric", "chue1", "password", "Hunter College")
# jd = Delivery("JD", "chue1", "password", "Coney Island")
# wilson = Delivery("Wilson", "chue1", "password", "Barclay Center")
# jeemong = Delivery("Jeemong", "chue1", "password", "Brooklyn BrIdge")
# mohammed = Delivery("Mohammed", "chue1", "password", "Grand St")

# order = Order(customer, [Food("Peanut", 100, "Entree", True, 100, 4, 1)])
# order.bId(chue, 26)
# sleep(5)
# order.bId(eric, 27)
# sleep(5)
# order.bId(jd, 20)
# sleep(5)
# order.bId(wilson, 15)
# sleep(5)
# order.bId(jeemong, 11)
# sleep(5)
# order.bId(wilson, 10)
# sleep(5)
# order.bId(jeemong, 9.5)
# sleep(5)
# order.bId(wilson, 7)
# sleep(5)
# order.bId(jeemong, 6)
# sleep(5)
# order.bId(mohammed, 5)
