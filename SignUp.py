from User import *

from PyQt5 import QtCore, QtGui, QtWidgets


class sign_window(object):
    def __init__(self):
        self.CurrentWindow = None;
        self.LoginWindow = None;

    def setupUi(self, CurrentWindow, LoginWindow):
        self.LoginWindow = LoginWindow
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(400, 286)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
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
        CurrentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

        self.signButton.clicked.connect(self.SignFunc)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "CurrentWindow"))
        self.First_Label.setText(_translate("CurrentWindow", "First Name"))
        self.Last_Label.setText(_translate("CurrentWindow", "Last Name"))
        self.User_Label.setText(_translate("CurrentWindow", "Username"))
        self.Pass_Label.setText(_translate("CurrentWindow", "Password"))
        self.Email_Label.setText(_translate("CurrentWindow", "Email"))
        self.signButton.setText(_translate("CurrentWindow", "Finish Signing Up"))

    def SignFunc(self):
        temp1 = self.First_lineEdit.text()
        temp2 = self.Last_lineEdit.text()
        temp3 = self.User_lineEdit.text()
        temp4 = self.Pass_lineEdit.text()
        temp5 = self.Email_lineEdit.text()

        eric = Member(temp1,temp2,temp3,temp4,temp5)
        Customer.addMember(eric)

        self.CurrentWindow.hide()
        self.LoginWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = sign_window()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())
