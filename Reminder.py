from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
import datetime
import pyodbc

class Ui_reminder_page(object):
    def setupUi(self, reminder_page):
        reminder_page.setObjectName("reminder_page")
        reminder_page.resize(1171, 738)
        reminder_page.setStyleSheet("#reminder_page{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(56, 143, 152, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(reminder_page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1171, 91))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(320, 20, 601, 51))
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
"color: white;\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.reminder_frame = QtWidgets.QFrame(reminder_page)
        self.reminder_frame.setGeometry(QtCore.QRect(10, 140, 1151, 491))
        self.reminder_frame.setStyleSheet("#reminder_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.reminder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reminder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reminder_frame.setObjectName("reminder_frame")
        self.reminder_table = QtWidgets.QTableWidget(self.reminder_frame)
        self.reminder_table.setGeometry(QtCore.QRect(20, 20, 1111, 451))
        self.reminder_table.setStyleSheet("#finish_table{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));}")
        self.reminder_table.setObjectName("reminder_table")
        self.reminder_table.setColumnCount(9)
        self.reminder_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reminder_table.setHorizontalHeaderItem(8, item)
        self.close_btn = QtWidgets.QPushButton(reminder_page)
        self.close_btn.setGeometry(QtCore.QRect(890, 650, 191, 71))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 28, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:red;\n"
"font:bold;}\n"
"#close_btn:pressed{border-style:outset;\n"
"border-width:9px;}")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(reminder_page)
        QtCore.QMetaObject.connectSlotsByName(reminder_page)

    def retranslateUi(self, reminder_page):
        _translate = QtCore.QCoreApplication.translate
        reminder_page.setWindowTitle(_translate("reminder_page", "Dialog"))
        self.title_label.setText(_translate("reminder_page", "Reminder for Function Bill"))
        item = self.reminder_table.horizontalHeaderItem(0)
        item.setText(_translate("reminder_page", "Bill No"))
        item = self.reminder_table.horizontalHeaderItem(1)
        item.setText(_translate("reminder_page", "Customer Name"))
        item = self.reminder_table.horizontalHeaderItem(2)
        item.setText(_translate("reminder_page", "Phone No"))
        item = self.reminder_table.horizontalHeaderItem(3)
        item.setText(_translate("reminder_page", "Function Name"))
        item = self.reminder_table.horizontalHeaderItem(4)
        item.setText(_translate("reminder_page", "Booking Date"))
        item = self.reminder_table.horizontalHeaderItem(5)
        item.setText(_translate("reminder_page", "Total Amt"))
        item = self.reminder_table.horizontalHeaderItem(6)
        item.setText(_translate("reminder_page", "Amt Recieved"))
        item = self.reminder_table.horizontalHeaderItem(7)
        item.setText(_translate("reminder_page", "Amt Due"))
        item = self.reminder_table.horizontalHeaderItem(8)
        item.setText(_translate("reminder_page", "Date"))
        self.close_btn.setText(_translate("reminder_page", "Close"))

class Reminder_Page(QDialog,Ui_reminder_page):
    def __init__(self,parent=None):
        super(Reminder_Page,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Function Reminder")

        self.table_records()

        self.table_population()

        self.close_btn.clicked.connect(self.closebtn)

    def connectdb(self):
        global cur
        global connect

        connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur

    def table_records(self):
        self.reminder_table.setRowCount(0)
        self.reminder_table.verticalHeader().setVisible(False)
        header = self.reminder_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def table_population(self):
        self.connectdb()
        today = datetime.date.today()

        reminder_set_days =5

        date_delta = today + datetime.timedelta(days=reminder_set_days)


        self.reminder_table.setRowCount(0)

        print ("The today date is ",today)

        print("The date delta days is",date_delta)

        select_query ="SELECT BILL.BILL_NO,BILL.CUSTOMER_NAME,BILL.PHONE_NO,CATEGORY ,BILL.FUNCTION_BOOKING_DATE, \
                       BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,BILL.AMOUNT_DUE,BILL.BILLING_DATE \
                       FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL ON \
                       ORD.BILL_NO = BILL.BILL_NO WHERE BILL_TYPE ='FUNCTION' AND  \
                       FUNCTION_BOOKING_DATE BETWEEN ? AND ?"

        cur.execute(select_query, (today, date_delta))
        result = cur.fetchall()

        print("result is", result)

        result_check = len(result)

        self.result_count = result_check

        if result_check >= 1:
            new_result = []
            column_count = self.reminder_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                tuple_value[8] = tuple_value[8].strftime('%d/%m/%Y')
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                # tuple_value.extend(self.work_finish)
                print('the modified tuple value is ', tuple_value)
                self.reminder_table.insertRow(row)
                for column in range(column_count):
                    value = tuple_value[column]

                    self.reminder_table.setItem(row, column, self.table_item(value,
                                                                             Qt.ItemIsSelectable | Qt.ItemIsEnabled))





    def table_item(self, text, flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem




    def closebtn(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reminder_page = QtWidgets.QDialog()
    #ui = Ui_reminder_page()
    #ui.setupUi(reminder_page)
    #reminder_page.show()
    ui = Reminder_Page()
    ui.show()
    sys.exit(app.exec_())
