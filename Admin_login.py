
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog
import Vasa
#from Mainwindow import Mainwindow
import pyodbc
import os
import sys


class Ui_Admin_Login(object):

    def setupUi(self,Admin_Login):
        Admin_Login.setObjectName("Admin_Login")
        Admin_Login.setEnabled(True)
        Admin_Login.resize(636, 629)
        Admin_Login.setAutoFillBackground(False)
        Admin_Login.setStyleSheet("#Admin_Login {background-image: url(:/Images/background-1462755_1280.jpg)}")
        self.login_title = QtWidgets.QLabel(Admin_Login)
        self.login_title.setGeometry(QtCore.QRect(130, -5, 341, 71))

        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setStyleSheet("color: rgb(85, 0, 0);")
        self.login_title.setAlignment(QtCore.Qt.AlignCenter)
        self.login_title.setObjectName("login_title")
        self.username_lbl = QtWidgets.QLabel(Admin_Login)
        self.username_lbl.setGeometry(QtCore.QRect(115, 250, 161, 51))
        self.username_lbl.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(Admin_Login)
        self.password_lbl.setGeometry(QtCore.QRect(116, 320, 161, 51))
        self.password_lbl.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.password_lbl.setObjectName("password_lbl")
        self.username_le = QtWidgets.QLineEdit(Admin_Login)
        self.username_le.setGeometry(QtCore.QRect(258, 256, 221, 41))
        self.username_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:white;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.username_le.setObjectName("username_le")
        self.password_le = QtWidgets.QLineEdit(Admin_Login)
        self.password_le.setGeometry(QtCore.QRect(258, 326, 221, 41))
        self.password_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:white;\n"
"font: 11pt \"Cambria\";\n"
"")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.login_btn = QtWidgets.QPushButton(Admin_Login)
        self.login_btn.setGeometry(QtCore.QRect(110, 426, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color:rgb(126, 255, 126);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;")
        self.login_btn.setObjectName("login_btn")
        self.cancel_btn = QtWidgets.QPushButton(Admin_Login)
        self.cancel_btn.setGeometry(QtCore.QRect(327, 426, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color:rgb(255, 131, 150);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:red;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.Login_frame = QtWidgets.QFrame(Admin_Login)
        self.Login_frame.setGeometry(QtCore.QRect(78, 126, 461, 421))
        self.Login_frame.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:red;\n"
"")
        self.Login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Login_frame.setObjectName("Login_frame")
        self.toolButton = QtWidgets.QToolButton(Admin_Login)
        self.toolButton.setGeometry(QtCore.QRect(246, 78, 121, 121))
        self.toolButton.setStyleSheet("background-color:rgb(142, 200, 156);\n"
"border-radius:60px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:red;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/man.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(90, 90))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName("toolButton")
        self.line = QtWidgets.QFrame(Admin_Login)
        self.line.setGeometry(QtCore.QRect(2, 57, 631, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Login_frame.raise_()
        self.login_title.raise_()
        self.username_lbl.raise_()
        self.password_lbl.raise_()
        self.username_le.raise_()
        self.password_le.raise_()
        self.login_btn.raise_()
        self.cancel_btn.raise_()
        self.toolButton.raise_()
        self.line.raise_()

        self.retranslateUi(Admin_Login)
        QtCore.QMetaObject.connectSlotsByName(Admin_Login)

    def retranslateUi(self, Admin_Login):
        _translate = QtCore.QCoreApplication.translate
        Admin_Login.setWindowTitle(_translate("Admin_Login", "Dialog"))
        self.login_title.setText(_translate("Admin_Login", "Admin Login Form"))
        self.username_lbl.setText(_translate("Admin_Login", "Username :"))
        self.password_lbl.setText(_translate("Admin_Login", "Password  :"))
        self.username_le.setPlaceholderText(_translate("Admin_Login", "Username here"))
        self.password_le.setPlaceholderText(_translate("Admin_Login", "Password here"))
        self.login_btn.setText(_translate("Admin_Login", "Login"))
        self.cancel_btn.setText(_translate("Admin_Login", "Cancel"))

class Admin_Login_User(QDialog,Ui_Admin_Login):
    def __init__(self,parent=None):
        super(Admin_Login_User,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Admin Login")

        self.login_btn.clicked.connect(self.loginbtn)
        self.cancel_btn.clicked.connect(self.cancelbtn)

        config_name = 'admin_login.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        self.show()

    def connectdb(self):
        global cur

        connect = pyodbc.connect('Driver={SQL SERVER};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur

    def loginbtn(self):

        self.username = str.lower(self.username_le.text())
        self.password = self.password_le.text()
        self.usercheck= False
        self.connectdb()

        query ='SELECT * FROM dbo.users WHERE username=? AND password =?'
        cur.execute(query,(self.username,self.password))

        result = cur.fetchall()

        if len(result)>0:
            if self.username == 'admin':

                print(self.username+' is logged in')

                self.usercheck = True
                self.close()
            else:
                QMessageBox.information(self,'Alert Window','Please enter only ADMIN credentials')
                self.username_le.setText('admin')
                self.password_le.clear()



        else:

            reply =QMessageBox.warning(self,'Alert Window','Please enter valid credentials',QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.username_le.clear()
                self.password_le.clear()

    def cancelbtn(self):
        self.canclclick =True
        self.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Login = QtWidgets.QDialog()
    ui = Admin_Login_User()
    #ui.setupUi(Admin_Login)
    #Admin_Login.show()
    ui.show()
    sys.exit(app.exec_())
