

        
        
from Main import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date

class Sales_Window(object):


    def __init__(self):
        self.CurrentWindow = None;
        self.LoginWindow = None;

    def setupUi(self, CurrentWindow, LoginWindow):
        self.CurrentWindow = CurrentWindow
        self.LoginWindow = LoginWindow
        self.total = 0 # total cost for the cart
        self.total = round(self.total, 2)
        self.budget_remaining = round(User[CurrentUser[1]].getBudget(), 2)
        self.budget_begin = round(User[CurrentUser[1]].getBudget(), 2)

        #page 1- profile page index 0============================================================================================================
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(800, 697)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.stackedWidget.setObjectName("stackedWidget")
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.profile)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 100, 181, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_37 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.label_37)
        self.restuarant_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.restuarant_label.setObjectName("restuarant_label")
        self.verticalLayout_2.addWidget(self.restuarant_label)
        self.budget_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.budget_label.setObjectName("budget_label")
        self.verticalLayout_2.addWidget(self.budget_label)
        self.rating_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.rating_label.setObjectName("rating_label")
        self.verticalLayout_2.addWidget(self.rating_label)
        self.salesperson_profile = QtWidgets.QLabel(self.profile)
        self.salesperson_profile.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.salesperson_profile.setObjectName("salesperson_profile")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.profile)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 100, 201, 491))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.name.setObjectName("name")
        self.verticalLayout_4.addWidget(self.name)
        self.restaurant = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.restaurant.setObjectName("restaurant")
        self.verticalLayout_4.addWidget(self.restaurant)
        self.budget = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.budget.setObjectName("budget")
        self.verticalLayout_4.addWidget(self.budget)
        self.rating = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.rating.setObjectName("rating")
        self.verticalLayout_4.addWidget(self.rating)
        self.deal_of_the_day = QtWidgets.QLabel(self.profile)
        self.deal_of_the_day.setGeometry(QtCore.QRect(540, 100, 131, 16))
        self.deal_of_the_day.setObjectName("deal_of_the_day")
        self.log_profile = QtWidgets.QPushButton(self.profile)
        self.log_profile.setGeometry(QtCore.QRect(230, 30, 113, 32))
        self.log_profile.setObjectName("log_profile")
        self.deal_of_the_day_list = QtWidgets.QListWidget(self.profile)
        self.deal_of_the_day_list.setGeometry(QtCore.QRect(490, 120, 221, 471))
        self.deal_of_the_day_list.setObjectName("deal_of_the_day_list")
        self.deal_of_the_day_list.setSpacing(15)
        self.deal_of_the_day_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shop_suppliers = QtWidgets.QPushButton(self.profile)
        self.shop_suppliers.setGeometry(QtCore.QRect(590, 30, 113, 32))
        self.shop_suppliers.setObjectName("shop_suppliers")
        self.stackedWidget.addWidget(self.profile)

        self.calculate_DOD()

        #page 2 - inventory required by cook - index 1============================================================================================================
        self.inventory_required = QtWidgets.QWidget()
        self.inventory_required.setObjectName("inventory_required")
        self.label_3 = QtWidgets.QLabel(self.inventory_required)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 171, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.inventory_required)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(60, 80, 661, 80))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.items_required_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.items_required_label_2.setObjectName("items_required_label_2")
        self.horizontalLayout_10.addWidget(self.items_required_label_2)
        self.items_required_label = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.items_required_label.setObjectName("items_required_label")
        self.horizontalLayout_10.addWidget(self.items_required_label)
        self.items_required = QtWidgets.QListWidget(self.inventory_required)
        self.items_required.setGeometry(QtCore.QRect(60, 160, 331, 471))
        self.items_required.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.items_required.setObjectName("items_required")
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.items_required.addItem(item)
        self.items_required.setSpacing(15) #changed spacing
        self.amounts_required = QtWidgets.QListWidget(self.inventory_required)
        self.amounts_required.setGeometry(QtCore.QRect(390, 160, 331, 471))
        self.amounts_required.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amounts_required.setObjectName("amounts_required")
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amounts_required.addItem(item)
        self.amounts_required.setSpacing(15) #changed spacing
        self.return_inventory = QtWidgets.QPushButton(self.inventory_required)
        self.return_inventory.setGeometry(QtCore.QRect(20, 10, 113, 32))
        self.return_inventory.setObjectName("return_inventory")
        self.choose_suppliers = QtWidgets.QPushButton(self.inventory_required)
        self.choose_suppliers.setGeometry(QtCore.QRect(590, 10, 131, 32))
        self.choose_suppliers.setObjectName("choose_suppliers")
        self.stackedWidget.addWidget(self.inventory_required)

        #page 3 - select between the 3 suppliers - index 2============================================================================================================
        self.select_supplier = QtWidgets.QWidget()
        self.select_supplier.setObjectName("select_supplier")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.select_supplier)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 221, 371))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.supplier_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.supplier_1.setObjectName("supplier_1")
        self.horizontalLayout_2.addWidget(self.supplier_1)
        self.shop_supplier_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)  #button to go to supplier 1
        self.shop_supplier_1.setObjectName("shop_supplier_1")
        self.horizontalLayout_2.addWidget(self.shop_supplier_1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.select_supplier)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(270, 110, 211, 371))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.supplier_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.supplier_4.setObjectName("supplier_4")
        self.horizontalLayout_3.addWidget(self.supplier_4)
        self.shop_supplier_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3) # button to go to supplier 2
        self.shop_supplier_2.setObjectName("shop_supplier_2")
        self.horizontalLayout_3.addWidget(self.shop_supplier_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.select_supplier)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(510, 110, 221, 371))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.supplier_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.supplier_5.setObjectName("supplier_5")
        self.horizontalLayout_4.addWidget(self.supplier_5)
        self.shop_supplier_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4) #button to go to supplier 3
        self.shop_supplier_3.setObjectName("shop_supplier_3")
        self.horizontalLayout_4.addWidget(self.shop_supplier_3)
        self.supplier_label = QtWidgets.QLabel(self.select_supplier)
        self.supplier_label.setGeometry(QtCore.QRect(350, 50, 60, 16))
        self.supplier_label.setObjectName("supplier_label")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.select_supplier)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(270, 510, 211, 80))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.log_suppliers = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.log_suppliers.setObjectName("log_suppliers")
        self.verticalLayout_7.addWidget(self.log_suppliers)
        self.stackedWidget.addWidget(self.select_supplier)


        #page 4 - supplier 1 - index 3 ============================================================================================================
        self.suppler_1 = QtWidgets.QWidget()
        self.suppler_1.setObjectName("suppler_1")
        self.supplier1_name = QtWidgets.QLabel(self.suppler_1)
        self.supplier1_name.setGeometry(QtCore.QRect(330, 20, 60, 16))
        self.supplier1_name.setObjectName("supplier1_name")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.suppler_1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 781, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.add_1.setObjectName("add_1")
        self.horizontalLayout.addWidget(self.add_1)
        self.amount_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.amount_1.setObjectName("amount_1")
        self.horizontalLayout.addWidget(self.amount_1)
        self.price_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.price_1.setObjectName("price_1")
        self.horizontalLayout.addWidget(self.price_1)
        self.quality_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.quality_1.setObjectName("quality_1")
        self.horizontalLayout.addWidget(self.quality_1)
        self.item_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.item_1.setObjectName("item_1")
        self.horizontalLayout.addWidget(self.item_1)
        self.item_list_1 = QtWidgets.QListWidget(self.suppler_1)
        self.item_list_1.setGeometry(QtCore.QRect(0, 80, 161, 541))
        self.item_list_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_list_1.setObjectName("item_list_1")
        self.item_list_1.setSpacing(15) # changed spacing
        self.quality_list_1 = QtWidgets.QListWidget(self.suppler_1)
        self.quality_list_1.setGeometry(QtCore.QRect(160, 80, 151, 541))
        self.quality_list_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quality_list_1.setObjectName("quality_list_1")
        self.quality_list_1.setSpacing(15) #changed spacing
        self.price_list_1 = QtWidgets.QListWidget(self.suppler_1)
        self.price_list_1.setGeometry(QtCore.QRect(310, 80, 161, 541))
        self.price_list_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_list_1.setObjectName("price_list_1")
        self.price_list_1.setSpacing(15)#changed spacing


        for i in range(len(SuppliesList1)):
            if SuppliesList1[i].isDealOfTheDay():
                self.item_list_1.addItem(self.add_DOD_item(SuppliesList1[i].getName()))
            else:
                self.item_list_1.addItem(SuppliesList1[i].getName())
            self.quality_list_1.addItem(SuppliesList1[i].getQuality())
            self.price_list_1.addItem(str(SuppliesList1[i].getPrice()))

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.suppler_1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(619, 80, 151, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add1_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_1.setObjectName("add1_1")
        self.verticalLayout_3.addWidget(self.add1_1)
        self.add1_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_2.setObjectName("add1_2")
        self.verticalLayout_3.addWidget(self.add1_2)
        self.add1_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_3.setObjectName("add1_3")
        self.verticalLayout_3.addWidget(self.add1_3)
        self.add1_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_4.setObjectName("add1_4")
        self.verticalLayout_3.addWidget(self.add1_4)
        self.add1_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_5.setObjectName("add1_5")
        self.verticalLayout_3.addWidget(self.add1_5)
        self.add1_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_6.setObjectName("add1_6")
        self.verticalLayout_3.addWidget(self.add1_6)
        self.add1_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_7.setObjectName("add1_7")
        self.verticalLayout_3.addWidget(self.add1_7)
        self.add1_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_8.setObjectName("add1_8")
        self.verticalLayout_3.addWidget(self.add1_8)
        self.add1_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_9.setObjectName("add1_9")
        self.verticalLayout_3.addWidget(self.add1_9)
        self.add1_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add1_10.setObjectName("add1_10")
        self.verticalLayout_3.addWidget(self.add1_10)
        self.return_supplier_1 = QtWidgets.QPushButton(self.suppler_1)
        self.return_supplier_1.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.return_supplier_1.setObjectName("return_supplier_1")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.suppler_1)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(120, 10, 191, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget_9) # budget remaining
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_9.addWidget(self.label_31)
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_9.addWidget(self.label_30)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.suppler_1)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(470, 80, 151, 491))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.amount1_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_1.setObjectName("amount1_1")
        self.verticalLayout_8.addWidget(self.amount1_1)
        self.amount1_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_2.setObjectName("amount1_2")
        self.verticalLayout_8.addWidget(self.amount1_2)
        self.amount1_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_3.setObjectName("amount1_3")
        self.verticalLayout_8.addWidget(self.amount1_3)
        self.amount1_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_4.setObjectName("amount1_4")
        self.verticalLayout_8.addWidget(self.amount1_4)
        self.amount1_5 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_5.setObjectName("amount1_5")
        self.verticalLayout_8.addWidget(self.amount1_5)
        self.amount1_6 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_6.setObjectName("amount1_6")
        self.verticalLayout_8.addWidget(self.amount1_6)
        self.amount1_7 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_7.setObjectName("amount1_7")
        self.verticalLayout_8.addWidget(self.amount1_7)
        self.amount1_8 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_8.setObjectName("amount1_8")
        self.verticalLayout_8.addWidget(self.amount1_8)
        self.amount1_9 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_9.setObjectName("amount1_9")
        self.verticalLayout_8.addWidget(self.amount1_9)
        self.amount1_10 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.amount1_10.setObjectName("amount1_10")
        self.verticalLayout_8.addWidget(self.amount1_10)
        self.go_cart_1 = QtWidgets.QPushButton(self.suppler_1)
        self.go_cart_1.setGeometry(QtCore.QRect(620, 10, 113, 32))
        self.go_cart_1.setObjectName("go_cart_1")
        self.check_list_1 = QtWidgets.QPushButton(self.suppler_1) #button to go to check list and then return after
        self.check_list_1.setGeometry(QtCore.QRect(470, 10, 113, 32))
        self.check_list_1.setObjectName("check_list_1")
        self.stackedWidget.addWidget(self.suppler_1)

        #page 5 - supplier 2 - index 4============================================================================================================
        self.supplier_2 = QtWidgets.QWidget()
        self.supplier_2.setObjectName("supplier_2")
        self.supplier2_name = QtWidgets.QLabel(self.supplier_2)
        self.supplier2_name.setGeometry(QtCore.QRect(330, 20, 60, 16))
        self.supplier2_name.setObjectName("supplier2_name")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.supplier_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 50, 781, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.add_2.setObjectName("add_2")
        self.horizontalLayout_5.addWidget(self.add_2)
        self.amount_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.amount_2.setObjectName("amount_2")
        self.horizontalLayout_5.addWidget(self.amount_2)
        self.price_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.price_2.setObjectName("price_2")
        self.horizontalLayout_5.addWidget(self.price_2)
        self.quality_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.quality_2.setObjectName("quality_2")
        self.horizontalLayout_5.addWidget(self.quality_2)
        self.item_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.item_2.setObjectName("item_2")
        self.horizontalLayout_5.addWidget(self.item_2)
        self.item_list_2 = QtWidgets.QListWidget(self.supplier_2)
        self.item_list_2.setGeometry(QtCore.QRect(0, 80, 161, 541))
        self.item_list_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_list_2.setObjectName("item_list_2")
        self.item_list_2.setSpacing(15)#changed spacing
        self.quality_list_2 = QtWidgets.QListWidget(self.supplier_2)
        self.quality_list_2.setGeometry(QtCore.QRect(160, 80, 151, 541))
        self.quality_list_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quality_list_2.setObjectName("quality_list_2")
        self.quality_list_2.setSpacing(15)#changed spacing
        self.price_list_2 = QtWidgets.QListWidget(self.supplier_2)
        self.price_list_2.setGeometry(QtCore.QRect(310, 80, 161, 541))
        self.price_list_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_list_2.setObjectName("price_list_2")
        self.price_list_2.setSpacing(15)#changed spacing

        for i in range(len(SuppliesList2)):
            if SuppliesList2[i].isDealOfTheDay():
                self.item_list_2.addItem(self.add_DOD_item(SuppliesList2[i].getName()))
            else:
                self.item_list_2.addItem(SuppliesList2[i].getName())
            self.quality_list_2.addItem(SuppliesList2[i].getQuality())
            self.price_list_2.addItem(str(SuppliesList2[i].getPrice()))

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.supplier_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(620, 80, 151, 501))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add2_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_1.setObjectName("add2_1")
        self.verticalLayout_5.addWidget(self.add2_1)
        self.add2_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_2.setObjectName("add2_2")
        self.verticalLayout_5.addWidget(self.add2_2)
        self.add2_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_3.setObjectName("add2_3")
        self.verticalLayout_5.addWidget(self.add2_3)
        self.add2_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_4.setObjectName("add2_4")
        self.verticalLayout_5.addWidget(self.add2_4)
        self.add2_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_5.setObjectName("add2_5")
        self.verticalLayout_5.addWidget(self.add2_5)
        self.add2_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_6.setObjectName("add2_6")
        self.verticalLayout_5.addWidget(self.add2_6)
        self.add2_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_7.setObjectName("add2_7")
        self.verticalLayout_5.addWidget(self.add2_7)
        self.add2_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_8.setObjectName("add2_8")
        self.verticalLayout_5.addWidget(self.add2_8)
        self.add2_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_9.setObjectName("add2_9")
        self.verticalLayout_5.addWidget(self.add2_9)
        self.add2_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add2_10.setObjectName("add2_10")
        self.verticalLayout_5.addWidget(self.add2_10)
        self.return_supplier_2 = QtWidgets.QPushButton(self.supplier_2)
        self.return_supplier_2.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.return_supplier_2.setObjectName("return_supplier_2")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.supplier_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(120, 10, 185, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_33 = QtWidgets.QLabel(self.horizontalLayoutWidget_8) # budget remaining - label 33
        self.label_33.setObjectName("label_33")
        
        self.label_33.setText(str(self.budget_remaining))
        
        self.horizontalLayout_8.addWidget(self.label_33)
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_8.addWidget(self.label_32)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.supplier_2)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(470, 80, 151, 491))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.amount2_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_1.setObjectName("amount2_1")
        self.verticalLayout_9.addWidget(self.amount2_1)
        self.amount2_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_2.setObjectName("amount2_2")
        self.verticalLayout_9.addWidget(self.amount2_2)
        self.amount2_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_3.setObjectName("amount2_3")
        self.verticalLayout_9.addWidget(self.amount2_3)
        self.amount2_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_4.setObjectName("amount2_4")
        self.verticalLayout_9.addWidget(self.amount2_4)
        self.amount2_5 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_5.setObjectName("amount2_5")
        self.verticalLayout_9.addWidget(self.amount2_5)
        self.amount2_6 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_6.setObjectName("amount2_6")
        self.verticalLayout_9.addWidget(self.amount2_6)
        self.amount2_7 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_7.setObjectName("amount2_7")
        self.verticalLayout_9.addWidget(self.amount2_7)
        self.amount2_8 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_8.setObjectName("amount2_8")
        self.verticalLayout_9.addWidget(self.amount2_8)
        self.amount2_9 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_9.setObjectName("amount2_9")
        self.verticalLayout_9.addWidget(self.amount2_9)
        self.amount2_10 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.amount2_10.setObjectName("amount2_10")
        self.verticalLayout_9.addWidget(self.amount2_10)
        self.go_cart_2 = QtWidgets.QPushButton(self.supplier_2)
        self.go_cart_2.setGeometry(QtCore.QRect(620, 10, 113, 32))
        self.go_cart_2.setObjectName("go_cart_2")
        self.check_list_2 = QtWidgets.QPushButton(self.supplier_2)
        self.check_list_2.setGeometry(QtCore.QRect(470, 10, 113, 32))
        self.check_list_2.setObjectName("check_list_2")
        self.stackedWidget.addWidget(self.supplier_2)

        #page 6 - supplier 3 - index 5============================================================================================================
        self.supplier_3 = QtWidgets.QWidget()
        self.supplier_3.setObjectName("supplier_3")
        self.supplier3_name = QtWidgets.QLabel(self.supplier_3)
        self.supplier3_name.setGeometry(QtCore.QRect(330, 20, 71, 16))
        self.supplier3_name.setObjectName("supplier3_name")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.supplier_3)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 50, 781, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.add_3.setObjectName("add_3")
        self.horizontalLayout_6.addWidget(self.add_3)
        self.amount_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.amount_3.setObjectName("amount_3")
        self.horizontalLayout_6.addWidget(self.amount_3)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_6.addWidget(self.label_28)
        self.quality_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.quality_3.setObjectName("quality_3")
        self.horizontalLayout_6.addWidget(self.quality_3)
        self.item_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.item_3.setObjectName("item_3")
        self.horizontalLayout_6.addWidget(self.item_3)
        self.item_list_3 = QtWidgets.QListWidget(self.supplier_3)
        self.item_list_3.setGeometry(QtCore.QRect(0, 80, 161, 541))
        self.item_list_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_list_3.setObjectName("item_list_3")
        self.item_list_3.setSpacing(15)#changed spacing
        self.quality_list_3 = QtWidgets.QListWidget(self.supplier_3)
        self.quality_list_3.setGeometry(QtCore.QRect(160, 80, 151, 541))
        self.quality_list_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quality_list_3.setObjectName("quality_list_3")
        self.quality_list_3.setSpacing(15)#changed spacing
        self.price_list_3 = QtWidgets.QListWidget(self.supplier_3)
        self.price_list_3.setGeometry(QtCore.QRect(310, 80, 161, 541))
        self.price_list_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_list_3.setObjectName("price_list_3")
        self.price_list_3.setSpacing(15)#changed spacing

        for i in range(len(SuppliesList3)):
            if SuppliesList3[i].isDealOfTheDay():
                self.item_list_3.addItem(self.add_DOD_item(SuppliesList3[i].getName()))
            else:
                self.item_list_3.addItem(SuppliesList3[i].getName())
            self.quality_list_3.addItem(SuppliesList3[i].getQuality())
            self.price_list_3.addItem(str(SuppliesList3[i].getPrice()))

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.supplier_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(619, 80, 151, 501))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.add3_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_1.setObjectName("add3_1")
        self.verticalLayout_6.addWidget(self.add3_1)
        self.add3_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_2.setObjectName("add3_2")
        self.verticalLayout_6.addWidget(self.add3_2)
        self.add3_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_3.setObjectName("add3_3")
        self.verticalLayout_6.addWidget(self.add3_3)
        self.add3_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_4.setObjectName("add3_4")
        self.verticalLayout_6.addWidget(self.add3_4)
        self.add3_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_5.setObjectName("add3_5")
        self.verticalLayout_6.addWidget(self.add3_5)
        self.add3_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_6.setObjectName("add3_6")
        self.verticalLayout_6.addWidget(self.add3_6)
        self.add3_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_7.setObjectName("add3_7")
        self.verticalLayout_6.addWidget(self.add3_7)
        self.add3_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_8.setObjectName("add3_8")
        self.verticalLayout_6.addWidget(self.add3_8)
        self.add3_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_9.setObjectName("add3_9")
        self.verticalLayout_6.addWidget(self.add3_9)
        self.add3_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add3_10.setObjectName("add3_10")
        self.verticalLayout_6.addWidget(self.add3_10)
        self.return_supplier_3 = QtWidgets.QPushButton(self.supplier_3)
        self.return_supplier_3.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.return_supplier_3.setObjectName("return_supplier_3")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.supplier_3)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(120, 10, 201, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_35 = QtWidgets.QLabel(self.horizontalLayoutWidget_7) #budget remaining - label 35
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_7.addWidget(self.label_35)
        self.label_34 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_7.addWidget(self.label_34)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.supplier_3)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(470, 80, 151, 491))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.amount3_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_1.setObjectName("amount3_1")
        self.verticalLayout_10.addWidget(self.amount3_1)
        self.amount3_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_2.setObjectName("amount3_2")
        self.verticalLayout_10.addWidget(self.amount3_2)
        self.amount3_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_3.setObjectName("amount3_3")
        self.verticalLayout_10.addWidget(self.amount3_3)
        self.amount3_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_4.setObjectName("amount3_4")
        self.verticalLayout_10.addWidget(self.amount3_4)
        self.amount3_5 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_5.setObjectName("amount3_5")
        self.verticalLayout_10.addWidget(self.amount3_5)
        self.amount3_6 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_6.setObjectName("amount3_6")
        self.verticalLayout_10.addWidget(self.amount3_6)
        self.amount3_7 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_7.setObjectName("amount3_7")
        self.verticalLayout_10.addWidget(self.amount3_7)
        self.amount3_8 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_8.setObjectName("amount3_8")
        self.verticalLayout_10.addWidget(self.amount3_8)
        self.amount3_9 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_9.setObjectName("amount3_9")
        self.verticalLayout_10.addWidget(self.amount3_9)
        self.amount3_10 = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.amount3_10.setObjectName("amount3_10")
        self.verticalLayout_10.addWidget(self.amount3_10)
        self.go_cart_3 = QtWidgets.QPushButton(self.supplier_3)
        self.go_cart_3.setGeometry(QtCore.QRect(620, 10, 113, 32))
        self.go_cart_3.setObjectName("go_cart_3")
        self.check_list_3 = QtWidgets.QPushButton(self.supplier_3)
        self.check_list_3.setGeometry(QtCore.QRect(470, 10, 113, 32))
        self.check_list_3.setObjectName("check_list_3")
        self.stackedWidget.addWidget(self.supplier_3)

        #page 7 - check out page - index 6============================================================================================================
        self.check_out = QtWidgets.QWidget()
        self.check_out.setObjectName("check_out")
        self.label_8 = QtWidgets.QLabel(self.check_out)
        self.label_8.setGeometry(QtCore.QRect(340, 40, 71, 16))
        self.label_8.setObjectName("label_8")
        self.check_out_list = QtWidgets.QListWidget(self.check_out) #the checkout list / cart list widget
        self.check_out_list.setGeometry(QtCore.QRect(100, 70, 261, 511))
        self.check_out_list.setObjectName("check_out_list")
        self.return_check_out = QtWidgets.QPushButton(self.check_out)
        self.return_check_out.setGeometry(QtCore.QRect(10, 20, 113, 32))
        self.return_check_out.setObjectName("return_check_out")
        self.log_check_out = QtWidgets.QPushButton(self.check_out)
        self.log_check_out.setGeometry(QtCore.QRect(610, 20, 113, 32))
        self.log_check_out.setObjectName("log_check_out")
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.check_out)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(420, 70, 160, 80))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.total_amount = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.total_amount.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.total_amount.setObjectName("total_amount")
        self.horizontalLayout_12.addWidget(self.total_amount)
        self.total_amount_label = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.total_amount_label.setObjectName("total_amount_label")
        self.horizontalLayout_12.addWidget(self.total_amount_label)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.check_out)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(420, 160, 160, 80))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.check_out_budget_label = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.check_out_budget_label.setObjectName("check_out_budget_label")
        self.verticalLayout_12.addWidget(self.check_out_budget_label)
        self.check_out_budget = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.check_out_budget.setObjectName("check_out_budget")
        self.verticalLayout_12.addWidget(self.check_out_budget)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.check_out)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(420, 250, 160, 171))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.check_out_check_list = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.check_out_check_list.setObjectName("check_out_check_list")
        self.verticalLayout_13.addWidget(self.check_out_check_list)
        self.check_out_supplier = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.check_out_supplier.setObjectName("check_out_supplier")
        self.verticalLayout_13.addWidget(self.check_out_supplier)
        self.check_out_remove = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.check_out_remove.setObjectName("check_out_remove")
        self.verticalLayout_13.addWidget(self.check_out_remove)
        self.confirm_order = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.confirm_order.setObjectName("confirm_order")
        self.verticalLayout_13.addWidget(self.confirm_order)
        self.stackedWidget.addWidget(self.check_out)

        #page 8 - check list - index 7 ============================================================================================================
        self.check_list = QtWidgets.QWidget()
        self.check_list.setObjectName("check_list")
        self.return_check_list = QtWidgets.QPushButton(self.check_list)
        self.return_check_list.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.return_check_list.setObjectName("return_check_list")
        self.label = QtWidgets.QLabel(self.check_list)
        self.label.setGeometry(QtCore.QRect(250, 40, 271, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.check_list)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(70, 70, 611, 80))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.amount_check_list_label = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.amount_check_list_label.setObjectName("amount_check_list_label")
        self.horizontalLayout_11.addWidget(self.amount_check_list_label)
        self.item_check_list_label = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.item_check_list_label.setObjectName("item_check_list_label")
        self.horizontalLayout_11.addWidget(self.item_check_list_label)
        self.item_check_list = QtWidgets.QListWidget(self.check_list)
        self.item_check_list.setGeometry(QtCore.QRect(70, 150, 301, 471))
        self.item_check_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_check_list.setObjectName("item_check_list")
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_check_list.addItem(item)
        self.item_check_list.setSpacing(10)
        self.amount_check_list = QtWidgets.QListWidget(self.check_list)
        self.amount_check_list.setGeometry(QtCore.QRect(370, 150, 311, 471))
        self.amount_check_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amount_check_list.setObjectName("amount_check_list")
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amount_check_list.addItem(item)
        self.amount_check_list.setSpacing(10)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.check_list)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 140, 61, 401))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.mark1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark1.setObjectName("mark1")
        self.verticalLayout_11.addWidget(self.mark1)
        self.mark2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark2.setObjectName("mark2")
        self.verticalLayout_11.addWidget(self.mark2)
        self.mark3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark3.setObjectName("mark3")
        self.verticalLayout_11.addWidget(self.mark3)
        self.mark4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark4.setObjectName("mark4")
        self.verticalLayout_11.addWidget(self.mark4)
        self.mark5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark5.setObjectName("mark5")
        self.verticalLayout_11.addWidget(self.mark5)
        self.mark6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark6.setObjectName("mark6")
        self.verticalLayout_11.addWidget(self.mark6)
        self.mark7 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark7.setObjectName("mark7")
        self.verticalLayout_11.addWidget(self.mark7)
        self.mark8 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark8.setObjectName("mark8")
        self.verticalLayout_11.addWidget(self.mark8)
        self.mark9 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark9.setObjectName("mark9")
        self.verticalLayout_11.addWidget(self.mark9)
        self.mark10 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.mark10.setObjectName("mark10")
        self.verticalLayout_11.addWidget(self.mark10)
        self.stackedWidget.addWidget(self.check_list)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        CurrentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CurrentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        CurrentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CurrentWindow)
        self.statusbar.setObjectName("statusbar")
        CurrentWindow.setStatusBar(self.statusbar)

        #sets profile page to be the first page
        self.retranslateUi(CurrentWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

        #connect each button to the functions==============================================

        #page 1 index 0 (profile page)
        self.log_profile.clicked.connect(self.logout)
        self.shop_suppliers.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        #page 2 index 1 (inventory required by cook)
        self.return_inventory.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.choose_suppliers.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        #page 3 index 2 (choose suppliers)
        self.shop_supplier_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.shop_supplier_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.shop_supplier_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.log_suppliers.clicked.connect(self.logout)

        #page 4 index 3 (supplier 1)
        self.return_supplier_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go_cart_1.clicked.connect(self.go_to_cart)
        self.check_list_1.clicked.connect(self.go_to_check_list)

        #page 5 index 4 (supplier 2)
        self.return_supplier_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go_cart_2.clicked.connect(self.go_to_cart)
        self.check_list_2.clicked.connect(self.go_to_check_list)

        #page 6 index 5 (supplier 3)
        self.return_supplier_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go_cart_3.clicked.connect(self.go_to_cart)
        self.check_list_3.clicked.connect(self.go_to_check_list)

        #page 7 index 6 ( check out page )
        self.return_check_out.clicked.connect(self.return_previous_cart)
        self.log_check_out.clicked.connect(self.logout)
        self.check_out_check_list.clicked.connect(self.go_to_check_list)
        self.check_out_supplier.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.check_out_remove.clicked.connect(self.remove)
        self.confirm_order.clicked.connect(self.confirmOrder)

        #page 8 index 7 (check list for inventory)
        self.return_check_list.clicked.connect(self.return_previous)

        #connect all the add to cart buttons
        ##########################################################################################################
        #supplier 1 add to cart buttons
        self.add1_1.clicked.connect(self.addButton1_1)
        self.add1_2.clicked.connect(self.addButton1_2)
        self.add1_3.clicked.connect(self.addButton1_3)
        self.add1_4.clicked.connect(self.addButton1_4)
        self.add1_5.clicked.connect(self.addButton1_5)
        self.add1_6.clicked.connect(self.addButton1_6)
        self.add1_7.clicked.connect(self.addButton1_7)
        self.add1_8.clicked.connect(self.addButton1_8)
        self.add1_9.clicked.connect(self.addButton1_9)
        self.add1_10.clicked.connect(self.addButton1_10)

        #supplier 2 add to cart buttons
        self.add2_1.clicked.connect(self.addButton2_1)
        self.add2_2.clicked.connect(self.addButton2_2)
        self.add2_3.clicked.connect(self.addButton2_3)
        self.add2_4.clicked.connect(self.addButton2_4)
        self.add2_5.clicked.connect(self.addButton2_5)
        self.add2_6.clicked.connect(self.addButton2_6)
        self.add2_7.clicked.connect(self.addButton2_7)
        self.add2_8.clicked.connect(self.addButton2_8)
        self.add2_9.clicked.connect(self.addButton2_9)
        self.add2_10.clicked.connect(self.addButton2_10)

        #supplier 3 add to cart buttons
        self.add3_1.clicked.connect(self.addButton3_1)
        self.add3_2.clicked.connect(self.addButton3_2)
        self.add3_3.clicked.connect(self.addButton3_3)
        self.add3_4.clicked.connect(self.addButton3_4)
        self.add3_5.clicked.connect(self.addButton3_5)
        self.add3_6.clicked.connect(self.addButton3_6)
        self.add3_7.clicked.connect(self.addButton3_7)
        self.add3_8.clicked.connect(self.addButton3_8)
        self.add3_9.clicked.connect(self.addButton3_9)
        self.add3_10.clicked.connect(self.addButton3_10)
        

        #grab salesperson information and display on the profile page
        self.name.setText(str(User[CurrentUser[1]].getFirst()))
        self.restaurant.setText(str(User[CurrentUser[1]].getRestaurant()))
        self.budget.setText(str(User[CurrentUser[1]].getBudget()))
        self.rating.setText(str(User[CurrentUser[1]].getRating()))

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "CurrentWindow"))
        self.label_37.setText(_translate("CurrentWindow", "Name:"))
        self.restuarant_label.setText(_translate("CurrentWindow", "Restuarant:"))
        self.budget_label.setText(_translate("CurrentWindow", "Budget:"))
        self.rating_label.setText(_translate("CurrentWindow", "Rating:"))
        self.salesperson_profile.setText(_translate("CurrentWindow", "Salesperson Profile"))
        self.name.setText(_translate("CurrentWindow", "name example"))
        self.restaurant.setText(_translate("CurrentWindow", "Restuarant example"))
        self.budget.setText(_translate("CurrentWindow", "$1000.00"))
        self.rating.setText(_translate("CurrentWindow", "4"))
        self.deal_of_the_day.setText(_translate("CurrentWindow", "DEALS OF THE DAY"))
        self.log_profile.setText(_translate("CurrentWindow", "Log Out"))
        self.shop_suppliers.setText(_translate("CurrentWindow", "Shop"))
        self.label_3.setText(_translate("CurrentWindow", "Inventory Required by Cook"))
        self.items_required_label_2.setText(_translate("CurrentWindow", "Amount by lb"))
        self.items_required_label.setText(_translate("CurrentWindow", "Item"))
        __sortingEnabled = self.items_required.isSortingEnabled()
        self.items_required.setSortingEnabled(False)
        item = self.items_required.item(0)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(1)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(2)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(3)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(4)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(5)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(6)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(7)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(8)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.items_required.item(9)
        item.setText(_translate("CurrentWindow", "New Item"))
        self.items_required.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.amounts_required.isSortingEnabled()
        self.amounts_required.setSortingEnabled(False)
        item = self.amounts_required.item(0)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(1)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(2)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(3)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(4)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(5)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(6)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(7)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(8)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amounts_required.item(9)
        item.setText(_translate("CurrentWindow", "New Item"))
        self.amounts_required.setSortingEnabled(__sortingEnabled)
        self.return_inventory.setText(_translate("CurrentWindow", "Return"))
        self.choose_suppliers.setText(_translate("CurrentWindow", "Choose Suppliers"))
        self.supplier_1.setText(_translate("CurrentWindow", "Supplier 1"))
        self.shop_supplier_1.setText(_translate("CurrentWindow", "Shop Here"))
        self.supplier_4.setText(_translate("CurrentWindow", "Supplier 2"))
        self.shop_supplier_2.setText(_translate("CurrentWindow", "Shop Here"))
        self.supplier_5.setText(_translate("CurrentWindow", "Supplier 3"))
        self.shop_supplier_3.setText(_translate("CurrentWindow", "Shop Here"))
        self.supplier_label.setText(_translate("CurrentWindow", "Suppliers"))
        self.log_suppliers.setText(_translate("CurrentWindow", "Log Out"))
        self.supplier1_name.setText(_translate("CurrentWindow", "Supplier 1"))
        self.add_1.setText(_translate("CurrentWindow", "Add"))
        self.amount_1.setText(_translate("CurrentWindow", "Quantity"))
        self.price_1.setText(_translate("CurrentWindow", "Price"))
        self.quality_1.setText(_translate("CurrentWindow", "Quality"))
        self.item_1.setText(_translate("CurrentWindow", "Item"))
        __sortingEnabled = self.item_list_1.isSortingEnabled()
        self.item_list_1.setSortingEnabled(False)

        self.item_list_1.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.quality_list_1.isSortingEnabled()
        self.quality_list_1.setSortingEnabled(False)

        self.quality_list_1.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.price_list_1.isSortingEnabled()

        self.price_list_1.setSortingEnabled(__sortingEnabled)
        self.add1_1.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_2.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_3.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_4.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_5.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_6.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_7.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_8.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_9.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add1_10.setText(_translate("CurrentWindow", "Add to Cart"))
        self.return_supplier_1.setText(_translate("CurrentWindow", "Return"))
        self.label_31.setText(_translate("CurrentWindow", "$1000")) #here
        self.label_30.setText(_translate("CurrentWindow", "Budget Remaining:"))
        self.go_cart_1.setText(_translate("CurrentWindow", "Go to Cart"))
        self.check_list_1.setText(_translate("CurrentWindow", "Check List"))
        self.supplier2_name.setText(_translate("CurrentWindow", "Supplier 2"))
        self.add_2.setText(_translate("CurrentWindow", "Add"))
        self.amount_2.setText(_translate("CurrentWindow", "Quantity"))
        self.price_2.setText(_translate("CurrentWindow", "Price"))
        self.quality_2.setText(_translate("CurrentWindow", "Quality"))
        self.item_2.setText(_translate("CurrentWindow", "Item"))
        __sortingEnabled = self.item_list_2.isSortingEnabled()
        self.item_list_2.setSortingEnabled(False)

        self.item_list_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.quality_list_2.isSortingEnabled()
        self.quality_list_2.setSortingEnabled(False)

        self.quality_list_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.price_list_2.isSortingEnabled()
        self.price_list_2.setSortingEnabled(False)

        self.price_list_2.setSortingEnabled(__sortingEnabled)
        self.add2_1.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_2.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_3.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_4.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_5.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_6.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_7.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_8.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_9.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add2_10.setText(_translate("CurrentWindow", "Add to Cart"))
        self.return_supplier_2.setText(_translate("CurrentWindow", "Return"))
        self.label_33.setText(_translate("CurrentWindow", "$1000"))
        self.label_32.setText(_translate("CurrentWindow", "Budget Remaining:"))
        self.go_cart_2.setText(_translate("CurrentWindow", "Go to Cart"))
        self.check_list_2.setText(_translate("CurrentWindow", "Check List"))
        self.supplier3_name.setText(_translate("CurrentWindow", "Supplier 3"))
        self.add_3.setText(_translate("CurrentWindow", "Add"))
        self.amount_3.setText(_translate("CurrentWindow", "Quantity"))
        self.label_28.setText(_translate("CurrentWindow", "Price"))
        self.quality_3.setText(_translate("CurrentWindow", "Quality"))
        self.item_3.setText(_translate("CurrentWindow", "Item"))
        __sortingEnabled = self.item_list_3.isSortingEnabled()
        self.item_list_3.setSortingEnabled(False)

        self.item_list_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.quality_list_3.isSortingEnabled()
        self.quality_list_3.setSortingEnabled(False)

        self.quality_list_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.price_list_3.isSortingEnabled()
        self.price_list_3.setSortingEnabled(False)

        self.price_list_3.setSortingEnabled(__sortingEnabled)
        self.add3_1.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_2.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_3.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_4.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_5.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_6.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_7.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_8.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_9.setText(_translate("CurrentWindow", "Add to Cart"))
        self.add3_10.setText(_translate("CurrentWindow", "Add to Cart"))
        self.return_supplier_3.setText(_translate("CurrentWindow", "Return"))
        self.label_35.setText(_translate("CurrentWindow", "$1000"))
        self.label_34.setText(_translate("CurrentWindow", "Budget Remaining:"))
        self.go_cart_3.setText(_translate("CurrentWindow", "Go to Cart"))
        self.check_list_3.setText(_translate("CurrentWindow", "Check List"))
        self.label_8.setText(_translate("CurrentWindow", "Check Out"))
        self.return_check_out.setText(_translate("CurrentWindow", "Return"))
        self.log_check_out.setText(_translate("CurrentWindow", "Log Out"))
        self.total_amount.setText(_translate("CurrentWindow", "$0.00"))
        self.total_amount_label.setText(_translate("CurrentWindow", "Total:"))
        self.check_out_budget_label.setText(_translate("CurrentWindow", "Budget Remaining:"))
        self.check_out_budget.setText(_translate("CurrentWindow", "$1000"))
        self.check_out_check_list.setText(_translate("CurrentWindow", "Check List"))
        self.check_out_supplier.setText(_translate("CurrentWindow", "Choose Supplier"))
        self.check_out_remove.setText(_translate("CurrentWindow", "Remove"))
        self.confirm_order.setText(_translate("CurrentWindow", "Confirm Order"))
        self.return_check_list.setText(_translate("CurrentWindow", "Return"))
        self.label.setText(_translate("CurrentWindow", "Inventory Required by Cook - Check List"))
        self.amount_check_list_label.setText(_translate("CurrentWindow", "Quantity"))
        self.item_check_list_label.setText(_translate("CurrentWindow", "Item"))
        __sortingEnabled = self.item_check_list.isSortingEnabled()
        self.item_check_list.setSortingEnabled(False)
        item = self.item_check_list.item(0)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(1)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(2)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(3)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(4)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(5)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(6)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(7)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(8)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.item_check_list.item(9)
        item.setText(_translate("CurrentWindow", "New Item"))
        self.item_check_list.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.amount_check_list.isSortingEnabled()
        self.amount_check_list.setSortingEnabled(False)
        item = self.amount_check_list.item(0)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(1)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(2)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(3)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(4)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(5)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(6)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(7)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(8)
        item.setText(_translate("CurrentWindow", "New Item"))
        item = self.amount_check_list.item(9)
        item.setText(_translate("CurrentWindow", "New Item"))
        self.amount_check_list.setSortingEnabled(__sortingEnabled)
        self.mark1.setText(_translate("CurrentWindow", "Mark"))
        self.mark2.setText(_translate("CurrentWindow", "Mark"))
        self.mark3.setText(_translate("CurrentWindow", "Mark"))
        self.mark4.setText(_translate("CurrentWindow", "Mark"))
        self.mark5.setText(_translate("CurrentWindow", "Mark"))
        self.mark6.setText(_translate("CurrentWindow", "Mark"))
        self.mark7.setText(_translate("CurrentWindow", "Mark"))
        self.mark8.setText(_translate("CurrentWindow", "Mark"))
        self.mark9.setText(_translate("CurrentWindow", "Mark"))
        self.mark10.setText(_translate("CurrentWindow", "Mark"))



    #define the button functions to navigate through the pages
    #################################################################################

    #define logout function to be connected to each button
    def logout(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Are you sure you want to logout?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.logout_confirm)
        x = msg.exec_()

    def logout_confirm(self, i):
        if (i.text() == "&Yes"):
            CurrentCart_SalesPerson.clear()
            self.check_out_list.clear()
            CurrentUser.clear()
            self.CurrentWindow.hide()
            self.LoginWindow.show()

    def send_supplies(self):
        for i in range(len(CurrentCart_SalesPerson)):
            addCookSupplies(CurrentCart_SalesPerson[i])

    def confirmOrder(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirm Order")
        msg.setText("Are you sure you want to confirm order")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, i): # need to clear listwidget, list, total and keep budget
        if (i.text() == "&Yes"):
            self.budget_begin=self.budget_remaining #changes the budget to what has been already used
            self.send_supplies() #sends supplies over to cook

            #clear everything
            CurrentCart_SalesPerson.clear()
            self.check_out_list.clear()

            #update the new total and display -> should be 0 total now with budget remaining from what was purchased
            self.update_total()
            self.budget_connected_total()

            #changes the budget of the salesperson to what he has now after ordering
            User[CurrentUser[1]].setBudget(self.budget_begin)

            msg = QMessageBox()
            msg.setWindowTitle("Order Confirmed.")
            msg.setText("Order Confirmed! Supplies sent to Cook.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()


    def remove(self):
        listItems = self.check_out_list.selectedItems()
        if not listItems: return
        for item in listItems:
            self.check_out_list.takeItem(self.check_out_list.row(item))
            CurrentCart_SalesPerson.pop(self.check_out_list.currentRow()+1)
        self.update_total()
        self.budget_connected_total()

    global current_index
    current_index=0

    def set_current(self):
        global current_index
        current_index=self.stackedWidget.currentIndex()

    global current_index1
    current_index1=0

    def set_current_for_cart(self):
        global current_index1
        current_index1 = self.stackedWidget.currentIndex()

    #method to go to check list while keeping the previous index so we can return to it
    def go_to_check_list(self):
        self.set_current()
        self.stackedWidget.setCurrentIndex(7)

    #method to go to cart while keeping previous supplier index
    def go_to_cart(self):
        self.set_current_for_cart()
        self.stackedWidget.setCurrentIndex(6)

    #return to previous from checklist
    def return_previous(self):
        self.stackedWidget.setCurrentIndex(current_index)

    #return to previous from cart - different from checklist because they can return to different indexes
    def return_previous_cart(self):
        self.stackedWidget.setCurrentIndex(current_index1)

    # check if budget if added item is going over budget
    def check_budget(self,price_of):
        if price_of > self.budget_remaining:
            return False
        else:
            return True

    #function used to update the budget remaining
    def update_budget(self):
        self.budget_remaining=self.budget_begin-self.total

    def update_budget_remaining(self):
        self.label_31.setText(str(round(self.budget_remaining, 2)))
        self.label_33.setText(str(round(self.budget_remaining, 2)))
        self.label_35.setText(str(round(self.budget_remaining, 2)))
        self.check_out_budget.setText(str(round(self.budget_remaining, 2)))

    def budget_connected_total(self):
        self.update_budget()
        self.update_budget_remaining()
        self.total_amount.setText(str(round(self.total, 2)))

    def budget_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Budget Exceeded.")
        msg.setText("This order exceeds the budget.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()

    def update_total(self):
        temp = 0;
        for i in range(len(CurrentCart_SalesPerson)):
            temp += (CurrentCart_SalesPerson[i].getPrice()*int(CurrentCart_SalesPerson[i].getQuantity()))

        self.total = round(temp, 2)

    ### Define the add buttons here
    ########################################################################################################
    # For Supplier 1
    def addButton1_1(self):
        if self.check_budget(SuppliesList1[0].getPrice()*int(self.amount1_1.value())):
            if SuppliesList1[0].isDealOfTheDay():
                temp = self.add_DOD_item(SuppliesList1[0].getName())
            else:
                temp = SuppliesList1[0].getName()
            self.check_out_list.addItem(temp + '\t' + SuppliesList1[0].getQuality() + \
                                    '\t' + self.amount1_1.text() + '\t' + str(round(SuppliesList1[0].getPrice()*int(self.amount1_1.value()), 2)))
            SuppliesList1[0].setQuantity(int(self.amount1_1.value()))
            addCurrentCart_SalesPerson(SuppliesList1[0])
            self.update_total()
            self.budget_connected_total()
        else:
            #pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")



    def addButton1_2(self):
        if self.check_budget(SuppliesList1[1].getPrice()*int(self.amount1_2.value())):
            self.check_out_list.addItem(SuppliesList1[1].getName() + '\t' + SuppliesList1[1].getQuality() + \
                                    '\t' + self.amount1_2.text() + '\t' + str(round(SuppliesList1[1].getPrice()*int(self.amount1_2.value()), 2)))
            SuppliesList1[1].setQuantity(int(self.amount1_2.value()))
            addCurrentCart_SalesPerson(SuppliesList1[1])
            self.update_total()
            self.budget_connected_total()
        else:
            #pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_3(self):
        if self.check_budget(SuppliesList1[2].getPrice() * int(self.amount1_3.value())):
            self.check_out_list.addItem(SuppliesList1[2].getName() + '\t' + SuppliesList1[2].getQuality() + \
                                    '\t' + self.amount1_3.text() + '\t' + str(round(SuppliesList1[2].getPrice() * int(self.amount1_3.value()), 2)))
            SuppliesList1[2].setQuantity(int(self.amount1_3.value()))
            addCurrentCart_SalesPerson(SuppliesList1[2])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")


    def addButton1_4(self):
        if self.check_budget(SuppliesList1[3].getPrice() * int(self.amount1_4.value())):
            self.check_out_list.addItem(SuppliesList1[3].getName() + '\t' + SuppliesList1[3].getQuality() + \
                                    '\t' + self.amount1_4.text() + '\t' + str(round(SuppliesList1[3].getPrice() * int(self.amount1_4.value()), 2)))
            SuppliesList1[3].setQuantity(int(self.amount1_4.value()))
            addCurrentCart_SalesPerson(SuppliesList1[3])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_5(self):
        if self.check_budget(SuppliesList1[4].getPrice() * int(self.amount1_5.value())):
            self.check_out_list.addItem(SuppliesList1[4].getName() + '\t' + SuppliesList1[4].getQuality() + \
                                    '\t' + self.amount1_5.text() + '\t' + str(round(SuppliesList1[4].getPrice() * int(self.amount1_5.value()), 2)))
            SuppliesList1[4].setQuantity(int(self.amount1_5.value()))
            addCurrentCart_SalesPerson(SuppliesList1[4])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_6(self):
        if self.check_budget(SuppliesList1[5].getPrice() * int(self.amount1_6.value())):
            self.check_out_list.addItem(SuppliesList1[5].getName() + '\t' + SuppliesList1[5].getQuality() + \
                                    '\t' + self.amount1_6.text() + '\t' + str(round(SuppliesList1[5].getPrice() * int(self.amount1_6.value()), 2)))
            SuppliesList1[5].setQuantity(int(self.amount1_6.value()))
            addCurrentCart_SalesPerson(SuppliesList1[5])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_7(self):
        if self.check_budget(SuppliesList1[6].getPrice() * int(self.amount1_7.value())):
            self.check_out_list.addItem(SuppliesList1[6].getName() + '\t' + SuppliesList1[6].getQuality() + \
                                    '\t' + self.amount1_7.text() + '\t' + str(round(SuppliesList1[6].getPrice() * int(self.amount1_7.value()), 2)))
            SuppliesList1[6].setQuantity(int(self.amount1_7.value()))
            addCurrentCart_SalesPerson(SuppliesList1[6])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_8(self):
        if self.check_budget(SuppliesList1[7].getPrice() * int(self.amount1_8.value())):
            self.check_out_list.addItem(SuppliesList1[7].getName() + '\t' + SuppliesList1[7].getQuality() + \
                                    '\t' + self.amount1_8.text() + '\t' + str(round(SuppliesList1[7].getPrice() * int(self.amount1_8.value()), 2)))
            SuppliesList1[7].setQuantity(int(self.amount1_8.value()))
            addCurrentCart_SalesPerson(SuppliesList1[7])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_9(self):
        if self.check_budget(SuppliesList1[8].getPrice() * int(self.amount1_9.value())):
            self.check_out_list.addItem(SuppliesList1[8].getName() + '\t' + SuppliesList1[8].getQuality() + \
                                    '\t' + self.amount1_9.text() + '\t' + str(round(SuppliesList1[8].getPrice() * int(self.amount1_9.value()), 2)))
            SuppliesList1[8].setQuantity(int(self.amount1_9.value()))
            addCurrentCart_SalesPerson(SuppliesList1[8])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton1_10(self):
        if self.check_budget(SuppliesList1[9].getPrice() * int(self.amount1_10.value())):
            self.check_out_list.addItem(SuppliesList1[9].getName() + '\t' + SuppliesList1[9].getQuality() + \
                                    '\t' + self.amount1_10.text() + '\t' + str(round(SuppliesList1[9].getPrice() * int(self.amount1_10.value()), 2)))
            SuppliesList1[9].setQuantity(int(self.amount1_10.value()))
            addCurrentCart_SalesPerson(SuppliesList1[9])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    # For Supplier 2
    def addButton2_1(self):
        if self.check_budget(SuppliesList2[0].getPrice() * int(self.amount2_1.value())):
            self.check_out_list.addItem(SuppliesList2[0].getName() + '\t' + SuppliesList2[0].getQuality() + \
                                    '\t' + self.amount2_1.text() + '\t' + str(round(SuppliesList2[0].getPrice() * int(self.amount2_1.value()), 2)))
            SuppliesList2[0].setQuantity(int(self.amount2_1.value()))
            addCurrentCart_SalesPerson(SuppliesList2[0])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_2(self):
        if self.check_budget(SuppliesList2[1].getPrice() * int(self.amount2_2.value())):
            self.check_out_list.addItem(SuppliesList2[1].getName() + '\t' + SuppliesList2[1].getQuality() + \
                                    '\t' + self.amount2_2.text() + '\t' + str(round(SuppliesList2[1].getPrice() * int(self.amount2_2.value()), 2)))
            SuppliesList2[1].setQuantity(int(self.amount2_2.value()))
            addCurrentCart_SalesPerson(SuppliesList2[1])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_3(self):
        if self.check_budget(SuppliesList2[2].getPrice() * int(self.amount2_3.value())):
            self.check_out_list.addItem(SuppliesList2[2].getName() + '\t' + SuppliesList2[2].getQuality() + \
                                    '\t' + self.amount2_3.text() + '\t' + str(round(SuppliesList2[2].getPrice() * int(self.amount2_3.value()), 2)))
            SuppliesList2[2].setQuantity(int(self.amount2_3.value()))
            addCurrentCart_SalesPerson(SuppliesList2[2])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_4(self):
        if self.check_budget(SuppliesList2[3].getPrice() * int(self.amount2_4.value())):
            self.check_out_list.addItem(SuppliesList2[3].getName() + '\t' + SuppliesList2[3].getQuality() + \
                                    '\t' + self.amount2_4.text() + '\t' + str(round(SuppliesList2[3].getPrice() * int(self.amount2_4.value()), 2)))
            SuppliesList2[3].setQuantity(int(self.amount2_4.value()))
            addCurrentCart_SalesPerson(SuppliesList2[3])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_5(self):
        if self.check_budget(SuppliesList2[4].getPrice() * int(self.amount2_5.value())):
            self.check_out_list.addItem(SuppliesList2[4].getName() + '\t' + SuppliesList2[4].getQuality() + \
                                    '\t' + self.amount2_5.text() + '\t' + str(round(SuppliesList2[4].getPrice() * int(self.amount2_5.value()), 2)))
            SuppliesList2[4].setQuantity(int(self.amount2_5.value()))
            addCurrentCart_SalesPerson(SuppliesList2[4])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_6(self):
        if self.check_budget(SuppliesList2[5].getPrice() * int(self.amount2_6.value())):
            self.check_out_list.addItem(SuppliesList2[5].getName() + '\t' + SuppliesList2[5].getQuality() + \
                                    '\t' + self.amount2_6.text() + '\t' + str(round(SuppliesList2[5].getPrice() * int(self.amount2_6.value()), 2)))
            SuppliesList2[5].setQuantity(int(self.amount2_6.value()))
            addCurrentCart_SalesPerson(SuppliesList2[5])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_7(self):
        if self.check_budget(SuppliesList2[6].getPrice() * int(self.amount2_7.value())):
            self.check_out_list.addItem(SuppliesList2[6].getName() + '\t' + SuppliesList2[6].getQuality() + \
                                    '\t' + self.amount2_7.text() + '\t' + str(round(SuppliesList2[6].getPrice() * int(self.amount2_7.value()), 2)))
            SuppliesList2[6].setQuantity(int(self.amount2_7.value()))
            addCurrentCart_SalesPerson(SuppliesList2[6])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_8(self):
        if self.check_budget(SuppliesList2[7].getPrice() * int(self.amount2_8.value())):
            self.check_out_list.addItem(SuppliesList2[7].getName() + '\t' + SuppliesList2[7].getQuality() + \
                                    '\t' + self.amount2_8.text() + '\t' + str(round(SuppliesList2[7].getPrice() * int(self.amount2_8.value()), 2)))
            SuppliesList2[7].setQuantity(int(self.amount2_8.value()))
            addCurrentCart_SalesPerson(SuppliesList2[7])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_9(self):
        if self.check_budget(SuppliesList2[8].getPrice() * int(self.amount2_9.value())):
            self.check_out_list.addItem(SuppliesList2[8].getName() + '\t' + SuppliesList2[8].getQuality() + \
                                    '\t' + self.amount2_9.text() + '\t' + str(round(SuppliesList2[8].getPrice() * int(self.amount2_9.value()), 2)))
            SuppliesList2[8].setQuantity(int(self.amount2_9.value()))
            addCurrentCart_SalesPerson(SuppliesList2[8])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton2_10(self):
        if self.check_budget(SuppliesList2[9].getPrice() * int(self.amount2_10.value())):
            self.check_out_list.addItem(SuppliesList2[9].getName() + '\t' + SuppliesList2[9].getQuality() + \
                                    '\t' + self.amount2_10.text() + '\t' + str(round(SuppliesList2[9].getPrice() * int(self.amount2_10.value()), 2)))
            SuppliesList2[9].setQuantity(int(self.amount2_10.value()))
            addCurrentCart_SalesPerson(SuppliesList2[9])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    # For Supplier 3
    def addButton3_1(self):
        if self.check_budget(SuppliesList3[0].getPrice() * int(self.amount3_1.value())):
            self.check_out_list.addItem(SuppliesList3[0].getName() + '\t' + SuppliesList3[0].getQuality() + \
                                    '\t' + self.amount3_1.text() + '\t' + str(round(SuppliesList3[0].getPrice() * int(self.amount3_1.value()), 2)))
            SuppliesList3[0].setQuantity(int(self.amount3_1.value()))
            addCurrentCart_SalesPerson(SuppliesList3[0])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_2(self):
        if self.check_budget(SuppliesList3[1].getPrice() * int(self.amount3_2.value())):
            self.check_out_list.addItem(SuppliesList3[1].getName() + '\t' + SuppliesList3[1].getQuality() + \
                                    '\t' + self.amount3_2.text() + '\t' + str(round(SuppliesList3[1].getPrice() * int(self.amount3_2.value()), 2)))
            SuppliesList3[1].setQuantity(int(self.amount3_2.value()))
            addCurrentCart_SalesPerson(SuppliesList3[1])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_3(self):
        if self.check_budget(SuppliesList3[2].getPrice() * int(self.amount3_3.value())):
            self.check_out_list.addItem(SuppliesList3[2].getName() + '\t' + SuppliesList3[2].getQuality() + \
                                    '\t' + self.amount3_3.text() + '\t' + str(round(SuppliesList3[2].getPrice() * int(self.amount3_3.value()), 2)))
            SuppliesList3[2].setQuantity(int(self.amount3_3.value()))
            addCurrentCart_SalesPerson(SuppliesList3[2])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_4(self):
        if self.check_budget(SuppliesList3[3].getPrice() * int(self.amount3_4.value())):
            self.check_out_list.addItem(SuppliesList3[3].getName() + '\t' + SuppliesList3[3].getQuality() + \
                                    '\t' + self.amount3_4.text() + '\t' + str(round(SuppliesList3[3].getPrice() * int(self.amount3_4.value()), 2)))
            SuppliesList3[3].setQuantity(int(self.amount3_4.value()))
            addCurrentCart_SalesPerson(SuppliesList3[3])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_5(self):
        if self.check_budget(SuppliesList3[4].getPrice() * int(self.amount3_5.value())):
            self.check_out_list.addItem(SuppliesList3[4].getName() + '\t' + SuppliesList3[4].getQuality() + \
                                    '\t' + self.amount3_5.text() + '\t' + str(round(SuppliesList3[4].getPrice() * int(self.amount3_5.value()), 2)))
            SuppliesList3[4].setQuantity(int(self.amount3_5.value()))
            addCurrentCart_SalesPerson(SuppliesList3[4])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_6(self):
        if self.check_budget(SuppliesList3[5].getPrice() * int(self.amount3_6.value())):
            self.check_out_list.addItem(SuppliesList3[5].getName() + '\t' + SuppliesList3[5].getQuality() + \
                                    '\t' + self.amount3_6.text() + '\t' + str(round(SuppliesList3[5].getPrice() * int(self.amount3_6.value()), 2)))
            SuppliesList3[5].setQuantity(int(self.amount3_6.value()))
            addCurrentCart_SalesPerson(SuppliesList3[5])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_7(self):
        if self.check_budget(SuppliesList3[6].getPrice() * int(self.amount3_7.value())):
            self.check_out_list.addItem(SuppliesList3[6].getName() + '\t' + SuppliesList3[6].getQuality() + \
                                    '\t' + self.amount3_7.text() + '\t' + str(round(SuppliesList3[6].getPrice() * int(self.amount3_7.value()), 2)))
            SuppliesList3[6].setQuantity(int(self.amount3_7.value()))
            addCurrentCart_SalesPerson(SuppliesList3[6])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_8(self):
        if self.check_budget(SuppliesList3[7].getPrice() * int(self.amount3_8.value())):
            self.check_out_list.addItem(SuppliesList3[7].getName() + '\t' + SuppliesList3[7].getQuality() + \
                                    '\t' + self.amount3_8.text() + '\t' + str(round(SuppliesList3[7].getPrice() * int(self.amount3_8.value()), 2)))
            SuppliesList3[7].setQuantity(int(self.amount3_8.value()))
            addCurrentCart_SalesPerson(SuppliesList3[7])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_9(self):
        if self.check_budget(SuppliesList3[8].getPrice() * int(self.amount3_9.value())):
            self.check_out_list.addItem(SuppliesList3[8].getName() + '\t' + SuppliesList3[8].getQuality() + \
                                    '\t' + self.amount3_9.text() + '\t' + str(round(SuppliesList3[8].getPrice() * int(self.amount3_9.value()), 2)))
            SuppliesList3[8].setQuantity(int(self.amount3_9.value()))
            addCurrentCart_SalesPerson(SuppliesList3[8])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")

    def addButton3_10(self):
        if self.check_budget(SuppliesList3[9].getPrice() * int(self.amount3_10.value())):
            self.check_out_list.addItem(SuppliesList3[9].getName() + '\t' + SuppliesList3[9].getQuality() + \
                                    '\t' + self.amount3_10.text() + '\t' + str(round(SuppliesList3[9].getPrice() * int(self.amount3_10.value()), 2)))
            SuppliesList3[9].setQuantity(int(self.amount3_10.value()))
            addCurrentCart_SalesPerson(SuppliesList3[9])
            self.update_total()
            self.budget_connected_total()
        else:
            # pop out window to show error
            self.budget_error()
            print("Amount exceeds Budget!")


    def if_index_error_DOD(self,n):
        if n>3:
            return 1
        else:
            return n

    def if_index_error_DOD2(self,n):
        if n>9:
            return 4
        else:
            return n

    def add_DOD_item(self,item):
        return str(item)+ " (Deal Of the Day)"

    #deal of the day function
    def calculate_DOD(self):
        determine_dod_num = 0;
        today = date.today()
        determine_dod_num+=int(today.month)
        determine_dod_num+=int(today.day)

        print(determine_dod_num)
        temp = determine_dod_num%5

        for i in range(0,temp): #determine mod 5 amount of deals every day

            temp = (temp%2)+i
            temp = self.if_index_error_DOD(temp)

            temp2 = (determine_dod_num%3) + (determine_dod_num%4) + i
            temp2 = self.if_index_error_DOD2(temp2)

            if (temp == 0 or temp == 1):
                #if  (not SuppliesList1[temp2].isDealOfTheDay):
                    SuppliesList1[temp2].setDealOfTheDay()
                    self.deal_of_the_day_list.addItem("Supplier 1: "+str(SuppliesList1[temp2].getName()))
                    SuppliesList1[temp2].changeQuality('Best')
                    SuppliesList1[temp2].updatePrice()
                    SuppliesList1[temp2].changePrice(int(SuppliesList1[temp2].getPrice())*.50)
            elif temp == 2:
                #if (not SuppliesList2[temp2].isDealOfTheDay):
                    SuppliesList2[temp2].setDealOfTheDay()
                    self.deal_of_the_day_list.addItem("Supplier 2: " + str(SuppliesList2[temp2].getName()))
                    SuppliesList1[temp2].changeQuality('Best')
                    SuppliesList1[temp2].updatePrice()
                    SuppliesList1[temp2].changePrice(int(SuppliesList2[temp2].getPrice()) * .50)
            elif temp == 3:
                #if (not SuppliesList3[temp2].isDealOfTheDay):
                    SuppliesList3[temp2].setDealOfTheDay()
                    self.deal_of_the_day_list.addItem("Supplier 2: " + str(SuppliesList3[temp2].getName()))
                    SuppliesList2[temp2].changeQuality('Best')
                    SuppliesList2[temp2].updatePrice()
                    SuppliesList2[temp2].changePrice(int(SuppliesList2[temp2].getPrice()) * .50)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QCurrentWindow()
    ui = Sales_Window()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())

