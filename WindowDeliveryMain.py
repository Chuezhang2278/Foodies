import qdarkstyle, Main
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKit, QtWebKitWidgets
from WindowMap import MapWindow

class DeliveryMainWindow(object):
    def __init__(self, LoginWindow):
        self.currentUser = Main.CurrentUser[0]
        self.rating = self.currentUser.getRating()
        self.LoginWindow = LoginWindow
        self.decideWhatToShow()

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

        self.currentOrder_button.clicked.connect(self.switch_currentOrder)
        self.logout_button.clicked.connect(self.switch_login)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Delivery Window", None, -1))
        self.logout_button.setText(QtWidgets.QApplication.translate("MainWindow", "Log Out", None, -1))
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

    def decideWhatToShow(self):
        if self.currentUser.getOrder() == None:
            pass # display biddings
        else:
            pass # display current order button

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

    def switch_login(self):
        self.MainWindow.hide()
        self.LoginWindow.logOut()
        self.LoginWindow.CurrentWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = DeliveryMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
