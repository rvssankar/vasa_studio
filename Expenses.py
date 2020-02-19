from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QMessageBox,QTableWidgetItem
from PyQt5.QtCore import QDate,Qt
import pyodbc
import datetime


class Ui_expense_dialog(object):
    def setupUi(self, expense_dialog):
        expense_dialog.setObjectName("expense_dialog")
        expense_dialog.resize(1226, 823)
        expense_dialog.setStyleSheet("#expense_dialog{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 162, 170, 249), stop:0.940299 rgba(255, 255, 255, 255));}")
        self.title_label = QtWidgets.QLabel(expense_dialog)
        self.title_label.setGeometry(QtCore.QRect(330, 20, 601, 51))
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
        self.date_le = QtWidgets.QLineEdit(expense_dialog)
        self.date_le.setEnabled(True)
        self.date_le.setGeometry(QtCore.QRect(920, 110, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_le.setFont(font)
        self.date_le.setEnabled(False)
        self.date_le.setObjectName("date_le")
        self.date_label = QtWidgets.QLabel(expense_dialog)
        self.date_label.setGeometry(QtCore.QRect(860, 108, 71, 31))
        self.date_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"")
        self.date_label.setObjectName("date_label")
        self.content_frame = QtWidgets.QFrame(expense_dialog)
        self.content_frame.setGeometry(QtCore.QRect(20, 190, 491, 591))
        self.content_frame.setStyleSheet("#content_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 153, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.serial_label = QtWidgets.QLabel(self.content_frame)
        self.serial_label.setGeometry(QtCore.QRect(30, 50, 161, 31))
        self.serial_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:blue;")
        self.serial_label.setObjectName("serial_label")
        self.serial_le = QtWidgets.QLineEdit(self.content_frame)
        self.serial_le.setEnabled(False)
        self.serial_le.setGeometry(QtCore.QRect(200, 50, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.serial_le.setFont(font)
        self.serial_le.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.serial_le.setObjectName("serial_le")
        self.expense_label = QtWidgets.QLabel(self.content_frame)
        self.expense_label.setGeometry(QtCore.QRect(30, 110, 161, 31))
        self.expense_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:blue;")
        self.expense_label.setObjectName("expense_label")
        self.expense_le = QtWidgets.QLineEdit(self.content_frame)
        self.expense_le.setGeometry(QtCore.QRect(200, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.expense_le.setFont(font)
        self.expense_le.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.expense_le.setObjectName("expense_le")
        self.amount_label = QtWidgets.QLabel(self.content_frame)
        self.amount_label.setGeometry(QtCore.QRect(30, 170, 161, 31))
        self.amount_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:blue;")
        self.amount_label.setObjectName("amount_label")
        self.amount_le = QtWidgets.QLineEdit(self.content_frame)
        self.amount_le.setGeometry(QtCore.QRect(200, 170, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.amount_le.setFont(font)
        self.amount_le.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.amount_le.setObjectName("amount_le")
        self.description_label = QtWidgets.QLabel(self.content_frame)
        self.description_label.setGeometry(QtCore.QRect(30, 250, 161, 31))
        self.description_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color:blue;")
        self.description_label.setObjectName("description_label")
        self.description_te = QtWidgets.QTextEdit(self.content_frame)
        self.description_te.setGeometry(QtCore.QRect(200, 250, 231, 191))
        self.description_te.setStyleSheet("\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"")
        self.description_te.setObjectName("description_te")
        self.save_btn = QtWidgets.QPushButton(self.content_frame)
        self.save_btn.setGeometry(QtCore.QRect(30, 480, 121, 61))
        self.save_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.save_btn.setObjectName("save_btn")
        self.clear_btn = QtWidgets.QPushButton(self.content_frame)
        self.clear_btn.setGeometry(QtCore.QRect(190, 480, 121, 61))
        self.clear_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(240, 238, 74, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.clear_btn.setObjectName("clear_btn")
        self.close_btn = QtWidgets.QPushButton(self.content_frame)
        self.close_btn.setGeometry(QtCore.QRect(350, 480, 121, 61))
        self.close_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.close_btn.setObjectName("close_btn")
        self.table_frame = QtWidgets.QFrame(expense_dialog)
        self.table_frame.setGeometry(QtCore.QRect(540, 190, 651, 591))
        self.table_frame.setStyleSheet("#table_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(17, 95, 197, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.expense_table_label = QtWidgets.QLabel(self.table_frame)
        self.expense_table_label.setGeometry(QtCore.QRect(220, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.expense_table_label.setFont(font)
        self.expense_table_label.setStyleSheet("font: 75 20pt \"Cambria\";\n"
"font:bold;\n"
"color:black;")
        self.expense_table_label.setObjectName("expense_table_label")
        self.expense_table = QtWidgets.QTableWidget(self.table_frame)
        self.expense_table.setGeometry(QtCore.QRect(10, 80, 631, 431))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.expense_table.setFont(font)
        self.expense_table.setObjectName("expense_table")
        self.expense_table.setColumnCount(5)
        self.expense_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expense_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expense_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expense_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expense_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expense_table.setHorizontalHeaderItem(4, item)
        self.show_btn = QtWidgets.QPushButton(self.table_frame)
        self.show_btn.setGeometry(QtCore.QRect(250, 530, 131, 41))
        self.show_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.show_btn.setObjectName("show_btn")
        self.frame = QtWidgets.QFrame(expense_dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1231, 91))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cal_tool_btn = QtWidgets.QToolButton(expense_dialog)
        self.cal_tool_btn.setGeometry(QtCore.QRect(1161, 110, 30, 32))
        self.cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cal_tool_btn.setIcon(icon)
        self.cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.cal_tool_btn.setObjectName("cal_tool_btn")
        self.frame.raise_()
        self.title_label.raise_()
        self.date_le.raise_()
        self.date_label.raise_()
        self.content_frame.raise_()
        self.table_frame.raise_()
        self.cal_tool_btn.raise_()

        self.retranslateUi(expense_dialog)
        QtCore.QMetaObject.connectSlotsByName(expense_dialog)

    def retranslateUi(self, expense_dialog):
        _translate = QtCore.QCoreApplication.translate
        expense_dialog.setWindowTitle(_translate("expense_dialog", "Dialog"))
        self.title_label.setText(_translate("expense_dialog", "Shop Expenses !!!"))
        self.date_label.setText(_translate("expense_dialog", "Date :"))
        self.serial_label.setText(_translate("expense_dialog", "Sl.No                          :"))
        self.expense_label.setText(_translate("expense_dialog", "Expense Details :"))
        self.amount_label.setText(_translate("expense_dialog", "Amount (Rs)         :"))
        self.description_label.setText(_translate("expense_dialog", "Description           :"))
        self.save_btn.setText(_translate("expense_dialog", "Save"))
        self.clear_btn.setText(_translate("expense_dialog", "Clear"))
        self.close_btn.setText(_translate("expense_dialog", "Close"))
        self.expense_table_label.setText(_translate("expense_dialog", "All Expenses"))
        item = self.expense_table.horizontalHeaderItem(0)
        item.setText(_translate("expense_dialog", "Sl No"))
        item = self.expense_table.horizontalHeaderItem(1)
        item.setText(_translate("expense_dialog", "Expense Details"))
        item = self.expense_table.horizontalHeaderItem(2)
        item.setText(_translate("expense_dialog", "Amount"))
        item = self.expense_table.horizontalHeaderItem(3)
        item.setText(_translate("expense_dialog", "Description"))
        item = self.expense_table.horizontalHeaderItem(4)
        item.setText(_translate("expense_dialog", "Date"))
        self.show_btn.setText(_translate("expense_dialog", "Show All"))

class Add_Expenses(QDialog,Ui_expense_dialog):
    def __init__(self,parent=None):
        super(Add_Expenses,self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Expenses Details")

        self.onlyint = QtGui.QIntValidator()
        self.amount_le.setValidator(self.onlyint)

        self.expense_table.setSortingEnabled(True)

        self.cal_tool_btn.clicked.connect(self.expense_calender)

        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)
        self.close_btn.clicked.connect(self.closebtn)
        self.show_btn.clicked.connect(self.table_population)

        self.table_records()
        self.serial_generator()
        self.current_date()

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
        self.expense_table.setRowCount(0)
        self.expense_table.verticalHeader().setVisible(False)
        header = self.expense_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")
        #header.sortIndicatorOrder()


    def table_population(self):
        if self.expense_table.rowCount() > 0:
            #self.expense_table.clear()
            self.expense_table.setRowCount(0)

        select_query = "SELECT * FROM dbo.EXPENSE_DETAILS"

        cur.execute(select_query)

        result = cur.fetchall()

        result_check = len(result)

        print("The total number of records fetched from table is ",result_check)

        if result_check >= 1:
            new_result =[]
            column_count = self.expense_table.columnCount()
            for row in range(result_check):

                tuple_value = list(result[row])
                tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                print('the modified tuple value is ', tuple_value)

                self.expense_table.insertRow(row)
                for column in range(column_count):
                        print("the row number is ",row)
                        print("the column number is",column)
                        value = tuple_value[column]
                        self.expense_table.setItem(row,column,self.table_item(value,Qt.ItemIsSelectable | Qt.ItemIsEnabled))

    def table_item(self,text,flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem


    def serial_generator(self):
        sel_query ='SELECT MAX(SL_NO) FROM dbo.EXPENSE_DETAILS'
        self.connectdb()
        cur.execute(sel_query)
        result = cur.fetchall()
        value = result[0][0]

        if value != None:
            value = value+1
            print(value)
        else:
            value=1
            print('No existing values present. So the Serial number starts with ',value)
            print(type(value))

        self.serial_le.setText(str(value))
        self.serial_le.setAlignment(QtCore.Qt.AlignCenter)

    def current_date(self):
        today = datetime.date.today()
        self.expensedate = today.strftime("%d/%m/%Y")
        date_format = today.strftime("%d/%m/%Y")
        print(date_format)

        self.date_le.setText(date_format)

    def expense_calender(self):
        self.calender = QCalendarWidget()
        self.calender.setMinimumDate(QDate(1900,1,1))
        self.calender.setMaximumDate(QDate(2999,12,31))
        self.calender.setGridVisible(True)
        self.calender.clicked.connect(self.updatedate)
        self.calender.setWindowModality(Qt.ApplicationModal)
        self.calender.setWindowTitle("Expense Date")

        self.calender.show()


    def updatedate(self,*args):

        getdate = self.calender.selectedDate().toString("dd/MM/yyyy")
        print('get date value is ',getdate)
        self.date_le.setText(getdate)
        self.calender.deleteLater()

    def savebtn(self):

        if self.expense_le.text() =='' or self.amount_le.text()=='':
            QMessageBox.warning(self,'Warning','Please enter the Expense details')
        else:

            serial_no = self.serial_le.text()
            expense_name = self.expense_le.text()
            amount = self.amount_le.text()
            description_text = self.description_te.toPlainText()
            expense_date = self.date_le.text()
            expensedate = datetime.datetime.strptime(expense_date, '%d/%m/%Y').date()

            serial_no = int(serial_no)
            amount = float(amount)

            print("The serial number is ",serial_no)
            print("The expense name  is ", expense_name)
            print("The amount value is ", amount)
            print("The description  is ", description_text)
            print("The expense date  is ", expense_date)


            ins_query = "INSERT INTO dbo.EXPENSE_DETAILS VALUES(?,?,?,?,?)"
            data = (serial_no,expense_name,amount,description_text,expensedate)

            cur.execute(ins_query, data)
            connect.commit()
            connect.close()

            QMessageBox.information(self, 'Message', 'Data saved successfully')
            #self.save_btn.setEnabled(False)
            self.clearbtn()
            self.serial_generator()
            self.table_population()

    def clearbtn(self):
        self.expense_le.clear()
        self.amount_le.clear()
        self.description_te.clear()

    def closebtn(self):

        self.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    expense_dialog = QtWidgets.QDialog()
    #ui = Ui_expense_dialog()
    #ui.setupUi(expense_dialog)
    #expense_dialog.show()
    ui = Add_Expenses()
    ui.show()
    sys.exit(app.exec_())
