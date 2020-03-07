
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QCalendarWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import QDate,Qt
import datetime
import pyodbc
import os
import sys

class Ui_work_complete(object):
    def setupUi(self, work_complete):
        work_complete.setObjectName("work_complete")
        work_complete.resize(1259, 827)
        work_complete.setStyleSheet("#work_complete{\n"
"    \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 153, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(work_complete)
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
        self.from_cal_tool_btn = QtWidgets.QToolButton(work_complete)
        self.from_cal_tool_btn.setGeometry(QtCore.QRect(720, 160, 30, 32))
        self.from_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.from_cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.from_cal_tool_btn.setIcon(icon)
        self.from_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.from_cal_tool_btn.setObjectName("from_cal_tool_btn")
        self.from_date = QtWidgets.QLineEdit(work_complete)
        self.from_date.setGeometry(QtCore.QRect(530, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.from_date.setFont(font)
        self.from_date.setObjectName("from_date")
        self.from_label = QtWidgets.QLabel(work_complete)
        self.from_label.setGeometry(QtCore.QRect(449, 160, 81, 31))
        self.from_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.from_label.setObjectName("from_label")
        self.to_cal_tool_btn = QtWidgets.QToolButton(work_complete)
        self.to_cal_tool_btn.setGeometry(QtCore.QRect(1121, 160, 30, 32))
        self.to_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.to_cal_tool_btn.setText("")
        self.to_cal_tool_btn.setIcon(icon)
        self.to_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.to_cal_tool_btn.setObjectName("to_cal_tool_btn")
        self.to_date = QtWidgets.QLineEdit(work_complete)
        self.to_date.setGeometry(QtCore.QRect(931, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.to_date.setFont(font)
        self.to_date.setObjectName("to_date")
        self.to_label = QtWidgets.QLabel(work_complete)
        self.to_label.setGeometry(QtCore.QRect(850, 160, 81, 31))
        self.to_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.to_label.setObjectName("to_label")
        self.finish_btn = QtWidgets.QPushButton(work_complete)
        self.finish_btn.setGeometry(QtCore.QRect(100, 150, 291, 61))
        self.finish_btn.setStyleSheet("#finish_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;\n"
"font:bold;} \n "
"#finish_btn:pressed{border-style:solid;border-width:9px}"                                      )
        self.finish_btn.setObjectName("finish_btn")
        self.finish_frame = QtWidgets.QFrame(work_complete)
        self.finish_frame.setGeometry(QtCore.QRect(20, 240, 1221, 541))
        self.finish_frame.setStyleSheet("#finish_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.finish_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.finish_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.finish_frame.setObjectName("finish_frame")
        self.finish_table = QtWidgets.QTableWidget(self.finish_frame)
        self.finish_table.setGeometry(QtCore.QRect(20, 20, 1181, 501))
        self.finish_table.setStyleSheet("#finish_table{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));}")
        self.finish_table.setObjectName("finish_table")
        self.finish_table.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.finish_table.setHorizontalHeaderItem(9, item)
        self.groupBox = QtWidgets.QGroupBox(work_complete)
        self.groupBox.setGeometry(QtCore.QRect(430, 110, 751, 111))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"  \n"
"    border: 3px solid brown;\n"
"    border-radius: 15px;\n"
"    margin-top: 6px;\n"
"    color:black;\n"
"    font: 75 13pt \"Calibri\";\n"
"     font: bold;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(64, 136, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position :top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.frame.raise_()
        self.from_cal_tool_btn.raise_()
        self.from_date.raise_()
        self.from_label.raise_()
        self.to_cal_tool_btn.raise_()
        self.to_date.raise_()
        self.to_label.raise_()
        self.finish_btn.raise_()
        self.finish_frame.raise_()

        self.retranslateUi(work_complete)
        QtCore.QMetaObject.connectSlotsByName(work_complete)

    def retranslateUi(self, work_complete):
        _translate = QtCore.QCoreApplication.translate
        work_complete.setWindowTitle(_translate("work_complete", "Dialog"))
        self.title_label.setText(_translate("work_complete", "Finished Orders"))
        self.from_label.setText(_translate("work_complete", "From :"))
        self.to_label.setText(_translate("work_complete", "To  :"))
        self.finish_btn.setText(_translate("work_complete", "Show All Finished"))
        item = self.finish_table.horizontalHeaderItem(0)
        item.setText(_translate("work_complete", "Bill No"))
        item = self.finish_table.horizontalHeaderItem(1)
        item.setText(_translate("work_complete", "Customer Name"))
        item = self.finish_table.horizontalHeaderItem(2)
        item.setText(_translate("work_complete", "Phone No"))
        item = self.finish_table.horizontalHeaderItem(3)
        item.setText(_translate("work_complete", "Event Name"))
        item = self.finish_table.horizontalHeaderItem(4)
        item.setText(_translate("work_complete", "Booking Date"))
        item = self.finish_table.horizontalHeaderItem(5)
        item.setText(_translate("work_complete", "Total Amount"))
        item = self.finish_table.horizontalHeaderItem(6)
        item.setText(_translate("work_complete", "Start Date"))
        item = self.finish_table.horizontalHeaderItem(7)
        item.setText(_translate("work_complete", "Finish Date"))
        item = self.finish_table.horizontalHeaderItem(8)
        item.setText(_translate("work_complete", "Studio Name"))
        item = self.finish_table.horizontalHeaderItem(9)
        item.setText(_translate("work_complete", "Status"))
        self.groupBox.setTitle(_translate("work_complete", "Select Date Range"))

class Work_Complete_Page(QDialog,Ui_work_complete):
    def __init__(self,parent=None):
        super(Work_Complete_Page,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Work Completed")

        self.table_records()

        self.from_cal_tool_btn.clicked.connect(self.from_calender)
        self.to_cal_tool_btn.clicked.connect(self.to_calender)
        self.current_date()
        self.table_population()
        self.finish_btn.clicked.connect(self.table_population)

        config_name = 'work_complete.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))


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
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def from_calender(self):
        self.from_calender = QCalendarWidget()
        self.from_calender.setMinimumDate(QDate(1900,1,1))
        self.from_calender.setMaximumDate(QDate(2999,12,31))
        self.from_calender.setGridVisible(True)
        self.from_calender.clicked.connect(self.from_updatedate)
        self.from_calender.setWindowModality(Qt.ApplicationModal)
        self.from_calender.setWindowTitle("Delivery Date")
        self.from_calender.show()

    def to_calender(self):
        self.to_calender = QCalendarWidget()
        self.to_calender.setMinimumDate(QDate(1900,1,1))
        self.to_calender.setMaximumDate(QDate(2999,12,31))
        self.to_calender.setGridVisible(True)
        self.to_calender.clicked.connect(self.to_updatedate)
        self.to_calender.setWindowModality(Qt.ApplicationModal)
        self.to_calender.setWindowTitle("Delivery Date")
        self.to_calender.show()


    def from_updatedate(self,*args):

        getdate = self.from_calender.selectedDate().toString("dd-MMM-yyyy")
        print('From date value is ',getdate)
        self.from_date.setText(getdate)
        self.from_calender.deleteLater()

    def to_updatedate(self,*args):

        getdate = self.to_calender.selectedDate().toString("dd-MMM-yyyy")
        print('to date value is ',getdate)
        self.to_date.setText(getdate)
        self.to_calender.deleteLater()

    def current_date(self):
        now = QDate.currentDate()
        print(now)
        print(now.toString(Qt.ISODate))

        today = datetime.date.today()

        date_format = today.strftime("%d-%b-%Y")
        print(date_format)

        self.from_date.setText(date_format)
        self.to_date.setText(date_format)

    def table_population(self):
        self.connectdb()

        self.finish_table.setRowCount(0)

        from_date = self.from_date.text()
        from_date =datetime.datetime.strptime(from_date,'%d-%b-%Y').date()
        print("The from date value is ",from_date)
        to_date = self.to_date.text()
        to_date=datetime.datetime.strptime(to_date,'%d-%b-%Y').date()

        select_query = "SELECT BILL_NO,CUSTOMER_NAME,PHONE_NO,EVENT_NAME,BOOKING_DATE,TOTAL_AMOUNT,\
                        WORK_START_DATE,WORK_FINISH_DATE,STUDIO_NAME,STATUS FROM dbo.WORK_ALLOCATE \
                        WHERE STATUS ='COMPLETED' AND WORK_FINISH_DATE BETWEEN ? AND ?"

        cur.execute(select_query,(from_date,to_date))

        result = cur.fetchall()

        print("result is",result)

        result_check = len(result)

        print("The total number of records fetched from table is ", result_check)

        if result_check >= 1:
                new_result = []
                column_count = self.finish_table.columnCount()
                for row in range(result_check):
                        tuple_value = list(result[row])
                        tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                        tuple_value[6] = tuple_value[6].strftime('%d/%m/%Y')
                        tuple_value[7] = tuple_value[7].strftime('%d/%m/%Y')
                        tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                        # tuple_value.extend(self.work_finish)
                        print('the modified tuple value is ', tuple_value)

                        self.finish_table.insertRow(row)
                        for column in range(column_count):
                                print("the row number is ", row)
                                print("the column number is", column)
                                value = tuple_value[column]

                                self.finish_table.setItem(row, column, self.table_item(value,
                                                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled))





    def table_item(self, text, flag):

            tablewidgetitem = QTableWidgetItem(text)
            tablewidgetitem.setFlags(flag)
            return tablewidgetitem




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    work_complete = QtWidgets.QDialog()
    #ui = Ui_work_complete()
    #ui.setupUi(work_complete)
    #work_complete.show()
    ui = Work_Complete_Page()
    ui.show()
    sys.exit(app.exec_())
