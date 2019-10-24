# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 26))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        self.menuChange_Password = QtWidgets.QMenu(self.menubar)
        self.menuChange_Password.setObjectName("menuChange_Password")
        self.menuAdd_Staffs = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Staffs.setObjectName("menuAdd_Staffs")
        self.menuCustomer_Billing = QtWidgets.QMenu(self.menubar)
        self.menuCustomer_Billing.setObjectName("menuCustomer_Billing")
        self.menuProduct_Cost = QtWidgets.QMenu(self.menubar)
        self.menuProduct_Cost.setObjectName("menuProduct_Cost")
        self.menuExpense = QtWidgets.QMenu(self.menubar)
        self.menuExpense.setObjectName("menuExpense")
        self.menuWork_Status = QtWidgets.QMenu(self.menubar)
        self.menuWork_Status.setObjectName("menuWork_Status")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuReminders = QtWidgets.QMenu(self.menubar)
        self.menuReminders.setObjectName("menuReminders")
        self.menuLogout = QtWidgets.QMenu(self.menubar)
        self.menuLogout.setObjectName("menuLogout")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdmin_Login = QtWidgets.QAction(MainWindow)
        self.actionAdmin_Login.setObjectName("actionAdmin_Login")
        self.actionStaff_Login = QtWidgets.QAction(MainWindow)
        self.actionStaff_Login.setObjectName("actionStaff_Login")
        self.menuLogin.addAction(self.actionAdmin_Login)
        self.menuLogin.addAction(self.actionStaff_Login)
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuChange_Password.menuAction())
        self.menubar.addAction(self.menuAdd_Staffs.menuAction())
        self.menubar.addAction(self.menuCustomer_Billing.menuAction())
        self.menubar.addAction(self.menuProduct_Cost.menuAction())
        self.menubar.addAction(self.menuExpense.menuAction())
        self.menubar.addAction(self.menuWork_Status.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuReminders.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuLogin.setTitle(_translate("MainWindow", "Login"))
        self.menuChange_Password.setTitle(_translate("MainWindow", "Change Password"))
        self.menuAdd_Staffs.setTitle(_translate("MainWindow", "Add Staffs"))
        self.menuCustomer_Billing.setTitle(_translate("MainWindow", "Customer Billing"))
        self.menuProduct_Cost.setTitle(_translate("MainWindow", "Product Cost"))
        self.menuExpense.setTitle(_translate("MainWindow", "Expense"))
        self.menuWork_Status.setTitle(_translate("MainWindow", "Work Status"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.menuReminders.setTitle(_translate("MainWindow", "Reminders"))
        self.menuLogout.setTitle(_translate("MainWindow", "Log Out"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionAdmin_Login.setText(_translate("MainWindow", "Admin Login"))
        self.actionStaff_Login.setText(_translate("MainWindow", "Staff Login"))
