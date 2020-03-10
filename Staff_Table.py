
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QTableWidgetItem,QMessageBox,QTableWidget
import pyodbc
import os
import sys


class Ui_Table_dialog(object):
    def setupUi(self, Table_dialog):
        Table_dialog.setObjectName("Table_dialog")
        Table_dialog.resize(1031, 679)
        Table_dialog.setStyleSheet("#Table_dialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0.05, y1:0, x2:1, y2:1, stop:0 rgba(215, 209, 54, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.staff_table = QtWidgets.QTableWidget(Table_dialog)
        self.staff_table.setGeometry(QtCore.QRect(30, 80, 971, 481))
        self.staff_table.setStyleSheet("")
        self.staff_table.setObjectName("staff_table")
        self.staff_table.setColumnCount(4)
        self.staff_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.staff_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.staff_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.staff_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.staff_table.setHorizontalHeaderItem(3, item)
        self.staff_table.horizontalHeader().setCascadingSectionResizes(True)
        self.staff_table.horizontalHeader().setSortIndicatorShown(False)
        self.staff_table.horizontalHeader().setStretchLastSection(True)
        self.staff_table.verticalHeader().setStretchLastSection(False)
        self.delete_btn = QtWidgets.QPushButton(Table_dialog)
        self.delete_btn.setGeometry(QtCore.QRect(130, 590, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("#delete_btn{background-color: rgb(202, 66, 68);\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:6px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#delete_btn:pressed{border-style:solid;border-width:10px}"                                      )
        self.delete_btn.setObjectName("delete_btn")
        self.close_btn = QtWidgets.QPushButton(Table_dialog)
        self.close_btn.setGeometry(QtCore.QRect(710, 590, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("#close_btn{background-color: rgb(139, 97, 186);\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:6px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#close_btn:pressed{border-style:solid;border-width:10px}"                                     )
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(Table_dialog)
        QtCore.QMetaObject.connectSlotsByName(Table_dialog)

    def retranslateUi(self, Table_dialog):
        _translate = QtCore.QCoreApplication.translate
        Table_dialog.setWindowTitle(_translate("Table_dialog", "Dialog"))
        item = self.staff_table.horizontalHeaderItem(0)
        item.setText(_translate("Table_dialog", "Username"))
        item = self.staff_table.horizontalHeaderItem(1)
        item.setText(_translate("Table_dialog", "Email"))
        item = self.staff_table.horizontalHeaderItem(2)
        item.setText(_translate("Table_dialog", "Contact_No"))
        item = self.staff_table.horizontalHeaderItem(3)
        item.setText(_translate("Table_dialog", "Address"))
        self.delete_btn.setText(_translate("Table_dialog", "Delete Staff"))
        self.close_btn.setText(_translate("Table_dialog", "Close"))

class Add_Staff_Details(QDialog,Ui_Table_dialog):
    def __init__(self,parent=None):
        super(Add_Staff_Details,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Staff Details")

        self.display_records()
        self.close_btn.clicked.connect(self.closebtn)
        self.delete_btn.clicked.connect(self.deletebtn)

        config_name = 'staff_table.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        delete_image = os.path.join(application_path, "images", "delete.png")
        close_image = os.path.join(application_path, "images", "cancel.png")

        self.delete_btn.setIcon(QtGui.QIcon(delete_image))
        self.delete_btn.setIconSize(QtCore.QSize(45, 45))

        self.close_btn.setIcon(QtGui.QIcon(close_image))
        self.close_btn.setIconSize(QtCore.QSize(45, 45))


    def display_records(self):
        connect = pyodbc.connect('Driver={SQL SERVER};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        sel_query = 'SELECT USERNAME,EMAIL_ID,CONTACT_NUMBER,ADDRESS FROM dbo.USERS'
        result = cur.execute(sel_query)
        self.staff_table.setRowCount(0)
        header= self.staff_table.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}");
        self.staff_table.setEditTriggers(QTableWidget.NoEditTriggers)

        for row_num,row_data in enumerate(result):
            self.staff_table.insertRow(row_num)
            for col_num,data in enumerate(row_data):
                self.staff_table.setItem(row_num,col_num,QTableWidgetItem(str(data)))
                self.staff_table.setEditTriggers(QTableWidget.NoEditTriggers)
        connect.close()

    def deletebtn(self):

        index = self.staff_table.selectionModel().currentIndex()
        value = index.sibling(index.row(), index.column()).row()
        print("The  row index is ",value)

        user_name = self.staff_table.item(value,0).text()
        print(user_name)
        phone_no = int(self.staff_table.item(value,2).text())

        if user_name != 'admin':


            del_data = (user_name,phone_no)

            connect = pyodbc.connect('Driver={SQL SERVER};'
                                     'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                     'Database=VASADB;'
                                     'Trusted_Connection=yes;')
            cur = connect.cursor()
            sel_query = 'SELECT USERNAME,EMAIL_ID,CONTACT_NUMBER,ADDRESS FROM dbo.USERS'
            del_query = 'DELETE FROM dbo.USERS WHERE USERNAME=? AND CONTACT_NUMBER =?'

            reply = QMessageBox.question(self,'Confirm Window', 'Are you sure to delete the user '+user_name+' ?', QMessageBox.Yes|QMessageBox.No)

            if reply == QMessageBox.Yes:

                cur.execute(del_query,del_data)
                connect.commit()

            self.display_records()
        else:
            QMessageBox.information(self,'Alert Window','Do not delete the ADMIN user. Please choose other user')

    def closebtn(self):
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Table_dialog = QtWidgets.QDialog()
    #ui = Ui_Table_dialog()
    #ui.setupUi(Table_dialog)
    #Table_dialog.show()
    ui=Add_Staff_Details()
    ui.show()
    sys.exit(app.exec_())
