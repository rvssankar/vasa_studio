from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QComboBox,QMessageBox
from PyQt5.QtCore import QDate,Qt
import os
import sys
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
        self.date_label.setGeometry(QtCore.QRect(730, 100, 71, 31))
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
        self.bill_le.setEnabled(False)
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
        self.booking_label.setGeometry(QtCore.QRect(131, 313, 221, 41))
        self.booking_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.booking_label.setObjectName("booking_label")
        self.booking_le = QtWidgets.QLineEdit(self.table_frame)
        self.booking_le.setGeometry(QtCore.QRect(370, 320, 241, 41))
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
        self.total_label.setGeometry(QtCore.QRect(131, 373, 221, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.total_label.setObjectName("total_label")
        self.total_le = QtWidgets.QLineEdit(self.table_frame)
        self.total_le.setGeometry(QtCore.QRect(370, 380, 241, 41))
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
        self.recieved_label.setGeometry(QtCore.QRect(131, 433, 221, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.recieved_le = QtWidgets.QLineEdit(self.table_frame)
        self.recieved_le.setGeometry(QtCore.QRect(370, 440, 241, 41))
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
        self.package_label.setGeometry(QtCore.QRect(130, 250, 221, 41))
        self.package_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.package_label.setObjectName("package_label")
        self.function_combo = QtWidgets.QComboBox(self.table_frame)
        self.function_combo.setGeometry(QtCore.QRect(370, 200, 241, 41))
        self.function_combo.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.function_combo.setObjectName("function_combo")
        self.package_combo = QtWidgets.QComboBox(self.table_frame)
        self.package_combo.setGeometry(QtCore.QRect(370, 260, 241, 41))
        self.package_combo.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.package_combo.setObjectName("package_combo")
        self.close_btn = QtWidgets.QPushButton(self.table_frame)
        self.close_btn.setGeometry(QtCore.QRect(520, 600, 131, 71))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#close_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.close_btn.setObjectName("close_btn")
        self.clear_btn = QtWidgets.QPushButton(self.table_frame)
        self.clear_btn.setGeometry(QtCore.QRect(360, 600, 121, 71))
        self.clear_btn.setStyleSheet("#clear_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(240, 238, 74, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#clear_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.clear_btn.setObjectName("clear_btn")
        self.print_btn = QtWidgets.QPushButton(self.table_frame)
        self.print_btn.setGeometry(QtCore.QRect(198, 600, 131, 71))
        self.print_btn.setStyleSheet("#print_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(153, 228, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#print_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.print_btn.setObjectName("print_btn")
        self.save_btn = QtWidgets.QPushButton(self.table_frame)
        self.save_btn.setGeometry(QtCore.QRect(40, 600, 121, 71))
        self.save_btn.setStyleSheet("#save_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#save_btn:pressed{border-style:solid;border-width:6px}"                                    )
        self.save_btn.setObjectName("save_btn")
        self.cal_tool_btn = QtWidgets.QToolButton(self.table_frame)
        self.cal_tool_btn.setGeometry(QtCore.QRect(579, 324, 31, 31))
        self.cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cal_tool_btn.setIcon(icon)
        self.cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.cal_tool_btn.setObjectName("cal_tool_btn")
        self.due_label = QtWidgets.QLabel(new_function)
        self.due_label.setGeometry(QtCore.QRect(241, 653, 221, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(135, 67, 0);\n"
"")
        self.due_label.setObjectName("due_label")
        self.due_le = QtWidgets.QLineEdit(new_function)
        self.due_le.setEnabled(False)
        self.due_le.setGeometry(QtCore.QRect(480, 660, 241, 41))
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
        self.title_label.setText(_translate("new_function", "New Function Bill"))
        self.date_label.setText(_translate("new_function", "Date :"))
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
        self.due_label.setText(_translate("new_function", "Amount Due (Rs.)       :"))

class Add_Function_Bill (QDialog,Ui_new_function):
    def __init__(self,parent=None):
        super(Add_Function_Bill,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Add Function Bill")

        self.onlyint = QtGui.QIntValidator()
        self.phone_le.setValidator(self.onlyint)
        self.bill_le.setValidator(self.onlyint)
        self.total_le.setValidator(self.onlyint)
        self.recieved_le.setValidator(self.onlyint)
        self.due_le.setValidator(self.onlyint)

        self.current_date()
        self.bill_generator()
        self.functioncombovalue()

        self.package_combo.setEnabled(False)
        self.package_combo.setStyleSheet('QPushButton: disabled{background - color:grey}')

        self.function_combo.currentIndexChanged['QString'].connect(self.comboindexchanged)
        self.total_le.textChanged.connect(self.amountdue)
        self.recieved_le.textChanged.connect(self.amountdue)


        self.cal_tool_btn.clicked.connect(self.delivery_calender)
        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)
        self.close_btn.clicked.connect(self.closebtn)
        self.print_btn.clicked.connect(self.printbill)

        config_name = 'function_bill.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        save_image = os.path.join(application_path, "images", "save.png")
        print_image = os.path.join(application_path, "images", "print.png")
        clear_image = os.path.join(application_path, "images", "clear.png")
        close_image = os.path.join(application_path, "images", "close.png")
        self.calender_image = os.path.join(application_path, "images", "calender.png")

        self.save_btn.setIcon(QtGui.QIcon(save_image))
        self.save_btn.setIconSize(QtCore.QSize(35, 35))

        self.print_btn.setIcon(QtGui.QIcon(print_image))
        self.print_btn.setIconSize(QtCore.QSize(35, 35))

        self.clear_btn.setIcon(QtGui.QIcon(clear_image))
        self.clear_btn.setIconSize(QtCore.QSize(35, 35))

        self.close_btn.setIcon(QtGui.QIcon(close_image))
        self.close_btn.setIconSize(QtCore.QSize(35, 35))



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

    def delivery_calender(self):
        self.calender = QCalendarWidget()
        self.calender.setMinimumDate(QDate(1900,1,1))
        self.calender.setMaximumDate(QDate(2999,12,31))
        self.calender.setGridVisible(True)
        self.calender.clicked.connect(self.updatedate)
        self.calender.setWindowModality(Qt.ApplicationModal)
        self.calender.setWindowTitle("Booking Calender")

        self.calender.setWindowIcon(QtGui.QIcon(self.calender_image))

        self.calender.show()

    def updatedate(self,*args):

        getdate = self.calender.selectedDate().toString("dd/MM/yyyy")
        print('get date value is ',getdate)
        self.booking_le.setText(getdate)
        self.calender.deleteLater()

    def functioncombovalue(self):
        self.combolist = set('',)

        sel_query ="SELECT DISTINCT PROD_NAME from dbo.PROD_DETAILS WHERE PROD_TYPE ='FUNCTION'"
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

                x=i[0]
                self.combolist.add(x)

        self.function_combo.addItems(self.combolist)


    def combopackagevalue(self):
        self.combolist = set('',)
        self.package_combo.clear()

        sel_query ="SELECT PACKAGE_NAME from dbo.PACKAGE_DETAILS"
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

                x=i[0]
                self.combolist.add(x)
        self.package_combo.addItems(self.combolist)
        self.package_combo.currentIndexChanged['QString'].connect(self.totalamount)


    def comboindexchanged(self):
        current_value =self.function_combo.currentText()
        print("The category combo box current value is ",current_value)
        if current_value =='MARRIAGE':
            self.total_le.clear()
            self.package_combo.setEnabled(True)
            self.package_combo.setStyleSheet("border-radius:10px;\n"
                                             "border-style:outset;\n"
                                             "border-width:2px;\n"
                                             "border-color:black;\n"
                                             "font: 11pt \"Cambria\";\n"
                                             "font:bold")
            self.combopackagevalue()



        else:
            self.package_combo.clear()
            self.package_combo.setEnabled(False)
            self.package_combo.setStyleSheet('QPushButton: disabled{background - color:grey}')
            self.totalamount()

    def totalamount(self):

        print('the total amount function is in')

        function_name = self.function_combo.currentText()

        print('the function name is' , function_name)

        if function_name !='MARRIAGE':

            SEL_QUERY = " SELECT PRICE from dbo.PROD_DETAILS WHERE PROD_TYPE ='FUNCTION' AND PROD_NAME =?"
            cur.execute(SEL_QUERY, function_name)
            result = cur.fetchall()
            total_amount_value = str(result[0][0])
            print("the total amount is ",total_amount_value)

            self.total_le.setText(total_amount_value)
        else:
            package_name = self.package_combo.currentText()
            print('the package name is',package_name)

            SEL_QUERY = " SELECT PROD.PRICE from dbo.PROD_DETAILS PROD JOIN dbo.PACKAGE_DETAILS PACKAGE ON PROD.PACKAGE_ID = PACKAGE.PACKAGE_ID AND PROD_TYPE ='FUNCTION' AND PROD_NAME ='MARRIAGE' AND PACKAGE.PACKAGE_NAME =?"
            cur.execute(SEL_QUERY, package_name)
            result = cur.fetchall()
            total_amount_value = str(result[0][0])
            print("the total amount is ", total_amount_value)

            self.total_le.setText(total_amount_value)

    def amountdue(self):
        print('Amount due function in')

        print("the test value is ",self.total_le.text())
        if self.total_le.text()=="":
            totalamount = float(0)
        else:
            totalamount = float(str(self.total_le.text()))
        if self.recieved_le.text()=="":
            Recievedamount = float(0)
        else:
            Recievedamount = float(self.recieved_le.text())
        print('Amount due is ', totalamount)
        print('amount  recieved is ',Recievedamount)

        balance = float(totalamount-Recievedamount )

        print('The balanced amount is ',balance)

        self.due_le.setText(str(balance))

    def savebtn(self):

        if self.customer_le.text() =='' or self.phone_le.text()=='':
            QMessageBox.warning(self,'Warning','Please enter the customer information')
        elif self.total_le.text() =='':
            QMessageBox.warning(self,'Warning','Please select proper function details')

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
            booking_date = self.booking_le.text()

            phoneno = int(phoneno)

            print('The order date is ',orderdate ,' and type is ', type(orderdate))
            totalamount= float(totalamount)
            amountreceived=float(amountreceived)
            dueamount=float(dueamount)
            billno =int(billno)

            bill_type ='FUNCTION'

            if booking_date != '':

                bookingdate = datetime.datetime.strptime(booking_date,'%d/%m/%Y').date()
            else:
                bookingdate = datetime.date(9999,12,31)

            print('the deliver date value is ', bookingdate, ' and type is ', type(bookingdate))

            sql_order_date = orderdate.strftime("%d/%m/%Y")
            sql_delivery_date = bookingdate.strftime("%d/%m/%Y")

            ins_query1 = 'INSERT INTO dbo.BILLING_TABLE VALUES(?,?,?,?,?,?,?,?,?)'
            ins_query = "INSERT INTO dbo.BILLING_TABLE (BILL_NO,CUSTOMER_NAME,PHONE_NO,BILLING_DATE,FUNCTION_BOOKING_DATE,TOTAL_AMOUNT,AMOUNT_RECIEVED,AMOUNT_DUE,BILL_TYPE) VALUES(?,?,?,?,?,?,?,?,?)"
            data = (billno,customername,phoneno,orderdate,bookingdate,totalamount,amountreceived,dueamount,bill_type)
            data1 = (billno, customername, phoneno, orderdate,bookingdate, totalamount)

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


            function_name = self.function_combo.currentText()
            package_name = self.package_combo.currentText()
            total_amount = self.total_le.text()

            print('the function_name values are',function_name)
            print('the package_name values are', package_name)
            print('the total amount values are', total_amount)


            # finding Prd_id

            if function_name != 'MARRIAGE':
                prd_select_query = "SELECT PROD_ID FROM dbo.PROD_DETAILS WHERE PROD_TYPE ='FUNCTION' AND PROD_NAME =?"
                cur.execute(prd_select_query, function_name)
                result = cur.fetchall()
                print('the result value is ', result[0][0])
                prd_id =result[0][0]
            else:
                prd_select_query = "SELECT PROD.PROD_ID from dbo.PROD_DETAILS PROD JOIN dbo.PACKAGE_DETAILS PACKAGE ON PROD.PACKAGE_ID = PACKAGE.PACKAGE_ID AND PROD_TYPE ='FUNCTION' AND PROD_NAME ='MARRIAGE' AND PACKAGE.PACKAGE_NAME =?"
                cur.execute(prd_select_query, package_name)
                result = cur.fetchall()
                prd_id =result[0][0]



            print( "The PRD_ID  values is ",prd_id)

            # insert data into ORDER_DETAILS table:

            size='NA'
            qty =1
            rate =total_amount


            insert_qry_order_table = "INSERT INTO dbo.ORDER_DETAILS VALUES (?,?,?,?,?,?,?,?)"
            cur.execute(insert_qry_order_table,(order_value,billno,prd_id,function_name,size,rate,qty,total_amount))

            connect.commit()
            connect.close()

            self.billno = billno
            self.customer_name = customername
            self.phone_number =phoneno
            self.total_amount =total_amount
            self.amount_recieved =amountreceived
            self.due_amount =dueamount
            self.function_name =function_name
            self.package_name =package_name
            self.booking_date =bookingdate


            QMessageBox.information(self, 'Message', 'Data saved successfully')
            self.save_btn.setEnabled(False)

    def clearbtn(self):
        columns_list =[self.customer_le,self.phone_le,self.booking_le,self.total_le,self.recieved_le,self.due_le]

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
        filename = str(folder) + "Function_Bill_" + str(time) + ".rtf"


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
    ui = Add_Function_Bill()
    ui.show()
    sys.exit(app.exec_())