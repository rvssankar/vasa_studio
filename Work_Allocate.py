
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableWidgetItem
from PyQt5.QtCore import Qt
import pyodbc
import datetime


class Ui_allocate_window(object):
    def setupUi(self, allocate_window):
        allocate_window.setObjectName("allocate_window")
        allocate_window.resize(1220, 859)
        allocate_window.setStyleSheet("#allocate_window{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 161, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(allocate_window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1241, 91))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(310, 20, 601, 51))
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
        self.allocate_frame = QtWidgets.QFrame(allocate_window)
        self.allocate_frame.setGeometry(QtCore.QRect(30, 150, 1161, 541))
        self.allocate_frame.setStyleSheet("#allocate_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.allocate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allocate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allocate_frame.setObjectName("allocate_frame")
        self.allocate_table = QtWidgets.QTableWidget(self.allocate_frame)
        self.allocate_table.setGeometry(QtCore.QRect(20, 20, 1121, 501))
        self.allocate_table.setObjectName("allocate_table")
        self.allocate_table.setColumnCount(8)
        self.allocate_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.allocate_table.setHorizontalHeaderItem(7, item)
        self.studio_le = QtWidgets.QLineEdit(allocate_window)
        self.studio_le.setGeometry(QtCore.QRect(450, 770, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.studio_le.setFont(font)
        self.studio_le.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.studio_le.setObjectName("studio_le")
        self.studio_label = QtWidgets.QLabel(allocate_window)
        self.studio_label.setGeometry(QtCore.QRect(280, 773, 161, 31))
        self.studio_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:brown;")
        self.studio_label.setObjectName("studio_label")
        self.bill_le = QtWidgets.QLineEdit(allocate_window)
        self.bill_le.setEnabled(True)
        self.bill_le.setGeometry(QtCore.QRect(450, 710, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bill_le.setFont(font)
        self.bill_le.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.bill_le.setObjectName("bill_le")
        self.bill_label = QtWidgets.QLabel(allocate_window)
        self.bill_label.setGeometry(QtCore.QRect(280, 716, 161, 31))
        self.bill_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:brown;")
        self.bill_label.setObjectName("bill_label")
        self.allocate_btn = QtWidgets.QPushButton(allocate_window)
        self.allocate_btn.setGeometry(QtCore.QRect(790, 713, 231, 81))
        self.allocate_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:40px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;\n"
"font:bold;")
        self.allocate_btn.setObjectName("allocate_btn")

        self.retranslateUi(allocate_window)
        QtCore.QMetaObject.connectSlotsByName(allocate_window)

    def retranslateUi(self, allocate_window):
        _translate = QtCore.QCoreApplication.translate
        allocate_window.setWindowTitle(_translate("allocate_window", "Dialog"))
        self.title_label.setText(_translate("allocate_window", "Allocate Order"))
        item = self.allocate_table.horizontalHeaderItem(0)
        item.setText(_translate("allocate_window", "Bill No"))
        item = self.allocate_table.horizontalHeaderItem(1)
        item.setText(_translate("allocate_window", "Customer Name"))
        item = self.allocate_table.horizontalHeaderItem(2)
        item.setText(_translate("allocate_window", "Phone No"))
        item = self.allocate_table.horizontalHeaderItem(3)
        item.setText(_translate("allocate_window", "Event Name"))
        item = self.allocate_table.horizontalHeaderItem(4)
        item.setText(_translate("allocate_window", "Booking Date"))
        item = self.allocate_table.horizontalHeaderItem(5)
        item.setText(_translate("allocate_window", "Total Amount"))
        item = self.allocate_table.horizontalHeaderItem(6)
        item.setText(_translate("allocate_window", "Date"))
        item = self.allocate_table.horizontalHeaderItem(7)
        item.setText(_translate("allocate_window", "Status"))
        self.studio_label.setText(_translate("allocate_window", "Studio Name     :"))
        self.bill_label.setText(_translate("allocate_window", "Bill No                   :"))
        self.allocate_btn.setText(_translate("allocate_window", "Allocate"))


class Work_Allocate_Page (QDialog,Ui_allocate_window):
    def __init__(self,parent=None):
        super(Work_Allocate_Page,self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Work Allocate")


        self.table_records()
        self.table_population()
        self.allocate_table.cellClicked.connect(self.cellvalue)
        self.allocate_btn.clicked.connect(self.allocatebtn)


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
        self.allocate_table.setRowCount(0)
        self.allocate_table.verticalHeader().setVisible(False)
        header = self.allocate_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def table_population(self):
        self.connectdb()

        select_query = "SELECT BILL.BILL_NO, BILL.CUSTOMER_NAME,BILL.PHONE_NO,PROD.PROD_NAME,\
                        BILL.FUNCTION_BOOKING_DATE, BILL.TOTAL_AMOUNT FROM dbo.BILLING_TABLE BILL ,\
                        dbo.ORDER_DETAILS ORDERS, dbo.PROD_DETAILS PROD \
                        WHERE BILL.BILL_NO  = ORDERS.BILL_NO \
                        AND ORDERS.PRD_ID = PROD.PROD_ID \
                        AND BILL.BILL_TYPE = 'FUNCTION'\
                        AND FUNCTION_BOOKING_DATE > DATEADD(mm,-6,CAST(GETDATE() AS DATE) ) \
                        AND NOT EXISTS ( SELECT 1 FROM DBO.WORK_ALLOCATE  WORK WHERE WORK.BILL_NO = BILL.BILL_NO)\
                        ORDER BY 1 DESC"

        cur.execute(select_query)

        result = cur.fetchall()

        result_check = len(result)

        print("The total number of records fetched from table is ",result_check)

        self.work_allocate = datetime.datetime.now().date().strftime('%d/%m/%Y')
        status = 'ALLOCATE'

        if result_check >= 1:
            new_result =[]
            column_count = self.allocate_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                tuple_value.extend((self.work_allocate,status))
                print('the modified tuple value is ', tuple_value)


                self.allocate_table.insertRow(row)
                for column in range(column_count):
                        print("the row number is ",row)
                        print("the column number is",column)
                        value = tuple_value[column]

                        self.allocate_table.setItem(row,column,self.table_item(value,Qt.ItemIsSelectable | Qt.ItemIsEnabled))



    def cellvalue(self,row,column):

        print("Row %d and column %d was clicked" %(row,column))

        bill_no = str(self.allocate_table.item(row,0).text())
        bill_no = str.strip(bill_no)
        print("the bill_no is ",bill_no,' and type is ',type(bill_no),' and the length is ',len(bill_no))

        self.bill_le.setText(bill_no)




    def table_item(self,text,flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def allocatebtn(self):

        bill_no = self.bill_le.text()
        print('the bill number is',bill_no, 'and type is ',type(bill_no))
        studio_name = str.upper(self.studio_le.text())

        if bill_no =='' :
            QMessageBox.warning(self,'Warning', "Please enter the Bill Number")
        elif studio_name =='':
            QMessageBox.warning(self,'Warning', "Please enter Studio details")

        else:

            print("studio name is ",studio_name)

            select_qry = "SELECT BILL.BILL_NO, BILL.CUSTOMER_NAME,BILL.PHONE_NO,PROD.PROD_NAME,\
                        BILL.FUNCTION_BOOKING_DATE, BILL.TOTAL_AMOUNT FROM dbo.BILLING_TABLE BILL , \
                        dbo.ORDER_DETAILS ORDERS, dbo.PROD_DETAILS PROD \
                        WHERE BILL.BILL_NO  = ORDERS.BILL_NO \
                        AND ORDERS.PRD_ID = PROD.PROD_ID \
                        AND BILL.BILL_TYPE = 'FUNCTION'\
						AND BILL.BILL_NO = ? "\

            cur.execute(select_qry,int(bill_no))
            result = cur.fetchall()
            print("the result is ",result)

            customer_name =result[0][1]
            bill_no_db = result[0][0]
            phone_no = result[0][2]
            event_name = result[0][3]
            booking_date = result[0][4]
            #booking_date=datetime.datetime.strptime(booking_date,'%d/%m/%Y').date()
            total_amount = result[0][5]
            work_allocate = self.work_allocate
            work_allocate = datetime.datetime.strptime(work_allocate,'%d/%m/%Y').date()
            status = 'IN PROGRESS'

            ins_query = "INSERT INTO dbo.WORK_ALLOCATE VALUES (NEXT VALUE FOR dbo.work_allocate_seq,?,?,?,?,?,?,?,?,?,?)"
            data  =(bill_no ,customer_name,int(phone_no),event_name,booking_date,float(total_amount),work_allocate,'',studio_name,status)


            cur.execute(ins_query,data)
            cur.commit()

            info = "Work Allocated to "+studio_name

            QMessageBox.information(self, 'Message',info)
            self.allocate_table.setRowCount(0)

            self.table_records()
            self.table_population()
            self.bill_le.clear()
            self.studio_le.clear()
            #self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allocate_window = QtWidgets.QDialog()
    #ui = Ui_allocate_window()
    #ui.setupUi(allocate_window)
    #allocate_window.show()
    ui = Work_Allocate_Page()
    ui.show()
    sys.exit(app.exec_())
