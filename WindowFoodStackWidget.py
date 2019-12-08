#SIDE NOTE
#YOU CANNOT JUST RUN THIS FILE ANYMORE FOR TESTING, YOU WILL GET AN ERROR ABOUT LISTS 
#RUN THE LOGIN FILE AND REFER TO MAIN.PY FOR USERLOGIN AND PASSWORD
#ALTERNIATIVELY USE GUEST OR MAKE AN ACCOUNT THROUGH SIGNUP

from Main import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Food_Window(object):
    def __init__(self):
        self.CurrentWindow = None
        self.LoginWindow = None
    
    def setupUi(self, CurrentWindow, LoginWindow):
        self.temp = 0
        self.LoginWindow = LoginWindow
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("MainWindow")
        CurrentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.Name_listWidget = QtWidgets.QListWidget(self.page)
        self.Name_listWidget.setEnabled(True)
        self.Name_listWidget.setGeometry(QtCore.QRect(30, 25, 221, 561))
        self.Name_listWidget.setAutoFillBackground(False)
        self.Name_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Name_listWidget.setLineWidth(0)
        self.Name_listWidget.setSpacing(15)
        self.Name_listWidget.setObjectName("Name_listWidget")

        self.Price_listWidget = QtWidgets.QListWidget(self.page)
        self.Price_listWidget.setGeometry(QtCore.QRect(260, 25, 91, 561))
        self.Price_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Price_listWidget.setSpacing(17)
        self.Price_listWidget.setObjectName("Price_listWidget")

        for i in range(len(Menu)):
                sortMenu()
                self.Name_listWidget.addItem(Menu[i].getName())
                self.Price_listWidget.addItem(str(Menu[i].getPrice()*CurrentUser[0].getDiscount()))

        self.AddButton2 = QtWidgets.QPushButton(self.page)
        self.AddButton2.setGeometry(QtCore.QRect(360, 90, 93, 28))
        self.AddButton2.setObjectName("AddButton2")
        self.AddButton4 = QtWidgets.QPushButton(self.page)
        self.AddButton4.setGeometry(QtCore.QRect(360, 192, 93, 28))
        self.AddButton4.setObjectName("AddButton4")
        self.AddButton9 = QtWidgets.QPushButton(self.page)
        self.AddButton9.setGeometry(QtCore.QRect(360, 452, 93, 28))
        self.AddButton9.setObjectName("AddButton9")
        self.AddButton1 = QtWidgets.QPushButton(self.page)
        self.AddButton1.setGeometry(QtCore.QRect(360, 38, 93, 28))
        self.AddButton1.setObjectName("AddButton1")
        self.Checkout_Button = QtWidgets.QPushButton(self.page)
        self.Checkout_Button.setGeometry(QtCore.QRect(660, 505, 93, 28))
        self.Checkout_Button.setObjectName("Checkout_Button")
        self.Remove_Button = QtWidgets.QPushButton(self.page)
        self.Remove_Button.setGeometry(QtCore.QRect(480, 505, 93, 28))
        self.Remove_Button.setObjectName("Checkout_Button")
        self.AddButton8 = QtWidgets.QPushButton(self.page)
        self.AddButton8.setGeometry(QtCore.QRect(360, 400, 93, 28))
        self.AddButton8.setObjectName("AddButton8")
        self.AddButton6 = QtWidgets.QPushButton(self.page)
        self.AddButton6.setGeometry(QtCore.QRect(360, 296, 93, 28))
        self.AddButton6.setObjectName("AddButton6")

        self.Cart = QtWidgets.QListWidget(self.page)
        self.Cart.setGeometry(QtCore.QRect(480, 39, 271, 441))
        self.Cart.setObjectName("Cart")
        
        self.AddButton5 = QtWidgets.QPushButton(self.page)
        self.AddButton5.setGeometry(QtCore.QRect(360, 244, 93, 28))
        self.AddButton5.setObjectName("AddButton5")
        self.AddButton10 = QtWidgets.QPushButton(self.page)
        self.AddButton10.setGeometry(QtCore.QRect(360, 504, 93, 28))
        self.AddButton10.setObjectName("AddButton10")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(580, 15, 55, 16))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.AddButton7 = QtWidgets.QPushButton(self.page)
        self.AddButton7.setGeometry(QtCore.QRect(360, 348, 93, 28))
        self.AddButton7.setObjectName("AddButton7")
        self.AddButton3 = QtWidgets.QPushButton(self.page)
        self.AddButton3.setGeometry(QtCore.QRect(360, 140, 93, 28))
        self.AddButton3.setObjectName("AddButton3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.finalCart = QtWidgets.QListWidget(self.page_2)
        self.finalCart.setGeometry(QtCore.QRect(230, 50, 301, 531))
        self.finalCart.setObjectName("finalCart")
        
        
        self.finalCheckOut = QtWidgets.QPushButton(self.page_2)
        self.finalCheckOut.setGeometry(QtCore.QRect(540, 150, 241, 31))
        self.finalCheckOut.setObjectName("finalCheckOut")
        self.finalTotal = QtWidgets.QLabel(self.page_2)
        self.finalTotal.setGeometry(QtCore.QRect(540, 60, 51, 16))
        self.finalTotal.setObjectName("finalTotal")
        self.finalCost = QtWidgets.QLabel(self.page_2)
        self.finalCost.setGeometry(QtCore.QRect(540, 100, 55, 16))
        self.finalCost.setObjectName("finalCost")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(230, 20, 55, 21))
        self.label_4.setObjectName("label_4")
        self.returnButton = QtWidgets.QPushButton(self.page_2)
        self.returnButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.returnButton.setObjectName("returnButton")
        self.stackedWidget.addWidget(self.page_2)
        CurrentWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.Cart)

        #====page1====#
        self.Remove_Button.clicked.connect(self.Remove)
        self.Checkout_Button.clicked.connect(self.Checkout)
        self.AddButton1.clicked.connect(self.Add_Button1)
        self.AddButton2.clicked.connect(self.Add_Button2)
        self.AddButton3.clicked.connect(self.Add_Button3)
        self.AddButton4.clicked.connect(self.Add_Button4)

        self.AddButton5.hide()
        self.AddButton6.hide()
        self.AddButton7.hide()
        self.AddButton8.hide()
        self.AddButton9.hide()
        self.AddButton10.hide()
        #====page1====#
        
        #====page2====#

        self.finalCheckOut.clicked.connect(self.Logout)
        self.returnButton.clicked.connect(self.Return)

        #====page2====#

        self.retranslateUi(CurrentWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.Name_listWidget.isSortingEnabled()
        self.Name_listWidget.setSortingEnabled(False)
        self.Name_listWidget.setSortingEnabled(__sortingEnabled)
        self.AddButton2.setText(_translate("MainWindow", "Add"))
        self.AddButton4.setText(_translate("MainWindow", "Add"))
        self.AddButton9.setText(_translate("MainWindow", "Add"))
        self.AddButton1.setText(_translate("MainWindow", "Add"))
        self.Checkout_Button.setText(_translate("MainWindow", "Checkout"))
        self.Remove_Button.setText(_translate("MainWindow", "Remove"))
        self.AddButton8.setText(_translate("MainWindow", "Add"))
        self.AddButton6.setText(_translate("MainWindow", "Add"))
        __sortingEnabled = self.Price_listWidget.isSortingEnabled()
        self.Price_listWidget.setSortingEnabled(False)
        self.Price_listWidget.setSortingEnabled(__sortingEnabled)
        self.AddButton5.setText(_translate("MainWindow", "Add"))
        self.AddButton10.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Cart"))
        self.AddButton7.setText(_translate("MainWindow", "Add"))
        self.AddButton3.setText(_translate("MainWindow", "Add"))
        #page 2
        self.finalCheckOut.setText(_translate("MainWindow", "Confirm Purchase"))
        self.finalTotal.setText(_translate("MainWindow", "Total"))
        self.finalCost.setText(_translate("MainWindow", "$$$"))
        self.label_4.setText(_translate("MainWindow", "My Cart"))
        self.returnButton.setText(_translate("MainWindow", "Return"))

    
    def Logout(self):
        self.CurrentWindow.hide()
        self.LoginWindow.show()
        self.finalCart.clear()
        CurrentUser.pop()
        CurrentUser.pop()
        self.finalCart.clear()
    
    def Checkout(self):
        i = 0
        self.stackedWidget.setCurrentIndex(1)
        self.finalCost.setText(str(self.temp))
        while i < currentCartSize():
            self.finalCart.addItem((User[CurrentUser[1]].order[i]) + "\t\t\t " + str(User[CurrentUser[1]].order[i+1]))
            i += 2
            
    def Return(self):
        self.stackedWidget.setCurrentIndex(0)
        self.finalCart.clear()
    
    def Remove(self): 
        listItems = self.Cart.selectedItems()
        if not listItems: return
        for item in listItems:
            self.Cart.takeItem(self.Cart.row(item))
            CurrentCart.pop(self.Cart.currentRow()+1)
            User[CurrentUser[1]].removeOrder()
        
    #Need a better method of implementing stuff below, VERY BAD EFFICIENCY
    #problem stems from the generation of buttons
    #when logging out, cart needs to still show 
    
    def Add_Button1(self):
        self.Cart.addItem(Menu[0].getName() + '\t\t\t' + str(Menu[0].getPrice()))    
        addCurrentCart(Menu[0])
        self.temp += (Menu[0].getPrice())
        User[CurrentUser[1]].addOrder(Menu[0].getName(),Menu[0].getPrice())
    def Add_Button2(self):
        self.Cart.addItem(Menu[1].getName() + '\t\t\t' + str(Menu[1].getPrice()))  
        addCurrentCart(Menu[1])
        self.temp += (Menu[1].getPrice())
        User[CurrentUser[1]].addOrder(Menu[1].getName(),Menu[1].getPrice())
    def Add_Button3(self):
        self.Cart.addItem(Menu[2].getName() + '\t\t\t' + str(Menu[2].getPrice()))  
        addCurrentCart(Menu[2])
        self.temp += (Menu[2].getPrice())
        User[CurrentUser[1]].addOrder(Menu[2].getName(),Menu[2].getPrice())
    def Add_Button4(self):
        self.Cart.addItem(Menu[3].getName() + '\t\t\t' + str(Menu[3].getPrice()))  
        addCurrentCart(Menu[3])
        self.temp += (Menu[3].getPrice())
        User[CurrentUser[1]].addOrder(Menu[3].getName(),Menu[3].getPrice())
    def Add_Button5(self):
        self.Cart.addItem(Menu[4].getName() + '\t\t\t' + str(Menu[4].getPrice())) 
        addCurrentCart(Menu[4])
        self.temp += (Menu[4].getPrice())
    def Add_Button6(self):
        self.Cart.addItem(Menu[5].getName() + '\t\t\t' + str(Menu[5].getNrice())) 
        addCurrentCart(Menu[5])
        self.temp += (Menu[5].getPrice())
    def Add_Button7(self):
        self.Cart.addItem(Menu[6].getName() + '\t\t\t' + str(Menu[6].getPrice()))  
        addCurrentCart(Menu[6])
        self.temp += (Menu[6].getPrice())
    def Add_Button8(self):
        self.Cart.addItem(Menu[7].getName() + '\t\t\t' + str(Menu[7].getPrice())) 
        addCurrentCart(Menu[7])
        self.temp += (Menu[7].getPrice())
    def Add_Button9(self):
        self.Cart.addItem(Menu[8].getName() + '\t\t\t' + str(Menu[8].getPrice()))
        addCurrentCart(Menu[8]) 
        self.temp += (Menu[8].getPrice())
    def Add_Button10(self):
        self.Cart.addItem(Menu[9].getName() + '\t\t\t' + str(Menu[9].getPrice()))  
        addCurrentCart(Menu[9])
        self.temp += (Menu[9].getPrice())
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = Food_Window()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())

