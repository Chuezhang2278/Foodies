from User import *

from PyQt5 import QtCore, QtGui, QtWidgets


class sign_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.First_Label = QtWidgets.QLabel(self.centralwidget)
        self.First_Label.setGeometry(QtCore.QRect(52, 20, 65, 20))
        self.First_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.First_Label.setObjectName("First_Label")
        self.Last_Label = QtWidgets.QLabel(self.centralwidget)
        self.Last_Label.setGeometry(QtCore.QRect(52, 60, 65, 20))
        self.Last_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Last_Label.setObjectName("Last_Label")
        self.User_Label = QtWidgets.QLabel(self.centralwidget)
        self.User_Label.setGeometry(QtCore.QRect(52, 100, 65, 16))
        self.User_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.User_Label.setObjectName("User_Label")
        self.Pass_Label = QtWidgets.QLabel(self.centralwidget)
        self.Pass_Label.setGeometry(QtCore.QRect(52, 140, 65, 16))
        self.Pass_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Pass_Label.setObjectName("Pass_Label")
        self.Email_Label = QtWidgets.QLabel(self.centralwidget)
        self.Email_Label.setGeometry(QtCore.QRect(52, 180, 65, 16))
        self.Email_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Email_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Email_Label.setObjectName("Email_Label")
        self.First_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.First_lineEdit.setGeometry(QtCore.QRect(128, 20, 201, 22))
        self.First_lineEdit.setObjectName("First_lineEdit")
        self.Last_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Last_lineEdit.setGeometry(QtCore.QRect(128, 60, 201, 22))
        self.Last_lineEdit.setObjectName("Last_lineEdit")
        self.User_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.User_lineEdit.setGeometry(QtCore.QRect(128, 100, 201, 22))
        self.User_lineEdit.setObjectName("User_lineEdit")
        self.Pass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Pass_lineEdit.setGeometry(QtCore.QRect(128, 140, 201, 22))
        self.Pass_lineEdit.setObjectName("Pass_lineEdit")
        self.Email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_lineEdit.setGeometry(QtCore.QRect(128, 180, 201, 22))
        self.Email_lineEdit.setObjectName("Email_lineEdit")
        self.signButton = QtWidgets.QPushButton(self.centralwidget)
        self.signButton.setGeometry(QtCore.QRect(60, 220, 271, 28))
        self.signButton.setObjectName("signButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.First_Label.setText(_translate("MainWindow", "First Name"))
        self.Last_Label.setText(_translate("MainWindow", "Last Name"))
        self.User_Label.setText(_translate("MainWindow", "Username"))
        self.Pass_Label.setText(_translate("MainWindow", "Password"))
        self.Email_Label.setText(_translate("MainWindow", "Email"))
        self.signButton.setText(_translate("MainWindow", "Finish Signing Up"))

    def SignButton(self):
        temp1 = self.First_lineEdit.text()
        temp2 = self.Last_lineEdit.text()
        temp3 = self.User_lineEdit.text()
        temp4 = self.Pass_lineEdit.text()
        temp5 = self.Email_lineEdit.text()

        eric = Member(temp1,temp2,temp3,temp4,temp5)
        Customer.addMember(eric)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = sign_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
