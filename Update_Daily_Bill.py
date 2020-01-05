from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QComboBox,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import QDate,Qt
import os
import pyodbc
import datetime


class Ui_Update_Daily_bill(object):
    def setupUi(self, Update_Daily_bill):
        Update_Daily_bill.setObjectName("Update_Daily_bill")
        Update_Daily_bill.resize(1215, 809)
        Update_Daily_bill.setStyleSheet("#Update_Daily_bill{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.179104 rgba(62, 94, 125, 255), stop:0.661692 rgba(161, 255, 255, 255));}")
        self.cust_det_frame = QtWidgets.QFrame(Update_Daily_bill)
        self.cust_det_frame.setGeometry(QtCore.QRect(40, 131, 1151, 71))
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
        self.bill_le.setEnabled(True)
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
        self.date_label = QtWidgets.QLabel(Update_Daily_bill)
        self.date_label.setGeometry(QtCore.QRect(70, 90, 71, 31))
        self.date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.date_label.setObjectName("date_label")
        self.date_le = QtWidgets.QLineEdit(Update_Daily_bill)
        self.date_le.setEnabled(False)
        self.date_le.setGeometry(QtCore.QRect(130, 92, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_le.setFont(font)
        self.date_le.setObjectName("date_le")
        self.delivery_date_label = QtWidgets.QLabel(Update_Daily_bill)
        self.delivery_date_label.setGeometry(QtCore.QRect(778, 92, 151, 31))
        self.delivery_date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.delivery_date_label.setObjectName("delivery_date_label")
        self.table_frame = QtWidgets.QFrame(Update_Daily_bill)
        self.table_frame.setGeometry(QtCore.QRect(40, 211, 1151, 581))
        self.table_frame.setStyleSheet("#table_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:grey}")
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.viewtable = QtWidgets.QTableWidget(self.table_frame)
        self.viewtable.setGeometry(QtCore.QRect(10, 12, 1131, 301))
        self.viewtable.setShowGrid(True)
        self.viewtable.setRowCount(0)
        self.viewtable.setObjectName("viewtable")
        self.viewtable.setColumnCount(0)
        self.save_btn = QtWidgets.QPushButton(self.table_frame)
        self.save_btn.setGeometry(QtCore.QRect(70, 353, 141, 71))
        self.save_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.save_btn.setObjectName("save_btn")
        self.print_btn = QtWidgets.QPushButton(self.table_frame)
        self.print_btn.setGeometry(QtCore.QRect(420, 353, 141, 71))
        self.print_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(153, 228, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.print_btn.setObjectName("print_btn")
        self.delete_btn = QtWidgets.QPushButton(self.table_frame)
        self.delete_btn.setGeometry(QtCore.QRect(70, 463, 141, 71))
        self.delete_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(240, 238, 74, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.delete_btn.setObjectName("delete_btn")
        self.close_btn = QtWidgets.QPushButton(self.table_frame)
        self.close_btn.setGeometry(QtCore.QRect(420, 463, 141, 71))
        self.close_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.close_btn.setObjectName("close_btn")
        self.total_label = QtWidgets.QLabel(self.table_frame)
        self.total_label.setGeometry(QtCore.QRect(654, 322, 221, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_label.setObjectName("total_label")
        self.total_le = QtWidgets.QLineEdit(self.table_frame)
        self.total_le.setEnabled(False)
        self.total_le.setGeometry(QtCore.QRect(899, 329, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setObjectName("total_le")
        self.recieved_label = QtWidgets.QLabel(self.table_frame)
        self.recieved_label.setGeometry(QtCore.QRect(654, 369, 241, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.recieved_le = QtWidgets.QLineEdit(self.table_frame)
        self.recieved_le.setEnabled(False)
        self.recieved_le.setGeometry(QtCore.QRect(900, 376, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recieved_le.setFont(font)
        self.recieved_le.setObjectName("recieved_le")
        self.due_label = QtWidgets.QLabel(self.table_frame)
        self.due_label.setGeometry(QtCore.QRect(654, 419, 221, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.due_label.setObjectName("due_label")
        self.due_le = QtWidgets.QLineEdit(self.table_frame)
        self.due_le.setEnabled(False)
        self.due_le.setGeometry(QtCore.QRect(900, 426, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.due_le.setFont(font)
        self.due_le.setObjectName("due_le")
        self.line_2 = QtWidgets.QFrame(self.table_frame)
        self.line_2.setGeometry(QtCore.QRect(630, 312, 519, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.table_frame)
        self.line_3.setGeometry(QtCore.QRect(620, 321, 20, 261))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pay_le = QtWidgets.QLineEdit(self.table_frame)
        self.pay_le.setGeometry(QtCore.QRect(899, 482, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pay_le.setFont(font)
        self.pay_le.setText("")
        self.pay_le.setObjectName("pay_le")
        self.pay_label = QtWidgets.QLabel(self.table_frame)
        self.pay_label.setGeometry(QtCore.QRect(653, 475, 221, 41))
        self.pay_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.pay_label.setObjectName("pay_label")
        self.balance_label = QtWidgets.QLabel(self.table_frame)
        self.balance_label.setGeometry(QtCore.QRect(654, 529, 221, 41))
        self.balance_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.balance_label.setObjectName("balance_label")
        self.balance_le = QtWidgets.QLineEdit(self.table_frame)
        self.balance_le.setEnabled(False)
        self.balance_le.setGeometry(QtCore.QRect(900, 536, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.balance_le.setFont(font)
        self.balance_le.setText("")
        self.balance_le.setObjectName("balance_le")
        self.line_4 = QtWidgets.QFrame(self.table_frame)
        self.line_4.setGeometry(QtCore.QRect(630, 462, 519, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.table_frame)
        self.line_5.setGeometry(QtCore.QRect(630, 513, 519, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.delivery_date_le = QtWidgets.QLineEdit(Update_Daily_bill)
        self.delivery_date_le.setGeometry(QtCore.QRect(919, 93, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delivery_date_le.setFont(font)
        self.delivery_date_le.setObjectName("delivery_date_le")
        self.title_label = QtWidgets.QLabel(Update_Daily_bill)
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
        self.line = QtWidgets.QFrame(Update_Daily_bill)
        self.line.setGeometry(QtCore.QRect(0, 71, 1211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.cal_tool = QtWidgets.QToolButton(Update_Daily_bill)
        self.cal_tool.setGeometry(QtCore.QRect(1160, 93, 30, 32))
        self.cal_tool.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cal_tool.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cal_tool.setIcon(icon)
        self.cal_tool.setIconSize(QtCore.QSize(30, 30))
        self.cal_tool.setObjectName("cal_tool")

        self.retranslateUi(Update_Daily_bill)
        QtCore.QMetaObject.connectSlotsByName(Update_Daily_bill)

    def retranslateUi(self, Update_Daily_bill):
        _translate = QtCore.QCoreApplication.translate
        Update_Daily_bill.setWindowTitle(_translate("Update_Daily_bill", "Dialog"))
        self.bill_label.setText(_translate("Update_Daily_bill", "Bill No :"))
        self.customer_label.setText(_translate("Update_Daily_bill", "Customer Name :"))
        self.phone_label.setText(_translate("Update_Daily_bill", "Phone No :"))
        self.date_label.setText(_translate("Update_Daily_bill", "Date :"))
        self.delivery_date_label.setText(_translate("Update_Daily_bill", "Delivery Date :"))
        self.save_btn.setText(_translate("Update_Daily_bill", "Save"))
        self.print_btn.setText(_translate("Update_Daily_bill", "Print"))
        self.delete_btn.setText(_translate("Update_Daily_bill", "Delete"))
        self.close_btn.setText(_translate("Update_Daily_bill", "Close"))
        self.total_label.setText(_translate("Update_Daily_bill", "Total Amount (Rs.)           :"))
        self.recieved_label.setText(_translate("Update_Daily_bill", "Amount Recieved (Rs.)  :"))
        self.due_label.setText(_translate("Update_Daily_bill", "Amount Due (Rs.)             :"))
        self.pay_label.setText(_translate("Update_Daily_bill", "Amount Pay (Rs.)              :"))
        self.balance_label.setText(_translate("Update_Daily_bill", "Balance Amt. (Rs.)           :"))
        self.title_label.setText(_translate("Update_Daily_bill", "Update Customer Bill"))

class Update_Daily_Bill(QDialog,Ui_Update_Daily_bill):
    def __init__(self,parent=None):
        super(Update_Daily_Bill, self).__init__(parent)
        self.setupUi(self)

        self.onlyint = QtGui.QIntValidator()
        self.phone_le.setValidator(self.onlyint)
        self.bill_le.setValidator(self.onlyint)
        self.total_le.setValidator(self.onlyint)
        self.recieved_le.setValidator(self.onlyint)
        self.due_le.setValidator(self.onlyint)
        self.pay_le.setValidator(self.onlyint)
        self.balance_le.setValidator(self.onlyint)

        self.pay_le.setPlaceholderText(str(0))
        self.cal_tool.clicked.connect(self.delivery_calender)
        self.save_btn.clicked.connect(self.savebtn)

        self.pay_le.textChanged.connect(self.amountdue)
        self.current_date()
        self.connectdb()



        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Tab),self.bill_le, context=QtCore.Qt.WidgetWithChildrenShortcut, activated =self.bill_value_fetch)

    def connectdb(self):
        global cur
        global connect

        connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur

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

        self.calender.show()

    def updatedate(self,*args):

        getdate = self.calender.selectedDate().toString("dd/MM/yyyy")
        print('get date value is ',getdate)
        self.delivery_date_le.setText(getdate)
        self.calender.deleteLater()

    def table_records(self):
        self.viewtable.setRowCount(0)
        self.viewtable.setColumnCount(7)
        header_label = ['Sl.No', 'Category', 'Size', 'Rate', 'Qty', 'Amount', 'Date']
        self.viewtable.verticalHeader().setVisible(False)
        self.viewtable.setHorizontalHeaderLabels(header_label)
        for i in range(0,7):
            self.viewtable.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter)
        header = self.viewtable.horizontalHeader()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        header.setFont(font)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def bill_value_fetch(self):
        print("This function get passed")
        bill_no = self.bill_le.text()
        print('The bill no is ',bill_no)
        self.table_records()

        select_query = "SELECT ORD.CATEGORY,ORD.SIZE,ORD.RATE,ORD.QTY,ORD.TOTAL_AMOUNT,BILL.BILLING_DATE,\
                        BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,BILL.AMOUNT_DUE\
                        FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL ON\
                        ORD.BILL_NO = BILL.BILL_NO\
                        AND BILL.BILL_NO = ? "
        cur.execute(select_query,bill_no)

        result = cur.fetchall()

        new_result =[]

        for i in range(len(result)):
            tuple_value = result[i]
            tuple_value =list(tuple_value)
            tuple_value[5] = tuple_value[5].strftime('%d/%m/%Y')
            tuple_value =[ str(value)for value in tuple_value if type(value)!='str']
            print('the modified tuple value is ', tuple_value)
            new_result.append(tuple_value)

        print('The new result value is ',new_result)

        print ("the length is ",len(new_result))
        print("the column range is ",range(self.viewtable.columnCount()))
        print("the row range is ", range(len(new_result)))
        for row in range(0,len(new_result)):
            self.viewtable.insertRow(row)
            self.viewtable.setItem(row,0,self.table_item(str(row+1),Qt.ItemIsSelectable | Qt.ItemIsEnabled))
            for column in range(1,self.viewtable.columnCount()):
                print(' the result value for '+str(row-1)+ ' and ' +str(column)+ ' is ', new_result[(row-1)][(column-1)])
                value =new_result[(row-1)][(column-1)]
                print ('the value is ',value, ' and type is ',type(value))
                self.viewtable.setItem(row, column, self.table_item(value,Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                print ('The value inserted in row ',row,' and column ',column,' is :',new_result[(row-1)][(column-1)])

        bill_select_query = "SELECT CUSTOMER_NAME,PHONE_NO,DELIVERY_DATE FROM \
                            dbo.BILLING_TABLE WHERE BILL_TYPE='DAILY' AND BILL_NO =?"

        cur.execute(bill_select_query,bill_no)

        bill_result = cur.fetchall()

        print(" The bill result value is",bill_result)
        bill_tuple_list =list(bill_result[0])
        print("the new bill result is ",bill_tuple_list)
        bill_tuple_list[2]=bill_tuple_list[2].strftime('%d/%m/%Y')
        bill_tuple_list = [ str(data) for data in bill_tuple_list if type(data)!= 'str']
        print ("the new value for bill list is ",bill_tuple_list)

        db_total_amount = new_result[0][6]
        db_amount_recieved =new_result[0][7]
        db_amount_due =new_result[0][8]
        db_customer_name = bill_tuple_list[0]
        db_phone_no = bill_tuple_list[1]
        db_delivery_date = bill_tuple_list[2]

        self.total_le.setText(db_total_amount)
        self.recieved_le.setText(db_amount_recieved)
        self.due_le.setText(db_amount_due)
        self.customer_le.setText(db_customer_name)
        self.phone_le.setText(db_phone_no)
        self.delivery_date_le.setText(db_delivery_date)


    def table_item(self,text,flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def amountdue(self):

        print('Amount due function in')

        print("the test value is ",self.due_le.text())
        amount_due = float(self.due_le.text())
        if self.pay_le.text()=="":
            Recievedamount = float(0)
        else:
            Recievedamount = float(self.pay_le.text())
        print('Amount due is ', amount_due)
        print('amount  recieved is ',Recievedamount)

        balance = float(amount_due-Recievedamount )

        print('The balanced amount is ',balance)

        self.balance_le.setText(str(balance))

    def savebtn(self):
        billno = int(self.bill_le.text())
        customer_name = self.customer_le.text()
        phone_no = self.phone_le.text()
        delivery_date =self.delivery_date_le.text()
        amount_paid_now = self.pay_le.text()
        amount_recieved_prev = int(float(self.recieved_le.text()))

        print ('amount paid now is ',amount_paid_now)
        print('amount paid previous is ', amount_recieved_prev)

        amount_recieved = int(amount_recieved_prev + int(amount_paid_now))

        print('amount received sum is',amount_recieved)

        amount_due = float(self.balance_le.text())
        int_phone_no = int(phone_no)

        delivery_date = datetime.datetime.strptime(delivery_date,'%d/%m/%Y').date()
        int_amount_due = int(amount_due)

        update_query ="UPDATE dbo.BILLING_TABLE SET CUSTOMER_NAME =?,PHONE_NO =?,DELIVERY_DATE =?,\
                        AMOUNT_RECIEVED=?,AMOUNT_DUE=? WHERE BILL_NO =? AND BILL_TYPE='DAILY'"
        update_data = [customer_name,int_phone_no,delivery_date,amount_recieved,int_amount_due,billno]
        print("the update data is ",update_data)

        cur.execute(update_query,update_data)

        connect.commit()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_Daily_bill = QtWidgets.QDialog()
    #ui = Ui_Update_Daily_bill()
    #ui.setupUi(Update_Daily_bill)
    #Update_Daily_bill.show()
    ui = Update_Daily_Bill()
    ui.show()
    sys.exit(app.exec_())
