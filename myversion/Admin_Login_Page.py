from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLabel,QLineEdit,QPushButton,QApplication,QFormLayout,QMessageBox
from PyQt5 import QtCore,QtGui

import sys
import pyodbc


class Admin_login(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.adminloginwindow()

        self.show()

    def adminloginwindow(self):
        self.title = 'Admin Login Page'

        self.setWindowTitle(self.title)
        self.resize(541,501)

        font= QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)

        vbox= QVBoxLayout(self)

        layout =QFormLayout()

        self.title_label = QLabel('Admin Login')
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        self.username_label = QLabel('User Name :')
        self.username_label.setGeometry(QtCore.QRect(80, 180, 161, 51))
        self.username_label.setStyleSheet('font-size:14pt;font-weight:600')

        self.password_label = QLabel('Password :')
        self.password_label.setGeometry(QtCore.QRect(80, 250, 161, 51))
        self.password_label.setStyleSheet('font-size:14pt;font-weight:600')

        self.username_le = QLineEdit()
        self.username_le.setGeometry(QtCore.QRect(240, 190, 221, 31))
        self.username_le.setStyleSheet("border-radius:10px;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-color:black;")

        self.password_le = QLineEdit()
        self.password_le.setGeometry(QtCore.QRect(240, 260, 221, 31))
        self.password_le.setEchoMode(QLineEdit.Password)
        self.password_le.setStyleSheet("border-radius:10px;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-color:black;")

        self.login_btn = QPushButton('Login')
        self.login_btn.setGeometry(QtCore.QRect(120, 360, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color:rgb(126, 255, 126);\n"
                                      "border-radius:20px;\n"
                                      "border-style:outset;\n"
                                      "border-width:3px;\n"
                                      "border-color:black;\n"
                                      "font:bold;")
        self.login_btn.clicked.connect(self.loginbtn)


        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setGeometry(QtCore.QRect(310, 360, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color:rgb(255, 131, 150);\n"
                                     "border-radius:20px;\n"
                                     "border-style:outset;\n"
                                     "border-width:3px;\n"
                                     "border-color:black;\n"
                                     "font:bold;")
        self.cancel_btn.clicked.connect(self.close)



        vbox.addWidget(self.title_label)
        layout.addRow(self.username_label,self.username_le)
        layout.addRow(self.password_label,self.password_le)
        layout.addRow(self.login_btn,self.cancel_btn)
        #layout.setGeometry(QtCore.QRect(310, 360, 151, 61))
        vbox.addLayout(layout)



        self.setLayout(vbox)

    def loginbtn(self):
        self.username = self.username_le.text()
        self.password = self.password_le.text()
        self.usercheck=False

        connect = pyodbc.connect('Driver={SQL SERVER};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur= connect.cursor()

        query ='SELECT * FROM dbo.users WHERE username=? AND password =?'
        cur.execute(query,(self.username,self.password))

        result = cur.fetchall()




        if len(result)>0:
            print(self.username+' is logged in')
            self.usercheck=True
            self.close()

        else:
            QMessageBox.warning(self,'Alert Window','Please enter valid credentials',QMessageBox.Ok)

    def cancelbtn(self):
        self.canclclick =True
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Admin_login()

    sys.exit(app.exec_())







