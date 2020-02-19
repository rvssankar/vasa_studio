from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate,Qt
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QMessageBox
import os
import pyodbc
import datetime


class Ui_new_function(object):
    def setupUi(self, new_function):
        new_function.setObjectName("new_function")
        new_function.resize(1055, 877)
        new_function.setStyleSheet("#new_function{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 114, 125, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.title_label = QtWidgets.QLabel(new_function)
        self.title_label.setGeometry(QtCore.QRect(210, 10, 601, 51))
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
        self.line = QtWidgets.QFrame(new_function)
        self.line.setGeometry(QtCore.QRect(0, 70, 1051, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.date_le = QtWidgets.QLineEdit(new_function)
        self.date_le.setEnabled(False)
        self.date_le.setGeometry(QtCore.QRect(790, 99, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.date_le.setFont(font)
        self.date_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.date_le.setObjectName("date_le")
        self.date_label = QtWidgets.QLabel(new_function)
        self.date_label.setGeometry(QtCore.QRect(690, 100, 91, 31))
        self.date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.date_label.setObjectName("date_label")
        self.table_frame = QtWidgets.QFrame(new_function)
        self.table_frame.setGeometry(QtCore.QRect(110, 160, 741, 701))
        self.table_frame.setStyleSheet("#table_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:grey;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 21, 235, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"border-radius:25px;\n"
"border-width:5px;\n"
"border-color:brown;\n"
"}")
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.bill_le = QtWidgets.QLineEdit(self.table_frame)
        #self.bill_le.setEnabled(False)
        self.bill_le.setGeometry(QtCore.QRect(370, 32, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bill_le.setFont(font)
        self.bill_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.bill_le.setObjectName("bill_le")
        self.bill_label = QtWidgets.QLabel(self.table_frame)
        self.bill_label.setGeometry(QtCore.QRect(130, 30, 221, 41))
        self.bill_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.bill_label.setObjectName("bill_label")
        self.customer_label = QtWidgets.QLabel(self.table_frame)
        self.customer_label.setGeometry(QtCore.QRect(131, 83, 221, 41))
        self.customer_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.customer_label.setObjectName("customer_label")
        self.customer_le = QtWidgets.QLineEdit(self.table_frame)
        self.customer_le.setGeometry(QtCore.QRect(370, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.customer_le.setFont(font)
        self.customer_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.customer_le.setObjectName("customer_le")
        self.function_label = QtWidgets.QLabel(self.table_frame)
        self.function_label.setGeometry(QtCore.QRect(130, 190, 221, 41))
        self.function_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.function_label.setObjectName("function_label")
        self.phone_label = QtWidgets.QLabel(self.table_frame)
        self.phone_label.setGeometry(QtCore.QRect(131, 140, 221, 41))
        self.phone_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.phone_label.setObjectName("phone_label")
        self.phone_le = QtWidgets.QLineEdit(self.table_frame)
        self.phone_le.setGeometry(QtCore.QRect(370, 147, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.phone_le.setFont(font)
        self.phone_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.phone_le.setObjectName("phone_le")
        self.booking_label = QtWidgets.QLabel(self.table_frame)
        self.booking_label.setGeometry(QtCore.QRect(131, 307, 221, 41))
        self.booking_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.booking_label.setObjectName("booking_label")
        self.booking_le = QtWidgets.QLineEdit(self.table_frame)
        self.booking_le.setGeometry(QtCore.QRect(370, 314, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.booking_le.setFont(font)
        self.booking_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.booking_le.setObjectName("booking_le")
        self.total_label = QtWidgets.QLabel(self.table_frame)
        self.total_label.setGeometry(QtCore.QRect(131, 367, 221, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.total_label.setObjectName("total_label")
        self.total_le = QtWidgets.QLineEdit(self.table_frame)
        self.total_le.setGeometry(QtCore.QRect(370, 374, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.total_le.setObjectName("total_le")
        self.recieved_label = QtWidgets.QLabel(self.table_frame)
        self.recieved_label.setGeometry(QtCore.QRect(131, 480, 221, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.recieved_le = QtWidgets.QLineEdit(self.table_frame)
        self.recieved_le.setGeometry(QtCore.QRect(370, 487, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.recieved_le.setFont(font)
        self.recieved_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.recieved_le.setObjectName("recieved_le")
        self.package_label = QtWidgets.QLabel(self.table_frame)
        self.package_label.setGeometry(QtCore.QRect(130, 246, 221, 41))
        self.package_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.package_label.setObjectName("package_label")
        self.close_btn = QtWidgets.QPushButton(self.table_frame)
        self.close_btn.setGeometry(QtCore.QRect(520, 600, 131, 71))
        self.close_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.close_btn.setObjectName("close_btn")
        self.clear_btn = QtWidgets.QPushButton(self.table_frame)
        self.clear_btn.setGeometry(QtCore.QRect(360, 600, 121, 71))
        self.clear_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(240, 238, 74, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.clear_btn.setObjectName("clear_btn")
        self.print_btn = QtWidgets.QPushButton(self.table_frame)
        self.print_btn.setGeometry(QtCore.QRect(198, 600, 131, 71))
        self.print_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(153, 228, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.print_btn.setObjectName("print_btn")
        self.save_btn = QtWidgets.QPushButton(self.table_frame)
        self.save_btn.setGeometry(QtCore.QRect(40, 600, 121, 71))
        self.save_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.save_btn.setObjectName("save_btn")
        self.cal_tool_btn = QtWidgets.QToolButton(self.table_frame)
        self.cal_tool_btn.setGeometry(QtCore.QRect(578, 318, 31, 31))
        self.cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cal_tool_btn.setIcon(icon)
        self.cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.cal_tool_btn.setObjectName("cal_tool_btn")
        self.function_le = QtWidgets.QLineEdit(self.table_frame)
        self.function_le.setEnabled(False)
        self.function_le.setGeometry(QtCore.QRect(370, 199, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.function_le.setFont(font)
        self.function_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.function_le.setObjectName("function_le")
        self.package_le = QtWidgets.QLineEdit(self.table_frame)
        self.package_le.setEnabled(False)
        self.package_le.setGeometry(QtCore.QRect(370, 256, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.package_le.setFont(font)
        self.package_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.package_le.setObjectName("package_le")
        self.paid_le = QtWidgets.QLineEdit(self.table_frame)
        self.paid_le.setGeometry(QtCore.QRect(369, 431, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.paid_le.setFont(font)
        self.paid_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.paid_le.setText("")
        self.paid_le.setObjectName("paid_le")
        self.paid_label = QtWidgets.QLabel(self.table_frame)
        self.paid_label.setGeometry(QtCore.QRect(130, 424, 221, 41))
        self.paid_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.paid_label.setObjectName("paid_label")
        self.due_label = QtWidgets.QLabel(new_function)
        self.due_label.setGeometry(QtCore.QRect(241, 700, 221, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.due_label.setObjectName("due_label")
        self.due_le = QtWidgets.QLineEdit(new_function)
        self.due_le.setEnabled(False)
        self.due_le.setGeometry(QtCore.QRect(480, 707, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.due_le.setFont(font)
        self.due_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.due_le.setObjectName("due_le")

        self.retranslateUi(new_function)
        QtCore.QMetaObject.connectSlotsByName(new_function)

    def retranslateUi(self, new_function):
        _translate = QtCore.QCoreApplication.translate
        new_function.setWindowTitle(_translate("new_function", "Dialog"))
        self.title_label.setText(_translate("new_function", "Update Function Bill"))
        self.date_label.setText(_translate("new_function", "Bill Date :"))
        self.bill_label.setText(_translate("new_function", "Bill No                                 :"))
        self.customer_label.setText(_translate("new_function", "Customer Name           :"))
        self.function_label.setText(_translate("new_function", "Function Name             :"))
        self.phone_label.setText(_translate("new_function", "Phone No                          :"))
        self.booking_label.setText(_translate("new_function", "Booking Date                 :"))
        self.total_label.setText(_translate("new_function", "Total Amount (Rs.)     :"))
        self.recieved_label.setText(_translate("new_function", "Amt. Recieved (Rs.)   :"))
        self.package_label.setText(_translate("new_function", "Package Name              :"))
        self.close_btn.setText(_translate("new_function", "Close"))
        self.clear_btn.setText(_translate("new_function", "Clear"))
        self.print_btn.setText(_translate("new_function", "Print"))
        self.save_btn.setText(_translate("new_function", "Save"))
        self.paid_label.setText(_translate("new_function", "Amt. Paid(Rs.)               :"))
        self.due_label.setText(_translate("new_function", "Amount Due (Rs.)       :"))

class Update_Function_Bill(QDialog,Ui_new_function):
    def __init__(self,parent=None):
        super(Update_Function_Bill, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Update Function Bill")

        self.onlyint = QtGui.QIntValidator()
        self.phone_le.setValidator(self.onlyint)
        self.bill_le.setValidator(self.onlyint)
        self.total_le.setValidator(self.onlyint)
        self.recieved_le.setValidator(self.onlyint)
        self.due_le.setValidator(self.onlyint)
        self.paid_le.setValidator(self.onlyint)

        self.paid_le.setPlaceholderText(str(0))
        self.cal_tool_btn.clicked.connect(self.delivery_calender)
        self.recieved_le.textChanged.connect(self.amountdue)

        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)
        self.close_btn.clicked.connect(self.closebtn)
        self.print_btn.clicked.connect(self.printbill)

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

    def delivery_calender(self):
        self.calender = QCalendarWidget()
        self.calender.setMinimumDate(QDate(1900,1,1))
        self.calender.setMaximumDate(QDate(2999,12,31))
        self.calender.setGridVisible(True)
        self.calender.clicked.connect(self.updatedate)
        self.calender.setWindowModality(Qt.ApplicationModal)
        self.calender.setWindowTitle("Booking Date")

        self.calender.show()

    def updatedate(self,*args):

        getdate = self.calender.selectedDate().toString("dd/MM/yyyy")
        print('get date value is ',getdate)
        self.booking_le.setText(getdate)
        self.calender.deleteLater()

    def bill_value_fetch(self):
        print("This function get passed")
        bill_no = self.bill_le.text()
        print('The bill no is ',bill_no)

        bill_value = int(bill_no)

        # find the function name:
        function_sel_query = "SELECT CATEGORY FROM DBO.ORDER_DETAILS WHERE BILL_NO =?"
        cur.execute(function_sel_query,bill_value)


        function_result = cur.fetchall()

        result_check = len(function_result)

        if result_check >=1:

                function_name = function_result[0][0]

                print('the function name is ',function_name)


                non_marriage_select_query = "SELECT BILL.CUSTOMER_NAME,BILL.PHONE_NO,ORD.CATEGORY,ORD.TOTAL_AMOUNT,\
                                BILL.BILLING_DATE,\
                                BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,BILL.AMOUNT_DUE,BILL.FUNCTION_BOOKING_DATE\
                                FROM DBO.ORDER_DETAILS ORD , DBO.BILLING_TABLE BILL WHERE\
                                ORD.BILL_NO = BILL.BILL_NO\
                                AND BILL.BILL_NO = ? AND BILL_TYPE ='FUNCTION' "

                marriage_select_query ="SELECT BILL.CUSTOMER_NAME,BILL.PHONE_NO, ORD.CATEGORY,ORD.TOTAL_AMOUNT,\
                                BILL.BILLING_DATE,BILL.TOTAL_AMOUNT, \
                                BILL.AMOUNT_RECIEVED,BILL.AMOUNT_DUE,BILL.FUNCTION_BOOKING_DATE, PACKAGE.PACKAGE_NAME\
                                FROM DBO.ORDER_DETAILS ORD , DBO.BILLING_TABLE BILL, DBO.PROD_DETAILS PROD,\
                                DBO.PACKAGE_DETAILS PACKAGE WHERE ORD.BILL_NO = BILL.BILL_NO\
                                AND PROD.PROD_ID =ORD.PRD_ID\
                                AND PROD.PACKAGE_ID = PACKAGE.PACKAGE_ID\
                                AND BILL.BILL_NO = ? AND BILL_TYPE ='FUNCTION' AND PROD_TYPE ='FUNCTION'"

                if function_name =='MARRIAGE':

                        cur.execute(marriage_select_query,bill_no)

                        result = cur.fetchall()
                else:
                        cur.execute(non_marriage_select_query, bill_no)

                        result = cur.fetchall()

                result_check =len(result)

                print('the test result length is',result_check)
                print('the test results are',result)



                print(" The output result value is",result)
                bill_tuple_list =list(result[0])
                print("the new bill result is ",bill_tuple_list)
                bill_tuple_list[4]=bill_tuple_list[4].strftime('%d/%m/%Y')
                bill_tuple_list[8] = bill_tuple_list[8].strftime('%d/%m/%Y')
                bill_tuple_list = [ str(data) for data in bill_tuple_list if type(data)!= 'str']
                print ("the new value for bill list is ",bill_tuple_list)

                db_customer_name=bill_tuple_list[0]
                db_phone_no=bill_tuple_list[1]
                db_function_name =bill_tuple_list[2]
                db_order_total_amount=bill_tuple_list[3]
                db_billing_date = bill_tuple_list[4]
                db_bill_total_amount=bill_tuple_list[5]
                db_amount_paid =bill_tuple_list[6]
                db_amount_due =bill_tuple_list[7]
                db_booking_date=bill_tuple_list[8]

                if db_function_name =='MARRIAGE':
                   db_package_name =bill_tuple_list[9]
                else:
                   db_package_name ='NA'

                print('the package name is',db_package_name)

                self.customer_le.setText(db_customer_name)
                self.phone_le.setText(db_phone_no)
                self.function_le.setText(db_function_name)
                self.total_le.setText(db_bill_total_amount)
                self.paid_le.setText(db_amount_paid)
                self.due_le.setText(db_amount_due)
                self.date_le.setText(db_billing_date)
                self.package_le.setText(db_package_name)

                self.booking_le.setText(db_booking_date)
        else:
            QMessageBox.warning(self,'Error','Please enter correct Bill No.')
            self.bill_le.clear()

    def amountdue(self):

        print('Amount due function in')

        print("the test value is ",self.due_le.text())
        print('the total amount is ', self.total_le.text())
        if self.paid_le.text()=="":
            amount_paid_prev = float(0)
        else:
            amount_paid_prev = float(self.paid_le.text())
        if self.total_le.text()=="":
            total_amount =float(0)
        else:
            total_amount = float(self.total_le.text())
        amount_due = total_amount - amount_paid_prev
        if self.recieved_le.text()=="":
            Recievedamount = float(0)
        else:
            Recievedamount = float(self.recieved_le.text())
        print('Amount due is ', amount_due)
        print('amount  recieved is ',Recievedamount)

        balance = float(amount_due-Recievedamount )

        print('The balanced amount is ',balance)

        self.due_le.setText(str(balance))

    def savebtn(self):
        billno = int(self.bill_le.text())
        customer_name = self.customer_le.text()
        phone_no = self.phone_le.text()
        booking_date =self.booking_le.text()
        amount_paid_now = self.recieved_le.text()
        amount_recieved_prev = int(float(self.paid_le.text()))
        function_name =self.function_le.text()
        package_name =self.package_le.text()

        if amount_paid_now =='':
            amount_paid_now = '0'

        print ('amount paid now is ',amount_paid_now)
        print('amount paid previous is ', amount_recieved_prev)

        amount_recieved = int(amount_recieved_prev + int(amount_paid_now))

        print('amount received sum is',amount_recieved)

        if self.due_le.text()=='':
            self.due_le.setText('0')
        amount_due = float(self.due_le.text())
        int_phone_no = int(phone_no)

        booking_date = datetime.datetime.strptime(booking_date,'%d/%m/%Y').date()
        int_amount_due = int(amount_due)

        update_query ="UPDATE dbo.BILLING_TABLE SET CUSTOMER_NAME =?,PHONE_NO =?,FUNCTION_BOOKING_DATE=?,\
                        AMOUNT_RECIEVED=?,AMOUNT_DUE=? WHERE BILL_NO =? AND BILL_TYPE='FUNCTION'"
        update_data = [customer_name,int_phone_no,booking_date,amount_recieved,int_amount_due,billno]
        print("the update data is ",update_data)

        cur.execute(update_query,update_data)
        connect.commit()

        self.billno = billno
        self.customer_name = customer_name
        self.phone_number = phone_no
        self.total_amount = self.total_le.text()
        self.amount_recieved = amount_paid_now
        self.due_amount = amount_due
        self.function_name = function_name
        self.package_name = package_name
        self.booking_date =booking_date



        if int(amount_due) == 0 and int(amount_paid_now) != 0:
            QMessageBox.information(self,'Message','Bill is successfully closed')
        else:
            QMessageBox.information(self,'Message','Bill is updated Successfully')

        self.save_btn.setEnabled(False)

    def clearbtn(self):
        columns_list =[self.bill_le,self.customer_le,self.phone_le,self.booking_le,self.total_le,self.recieved_le,self.due_le,self.function_le,self.package_le,self.paid_le]

        for i in columns_list:
            i.clear()


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

        phoneno =str(self.phone_number)
        total_amount = self.total_amount
        amount_paid = self.amount_recieved
        amount_due = self.due_amount
        function_name = self.function_name
        package_name =self.package_name
        book =str(self.booking_date)

        print("the time is ", time, " and the format is ", type(time))

        folder = folder_path+year+"\\"+month+"\\"+str(today) + '\\'
        filename = str(folder) + "Update_Function_Bill_" + str(time) + ".rtf"


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
        title = "\n\n\t\t\t\t\"FUNCTION BILL\"\n===================================================================="
        bill_section = "\n\n Bill No\t: " + bill_number + "\t\t\t\tDate  : " + today_date + "\n"
        bill_section2 = "\n\n Customer Name\t\t: " + cust_name
        bill_section21 = "\n\n Customer Phone No. \t: " + phoneno
        bill_section22 = "\n\n Function Name \t\t: " + function_name
        bill_section23 = "\n\n Booking Date \t\t: " + book
        bill_section_package = "\n\n Package Name \t\t: " + package_name

        bill_section_combined = bill_section2 + bill_section21 + bill_section22 + bill_section23 + "\n" + lines

        bill_section_combined_marriage = bill_section2 + bill_section21 + bill_section22 + bill_section_package + bill_section23 + "\n" + lines

        if function_name == 'MARRIAGE':

            final = header + address1 + address2 + address3 + address4 + address5 + title + bill_section + lines + bill_section_combined_marriage
            file.write(final)
        else:
            final = header + address1 + address2 + address3 + address4 + address5 + title + bill_section + lines + bill_section_combined
            file.write(final)

        footer1 = "\n\n  TIME  :" + footer_time + "\t\t\t\tTOTAL AMOUNT\t:\t" + str(float(total_amount))
        footer2 = "\n\t\t\t\t\t\tAMOUNT PAID\t\t:\t" + str(float(amount_paid))
        footer3 = "\n  SIGN  :\t\t\t\t\tAMOUNT DUE\t\t:\t" + str(float(amount_due)) + "\n"

        footer_final = footer1 + footer2 + footer3

        file.write(footer_final)
        file.write(lines)

        message = "\n\t\t*** THANK YOU... PLEASE VISIT US AGAIN ***"
        file.write(message)

        self.file_name = filename

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
    new_function = QtWidgets.QDialog()
    #ui = Ui_new_function()
    #ui.setupUi(new_function)
    #new_function.show()
    ui=Update_Function_Bill()
    ui.show()
    sys.exit(app.exec_())
