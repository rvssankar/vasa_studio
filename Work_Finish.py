
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QTableWidgetItem
from PyQt5.QtCore import Qt
import pyodbc
import datetime


class Ui_finish_window(object):
    def setupUi(self, finish_window):
        finish_window.setObjectName("finish_window")
        finish_window.resize(1254, 849)
        finish_window.setStyleSheet("#finish_window{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.273632 rgba(21, 224, 235, 249), stop:1 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(finish_window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 91))
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
        self.finish_frame = QtWidgets.QFrame(finish_window)
        self.finish_frame.setGeometry(QtCore.QRect(70, 180, 1161, 541))
        self.finish_frame.setStyleSheet("#finish_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.finish_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.finish_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.finish_frame.setObjectName("finish_frame")
        self.finish_table = QtWidgets.QTableWidget(self.finish_frame)
        self.finish_table.setGeometry(QtCore.QRect(20, 20, 1121, 501))
        self.finish_table.setObjectName("finish_table")
        self.finish_table.setColumnCount(9)
        self.finish_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(8, item)
        self.bill_le = QtWidgets.QLineEdit(finish_window)
        self.bill_le.setEnabled(True)
        self.bill_le.setGeometry(QtCore.QRect(400, 750, 231, 41))
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
        self.bill_label = QtWidgets.QLabel(finish_window)
        self.bill_label.setGeometry(QtCore.QRect(230, 756, 161, 31))
        self.bill_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:brown;")
        self.bill_label.setObjectName("bill_label")
        self.finish_btn = QtWidgets.QPushButton(finish_window)
        self.finish_btn.setGeometry(QtCore.QRect(670, 730, 231, 81))
        self.finish_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:40px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;\n"
"font:bold;")
        self.finish_btn.setObjectName("finish_btn")

        self.retranslateUi(finish_window)
        QtCore.QMetaObject.connectSlotsByName(finish_window)

    def retranslateUi(self, finish_window):
        _translate = QtCore.QCoreApplication.translate
        finish_window.setWindowTitle(_translate("finish_window", "Dialog"))
        self.title_label.setText(_translate("finish_window", "Pending Orders"))
        item = self.finish_table.horizontalHeaderItem(0)
        item.setText(_translate("finish_window", "Bill No"))
        item = self.finish_table.horizontalHeaderItem(1)
        item.setText(_translate("finish_window", "Customer Name"))
        item = self.finish_table.horizontalHeaderItem(2)
        item.setText(_translate("finish_window", "Phone No"))
        item = self.finish_table.horizontalHeaderItem(3)
        item.setText(_translate("finish_window", "Event Name"))
        item = self.finish_table.horizontalHeaderItem(4)
        item.setText(_translate("finish_window", "Booking Date"))
        item = self.finish_table.horizontalHeaderItem(5)
        item.setText(_translate("finish_window", "Total Amount"))
        item = self.finish_table.horizontalHeaderItem(6)
        item.setText(_translate("finish_window", "Finish Date"))
        item = self.finish_table.horizontalHeaderItem(7)
        item.setText(_translate("finish_window", "Studio Name"))
        item = self.finish_table.horizontalHeaderItem(8)
        item.setText(_translate("finish_window", "Status"))
        self.bill_label.setText(_translate("finish_window", "Bill No                   :"))
        self.finish_btn.setText(_translate("finish_window", "Finish"))

class Work_Finish_Window(QDialog,Ui_finish_window):
    def __init__(self, parent=None):
        super(Work_Finish_Window,self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Work Progress")

        self.table_records()
        self.table_population()

        self.finish_table.cellClicked.connect(self.cellvalue)


        self.finish_btn.clicked.connect(self.finishbtn)

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
        self.finish_table.setRowCount(0)
        self.finish_table.verticalHeader().setVisible(False)
        header = self.finish_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def table_population(self):
        self.connectdb()

        select_query = "SELECT BILL_NO,CUSTOMER_NAME,PHONE_NO,EVENT_NAME,BOOKING_DATE,TOTAL_AMOUNT,\
                        WORK_START_DATE,STUDIO_NAME,STATUS FROM dbo.WORK_ALLOCATE \
                        WHERE STATUS ='IN PROGRESS'"

        cur.execute(select_query)

        result = cur.fetchall()

        result_check = len(result)

        print("The total number of records fetched from table is ",result_check)

        self.work_finish = datetime.datetime.now().date().strftime('%d/%m/%Y')
        #status = 'ALLOCATE'

        if result_check >= 1:
            new_result =[]
            column_count = self.finish_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                tuple_value[6] = self.work_finish
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                #tuple_value.extend(self.work_finish)
                print('the modified tuple value is ', tuple_value)


                self.finish_table.insertRow(row)
                for column in range(column_count):
                        print("the row number is ",row)
                        print("the column number is",column)
                        value = tuple_value[column]

                        self.finish_table.setItem(row,column,self.table_item(value,Qt.ItemIsSelectable | Qt.ItemIsEnabled))



    def cellvalue(self,row,column):

        print("Row %d and column %d was clicked" %(row,column))

        bill_no = str(self.finish_table.item(row,0).text())
        bill_no = str.strip(bill_no)
        print("the bill_no is ",bill_no,' and type is ',type(bill_no),' and the length is ',len(bill_no))

        self.bill_le.setText(bill_no)




    def table_item(self,text,flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def finishbtn(self):

        bill_no = self.bill_le.text()
        print('the bill number is', bill_no, 'and type is ', type(bill_no))


        if bill_no == '':
            QMessageBox.warning(self, 'Warning', "Please enter the Bill Number")

        else:

            work_finish =self.work_finish
            work_finish = datetime.datetime.strptime(work_finish,'%d/%m/%Y').date()

            update_qry = "UPDATE dbo.WORK_ALLOCATE SET STATUS ='COMPLETED',WORK_FINISH_DATE =? WHERE BILL_NO =?"

            cur.execute(update_qry, (work_finish,int(bill_no)))
            cur.commit()

            info = "Work Finished for Bill No "+bill_no

            QMessageBox.information(self, 'Message', info)

            self.finish_table.setRowCount(0)
            self.table_records()
            self.table_population()
            self.bill_le.clear()
            #self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    finish_window = QtWidgets.QDialog()
    #ui = Ui_finish_window()
    #ui.setupUi(finish_window)
    #finish_window.show()
    ui=Work_Finish_Window()
    ui.show()
    sys.exit(app.exec_())
