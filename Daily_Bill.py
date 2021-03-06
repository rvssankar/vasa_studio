
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QComboBox,QTableWidgetItem,QMessageBox,QDateEdit
from PyQt5.QtCore import QDate,Qt
import os
import sys
import pyodbc
import datetime
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from Odbc_Connection import Add_Odbc_Connection



class Ui_Daily_bill(object):
    def setupUi(self, Daily_bill):
        Daily_bill.setObjectName("Daily_bill")
        Daily_bill.resize(1215, 809)
        Daily_bill.setStyleSheet("#Daily_bill{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.616915 rgba(115, 242, 115, 255), stop:1 rgba(218, 218, 218, 255))}")
        self.cust_det_frame = QtWidgets.QFrame(Daily_bill)
        self.cust_det_frame.setGeometry(QtCore.QRect(40, 158, 1151, 71))
        self.cust_det_frame.setStyleSheet("#cust_det_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:grey;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.045, x2:0.015, y2:0.0797727, stop:0.169154 rgba(138, 255, 215, 255), stop:1 rgba(189, 255, 218, 255))}")
        self.cust_det_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cust_det_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cust_det_frame.setObjectName("cust_det_frame")
        self.bill_label = QtWidgets.QLabel(self.cust_det_frame)
        self.bill_label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.bill_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:red;")
        self.bill_label.setObjectName("bill_label")
        self.bill_le = QtWidgets.QLineEdit(self.cust_det_frame)
        self.bill_le.setEnabled(False)
        self.bill_le.setGeometry(QtCore.QRect(90, 21, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bill_le.setFont(font)
        self.bill_le.setObjectName("bill_le")
        self.customer_label = QtWidgets.QLabel(self.cust_det_frame)
        self.customer_label.setGeometry(QtCore.QRect(404, 20, 161, 31))
        self.customer_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:red;")
        self.customer_label.setObjectName("customer_label")
        self.customer_le = QtWidgets.QLineEdit(self.cust_det_frame)
        self.customer_le.setGeometry(QtCore.QRect(574, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.customer_le.setFont(font)
        self.customer_le.setObjectName("customer_le")
        self.phone_label = QtWidgets.QLabel(self.cust_det_frame)
        self.phone_label.setGeometry(QtCore.QRect(840, 20, 121, 31))
        self.phone_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:red;")
        self.phone_label.setObjectName("phone_label")
        self.phone_le = QtWidgets.QLineEdit(self.cust_det_frame)
        self.phone_le.setGeometry(QtCore.QRect(940, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.phone_le.setFont(font)
        self.phone_le.setObjectName("phone_le")
        self.date_label = QtWidgets.QLabel(Daily_bill)
        self.date_label.setGeometry(QtCore.QRect(70, 95, 71, 31))
        self.date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.date_label.setObjectName("date_label")
        self.date_le = QtWidgets.QLineEdit(Daily_bill)
        self.date_le.setEnabled(False)
        self.date_le.setGeometry(QtCore.QRect(130, 97, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_le.setFont(font)
        self.date_le.setObjectName("date_le")
        self.delivery_date_label = QtWidgets.QLabel(Daily_bill)
        self.delivery_date_label.setGeometry(QtCore.QRect(778, 97, 151, 31))
        self.delivery_date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.delivery_date_label.setObjectName("delivery_date_label")
        self.table_frame = QtWidgets.QFrame(Daily_bill)
        self.table_frame.setGeometry(QtCore.QRect(40, 248, 1151, 531))
        self.table_frame.setStyleSheet("#table_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:grey}")
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.viewtable = QtWidgets.QTableWidget(self.table_frame)
        self.viewtable.setGeometry(QtCore.QRect(10, 10, 1131, 301))
        self.viewtable.setShowGrid(True)
        self.viewtable.setRowCount(0)
        self.viewtable.setObjectName("viewtable")
        self.viewtable.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.viewtable.setHorizontalHeaderItem(5, item)
        self.remove_btn = QtWidgets.QPushButton(self.table_frame)
        self.remove_btn.setGeometry(QtCore.QRect(20, 320, 101, 41))
        self.remove_btn.setStyleSheet("#remove_btn{background-color: rgb(202, 66, 68);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#remove_btn:pressed{border-style:solid;border-width:6px}"                                      )
        self.remove_btn.setObjectName("remove_btn")
        self.save_btn = QtWidgets.QPushButton(self.table_frame)
        self.save_btn.setGeometry(QtCore.QRect(20, 430, 111, 51))
        self.save_btn.setStyleSheet("#save_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#save_btn:pressed{border-style:solid;border-width:6px}"                                    )
        self.save_btn.setObjectName("save_btn")
        self.print_btn = QtWidgets.QPushButton(self.table_frame)
        self.print_btn.setGeometry(QtCore.QRect(160, 430, 111, 51))
        self.print_btn.setStyleSheet("#print_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(153, 228, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#print_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.print_btn.setObjectName("print_btn")
        self.clear_btn = QtWidgets.QPushButton(self.table_frame)
        self.clear_btn.setGeometry(QtCore.QRect(302, 430, 111, 51))
        self.clear_btn.setStyleSheet("#clear_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(240, 238, 74, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#clear_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.clear_btn.setObjectName("clear_btn")
        self.close_btn = QtWidgets.QPushButton(self.table_frame)
        self.close_btn.setGeometry(QtCore.QRect(442, 430, 111, 51))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#close_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.close_btn.setObjectName("close_btn")
        self.total_label = QtWidgets.QLabel(self.table_frame)
        self.total_label.setGeometry(QtCore.QRect(654, 343, 221, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_label.setObjectName("total_label")
        self.total_le = QtWidgets.QLineEdit(self.table_frame)
        self.total_le.setGeometry(QtCore.QRect(899, 350, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setObjectName("total_le")
        self.recieved_label = QtWidgets.QLabel(self.table_frame)
        self.recieved_label.setGeometry(QtCore.QRect(654, 403, 241, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.recieved_le = QtWidgets.QLineEdit(self.table_frame)
        self.recieved_le.setGeometry(QtCore.QRect(900, 410, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recieved_le.setFont(font)
        self.recieved_le.setObjectName("recieved_le")
        self.due_label = QtWidgets.QLabel(self.table_frame)
        self.due_label.setGeometry(QtCore.QRect(654, 463, 221, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.due_label.setObjectName("due_label")
        self.due_le = QtWidgets.QLineEdit(self.table_frame)
        self.due_le.setGeometry(QtCore.QRect(900, 470, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.due_le.setFont(font)
        self.due_le.setObjectName("due_le")
        self.line_2 = QtWidgets.QFrame(self.table_frame)
        self.line_2.setGeometry(QtCore.QRect(630, 323, 519, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.table_frame)
        self.line_3.setGeometry(QtCore.QRect(620, 332, 20, 197))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.new_row_btn = QtWidgets.QPushButton(self.table_frame)
        self.new_row_btn.setGeometry(QtCore.QRect(160, 320, 101, 41))
        self.new_row_btn.setStyleSheet("#new_row_btn{background-color: green;\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#new_row_btn:pressed{border-style:solid;border-width:6px}"                                       )
        self.new_row_btn.setObjectName("new_row_btn")
        self.cal_tool_btn = QtWidgets.QToolButton(Daily_bill)
        self.cal_tool_btn.setGeometry(QtCore.QRect(1159, 97, 30, 32))
        self.cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cal_tool_btn.setIcon(icon)
        self.cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.cal_tool_btn.setObjectName("cal_tool_btn")
        self.delivery_date_le = QtWidgets.QLineEdit(Daily_bill)
        self.delivery_date_le.setGeometry(QtCore.QRect(919, 98, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delivery_date_le.setFont(font)
        self.delivery_date_le.setObjectName("delivery_date_le")
        self.title_label = QtWidgets.QLabel(Daily_bill)
        self.title_label.setGeometry(QtCore.QRect(330, 10, 601, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("font: 75 22pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(0, 0, 127);\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.line = QtWidgets.QFrame(Daily_bill)
        self.line.setGeometry(QtCore.QRect(0, 54, 1211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Daily_bill)
        QtCore.QMetaObject.connectSlotsByName(Daily_bill)

    def retranslateUi(self, Daily_bill):
        _translate = QtCore.QCoreApplication.translate
        Daily_bill.setWindowTitle(_translate("Daily_bill", "Dialog"))
        self.bill_label.setText(_translate("Daily_bill", "Bill No :"))
        self.customer_label.setText(_translate("Daily_bill", "Customer Name :"))
        self.phone_label.setText(_translate("Daily_bill", "Phone No :"))
        self.date_label.setText(_translate("Daily_bill", "Date :"))
        self.delivery_date_label.setText(_translate("Daily_bill", "Delivery Date :"))
        item = self.viewtable.horizontalHeaderItem(0)
        item.setText(_translate("Daily_bill", "Sl.No"))
        item = self.viewtable.horizontalHeaderItem(1)
        item.setText(_translate("Daily_bill", "Category"))
        item = self.viewtable.horizontalHeaderItem(2)
        item.setText(_translate("Daily_bill", "Frame Size"))
        item = self.viewtable.horizontalHeaderItem(3)
        item.setText(_translate("Daily_bill", "Rate (Rs.)"))
        item = self.viewtable.horizontalHeaderItem(4)
        item.setText(_translate("Daily_bill", "Qty."))
        item = self.viewtable.horizontalHeaderItem(5)
        item.setText(_translate("Daily_bill", "Amount (Rs.)"))
        self.remove_btn.setText(_translate("Daily_bill", "Remove"))
        self.save_btn.setText(_translate("Daily_bill", "Save"))
        self.print_btn.setText(_translate("Daily_bill", "Print"))
        self.clear_btn.setText(_translate("Daily_bill", "Clear"))
        self.close_btn.setText(_translate("Daily_bill", "Close"))
        self.total_label.setText(_translate("Daily_bill", "Total Amount (Rs.)           :"))
        self.recieved_label.setText(_translate("Daily_bill", "Amount Recieved (Rs.)  :"))
        self.due_label.setText(_translate("Daily_bill", "Amount Due (Rs.)             :"))
        self.new_row_btn.setText(_translate("Daily_bill", "New Row"))
        self.title_label.setText(_translate("Daily_bill", "New Customer Bill"))



class Add_Daily_Bill(QDialog,Ui_Daily_bill):
    def __init__(self,parent=None):
        super(Add_Daily_Bill,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Daily Bill")

        self.onlyint = QtGui.QIntValidator()
        self.phone_le.setValidator(self.onlyint)
        self.bill_le.setValidator(self.onlyint)
        self.total_le.setValidator(self.onlyint)
        self.recieved_le.setValidator(self.onlyint)
        self.due_le.setValidator(self.onlyint)

        self.total_le.setEnabled(False)
        self.total_le.setText(str(0))

        self.due_le.setEnabled(False)
        self.due_le.setText(str(0))

        #self.recieved_le.setText(str(0))
        self.recieved_le.setPlaceholderText(str(0))
        self.recieved_le.textChanged.connect(self.amountdue)

        self.cal_tool_btn.clicked.connect(self.delivery_calender)
        self.new_row_btn.clicked.connect(self.newrowbtn)
        self.remove_btn.clicked.connect(self.deleterow)
        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)
        self.close_btn.clicked.connect(self.closebtn)
        self.print_btn.clicked.connect(self.printbill)

        self.total_le.textChanged.connect(self.amountdue)


        self.bill_generator()
        self.current_date()
        self.table_records()
        #self.connectdb()
        #self.totalamount()

        config_name = 'daily_bill.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)



        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")
        save_image = os.path.join(application_path, "images", "save.png")
        print_image = os.path.join(application_path, "images", "print.png")
        clear_image = os.path.join(application_path, "images", "clear.png")
        close_image = os.path.join(application_path, "images", "close.png")
        self.calender_image = os.path.join(application_path, "images", "calender.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        self.save_btn.setIcon(QtGui.QIcon(save_image))
        self.save_btn.setIconSize(QtCore.QSize(30,30))

        self.print_btn.setIcon(QtGui.QIcon(print_image))
        self.print_btn.setIconSize(QtCore.QSize(30, 30))

        self.clear_btn.setIcon(QtGui.QIcon(clear_image))
        self.clear_btn.setIconSize(QtCore.QSize(30, 30))

        self.close_btn.setIcon(QtGui.QIcon(close_image))
        self.close_btn.setIconSize(QtCore.QSize(30, 30))






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

    def table_records(self):
        self.viewtable.setRowCount(0)
        self.viewtable.verticalHeader().setVisible(False)
        header = self.viewtable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}");

        self.existingvaluechange()

        self.viewtable.itemChanged.connect(self.totalamount)



    def newrowbtn(self):
        self.combovalue()
        rowvalue = self.viewtable.rowCount()
        print('the row value is ',rowvalue)
        self.viewtable.insertRow(rowvalue)
        self.newrow()


    def newrow(self):

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo1.addItems(self.combolist)
        self.combo1.setCurrentText('NA')


        self.combo2.addItems(self.framelist)
        self.combo2.setCurrentText('NA')

        self.rowposition = self.viewtable.rowCount()-1
        print('The number of rows is ', self.rowposition)

        self.viewtable.setItem(self.rowposition,0,QTableWidgetItem(str(self.rowposition+1)))
        self.viewtable.setCellWidget(self.rowposition, 1, self.combo1)
        self.viewtable.setCellWidget(self.rowposition, 2, self.combo2)
        self.combo1.currentIndexChanged.connect(self.framecomboassign)
        self.combo1.currentIndexChanged.connect(self.ratevalue)
        #self.combo2.currentIndexChanged.connect(self.ratevalue)

        print('the value is ',self.combo1.currentText())
        if self.combo1.currentText() =='FRAME':
            self.combo2.setEnabled(True)
        else:
            self.combo2.setEnabled(False)

    def deleterow(self):
        rownum = self.viewtable.currentRow()
        print('the rownum is ',rownum)

        if rownum == -1:
            QMessageBox.warning(self,'Warning', 'Please select a row for delete')
        else:

            self.viewtable.removeRow(rownum)

            rowcount= self.viewtable.rowCount()

            print('the row number is ',rowcount)

            for i in range(rowcount):
                value =i+1
                print('the row numbers is ',i)
                rowvalue=QTableWidgetItem()
                rowvalue.setText(str(value))
                self.viewtable.setItem(i,0,rowvalue)

            total = 0
            for row in range(rowcount):
                rowvalue = float(self.viewtable.item(row, 5).text())
                total += rowvalue
            self.total_le.setText(str(total))


    def framecomboassign(self):
        rownum = self.viewtable.currentRow()
        print('The row number value is ',rownum)
        current_value = self.combo1.currentText()
        print(current_value)
        if current_value == 'FRAME':
            self.combo2.setEnabled(True)

        else:
            self.combo2.setEnabled(False)

    def ratevalue(self):
        rownum= self.viewtable.currentRow()
        curr_value = self.combo1.currentText()
        if curr_value != 'FRAME':
            SEL_QUERY =" SELECT PRICE from dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY' AND PROD_NAME =?"

            cur.execute(SEL_QUERY,curr_value)
            result = cur.fetchall()
            rate_value =str(result[0][0])
            rate_table = QTableWidgetItem()
            rate_table.setText(rate_value)
            rate_table.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.viewtable.setItem(rownum, 3, rate_table)



            self.viewtable.itemChanged.connect(self.amount_rate_calculation)


            print('the result value is ',rate_value)
            print(type(rate_value))
        else:

            self.combo2.currentIndexChanged.connect(self.frame_rate_value)


    def frame_rate_value(self):
            SEL_QUERY = "SELECT PRICE from dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY' AND PROD_NAME =? AND SIZE=?"
            frame_curr_value = self.combo2.currentText()
            curr_value = self.combo1.currentText()
            rownum = self.viewtable.currentRow()

            cur.execute(SEL_QUERY, (curr_value, frame_curr_value))
            result = cur.fetchall()
            rate_value = str(result[0][0])
            rate_table = QTableWidgetItem()
            rate_table.setText(rate_value)
            rate_table.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            self.viewtable.setItem(rownum, 3, rate_table)

            self.viewtable.itemChanged.connect(self.amount_rate_calculation)

    def amount_rate_calculation(self,item):
        rownum = item.row()
        colnum = item.column()

        print('the row number is ',rownum)

        print('the column number is ',colnum)

        if colnum ==4:
            rate_value = self.viewtable.item(rownum,3).text()
            print('the rate value is ',rate_value,' and its type is ',type(rate_value))

            qty_value  = self.viewtable.item(rownum,4).text()
            print('the qty value is ',qty_value)

            int_rate_value = int(rate_value)
            int_qty_value = int(qty_value)

            amount_value = int_rate_value*int_qty_value
            print('the amount value is',amount_value)
            amount_table = QTableWidgetItem()
            amount_table.setText(str(amount_value))
            amount_table.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

            self.viewtable.setItem(rownum,5,amount_table)

    def totalamount(self,item):
        self.total_le.setEnabled(False)
        if item.column() == 5:


            rowcount = self.viewtable.rowCount()

            if rowcount == 0:
                self.total_le.setText(str(0))

            else:
                total = 0
                for row in range(rowcount):
                    rowvalue = float(self.viewtable.item(row,5).text())
                    total+=rowvalue
                self.total_le.setText(str(total))

    def amountdue(self):
        print('Amount due function in')

        print("the test value is ",self.total_le.text())
        totalamount = float(self.total_le.text())
        if self.recieved_le.text()=="":
            Recievedamount = float(0)
        else:
            Recievedamount = float(self.recieved_le.text())
        print('Amount due is ', totalamount)
        print('amoint  recieved is ',Recievedamount)

        balance = float(totalamount-Recievedamount )

        print('The balanced amount is ',balance)

        self.due_le.setText(str(balance))

    def existingvaluechange(self):
        rownum = self.viewtable.cellWidget(0,1)
        print('The row number value is ', rownum)
        #print('The value in Row is ',self.viewtable.item(rownum,1))






    def combovalue(self):
        self.combolist = set()
        self.framelist =set()
        sel_query ="SELECT PROD_NAME from dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY'"
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

            x=i[0]
            self.combolist.add(x)
        self.combolist.add('NA')

        frame_query = "SELECT SIZE FROM dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY' AND PROD_NAME ='FRAME' AND SIZE IS NOT NULL AND SIZE !=''"

        cur.execute(frame_query)
        frame_result = cur.fetchall()


        for j in frame_result:
            x =j[0]
            self.framelist.add(x)
        self.framelist.add('NA')



    def bill_generator(self):
        sel_query ='SELECT MAX(BILL_NO) FROM dbo.BILLING_TABLE'
        self.connectdb()
        cur.execute(sel_query)
        result = cur.fetchall()
        value = result[0][0]

        if value != None:
            value = value+1
            print(value)
        else:
            value=1
            print('The else condition ',value)
            print(type(value))

        self.bill_le.setText(str(value))

    def current_date(self):
        now = QDate.currentDate()
        print(now)
        print(now.toString(Qt.ISODate))

        today = datetime.date.today()
        self.billdate = today.strftime("%d/%m/%Y")
        date_format = today.strftime("%d/%m/%Y %A")
        print(date_format)

        self.date_le.setText(date_format)

    def delivery_calender(self):
        self.calender = QCalendarWidget()
        self.calender.setMinimumDate(QDate(1900,1,1))
        self.calender.setMaximumDate(QDate(2999,12,31))
        self.calender.setGridVisible(True)
        self.calender.clicked.connect(self.updatedate)
        self.calender.setWindowModality(Qt.ApplicationModal)
        self.calender.setWindowTitle("Delivery Date")

        self.calender.setWindowIcon(QtGui.QIcon(self.calender_image))




        self.calender.show()


    def updatedate(self,*args):

        getdate = self.calender.selectedDate().toString("dd/MM/yyyy")
        print('get date value is ',getdate)
        self.delivery_date_le.setText(getdate)
        self.calender.deleteLater()

    def savebtn(self):

        if self.customer_le.text() =='' or self.phone_le.text()=='':
            QMessageBox.warning(self,'Warning','Please enter the customer information')
        elif self.viewtable.rowCount() ==0:
            QMessageBox.warning(self,'Warning','Please add the bill entry')

        else:
            billno = self.bill_le.text()
            orderdate = datetime.datetime.now().date()


            print('the order date value is ',orderdate,' and type is ',type(orderdate))

            customername = self.customer_le.text()
            phoneno = self.phone_le.text()
            totalamount = self.total_le.text()
            if self.recieved_le.text()=="":
                amountreceived =0
            else:
                amountreceived = self.recieved_le.text()

            dueamount = self.due_le.text()
            deliverydate = self.delivery_date_le.text()

            phoneno = int(phoneno)
            #orderdate =
            #orderdate = datetime.datetime.strptime(orderdate,'%d/%m/%Y').date()
            #orderdate= datetime.date.today()
            print('The order date is ',orderdate ,' and type is ', type(orderdate))
            totalamount= float(totalamount)
            amountreceived=float(amountreceived)
            dueamount=float(dueamount)
            billno =int(billno)

            bill_type ='DAILY'

            if deliverydate != '':

                deliverydate = datetime.datetime.strptime(deliverydate,'%d/%m/%Y').date()
            else:
                deliverydate = datetime.date(9999,12,31)

            print('the deliver date value is ', deliverydate, ' and type is ', type(deliverydate))

            sql_order_date = orderdate.strftime("%d/%m/%Y")
            sql_delivery_date = deliverydate.strftime("%d/%m/%Y")

            ins_query = 'INSERT INTO dbo.BILLING_TABLE VALUES(?,?,?,?,?,?,?,?,?,?)'
            ins_query1 = "INSERT INTO dbo.BILLING_TABLE (BILL_NO,CUSTOMER_NAME,PHONE_NO,BILLING_DATE,DELIVERY_DATE,TOTAL_AMOUNT) VALUES(?,?,?,?,?,?)"
            data = (billno,customername,phoneno,orderdate,deliverydate,totalamount,amountreceived,dueamount,None,bill_type)
            data1 = (billno, customername, phoneno, orderdate,deliverydate, totalamount)

            cur.execute(ins_query,data)
            connect.commit()
            connect.close()



            # order details in order_table:

            max_order_id_query = " SELECT MAX(ORDER_ID) FROM DBO.ORDER_DETAILS"
            self.connectdb()
            cur.execute(max_order_id_query)
            result = cur.fetchall()
            order_value = result[0][0]

            if order_value != None:
                order_value = order_value + 1
                print("The order_id Value is ",order_value)
            else:
                order_value = 1
                print('The new Order Id value is ', order_value)
                print(type(order_value))



            category_list =[self.viewtable.cellWidget(row,1).currentText() for row in range(self.viewtable.rowCount())]
            frame_size_list = [self.viewtable.cellWidget(row,2).currentText() for row in range(self.viewtable.rowCount())]
            rate_list = [self.viewtable.item(row,3).text() for row in range(self.viewtable.rowCount())]
            qty_list = [self.viewtable.item(row,4).text() for row in range(self.viewtable.rowCount())]
            amount_list =[self.viewtable.item(row,5).text() for row in range(self.viewtable.rowCount())]

            print('the category values are',category_list)
            print('the frame values are', frame_size_list)
            print('the rate values are', rate_list)
            print('the qty values are', qty_list)
            print('the amount values are', amount_list)

            # finding Prd_id
            prd_id_list =[]

            for category , frame in zip(category_list,frame_size_list):
                if category != 'FRAME':
                    prd_select_query = "SELECT PROD_ID FROM dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY' AND PROD_NAME =?"
                    cur.execute(prd_select_query,category)
                    result = cur.fetchall()
                    print('the result value is ',result[0][0])
                    prd_id_list.append(result[0][0])
                else:
                    prd_select_query= "SELECT PROD_ID FROM dbo.PROD_DETAILS WHERE PROD_TYPE ='DAILY' AND PROD_NAME ='FRAME' AND SIZE =?"
                    cur.execute(prd_select_query,frame)
                    result=cur.fetchall()
                    prd_id_list.append(result[0][0])

            print( "The PRD_ID list values are ",prd_id_list)

            # insert data into ORDER_DETAILS table:

            for prd_id ,category,size,rate,qty,amount in zip(prd_id_list,category_list,frame_size_list,rate_list,qty_list,amount_list):
                insert_qry_order_table = "INSERT INTO dbo.ORDER_DETAILS VALUES (?,?,?,?,?,?,?,?)"
                cur.execute(insert_qry_order_table,(order_value,billno,prd_id,category,size,rate,qty,amount))

            connect.commit()
            connect.close()

            self.billno = billno
            self.customer_name = customername
            self.phone_number =phoneno
            self.total_amount =totalamount
            self.amount_recieved =amountreceived
            self.due_amount =dueamount
            self.prod_details =category_list
            self.prod_size =frame_size_list
            self.qty_list =qty_list
            self.amount_list =amount_list

            QMessageBox.information(self, 'Message', 'Data saved successfully')
            self.save_btn.setEnabled(False)


    def clearbtn(self):
        columns_list =[self.customer_le,self.phone_le,self.delivery_date_le]

        for i in columns_list:
            i.clear()

        self.viewtable.setRowCount(0)

        self.total_le.setText(str(0))
        print("the clearbtn total amt value is ",self.total_le.text())
        self.recieved_le.setText(str(0))
        self.due_le.setText(str(0))

    def closebtn(self):

        self.close()

    def billcontent(self):
        folder_path ="D:\\Python\\Project\\bills\\"
        timenow = datetime.datetime.now()
        year = str(timenow.year)
        month = timenow.strftime("%B")
        print("the year is", year)
        print("the month is ", month)
        time = str(timenow.strftime("%H-%M"))
        footer_time = str(timenow.strftime("%I:%M %p"))
        print("the footer time is ", footer_time)
        today = datetime.date.today()

        bill_number = str(self.billno)
        cust_name = self.customer_name
        place = 'Mannargudi'
        lines ="\n===================================================================="
        today_date = today.strftime("%d/%m/%Y")

        product = self.prod_details
        size = self.prod_size
        qty = self.qty_list
        amount = self.amount_list
        total_amount = self.total_amount
        amount_paid = self.amount_recieved
        amount_due = self.due_amount

        print("the time is ", time, " and the format is ", type(time))

        folder = folder_path+year+"\\"+month+"\\"+str(today) + '\\'
        filename = str(folder) + "Daily_Bill_" + str(time) + ".rtf"


        print("the file name is ", filename)

        if not os.path.exists(folder):
            os.makedirs(folder)

        file = open(filename, 'w+')

        # file = open('D:/Python/bills/2019-12-30/Daily_Bill_16:49:50.docx','w+')

        # file =open('C:\\bill\\Daily_Bill.rtf','w')

        header = "\n\n\t\t\t\t VASA PHOTOGRAPHY"
        address1 = "\n\t\t\t   No.100, Balakrishna Nagar,"
        address2 = "\n\t\t\t\tKeerthi Clinic [opp],"
        address3 = "\n\t\t\t\t Mannargudi -614001"
        address4 = "\n\n Phone: 9944332270"
        address5 = "\t\t\t\tEmail: vasaclicks@gmail.com"
        title = "\n\n\t\t\t\t\t\"CASH BILL\"\n===================================================================="
        bill_section = "\n\n Bill No\t: " + bill_number + "\t\t\t\tName  : " + cust_name
        bill_section2 = "\n Date\t\t: " + today_date + "\t\t\tAddr  : " + place + "\n\n===================================================================="
        table_header = "\n SL.No\tPRODUCT\t\t\tSIZE\t\tQTY\t\tAMOUNT\n===================================================================="

        final = header + address1 + address2 + address3 + address4 + address5 + title + bill_section + bill_section2 + table_header
        file.write(final)

        slno = 1
        table_data=''

        for prd, size, qty, amt in zip(product, size, qty, amount):
            if len(prd) < 6 and prd != 'FRAME':
                table_value = "\n   " + str(slno) + "\t\t" + prd + "\t\t\t\t" + size + "\t\t" + str(qty) + "\t\t" + str(
                    amt)
                file.write(table_value)
            elif len(prd) > 5 and prd != 'FRAME':
                table_value = "\n   " + str(slno) + "\t\t" + prd + "\t\t\t" + size + "\t\t" + str(qty) + "\t\t" + str(
                    amt)
                file.write(table_value)
            elif prd == 'FRAME' and len(size) > 5:
                table_value = "\n   " + str(slno) + "\t\t" + prd + "\t\t\t\t" + size + "\t" + str(qty) + "\t\t" + str(
                    amt)
                file.write(table_value)
            else:
                table_value = "\n   " + str(slno) + "\t\t" + prd + "\t\t\t\t" + size + "\t\t" + str(qty) + "\t\t" + str(
                    amt)
                file.write(table_value)
            slno += 1
            table_data =table_data+table_value
        file.write(lines)

        footer1 = "\n\n  TIME  :" + footer_time + "\t\t\t\t\tSUB TOTAL\t:\t" + str(float(total_amount))
        footer2 = "\n\t\t\t\t\t\t\tAMT.PAID\t:\t" + str(float(amount_paid))
        footer3 = "\n  SIGN  :\t\t\t\t\t\tAMT.DUE\t:\t" + str(float(amount_due))

        footer_final = footer1 + footer2 + footer3

        file.write(footer_final)
        file.write(lines)

        message = "\n\t\t*** THANK YOU... PLEASE VISIT US AGAIN ***"
        file.write(message)

        self.file_name =filename

        file.close()

    def printbill(self):
        print("the save btn status is ",self.save_btn.isEnabled())
        if not self.save_btn.isEnabled():
            self.billcontent()
            os.startfile(self.file_name,'print')
        else:
            QMessageBox.warning(self,'Warning','Please save the data first before printing the bill.')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Daily_bill = QtWidgets.QDialog()
    #ui = Ui_Daily_bill()
    #ui.setupUi(Daily_bill)
    #Daily_bill.show()
    ui = Add_Daily_Bill()
    ui.show()
    sys.exit(app.exec_())

