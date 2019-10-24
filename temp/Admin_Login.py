# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_Login(object):
    def loginwindow(self, Admin_Login):
        Admin_Login.setObjectName("Admin_Login")
        Admin_Login.resize(547, 379)
        self.username_lbl = QtWidgets.QLabel(Admin_Login)
        self.username_lbl.setGeometry(QtCore.QRect(50, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_lbl.setFont(font)
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(Admin_Login)
        self.password_lbl.setGeometry(QtCore.QRect(50, 160, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_lbl.setFont(font)
        self.password_lbl.setObjectName("password_lbl")
        self.username_le = QtWidgets.QLineEdit(Admin_Login)
        self.username_le.setGeometry(QtCore.QRect(200, 114, 221, 30))
        self.username_le.setObjectName("username_le")
        self.password_le = QtWidgets.QLineEdit(Admin_Login)
        self.password_le.setGeometry(QtCore.QRect(200, 170, 221, 30))
        self.password_le.setObjectName("password_le")
        self.login_btn = QtWidgets.QPushButton(Admin_Login)
        self.login_btn.setGeometry(QtCore.QRect(160, 260, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color:rgb(0, 255, 127)")
        self.login_btn.setObjectName("login_btn")
        self.cancel_btn = QtWidgets.QPushButton(Admin_Login)
        self.cancel_btn.setGeometry(QtCore.QRect(320, 260, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color:rgb(255, 148, 155)")
        self.cancel_btn.setObjectName("cancel_btn")

        self.retranslateUi(Admin_Login)
        QtCore.QMetaObject.connectSlotsByName(Admin_Login)

    def retranslateUi(self, Admin_Login):
        _translate = QtCore.QCoreApplication.translate
        Admin_Login.setWindowTitle(_translate("Admin_Login", "Dialog"))
        self.username_lbl.setText(_translate("Admin_Login", "User Name :"))
        self.password_lbl.setText(_translate("Admin_Login", "Password   :"))
        self.login_btn.setText(_translate("Admin_Login", "Login"))
        self.cancel_btn.setText(_translate("Admin_Login", "Cancel"))
