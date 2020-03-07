
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import pyqtSlot
import pyodbc
import Vasa
import os
import sys


class Ui_Change_Admin_Password(object):
    def setupUi(self, Change_Admin_Password):
        Change_Admin_Password.setObjectName("Change_Admin_Password")
        Change_Admin_Password.resize(699, 647)
        Change_Admin_Password.setStyleSheet("#Change_Admin_Password {background-image: url(:/Images/36565647561_d380a3d691_b.jpg);}")
        self.username_label = QtWidgets.QLabel(Change_Admin_Password)
        self.username_label.setGeometry(QtCore.QRect(130, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.username_label.setWordWrap(False)
        self.username_label.setIndent(-1)
        self.username_label.setObjectName("username_label")
        self.cur_pass_label = QtWidgets.QLabel(Change_Admin_Password)
        self.cur_pass_label.setGeometry(QtCore.QRect(129, 314, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cur_pass_label.setFont(font)
        self.cur_pass_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.cur_pass_label.setWordWrap(True)
        self.cur_pass_label.setObjectName("cur_pass_label")
        self.new_pass_lbl = QtWidgets.QLabel(Change_Admin_Password)
        self.new_pass_lbl.setGeometry(QtCore.QRect(130, 410, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.new_pass_lbl.setFont(font)
        self.new_pass_lbl.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(255, 255, 255);")
        self.new_pass_lbl.setWordWrap(False)
        self.new_pass_lbl.setObjectName("new_pass_lbl")
        self.username_le = QtWidgets.QLineEdit(Change_Admin_Password)
        self.username_le.setGeometry(QtCore.QRect(351, 250, 221, 41))
        self.username_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.username_le.setObjectName("username_le")
        self.cur_pass_le = QtWidgets.QLineEdit(Change_Admin_Password)
        self.cur_pass_le.setGeometry(QtCore.QRect(351, 330, 221, 41))
        self.cur_pass_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.cur_pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cur_pass_le.setObjectName("cur_pass_le")
        self.new_pass_le = QtWidgets.QLineEdit(Change_Admin_Password)
        self.new_pass_le.setGeometry(QtCore.QRect(351, 410, 221, 41))
        self.new_pass_le.setStyleSheet("border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.new_pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass_le.setObjectName("new_pass_le")
        self.change_btn = QtWidgets.QPushButton(Change_Admin_Password)
        self.change_btn.setGeometry(QtCore.QRect(113, 508, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(143, 89, 162, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.change_btn.setObjectName("change_btn")
        self.clr_btn = QtWidgets.QPushButton(Change_Admin_Password)
        self.clr_btn.setGeometry(QtCore.QRect(280, 508, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clr_btn.setFont(font)
        self.clr_btn.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 144, 35, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.clr_btn.setObjectName("clr_btn")
        self.cncl_btn = QtWidgets.QPushButton(Change_Admin_Password)
        self.cncl_btn.setGeometry(QtCore.QRect(445, 508, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cncl_btn.setFont(font)
        self.cncl_btn.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 53, 35, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.cncl_btn.setObjectName("cncl_btn")
        self.page_frame = QtWidgets.QFrame(Change_Admin_Password)
        self.page_frame.setGeometry(QtCore.QRect(80, 140, 521, 481))
        self.page_frame.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;\n"
"")
        self.page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_frame.setObjectName("page_frame")
        self.toolButton = QtWidgets.QToolButton(Change_Admin_Password)
        self.toolButton.setGeometry(QtCore.QRect(160, 102, 371, 81))
        self.toolButton.setStyleSheet(";\n"
";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(89, 162, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 16pt \"Cambria\";\n"
"font: Bold;\n"
"color: rgb(34, 48, 170);\n"
"border-radius:40px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Change_Admin_Password)
        self.toolButton_2.setGeometry(QtCore.QRect(300, 2, 101, 101))
        self.toolButton_2.setStyleSheet("\n"
"border-radius:50px;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-color:white;\n"
"")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/adminpasswordchange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(110, 110))
        self.toolButton_2.setCheckable(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.page_frame.raise_()
        self.username_label.raise_()
        self.cur_pass_label.raise_()
        self.new_pass_lbl.raise_()
        self.username_le.raise_()
        self.cur_pass_le.raise_()
        self.new_pass_le.raise_()
        self.change_btn.raise_()
        self.clr_btn.raise_()
        self.cncl_btn.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()

        self.retranslateUi(Change_Admin_Password)
        QtCore.QMetaObject.connectSlotsByName(Change_Admin_Password)

    def retranslateUi(self, Change_Admin_Password):
        _translate = QtCore.QCoreApplication.translate
        Change_Admin_Password.setWindowTitle(_translate("Change_Admin_Password", "Dialog"))
        self.username_label.setText(_translate("Change_Admin_Password", "User Name           :"))
        self.cur_pass_label.setText(_translate("Change_Admin_Password", "Current Password              :"))
        self.new_pass_lbl.setText(_translate("Change_Admin_Password", "New Password    :"))
        self.username_le.setPlaceholderText(_translate("Change_Admin_Password", "Username"))
        self.cur_pass_le.setPlaceholderText(_translate("Change_Admin_Password", "Current password"))
        self.new_pass_le.setPlaceholderText(_translate("Change_Admin_Password", "New password"))
        self.change_btn.setText(_translate("Change_Admin_Password", "Change"))
        self.clr_btn.setText(_translate("Change_Admin_Password", "Clear"))
        self.cncl_btn.setText(_translate("Change_Admin_Password", "Cancel"))
        self.toolButton.setText(_translate("Change_Admin_Password", "Change Staff Password"))


class Staff_Password_Change(QDialog,Ui_Change_Admin_Password):
    def __init__(self,parent=None):
        super(Staff_Password_Change,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Change Staff Password")

        self.change_btn.clicked.connect(self.changebtn)
        self.clr_btn.clicked.connect(self.clear_btn)
        self.cncl_btn.clicked.connect(self.cancelbtn)

        config_name = 'staff_password.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))


        self.show()

    def changebtn(self):
        self.username = str.lower(self.username_le.text())
        self.currpass = self.cur_pass_le.text()
        self.newpass = self.new_pass_le.text()
        print(self.username)

        if self.username != 'admin':

            sel_query = 'SELECT * FROM dbo.users WHERE USERNAME=? AND PASSWORD =?'
            query = "UPDATE dbo.users set PASSWORD='%s' WHERE USERNAME ='%s' AND PASSWORD='%s' "
            data = (self.newpass,self.username,self.currpass)


            connect = pyodbc.connect('Driver={SQL SERVER};'
                                     'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                     'Database=VASADB;'
                                     'Trusted_Connection=yes;')
            cur = connect.cursor()

            cur.execute(sel_query,(self.username,self.currpass))
            result = cur.fetchall()

            if len(result)>0:
                cur.execute(query % data)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Info','Password Changed Successfully')
                self.close()
                print('ran welll')
            else:
                reply = QMessageBox.warning(self, 'Alert Window', 'Please enter valid credentials', QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    self.username_le.clear()
                    self.cur_pass_le.clear()
                    self.new_pass_le.clear()
        else:
            QMessageBox.information(self,'Alert','Please enter only staff user')
            self.username_le.clear()
            self.cur_pass_le.clear()
            self.new_pass_le.clear()





    def clear_btn(self):
        print("hello")
        self.username_le.clear()
        self.cur_pass_le.clear()
        self.new_pass_le.clear()



    def cancelbtn(self):
        print('closed')
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Change_Admin_Password = QtWidgets.QDialog()
    #ui = Ui_Change_Admin_Password()
    ui=Staff_Password_Change()
    #ui.setupUi(Change_Admin_Password)
    #Change_Admin_Password.show()
    ui.show()
    sys.exit(app.exec_())
