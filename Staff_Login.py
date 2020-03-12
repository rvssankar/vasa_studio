
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
import pyodbc
import Vasa
import os
import sys
from Odbc_Connection import Add_Odbc_Connection

class Ui_Staff_Login(object):
    def setupUi(self, Staff_Login):
        Staff_Login.setObjectName("Staff_Login")
        Staff_Login.setEnabled(True)
        Staff_Login.resize(636, 629)
        Staff_Login.setAutoFillBackground(False)
        Staff_Login.setStyleSheet("#Staff_Login{background-image:url(:/Images/50-Beautiful.jpg)}")
        self.login_title = QtWidgets.QLabel(Staff_Login)
        self.login_title.setGeometry(QtCore.QRect(130, -5, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setStyleSheet("color:rgb(61, 61, 91)")
        self.login_title.setAlignment(QtCore.Qt.AlignCenter)
        self.login_title.setObjectName("login_title")
        self.username_lbl = QtWidgets.QLabel(Staff_Login)
        self.username_lbl.setGeometry(QtCore.QRect(115, 250, 161, 51))
        self.username_lbl.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(Staff_Login)
        self.password_lbl.setGeometry(QtCore.QRect(116, 320, 161, 51))
        self.password_lbl.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.password_lbl.setObjectName("password_lbl")
        self.username_le = QtWidgets.QLineEdit(Staff_Login)
        self.username_le.setGeometry(QtCore.QRect(258, 256, 221, 41))
        self.username_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:white;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.username_le.setObjectName("username_le")
        self.password_le = QtWidgets.QLineEdit(Staff_Login)
        self.password_le.setGeometry(QtCore.QRect(258, 326, 221, 41))
        self.password_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:white;\n"
"font: 11pt \"Cambria\";")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.login_btn = QtWidgets.QPushButton(Staff_Login)
        self.login_btn.setGeometry(QtCore.QRect(120, 426, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("#login_btn{background-color:rgb(126, 255, 126);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;} \n"
"#login_btn:pressed{border-style:solid;border-width:9px}"                                     )
        self.login_btn.setObjectName("login_btn")
        self.cancel_btn = QtWidgets.QPushButton(Staff_Login)
        self.cancel_btn.setGeometry(QtCore.QRect(326, 426, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("#cancel_btn{background-color:rgb(255, 131, 150);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:red;} \n"
"#cancel_btn:pressed{border-style:solid;border-width:9px}"                                      )
        self.cancel_btn.setObjectName("cancel_btn")
        self.frame = QtWidgets.QFrame(Staff_Login)
        self.frame.setGeometry(QtCore.QRect(78, 126, 461, 421))
        self.frame.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:red;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(Staff_Login)
        self.toolButton.setGeometry(QtCore.QRect(246, 78, 121, 121))
        self.toolButton.setStyleSheet("background-color:rgb(200, 154, 47);\n"
"border-radius:60px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:red;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Staff_Login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(110, 110))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName("toolButton")
        self.line = QtWidgets.QFrame(Staff_Login)
        self.line.setGeometry(QtCore.QRect(2, 57, 631, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame.raise_()
        self.login_title.raise_()
        self.username_lbl.raise_()
        self.password_lbl.raise_()
        self.username_le.raise_()
        self.password_le.raise_()
        self.login_btn.raise_()
        self.cancel_btn.raise_()
        self.toolButton.raise_()
        self.line.raise_()

        self.retranslateUi(Staff_Login)
        QtCore.QMetaObject.connectSlotsByName(Staff_Login)

    def retranslateUi(self, Staff_Login):
        _translate = QtCore.QCoreApplication.translate
        Staff_Login.setWindowTitle(_translate("Staff_Login", "Dialog"))
        self.login_title.setText(_translate("Staff_Login", "Staff Login Form"))
        self.username_lbl.setText(_translate("Staff_Login", "Username :"))
        self.password_lbl.setText(_translate("Staff_Login", "Password  :"))
        self.username_le.setPlaceholderText(_translate("Staff_Login", "Username here"))
        self.password_le.setPlaceholderText(_translate("Staff_Login", "Password here"))
        self.login_btn.setText(_translate("Staff_Login", "Login"))
        self.cancel_btn.setText(_translate("Staff_Login", "Cancel"))

class Staff_Login_User(QDialog,Ui_Staff_Login):
    def __init__(self,parent=None):
        super(Staff_Login_User,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Staff Login")

        self.login_btn.clicked.connect(self.loginbtn)
        self.cancel_btn.clicked.connect(self.cancelbtn)

        config_name = 'staff_login.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        login_image = os.path.join(application_path, "images", "login.png")
        cancel_image = os.path.join(application_path, "images", "cancel.png")

        self.login_btn.setIcon(QtGui.QIcon(login_image))
        self.login_btn.setIconSize(QtCore.QSize(40, 40))

        self.cancel_btn.setIcon(QtGui.QIcon(cancel_image))
        self.cancel_btn.setIconSize(QtCore.QSize(40, 40))

        self.show()

    def connectdb(self):
        global cur
        global connect
        cur, con = Add_Odbc_Connection.connectdb(self)
        connect = con
        return cur

        '''global cur
        global connect

        connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur'''

    def loginbtn(self):

        self.username = self.username_le.text()
        self.password = self.password_le.text()
        self.usercheck = False
        self.connectdb()

        query = 'SELECT * FROM dbo.users WHERE username=? AND password =?'
        cur.execute(query, (self.username, self.password))

        result = cur.fetchall()


        if len(result) > 0:
            print(self.username + ' is logged in')
            self.usercheck = True
            self.close()
        else:

            reply = QMessageBox.warning(self, 'Alert Window', 'Please enter valid credentials', QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.username_le.clear()
                self.password_le.clear()

    def cancelbtn(self):
        self.canclclick = True
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Staff_Login = QtWidgets.QDialog()
    ui = Staff_Login_User()
    #ui.setupUi(Staff_Login)
    ui.show()
    sys.exit(app.exec_())
