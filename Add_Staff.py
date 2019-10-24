from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
import pyodbc
from Staff_Table import Add_Staff_Details
import Vasa

class Ui_New_staff(object):
    def setupUi(self, New_staff):
        New_staff.setObjectName("New_staff")
        New_staff.resize(698, 684)
        New_staff.setStyleSheet("#New_staff{\n"
"    background-image: url(:/Images/New-Blue-Background-Main-2.jpg)}")
        self.staff_frame = QtWidgets.QFrame(New_staff)
        self.staff_frame.setGeometry(QtCore.QRect(90, 100, 521, 511))
        self.staff_frame.setStyleSheet("#staff_frame{background-color:rgb(223, 223, 223);\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;}")
        self.staff_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staff_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staff_frame.setObjectName("staff_frame")
        self.username_le = QtWidgets.QLineEdit(self.staff_frame)
        self.username_le.setGeometry(QtCore.QRect(250, 74, 241, 41))
        self.username_le.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.username_le.setObjectName("username_le")
        self.username_label = QtWidgets.QLabel(self.staff_frame)
        self.username_label.setGeometry(QtCore.QRect(30, 74, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color:rgb(39, 140, 81);")
        self.username_label.setWordWrap(False)
        self.username_label.setIndent(-1)
        self.username_label.setObjectName("username_label")
        self.password_le = QtWidgets.QLineEdit(self.staff_frame)
        self.password_le.setGeometry(QtCore.QRect(250, 134, 241, 41))
        self.password_le.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.password_le.setText("")
        self.password_le.setObjectName("password_le")
        self.password_label = QtWidgets.QLabel(self.staff_frame)
        self.password_label.setGeometry(QtCore.QRect(30, 134, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color:rgb(39, 140, 81);")
        self.password_label.setWordWrap(False)
        self.password_label.setIndent(-1)
        self.password_label.setObjectName("password_label")
        self.email_label = QtWidgets.QLabel(self.staff_frame)
        self.email_label.setGeometry(QtCore.QRect(30, 194, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color:rgb(39, 140, 81);")
        self.email_label.setWordWrap(False)
        self.email_label.setIndent(-1)
        self.email_label.setObjectName("email_label")
        self.email_le = QtWidgets.QLineEdit(self.staff_frame)
        self.email_le.setGeometry(QtCore.QRect(250, 194, 241, 41))
        self.email_le.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.email_le.setText("")
        self.email_le.setObjectName("email_le")
        self.contact_label = QtWidgets.QLabel(self.staff_frame)
        self.contact_label.setGeometry(QtCore.QRect(30, 254, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.contact_label.setFont(font)
        self.contact_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color:rgb(39, 140, 81);")
        self.contact_label.setWordWrap(False)
        self.contact_label.setIndent(-1)
        self.contact_label.setObjectName("contact_label")
        self.contact_le = QtWidgets.QLineEdit(self.staff_frame)
        self.contact_le.setGeometry(QtCore.QRect(250, 254, 241, 41))
        self.contact_le.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.contact_le.setText("")
        self.contact_le.setObjectName("contact_le")
        self.address_le = QtWidgets.QLineEdit(self.staff_frame)
        self.address_le.setGeometry(QtCore.QRect(250, 324, 241, 41))
        self.address_le.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.address_le.setText("")
        self.address_le.setObjectName("address_le")
        self.address_label = QtWidgets.QLabel(self.staff_frame)
        self.address_label.setGeometry(QtCore.QRect(30, 324, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color:rgb(39, 140, 81);")
        self.address_label.setWordWrap(False)
        self.address_label.setIndent(-1)
        self.address_label.setObjectName("address_label")
        self.change_btn = QtWidgets.QPushButton(self.staff_frame)
        self.change_btn.setGeometry(QtCore.QRect(200, 410, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.05, y1:0, x2:1, y2:1, stop:0 rgba(68, 187, 0, 243), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.change_btn.setObjectName("change_btn")
        self.clr_btn = QtWidgets.QPushButton(self.staff_frame)
        self.clr_btn.setGeometry(QtCore.QRect(360, 409, 131, 61))
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
        self.change_btn_2 = QtWidgets.QPushButton(self.staff_frame)
        self.change_btn_2.setGeometry(QtCore.QRect(10, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.change_btn_2.setFont(font)
        self.change_btn_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(143, 89, 162, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.change_btn_2.setObjectName("change_btn_2")
        self.toolButton = QtWidgets.QToolButton(New_staff)
        self.toolButton.setGeometry(QtCore.QRect(160, 61, 371, 81))
        self.toolButton.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.05, y1:0, x2:1, y2:1, stop:0 rgba(105, 121, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 16pt \"Cambria\";\n"
"font: Bold;\n"
"color: rgb(34, 48, 170);\n"
"border-radius:40px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;")
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(New_staff)
        self.toolButton_2.setGeometry(QtCore.QRect(162, 61, 81, 81))
        self.toolButton_2.setStyleSheet("border-radius:15px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/employee-icon_246750.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(New_staff)
        QtCore.QMetaObject.connectSlotsByName(New_staff)

    def retranslateUi(self, New_staff):
        _translate = QtCore.QCoreApplication.translate
        New_staff.setWindowTitle(_translate("New_staff", "Dialog"))
        self.username_label.setText(_translate("New_staff", "User Name           :"))
        self.password_label.setText(_translate("New_staff", "Password              :"))
        self.email_label.setText(_translate("New_staff", "Email ID                 :"))
        self.contact_label.setText(_translate("New_staff", "Contact No            :"))
        self.address_label.setText(_translate("New_staff", "Address                 :"))
        self.change_btn.setText(_translate("New_staff", "ADD"))
        self.clr_btn.setText(_translate("New_staff", "Clear"))
        self.change_btn_2.setText(_translate("New_staff", "View Staffs"))
        self.toolButton.setText(_translate("New_staff", "New Staff Form"))
        self.toolButton_2.setText(_translate("New_staff", "..."))

class Add_Staff_Window(QDialog,Ui_New_staff):
    def __init__(self,parent=None):
        super(Add_Staff_Window,self).__init__(parent)
        self.setupUi(self)
        self.onlyint = QtGui.QIntValidator()
        self.contact_le.setValidator(self.onlyint)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)

        self.linedit = [self.username_le, self.password_le, self.email_le, self.contact_le, self.address_le]

        self.change_btn.clicked.connect(self.addbtn)
        self.clr_btn.clicked.connect(self.clearbtn)
        self.change_btn_2.clicked.connect(self.viewstaff)

    def addbtn(self):

        if self.username_le.text() =='':
            self.username =''

        else:
            self.username = str.lower(self.username_le.text())


        if self.contact_le.text()=='':
            self.contact=0
        else:
            self.contact = int(self.contact_le.text())


        self.password = self.password_le.text()
        self.email = self.email_le.text()

        self.address = self.address_le.text()


        if self.username !='' and self.password != '' and self.contact!=0:

            sel_query = 'SELECT * FROM dbo.USERS WHERE USERNAME=? AND PASSWORD=?'
            insert_query = "INSERT INTO dbo.USERS VALUES (NEXT VALUE FOR audit.users_seq,?,?,?,?,?) "
            data =(self.username,self.password,self.email,self.contact,self.address)

            connect = pyodbc.connect('Driver={SQL SERVER};' 
                                     'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                     'Database=VASADB;'
                                     'Trusted_Connection=yes;')
            cur = connect.cursor()
            cur.execute(sel_query,(self.username,self.password))
            result = cur.fetchall()

            if len(result)==0:
                    cur.execute(insert_query ,data)
                    connect.commit()
                    connect.close()
                    QMessageBox.information(self,'Add Staff','Staff '+str.upper(self.username)+' added successfully')

            else:
                    QMessageBox.information(self,'Alert','Sorry! User already available')

            for i in self.linedit:
                    i.clear()
        else:
            QMessageBox.information(self,'Alert Window','Please enter the proper staff details')

    def clearbtn(self):
            for i in self.linedit:
                    i.clear()

    def viewstaff(self):
        dialog = Add_Staff_Details()
        dialog.exec_()


















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_staff = QtWidgets.QDialog()
   # ui = Ui_New_staff()
    ui =Add_Staff_Window()
    #ui.setupUi(New_staff)
    #New_staff.show()
    ui.show()
    sys.exit(app.exec_())
