import qdarkstyle, Main, random
from threading import Thread
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKit, QtWebKitWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from WindowMap import MapWindow

class DeliveryMainWindow(object):
    def __init__(self, LoginWindow):
        self.currentUser = Main.CurrentUser[0]
        self.orders = Main.Orders
        self.rating = self.currentUser.getRating()
        self.LoginWindow = LoginWindow
        self.selectOrder = False
        self.viewingOrder = None
        self.firstScene = [] # delivery man already has an order
        self.secondScene = [] # delivery man looking at a selected order
        self.thirdScene = [] # delivery man looking at a list of orders

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 667)
        MainWindow.setMinimumSize(QtCore.QSize(467, 667))
        MainWindow.setMaximumSize(QtCore.QSize(467, 667))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(330, 40, 93, 28))
        self.logout_button.setObjectName("logout_button")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(330, 80, 93, 28))
        self.refresh_button.setObjectName("refresh_button")
        self.currentOrder_button = QtWidgets.QPushButton(self.centralwidget)
        self.currentOrder_button.setGeometry(QtCore.QRect(130, 360, 181, 28))
        self.currentOrder_button.setObjectName("currentOrder_button")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(30, 40, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.rating_label = QtWidgets.QLabel(self.centralwidget)
        self.rating_label.setGeometry(QtCore.QRect(30, 130, 271, 20))
        self.rating_label.setObjectName("rating_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 100, 211, 20))
        self.username_label.setObjectName("username_label")
        self.last_3_rating_label = QtWidgets.QLabel(self.centralwidget)
        self.last_3_rating_label.setGeometry(QtCore.QRect(30, 160, 450, 20))
        self.last_3_rating_label.setObjectName("last_3_rating_label")
        self.warning_label = QtWidgets.QLabel(self.centralwidget)
        self.warning_label.setGeometry(QtCore.QRect(30, 190, 350, 20))
        self.warning_label.setObjectName("warnings")
        MainWindow.setCentralWidget(self.centralwidget)

        # third scene
        self.orderWidgets = QtWidgets.QListWidget(self.centralwidget)
        self.orderWidgets.setEnabled(True)
        self.orderWidgets.setGeometry(QtCore.QRect(30, 225, 400, 425))
        self.orderWidgets.setAutoFillBackground(False)
        self.orderWidgets.setObjectName("orderWidgets")
        self.orderWidgets.itemDoubleClicked.connect(self.openBid)
        self.orderWidgets.setStyleSheet("QListWidget:item{border-left: 3px solid #7FB3D5;} QListWidget::item:selected {border-left: 3px solid #C39BD3;}")

        # second scene
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(30, 40, 93, 28))
        self.back_button.setText("Back")
        self.custName_label = QtWidgets.QLabel(self.centralwidget)
        self.custName_label.setGeometry(QtCore.QRect(30, 70, 271, 40))
        self.custName_label.setFont(font)
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(350, 37, 93, 40))
        self.orderID_label = QtWidgets.QLabel(self.centralwidget)
        self.orderID_label.setGeometry(QtCore.QRect(30, 120, 211, 40))
        self.totalCost_label = QtWidgets.QLabel(self.centralwidget)
        self.totalCost_label.setGeometry(QtCore.QRect(30, 150, 211, 40))
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(30, 180, 500, 40))
        self.starting_label = QtWidgets.QLabel(self.centralwidget)
        self.starting_label.setGeometry(QtCore.QRect(30, 210, 211, 40))
        self.current_label = QtWidgets.QLabel(self.centralwidget)
        self.current_label.setGeometry(QtCore.QRect(30, 240, 211, 40))
        self.autoWin_label = QtWidgets.QLabel(self.centralwidget)
        self.autoWin_label.setGeometry(QtCore.QRect(30, 270, 211, 40))
        self.bidHistoryWidget = QtWidgets.QListWidget(self.centralwidget)
        self.bidHistoryWidget.setEnabled(True)
        self.bidHistoryWidget.setGeometry(QtCore.QRect(30, 310, 400, 260))
        self.bidHistoryWidget.setAutoFillBackground(False)
        self.bidHistoryWidget.setStyleSheet("QListWidget:item{border-left: 3px solid #7FB3D5;} QListWidget::item:selected {border-left: 3px solid #C39BD3;}")
        self.bidAmount_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.bidAmount_edit.setGeometry(QtCore.QRect(120, 600, 93, 28))
        self.bidAmount_edit.setValidator(QtGui.QDoubleValidator())
        self.bid_button = QtWidgets.QPushButton(self.centralwidget)
        self.bid_button.setGeometry(QtCore.QRect(240, 600, 93, 28))


        self.firstScene = [self.logout_button, self.currentOrder_button, self.name_label, self.rating_label, self.username_label, self.last_3_rating_label, self.warning_label]
        self.secondScene = [self.back_button, self.custName_label, self.time_label, self.orderID_label, self.totalCost_label, self.address_label, self.starting_label, self.current_label, self.autoWin_label, self.bidHistoryWidget, self.bidAmount_edit, self.bid_button]
        self.thirdScene = [self.logout_button, self.refresh_button, self.name_label, self.rating_label, self.username_label, self.last_3_rating_label, self.warning_label, self.orderWidgets]

        self.centralwidget.keyPressEvent = self.keyPressEvent
        self.bid_button.clicked.connect(self.bid)
        self.back_button.clicked.connect(self.back)
        self.currentOrder_button.clicked.connect(self.switch_currentOrder)
        self.logout_button.clicked.connect(self.open_logoutConfirmation)
        self.refresh_button.clicked.connect(self.refresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.decideWhatToShow()
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Delivery Window", None, -1))
        self.logout_button.setText(QtWidgets.QApplication.translate("MainWindow", "Log Out", None, -1))
        self.refresh_button.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.currentOrder_button.setText(QtWidgets.QApplication.translate("MainWindow", "View Current Order", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("MainWindow", self.currentUser.getFirst(), None, -1))
        if self.rating > -1:
            self.last_3_rating_label.setText(QtWidgets.QApplication.translate("MainWindow", "Last 3 Ratings: " + self.getLast3AsStars(self.currentUser), None, -1))
            self.rating_label.setText(QtWidgets.QApplication.translate("MainWindow", "Customer Rating: " + self.convertRatingToStars(self.rating), None, -1))
        else:
            self.last_3_rating_label.setText(QtWidgets.QApplication.translate("MainWindow", "Last 3 Ratings: None", None, -1))
            self.rating_label.setText(QtWidgets.QApplication.translate("MainWindow", "Customer Rating: None", None, -1))
        self.username_label.setText(QtWidgets.QApplication.translate("MainWindow", "Username: " + self.currentUser.getUser(), None, -1))
        self.warning_label.setText(QtWidgets.QApplication.translate("MainWindow", "Warnings: " + str(self.currentUser.getWarnings()), None, -1))

    def updateSecondScene(self):
        self.custName_label.setText(self.viewingOrder.getCustomer().getFirst())
        self.time_label.setText(self.viewingOrder.getTime())
        self.orderID_label.setText("Order ID: " + self.viewingOrder.getId())
        self.totalCost_label.setText("Order Cost: $" + format(self.viewingOrder.getTotalCost(), '.2f'))
        self.address_label.setText("Order Address: " + self.viewingOrder.getCustomer().getAddress())
        self.starting_label.setText("Starting Bid: $" + format(self.viewingOrder.getStartingBid(), '.2f'))
        self.current_label.setText("Current Bid: $" + format(self.viewingOrder.getCurrentBid(), '.2f'))
        self.autoWin_label.setText("Auto Win: $" + format(self.viewingOrder.getAutoWin(), '.2f'))
        self.bid_button.setText("Bid")

    def addHistory(self, str):
        self.bidHistoryWidget.addItem(str)

    def refresh(self):
        self.orders = Main.Orders
        self.orderWidgets.clear()
        for i in self.orders:
            self.orderWidgets.addItem("Order ID: " + i.getId() + " (" + i.getCustomer().getFirst() + ")\nAddress: " + i.getCustomer().getAddress() + "\nCurrent Bid: $" + format(i.getCurrentBid(), '.2f') + "\nBid Time: " + i.getTime() + "\n")

    def bid(self):
        self.viewingOrder.bid(self.currentUser, float(self.bidAmount_edit.text()))
        self.updateSecondScene()

    def back(self):
        if self.currentUser.getBidded() == False:
            self.viewingOrder.setWindow(None)
            self.selectOrder = False
            self.refresh()
            self.decideWhatToShow()

    def autoRefresh(self):
        while True:
            self.refresh()
            sleep(1)
            if Main.threadKill == True or self.currentUser.getOrder() != None or self.selectOrder == True or self.onWindow == False:
                break
        print("Auto refresh thread killed")

    def openBid(self):
        for i in self.orders:
            if i.getId() == self.orderWidgets.currentItem().text()[10:18]:
                self.viewingOrder = i
                self.viewingOrder.setWindow(self)
        if self.viewingOrder != None:
            self.selectOrder = True
        self.decideWhatToShow()

    def decideWhatToShow(self):
        self.onWindow = True
        if self.currentUser.getOrder() == None and self.selectOrder == False:
            for i in self.firstScene:
                i.hide()
            for i in self.secondScene:
                i.hide()
            self.viewingOrder = None
            for i in self.thirdScene:
                i.show()
            self.refresh()
            self.autoRefreshThread = Thread(target=self.autoRefresh)
            self.autoRefreshThread.start()
        elif self.currentUser.getOrder() == None:
            for i in self.thirdScene:
                i.hide()
            for i in self.secondScene:
                i.show()
            self.bidHistoryWidget.clear()
            self.updateSecondScene()
            for i in self.firstScene:
                i.hide()
        else:
            for i in self.thirdScene:
                i.hide()
            for i in self.secondScene:
                i.hide()
            self.viewingOrder = None
            for i in self.firstScene:
                i.show()

    def convertRatingToStars(self, rating):
        s = ''
        for i in range(int(rating)):
            s += '★'
        for i in range(5 - int(rating)):
            s += '☆'
        return s + " (" + str(rating) + ") "

    def getLast3AsStars(self, User):
        s = ''
        if len(User.getLast3Rating()) == 0:
            return "None"
        for i in User.getLast3Rating():
            s += self.convertRatingToStars(i)
        return s

    def switch_currentOrder(self):
        if self.currentUser.getOrder() != None:
            self.NewWindow = QtWidgets.QMainWindow()
            self.ui = MapWindow(self)
            self.ui.setupUi(self.NewWindow)
            self.MainWindow.hide()
            self.NewWindow.show()
            self.onWindow = False

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Backspace:
            print('Backspace pressed')
            self.open_logoutConfirmation()

    def open_logoutConfirmation(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Logout")
        self.msg.setText("Are you sure you want to logout?")
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.Yes)

        self.msg.buttonClicked.connect(self.switch_login)

        x = self.msg.exec_()

    def switch_login(self, i):
        if(i.text() == "&Yes"):
            self.onWindow = False
            Main.CurrentUser.clear()
            self.MainWindow.hide()
            self.LoginWindow.show()
