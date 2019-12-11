#SIDE NOTE
#YOU CANNOT JUST RUN THIS FILE ANYMORE FOR TESTING, YOU WILL GET AN ERROR ABOUT LISTS
#RUN THE LOGIN FILE AND REFER TO MAIN.PY FOR USERLOGIN AND PASSWORD
#ALTERNIATIVELY USE GUEST OR MAKE AN ACCOUNT THROUGH SIGNUP

from Main import *
from Order import Order
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import speech_recognition as sr

class Food_Window(object):
    def __init__(self):
        self.CurrentWindow = None
        self.LoginWindow = None
        self.r = sr.Recognizer()

    def setupUi(self, CurrentWindow, LoginWindow):
        self.temp = 0
        self.LoginWindow = LoginWindow
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("MainWindow")
        CurrentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.keyPressEvent = self.keyPressEvent
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
        self.Name_listWidget.setSpacing(17)
        self.Name_listWidget.setObjectName("Name_listWidget")

        self.Price_listWidget = QtWidgets.QListWidget(self.page)
        self.Price_listWidget.setGeometry(QtCore.QRect(260, 25, 91, 561))
        self.Price_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Price_listWidget.setSpacing(17)
        self.Price_listWidget.setObjectName("Price_listWidget")

        first = 0
        second = 0
        third = 0
        m1 = None
        m2 = None
        m3 = None

        for i in range(len(Menu)):
            #print(Menu[i].getSold())
            if(Menu[i].getSold() > first):
                third = second
                second = first
                first = Menu[i].getSold()
                m1 = Menu[i]

            elif(Menu[i].getSold() > second):
                third = second
                second = Menu[i].getSold()
                m2 = Menu[i]
            elif(Menu[i].getSold() > third):
                third = Menu[i].getSold()
                m3 = Menu[i]


        print(m1.getName())
        print(m2.getName())
        #print(m3.getName())

        for i in range(len(Menu)):
            if(Menu[i] == m1 or Menu[i] == m2 or Menu[i] == m3):
                self.Name_listWidget.addItem(Menu[i].getName() + "\t [Your top choice!]")
                self.Price_listWidget.addItem(format(Menu[i].getPrice()*CurrentUser[0].getDiscount(), '.2f'))
            else:
                self.Name_listWidget.addItem(Menu[i].getName())
                self.Price_listWidget.addItem(format(Menu[i].getPrice()*CurrentUser[0].getDiscount(), '.2f'))


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
        self.voice_button = QtWidgets.QPushButton(self.page)
        self.voice_button.setGeometry(QtCore.QRect(480, 540, 273, 28))
        self.voice_button.setText("Voice Recognition")
        self.voice_button.clicked.connect(self.voice_recognize)
        self.AddButton8 = QtWidgets.QPushButton(self.page)
        self.AddButton8.setGeometry(QtCore.QRect(360, 400, 93, 28))
        self.AddButton8.setObjectName("AddButton8")
        self.AddButton6 = QtWidgets.QPushButton(self.page)
        self.AddButton6.setGeometry(QtCore.QRect(360, 296, 93, 28))
        self.AddButton6.setObjectName("AddButton6")

        self.Cart = QtWidgets.QListWidget(self.page)
        self.Cart.setGeometry(QtCore.QRect(480, 39, 281, 441))
        self.Cart.setObjectName("Cart")



        if(len(User[CurrentUser[1]].order) > 0):
            for i in range(len(User[CurrentUser[1]].order)):
                self.Cart.addItem(User[CurrentUser[1]].order[i].getName() + "\t\t\t" + format(User[CurrentUser[1]].order[i].getPrice(), '.2f'))
                CurrentCart.append(User[CurrentUser[1]].order[i])

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

        self.Page2_Address = QtWidgets.QLineEdit(self.page_2)
        self.Page2_Address.setGeometry(QtCore.QRect(540,170,241,20))
        self.Page2_Address.setObjectName("Page2_Address")
        self.Page2_AddLabel = QtWidgets.QLabel(self.page_2)
        self.Page2_AddLabel.setGeometry(QtCore.QRect(540,140,47,13))
        self.Page2_AddLabel.setObjectName("Page2_AddLabel")

        self.finalCart = QtWidgets.QListWidget(self.page_2)
        self.finalCart.setGeometry(QtCore.QRect(230, 50, 301, 531))
        self.finalCart.setObjectName("finalCart")
        self.finalCheckOut = QtWidgets.QPushButton(self.page_2)
        self.finalCheckOut.setGeometry(QtCore.QRect(540, 200, 241, 31))
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
        self.Page2_logout = QtWidgets.QPushButton(self.page_2)
        self.Page2_logout.setGeometry(QtCore.QRect(700, 10, 75, 23))
        self.Page2_logout.setObjectName("Page2_logout")

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Page3_listView = QtWidgets.QListWidget(self.page_3)
        self.Page3_listView.setGeometry(QtCore.QRect(20, 50, 301, 531))
        self.Page3_listView.setObjectName("Page3_listView")


        self.Page3_label3 = QtWidgets.QLabel(self.page_3)
        self.Page3_label3.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.Page3_label3.setObjectName("Page3_label3")
        self.Page3_label1 = QtWidgets.QLabel(self.page_3)
        self.Page3_label1.setGeometry(QtCore.QRect(470, 90, 221, 21))
        self.Page3_label1.setObjectName("Page3_label1")
        self.Page3_label2 = QtWidgets.QLabel(self.page_3)
        self.Page3_label2.setGeometry(QtCore.QRect(470, 110, 191, 16))
        self.Page3_label2.setObjectName("Page3_label2")
        self.Page3_logout = QtWidgets.QPushButton(self.page_3)
        self.Page3_logout.setGeometry(QtCore.QRect(700, 10, 75, 23))
        self.Page3_logout.setObjectName("Page3_logout")
        self.stackedWidget.addWidget(self.page_3)
        self.Page3_next = QtWidgets.QPushButton(self.page_3)
        self.Page3_next.setGeometry(QtCore.QRect(700, 565, 75, 23))
        self.Page3_next.setObjectName("Page3_next2")
        self.Page3_label4 = QtWidgets.QLabel(self.page_3)
        self.Page3_label4.setGeometry(QtCore.QRect(400,140,351,61))
        self.Page3_label4.setObjectName("Page3_label4")
        self.stackedWidget.addWidget(self.page_3)


        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.Page4_label1 = QtWidgets.QLabel(self.page_4)
        self.Page4_label1.setGeometry(QtCore.QRect(50, 30, 181, 16))
        self.Page4_label1.setObjectName("Page4_label1")
        self.Page4_label2 = QtWidgets.QLabel(self.page_4)
        self.Page4_label2.setGeometry(QtCore.QRect(50, 70, 181, 16))
        self.Page4_label2.setObjectName("Page4_label2")
        self.Page4_label3 = QtWidgets.QLabel(self.page_4)
        self.Page4_label3.setGeometry(QtCore.QRect(50, 110, 371, 16))
        self.Page4_label3.setObjectName("Page4_label3")
        self.Page4_textedit = QtWidgets.QTextEdit(self.page_4)
        self.Page4_textedit.setGeometry(QtCore.QRect(50, 140, 561, 241))
        self.Page4_textedit.setObjectName("Page4_lineedit")
        self.Page4_submit = QtWidgets.QPushButton(self.page_4)
        self.Page4_submit.setGeometry(QtCore.QRect(700, 560, 75, 23))
        self.Page4_submit.setObjectName("Page4_submit")
        self.comboBox = QtWidgets.QComboBox(self.page_4)
        self.comboBox.setGeometry(QtCore.QRect(240, 30, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_4)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 70, 51, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(5, "")
        self.Page4_logout = QtWidgets.QPushButton(self.page_4)
        self.Page4_logout.setGeometry(QtCore.QRect(700, 10, 75, 23))
        self.Page4_logout.setObjectName("Page4_logout")
        self.stackedWidget.addWidget(self.page_4)

        #====page1====#
        self.Remove_Button.clicked.connect(self.Remove)
        self.Checkout_Button.clicked.connect(self.Checkout)

        self.AddButton1.hide()
        self.AddButton2.hide()
        self.AddButton3.hide()
        self.AddButton4.hide()
        self.AddButton5.hide()
        self.AddButton6.hide()
        self.AddButton7.hide()
        self.AddButton8.hide()
        self.AddButton9.hide()
        self.AddButton10.hide()
        self.Page2_Address.hide()
        self.Page2_AddLabel.hide()

        for i in range(len(Menu)):
            if i == 0:
                self.AddButton1.show()
            if i == 1:
                self.AddButton2.show()
            if i == 2:
                self.AddButton3.show()
            if i == 3:
                self.AddButton4.show()
            if i == 4:
                self.AddButton5.show()
            if i == 5:
                self.AddButton6.show()
            if i == 6:
                self.AddButton7.show()
            if i == 7:
                self.AddButton8.show()
            if i == 8:
                self.AddButton9.show()
            if i == 9:
                self.AddButton10.show()

        self.AddButton1.clicked.connect(self.Add_Button1)
        self.AddButton2.clicked.connect(self.Add_Button2)
        self.AddButton3.clicked.connect(self.Add_Button3)
        self.AddButton4.clicked.connect(self.Add_Button4)
        self.AddButton5.clicked.connect(self.Add_Button5)
        self.AddButton6.clicked.connect(self.Add_Button6)
        self.AddButton7.clicked.connect(self.Add_Button7)
        self.AddButton8.clicked.connect(self.Add_Button8)
        self.AddButton9.clicked.connect(self.Add_Button9)
        self.AddButton10.clicked.connect(self.Add_Button10)

        self.retranslateUi(CurrentWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)


        #====page1====#

        #====page2====#

        self.finalCheckOut.clicked.connect(self.change)
        self.returnButton.clicked.connect(self.Return)
        self.Page2_logout.clicked.connect(self.Logout)

        #====page2====#

        #====page3====#

        self.Page3_logout.clicked.connect(self.Logout)
        self.Page3_next.clicked.connect(self.changeFinal)
        self.Page3_label4.hide()

        #====page4====#

        self.Page4_submit.clicked.connect(self.Submittion)
        self.Page4_logout.clicked.connect(self.Logout)

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
        self.Page2_logout.setText(_translate("MainWindow", "Logout"))
        self.Page2_AddLabel.setText(_translate("Mainwindow", "Address"))
        #page 3
        self.Page3_label3.setText(_translate("MainWindow", "Your orders"))
        self.Page3_label1.setText(_translate("MainWindow", "Thank you for purchasing using our App! "))
        self.Page3_label2.setText(_translate("MainWindow", "Your food will be arriving shortly"))
        self.Page3_logout.setText(_translate("MainWindow", "Logout"))
        self.Page3_label4.setText(_translate("MainWindow", "Because You are a VIP, You get a random item on the menu FOR FREE"))
        self.Page3_next.setText(_translate("MainWindow", "Next"))

        #page 4
        self.Page4_label1.setText(_translate("MainWindow", "Please give the Delivery man a rating!"))
        self.Page4_label2.setText(_translate("MainWindow", "Please give our Chefs a rating!"))
        self.Page4_label3.setText(_translate("MainWindow", "If you have any complaints or concern, Please leave a message down below"))
        self.Page4_submit.setText(_translate("MainWindow", "Submit"))
        self.Page4_logout.setText(_translate("MainWindow", "Logout"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))

    def voice_recognize(self):
        self.mic = sr.Microphone()
        with self.mic as source:
            print("Listening to User")
            audio = self.r.listen(source)
        try:
            msg = self.r.recognize_google(audio)
        except Exception:
            print("Caught Exception")
            return

        print(msg)
        if "buy" in msg or "by" in msg or "hi" in msg or "ad" in msg or "find" in msg: # they all sound like buy
            print("Recognized buy")
            if "chicken" in msg:
                if self.hasNumbers(msg):
                    for i in range(self.determine1to9(msg)):
                        self.Add_Button1()
                else:
                    self.Add_Button1()
            elif "fish" in msg:
                if self.hasNumbers(msg):
                    for i in range(self.determine1to9(msg)):
                        self.Add_Button2()
                else:
                    self.Add_Button2()
            elif "duck" in msg or "thugs" in msg: # sound like ducks
                if self.hasNumbers(msg):
                    for i in range(self.determine1to9(msg)):
                        self.Add_Button3()
                else:
                    self.Add_Button3()
            elif "dog" in msg:
                if self.hasNumbers(msg):
                    for i in range(self.determine1to9(msg)):
                        self.Add_Button4()
                else:
                    self.Add_Button4()
            elif "eel" in msg or "seal" in msg: # sounds like eels
                if self.hasNumbers(msg):
                    for i in range(self.determine1to9(msg)):
                        self.Add_Button5()
                else:
                    self.Add_Button5()
        elif "sell" in msg or "remove" in msg:
            print("Recognized sell")
        elif "check" in msg or "out" in msg:
            print("Recognized checkout")
            self.Checkout()

    # def Remove(self):
    #     listItems = self.Cart.selectedItems()
    #     if not listItems: return
    #     for item in listItems:
    #         self.Cart.takeItem(self.Cart.row(item))
    #         CurrentCart.pop(self.Cart.currentRow()+1)
    #         User[CurrentUser[1]].removeUserOrder(self.Cart.currentRow())

    def hasNumbers(self, inputString):
        nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for i in nums:
            if i in inputString:
                return True
        return any(char.isdigit() for char in inputString)

    def determine1to9(self, inputString):
        for i in range(1, 10):
            if str(i) in inputString:
                return i
        nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for i in range(len(nums)):
            if nums[i] in inputString:
                return i + 1

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Backspace:
            print('Backspace pressed')
            self.Logout()

    def Recieved(self):
        User[CurrentUser[1]].confirmDelivery()

    def Submittion(self):
        try:
            User[CurrentUser[1]].deliveryPerson.setRating(int(self.comboBox.currentText()))
            checkLaidOff(User[CurrentUser[1]].deliveryPerson)
            User[CurrentUser[1]].cookPerson.setRating(int(self.comboBox_2.currentText()))
            checkLaidOff(User[CurrentUser[1]].cookPerson)
            temp = self.Page4_textedit.toPlainText()
            Complaint.append(temp)
        except Exception:
            pass

    def Logout(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Are you sure you want to logout?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, i):
        if(i.text() == "&Yes"):
            CurrentUser.clear()
            CurrentCart.clear()
            self.CurrentWindow.hide()
            self.LoginWindow.show()

    def Checkout(self):
        i = 0
        if currentCartSize() != 0:
            self.stackedWidget.setCurrentIndex(1)
        self.finalCost.setText(format(self.temp, '.2f'))

        while i < currentCartSize():
            self.finalCart.addItem(CurrentCart[i].getName() + "\t\t\t" + format(CurrentCart[i].getPrice(), '.2f'))
            i += 1

        if(User[CurrentUser[1]].getType()):
            self.Page2_AddLabel.show()
            self.Page2_Address.show()

        print(currentCartSize())

    def Return(self):
        self.stackedWidget.setCurrentIndex(0)
        self.finalCart.clear()

    def change(self):
        i = 0

        self.stackedWidget.setCurrentIndex(2)
        randFood = random.randint(0, len(Menu)-1)
        temp = CurrentCart.copy()
        if(User[CurrentUser[1]].getType() == 0):
            addPendingOrder(Order(void, temp))

        elif(User[CurrentUser[1]].getType() != 0):
            if(User[CurrentUser[1]].getType() == 2):

                randomFood = Food(Menu[randFood].getName() + " *Free*",0,Menu[randFood].getCate(),Menu[randFood].getSpice())
                User[CurrentUser[1]].addUserOrder(randomFood)
                addCurrentCart(randomFood)
                self.Page3_label4.show()

            addPendingOrder(Order(User[CurrentUser[1]], temp))
        while i < len(User[CurrentUser[1]].order):
            self.Page3_listView.addItem(User[CurrentUser[1]].order[i].getName() + "\t\t\t" + format(User[CurrentUser[1]].order[i].getPrice(), '.2f'))
            i += 1

        print(currentCartSize())


    def changeFinal(self):
        if(User[CurrentUser[1]].getType() == 0):
            print("Thank You for Purchasing")
        else:
            self.stackedWidget.setCurrentIndex(3)

    def Remove(self):
        listItems = self.Cart.selectedItems()
        if not listItems: return
        for item in listItems:
            self.Cart.takeItem(self.Cart.row(item))
            CurrentCart.pop(self.Cart.currentRow()+1)
            User[CurrentUser[1]].removeUserOrder(self.Cart.currentRow())

    def Add_Button1(self):
        self.Cart.addItem(Menu[0].getName() + '\t\t\t' + format(Menu[0].getPrice(), '.2f'))
        addCurrentCart(Menu[0])
        self.temp += (Menu[0].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[0])
    def Add_Button2(self):
        self.Cart.addItem(Menu[1].getName() + '\t\t\t' + format(Menu[1].getPrice(), '.2f'))
        addCurrentCart(Menu[1])
        self.temp += (Menu[1].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[1])
    def Add_Button3(self):
        self.Cart.addItem(Menu[2].getName() + '\t\t\t' + format(Menu[2].getPrice(), '.2f'))
        addCurrentCart(Menu[2])
        self.temp += (Menu[2].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[2])
    def Add_Button4(self):
        self.Cart.addItem(Menu[3].getName() + '\t\t\t' + format(Menu[3].getPrice(), '.2f'))
        addCurrentCart(Menu[3])
        self.temp += (Menu[3].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[3])
    def Add_Button5(self):
        self.Cart.addItem(Menu[4].getName() + '\t\t\t' + format(Menu[4].getPrice(), '.2f'))
        addCurrentCart(Menu[4])
        self.temp += (Menu[4].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[4])
    def Add_Button6(self):
        self.Cart.addItem(Menu[5].getName() + '\t\t\t' + format(Menu[5].getPrice(), '.2f'))
        addCurrentCart(Menu[5])
        self.temp += (Menu[5].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[5])
    def Add_Button7(self):
        self.Cart.addItem(Menu[6].getName() + '\t\t\t' + format(Menu[6].getPrice(), '.2f'))
        addCurrentCart(Menu[6])
        self.temp += (Menu[6].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[6])
    def Add_Button8(self):
        self.Cart.addItem(Menu[7].getName() + '\t\t\t' + format(Menu[7].getPrice(), '.2f'))
        addCurrentCart(Menu[7])
        self.temp += (Menu[7].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[7])
    def Add_Button9(self):
        self.Cart.addItem(Menu[8].getName() + '\t\t\t' + format(Menu[8].getPrice(), '.2f'))
        addCurrentCart(Menu[8])
        self.temp += (Menu[8].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[8])
    def Add_Button10(self):
        self.Cart.addItem(Menu[9].getName() + '\t\t\t' + format(Menu[9].getPrice(), '.2f'))
        addCurrentCart(Menu[9])
        self.temp += (Menu[9].getPrice())
        User[CurrentUser[1]].addUserOrder(Menu[9])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = Food_Window()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())
