from Main import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Food_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.Name_listWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.Name_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Name_listWidget.setLineWidth(0)
        self.Name_listWidget.setSpacing(15)
        self.Name_listWidget.setObjectName("Name_listWidget")

        for i in range(len(Menu)):
            self.Name_listWidget.addItem(Menu[i].getFood_name())

        self.Price_listWidget = QtWidgets.QListWidget(self.page)
        self.Price_listWidget.setGeometry(QtCore.QRect(260, 25, 91, 561))
        self.Price_listWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.Price_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Price_listWidget.setSpacing(15)
        self.Price_listWidget.setObjectName("Price_listWidget")

        for i in range(len(Menu)):
            self.Price_listWidget.addItem(str(Menu[i].getFood_price()))

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
        self.Checkout_Button.setGeometry(QtCore.QRect(650, 505, 93, 28))
        self.Checkout_Button.setObjectName("Checkout_Button")
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
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(250, 160, 301, 121))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.Cart)

        self.Checkout_Button.clicked.connect(self.Checkout)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.Name_listWidget.isSortingEnabled()
        self.Name_listWidget.setSortingEnabled(False)
        self.Name_listWidget.setSortingEnabled(__sortingEnabled)
        self.AddButton2.setText(_translate("MainWindow", "Add"))
        self.AddButton4.setText(_translate("MainWindow", "Add"))
        self.AddButton9.setText(_translate("MainWindow", "Add"))
        self.AddButton1.setText(_translate("MainWindow", "Add"))
        self.Checkout_Button.setText(_translate("MainWindow", "Checkout"))
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
        self.label_2.setText(_translate("MainWindow", "CHECK OUT PAGE| UNDER CONSTRUCTION"))

    def Checkout(self):
        self.stackedWidget.setCurrentIndex(1)

    def Remove(self): #removal method has to be the same as cursed efficiency methods
        for item in self.Cart.selectedItems():
            self.Cart.takeItem(self.Cart.row(item))
            for i in range(MainMenu.getPurchaseSize()):
                if(MainMenu.Purchases[i].getFood_name() + '\t' + str(MainMenu.Purchases[i].getFood_price()) == item.text()): 
                    MainMenu.Purchases.pop(i)
                    break

    def Print(self):
        MainMenu.PrintCart()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Food_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
