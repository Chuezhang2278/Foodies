from threading import Thread
from time import sleep
from User import VIP, Member, Guest
from Food import Food
from Employee import Delivery
import sys

class Order():
    def __init__(self, User, cart):
        # User is a User object and cart is a List of Food objects
        self.customer = User
        self.delivery = None
        self.cart = cart
        # prices are in dollars
        self.totalCost = 0
        for i in range(len(self.cart)):
            self.totalCost += self.cart[i].getPrice()
        self.startingBid = 10 + (.2 * self.totalCost)
        self.currentBid = self.startingBid
        self.autoWin = 5
        self.bidCompleted = False
        # time is in seconds
        self.time = 120
        self.timerStarted = False

        print("\n\norder started...")
        print("startingBid: 10 + (.2 * " + str(self.totalCost) + ") = $" + str(self.startingBid))
        print("currentBid: $" + str(self.currentBid))
        print("autoWin: $" + str(self.autoWin))

    def bidComplete(self):
        self.bidCompleted = True
        self.delivery.startNewOrder(self)

    def bid(self, Delivery, bidAmount):
        # Delivery is a Delivery object
        print("\n\n" + Delivery.getFirst() + " bidded $" + str(bidAmount))
        if self.bidCompleted == False:
            if bidAmount < self.currentBid:
                self.delivery = Delivery
                self.currentBid = bidAmount
            else:
                print("currentBid not updated because the bidAmount is bigger than currentBid")
            print("currentBid: $" + str(self.currentBid), end="\n\n")
        if self.timerStarted == False:
            self.timeThread = Thread(target=self.startTimer)
            self.timeThread.start()
        if bidAmount <= self.autoWin:
            print("bid completed because bidAmount is equal to autoWin")
            self.bidComplete()

    def startTimer(self):
        self.timerStarted = True
        for i in range(120):
            if self.bidCompleted == True:
                break
            self.time -= 1
            print(self.secondsToMinute() + " time left")
            sleep(1)
        if self.bidCompleted == False:
            print("bid completed because times up")
            self.bidComplete()

    def getCustomer(self):
        return self.customer

    def secondsToMinute(self):
        min = int(self.time / 60)
        sec = self.time % 60
        if sec > 9:
            return str(min) + ":" + str(sec)
        else:
            return str(min) + ":0" + str(sec)

customer = Member("Jia Ming", "Ma", "jma8774", "password", "jma8774@bths.edu", "2369 W 11th St, NY")
chue = Delivery("Chue", "chue1", "password", "City College of New York")
eric = Delivery("Eric", "chue1", "password", "Hunter College")
jd = Delivery("JD", "chue1", "password", "Coney Island")
wilson = Delivery("Wilson", "chue1", "password", "Barclay Center")
jeemong = Delivery("Jeemong", "chue1", "password", "Brooklyn Bridge")
mohammed = Delivery("Mohammed", "chue1", "password", "Grand St")

order = Order(customer, [Food("Peanut", 100, "Entree", True, 100, 4)])
order.bid(chue, 26)
sleep(5)
order.bid(eric, 27)
sleep(5)
order.bid(jd, 20)
sleep(5)
order.bid(wilson, 15)
sleep(5)
order.bid(jeemong, 11)
sleep(5)
order.bid(wilson, 10)
sleep(5)
order.bid(jeemong, 9.5)
sleep(5)
order.bid(wilson, 7)
sleep(5)
order.bid(jeemong, 6)
sleep(5)
order.bid(mohammed, 5)
