
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox,QFileDialog,QTableWidget,QTableWidgetItem,QCalendarWidget
from PyQt5.QtCore import QDate,Qt
import pyodbc
import datetime
import xlsxwriter
import os
import sys

class Ui_daily_report(object):
    def setupUi(self, daily_report):
        daily_report.setObjectName("daily_report")
        daily_report.resize(1343, 938)
        daily_report.setStyleSheet("#daily_report{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.238806 rgba(101, 186, 0, 255), stop:0.840796 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(daily_report)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1351, 91))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(350, 20, 601, 51))
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
        self.groupBox = QtWidgets.QGroupBox(daily_report)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 1021, 111))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"  \n"
"    border: 3px solid brown;\n"
"    border-radius: 15px;\n"
"    margin-top: 6px;\n"
"    color:black;\n"
"    font: 75 13pt \"Calibri\";\n"
"     font: bold;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(137, 104, 235, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position :top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.from_cal_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.from_cal_tool_btn.setGeometry(QtCore.QRect(590, 50, 30, 32))
        self.from_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.from_cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.from_cal_tool_btn.setIcon(icon)
        self.from_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.from_cal_tool_btn.setObjectName("from_cal_tool_btn")
        self.to_cal_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.to_cal_tool_btn.setGeometry(QtCore.QRect(950, 50, 30, 32))
        self.to_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.to_cal_tool_btn.setText("")
        self.to_cal_tool_btn.setIcon(icon)
        self.to_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.to_cal_tool_btn.setObjectName("to_cal_tool_btn")
        self.show_all_radio = QtWidgets.QRadioButton(self.groupBox)
        self.show_all_radio.setGeometry(QtCore.QRect(60, 30, 161, 21))
        self.show_all_radio.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.show_all_radio.setChecked(True)
        self.show_all_radio.setObjectName("show_all_radio")
        self.due_bill_radio = QtWidgets.QRadioButton(self.groupBox)
        self.due_bill_radio.setGeometry(QtCore.QRect(60, 70, 161, 21))
        self.due_bill_radio.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.due_bill_radio.setObjectName("due_bill_radio")
        self.from_label = QtWidgets.QLabel(daily_report)
        self.from_label.setGeometry(QtCore.QRect(329, 160, 81, 31))
        self.from_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.from_label.setObjectName("from_label")
        self.to_date = QtWidgets.QLineEdit(daily_report)
        self.to_date.setGeometry(QtCore.QRect(771, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.to_date.setFont(font)
        self.to_date.setObjectName("to_date")
        self.from_date = QtWidgets.QLineEdit(daily_report)
        self.from_date.setGeometry(QtCore.QRect(410, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.from_date.setFont(font)
        self.from_date.setObjectName("from_date")
        self.to_label = QtWidgets.QLabel(daily_report)
        self.to_label.setGeometry(QtCore.QRect(690, 160, 81, 31))
        self.to_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.to_label.setObjectName("to_label")
        self.daily_frame = QtWidgets.QFrame(daily_report)
        self.daily_frame.setGeometry(QtCore.QRect(10, 230, 1321, 491))
        self.daily_frame.setStyleSheet("#daily_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.daily_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.daily_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.daily_frame.setObjectName("daily_frame")
        self.daily_table = QtWidgets.QTableWidget(self.daily_frame)
        self.daily_table.setGeometry(QtCore.QRect(20, 20, 1281, 451))
        self.daily_table.setStyleSheet("#finish_table{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));}")
        self.daily_table.setObjectName("daily_table")
        self.daily_table.setColumnCount(13)
        self.daily_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.daily_table.setHorizontalHeaderItem(12, item)
        self.recieved_label = QtWidgets.QLabel(daily_report)
        self.recieved_label.setGeometry(QtCore.QRect(20, 792, 281, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.total_le = QtWidgets.QLineEdit(daily_report)
        self.total_le.setEnabled(True)
        self.total_le.setGeometry(QtCore.QRect(329, 732, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setStyleSheet("color:brown;")
        self.total_le.setObjectName("total_le")
        self.total_label = QtWidgets.QLabel(daily_report)
        self.total_label.setGeometry(QtCore.QRect(20, 732, 281, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_label.setObjectName("total_label")
        self.due_label = QtWidgets.QLabel(daily_report)
        self.due_label.setGeometry(QtCore.QRect(20, 852, 281, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.due_label.setObjectName("due_label")
        self.recieved_le = QtWidgets.QLineEdit(daily_report)
        self.recieved_le.setEnabled(True)
        self.recieved_le.setGeometry(QtCore.QRect(330, 793, 241, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 216, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 216, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.recieved_le.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.recieved_le.setFont(font)
        self.recieved_le.setStyleSheet("color:green;")
        self.recieved_le.setObjectName("recieved_le")
        self.due_le = QtWidgets.QLineEdit(daily_report)
        self.due_le.setEnabled(True)
        self.due_le.setGeometry(QtCore.QRect(330, 854, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.due_le.setFont(font)
        self.due_le.setStyleSheet("color:red;")
        self.due_le.setObjectName("due_le")
        self.total_orders_label = QtWidgets.QLabel(daily_report)
        self.total_orders_label.setGeometry(QtCore.QRect(650, 734, 221, 41))
        self.total_orders_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_orders_label.setObjectName("total_orders_label")
        self.total_order_label_value = QtWidgets.QLabel(daily_report)
        self.total_order_label_value.setGeometry(QtCore.QRect(867, 735, 41, 41))
        self.total_order_label_value.setStyleSheet("font: 75 16pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_order_label_value.setObjectName("total_order_label_value")
        self.total_due_label = QtWidgets.QLabel(daily_report)
        self.total_due_label.setGeometry(QtCore.QRect(650, 784, 221, 41))
        self.total_due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_due_label.setObjectName("total_due_label")
        self.total_due_label_value = QtWidgets.QLabel(daily_report)
        self.total_due_label_value.setGeometry(QtCore.QRect(867, 785, 51, 41))
        self.total_due_label_value.setStyleSheet("font: 75 16pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_due_label_value.setObjectName("total_due_label_value")
        self.show_btn = QtWidgets.QPushButton(daily_report)
        self.show_btn.setGeometry(QtCore.QRect(630, 844, 191, 71))
        self.show_btn.setStyleSheet("#show_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;\n"
"font:bold;} \n"
"#show_btn:pressed{border-style:solid; border-width :7px}"                                    )

        self.show_btn.setObjectName("show_btn")
        self.export_btn = QtWidgets.QPushButton(daily_report)
        self.export_btn.setGeometry(QtCore.QRect(850, 844, 191, 71))
        self.export_btn.setStyleSheet("#export_btn{background-color: qlineargradient(spread:pad, x1:0.0348259, y1:0.085, x2:1, y2:1, stop:0 rgba(235, 107, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:brown;\n"
"font:bold;} \n"
"#export_btn:pressed{border-style:solid; border-width:7px}"                                      )
        self.export_btn.setObjectName("export_btn")
        self.close_btn = QtWidgets.QPushButton(daily_report)
        self.close_btn.setGeometry(QtCore.QRect(1070, 844, 191, 71))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 28, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:red;\n"
"font:bold;} \n"
"#close_btn:pressed{border-style:solid;border-width:7px}"                                     )
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(daily_report)
        QtCore.QMetaObject.connectSlotsByName(daily_report)

    def retranslateUi(self, daily_report):
        _translate = QtCore.QCoreApplication.translate
        daily_report.setWindowTitle(_translate("daily_report", "Dialog"))
        self.title_label.setText(_translate("daily_report", "View All Daily Reports"))
        self.groupBox.setTitle(_translate("daily_report", "Search By Date"))
        self.show_all_radio.setText(_translate("daily_report", "Show All Bills"))
        self.due_bill_radio.setText(_translate("daily_report", "Due Bills Only"))
        self.from_label.setText(_translate("daily_report", "From :"))
        self.to_label.setText(_translate("daily_report", "To  :"))
        item = self.daily_table.horizontalHeaderItem(0)
        item.setText(_translate("daily_report", "Bill No"))
        item = self.daily_table.horizontalHeaderItem(1)
        item.setText(_translate("daily_report", "Sno"))
        item = self.daily_table.horizontalHeaderItem(2)
        item.setText(_translate("daily_report", "Date"))
        item = self.daily_table.horizontalHeaderItem(3)
        item.setText(_translate("daily_report", "Category"))
        item = self.daily_table.horizontalHeaderItem(4)
        item.setText(_translate("daily_report", "Frame Size"))
        item = self.daily_table.horizontalHeaderItem(5)
        item.setText(_translate("daily_report", "Rate"))
        item = self.daily_table.horizontalHeaderItem(6)
        item.setText(_translate("daily_report", "Qty"))
        item = self.daily_table.horizontalHeaderItem(7)
        item.setText(_translate("daily_report", "Amount"))
        item = self.daily_table.horizontalHeaderItem(8)
        item.setText(_translate("daily_report", "Total Amount"))
        item = self.daily_table.horizontalHeaderItem(9)
        item.setText(_translate("daily_report", "Amt Recieved"))
        item = self.daily_table.horizontalHeaderItem(10)
        item.setText(_translate("daily_report", "Amt Due"))
        item = self.daily_table.horizontalHeaderItem(11)
        item.setText(_translate("daily_report", "Cust Name"))
        item = self.daily_table.horizontalHeaderItem(12)
        item.setText(_translate("daily_report", "Phone No"))
        self.recieved_label.setText(_translate("daily_report", "Total Amount Recieved (Rs.)  :"))
        self.total_label.setText(_translate("daily_report", "Total Order Amount (Rs.)         :"))
        self.due_label.setText(_translate("daily_report", "Total Due Amount (Rs.)              :"))
        self.total_orders_label.setText(_translate("daily_report", "Total No. Of Orders        :"))
        self.total_order_label_value.setText(_translate("daily_report", "0"))
        self.total_due_label.setText(_translate("daily_report", "Total No. Of Due Bills    :"))
        self.total_due_label_value.setText(_translate("daily_report", "0"))
        self.show_btn.setText(_translate("daily_report", "Show Report"))
        self.export_btn.setText(_translate("daily_report", "Export Report"))
        self.close_btn.setText(_translate("daily_report", "Close"))


class Daily_Report_Page(QDialog,Ui_daily_report):
    def __init__(self,parent=None):
        super(Daily_Report_Page,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Daily Bill Report")

        self.table_records()

        self.from_cal_tool_btn.clicked.connect(self.from_calender)
        self.to_cal_tool_btn.clicked.connect(self.to_calender)
        self.current_date()
        #self.table_population()

        self.show_btn.clicked.connect(self.table_population)
        self.export_btn.clicked.connect(self.exportbtn)
        self.close_btn.clicked.connect(self.closebtn)

        config_name = 'daily_report.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        excel_image = os.path.join(application_path, "images", "excel.png")
        close_image = os.path.join(application_path, "images", "close.png")
        show_image = os.path.join(application_path, "images", "search.png")

        self.export_btn.setIcon(QtGui.QIcon(excel_image))
        self.export_btn.setIconSize(QtCore.QSize(30, 30))

        self.close_btn.setIcon(QtGui.QIcon(close_image))
        self.close_btn.setIconSize(QtCore.QSize(30, 30))

        self.show_btn.setIcon(QtGui.QIcon(show_image))
        self.show_btn.setIconSize(QtCore.QSize(30, 30))


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
        self.daily_table.setRowCount(0)
        self.daily_table.verticalHeader().setVisible(False)
        header = self.daily_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("QHeaderView::section { border: 1px solid ;}")

    def from_calender(self):
        self.from_calender = QCalendarWidget()
        self.from_calender.setMinimumDate(QDate(1900,1,1))
        self.from_calender.setMaximumDate(QDate(2999,12,31))
        self.from_calender.setGridVisible(True)
        self.from_calender.clicked.connect(self.from_updatedate)
        self.from_calender.setWindowModality(Qt.ApplicationModal)
        self.from_calender.setWindowTitle("From Date")
        self.from_calender.show()

    def to_calender(self):
        self.to_calender = QCalendarWidget()
        self.to_calender.setMinimumDate(QDate(1900,1,1))
        self.to_calender.setMaximumDate(QDate(2999,12,31))
        self.to_calender.setGridVisible(True)
        self.to_calender.clicked.connect(self.to_updatedate)
        self.to_calender.setWindowModality(Qt.ApplicationModal)
        self.to_calender.setWindowTitle("To Date")
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

        self.daily_table.setRowCount(0)

        from_date = self.from_date.text()
        from_date =datetime.datetime.strptime(from_date,'%d-%b-%Y').date()
        self.table_from_date =from_date
        print("The from date value is ",from_date)
        to_date = self.to_date.text()
        to_date=datetime.datetime.strptime(to_date,'%d-%b-%Y').date()
        self.table_to_date = to_date

        select_query_all = "SELECT BILL.BILL_NO,ROW_NUMBER() OVER( PARTITION BY BILL.BILL_NO ORDER BY CATEGORY) SLNO,\
                                BILL.BILLING_DATE,CATEGORY,ORD.SIZE,ORD.RATE,ORD.QTY,ORD.TOTAL_AMOUNT,BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,\
                                BILL.AMOUNT_DUE,BILL.CUSTOMER_NAME,BILL.PHONE_NO \
                                FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND BILLING_DATE BETWEEN ? AND ? ORDER BY BILL.BILL_NO"

        select_query_due = "SELECT BILL.BILL_NO,ROW_NUMBER() OVER( PARTITION BY BILL.BILL_NO ORDER BY CATEGORY) SLNO,\
                                BILL.BILLING_DATE,CATEGORY,ORD.SIZE,ORD.RATE,ORD.QTY,ORD.TOTAL_AMOUNT,BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,\
                                BILL.AMOUNT_DUE,BILL.CUSTOMER_NAME,BILL.PHONE_NO \
                                FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND AMOUNT_DUE <> 0 AND BILLING_DATE BETWEEN ? AND ? \
                                ORDER BY BILL.BILL_NO"

        select_count_all = "SELECT COUNT(DISTINCT BILL.BILL_NO) BILL_COUNT ,(SELECT COUNT(A.AMOUNT_DUE) FROM \
                                (SELECT BILL.BILL_NO, AMOUNT_DUE FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL \
                                 ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND BILLING_DATE BETWEEN ? AND ? AND  \
                                AMOUNT_DUE<>0 GROUP BY BILL.BILL_NO,AMOUNT_DUE) AS A) DUE_COUNT  FROM DBO.ORDER_DETAILS ORD \
                                INNER JOIN DBO.BILLING_TABLE BILL ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND BILLING_DATE BETWEEN ? AND ? "

        select_count_due = "SELECT COUNT(DISTINCT BILL.BILL_NO) BILL_COUNT ,(SELECT COUNT(A.AMOUNT_DUE) FROM \
                                (SELECT BILL.BILL_NO, AMOUNT_DUE FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL \
                                 ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND BILLING_DATE BETWEEN ? AND ? AND  \
                                AMOUNT_DUE<>0 GROUP BY BILL.BILL_NO,AMOUNT_DUE) AS A) DUE_COUNT  FROM DBO.ORDER_DETAILS ORD \
                                INNER JOIN DBO.BILLING_TABLE BILL ON \
                                ORD.BILL_NO = BILL.BILL_NO \
                                WHERE BILL_TYPE ='DAILY' AND BILLING_DATE BETWEEN ? AND ? AND AMOUNT_DUE<>0 "



        if self.show_all_radio.isChecked():
                cur.execute(select_query_all, (from_date, to_date,))
                result = cur.fetchall()
                cur.execute(select_count_all,(from_date,to_date,from_date, to_date))
                count_result =cur.fetchone()
        else:
                cur.execute(select_query_due, (from_date, to_date))
                result = cur.fetchall()
                cur.execute(select_count_due, (from_date, to_date,from_date, to_date))
                count_result = cur.fetchone()

        print("result is", result)

        self.data_result = [data for data in result]

        result_check = len(result)

        self.total_amount = 0
        self.amount_recieved = 0
        self.due_amount = 0
        self.prev_row_bill_no = None

        if result_check >= 1:
            new_result = []
            column_count = self.daily_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value[2] = tuple_value[2].strftime('%d/%m/%Y')
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                # tuple_value.extend(self.work_finish)
                print('the modified tuple value is ', tuple_value)
                current_row_bill_no = tuple_value[0]

                if (current_row_bill_no != self.prev_row_bill_no) or self.prev_row_bill_no== None:
                    self.total_amount = self.total_amount+int(float(tuple_value[8]))
                    self.amount_recieved = self.amount_recieved + int(float(tuple_value[9]))
                    self.due_amount = self.due_amount+ int(float(tuple_value[10]))

                self.prev_row_bill_no =tuple_value[0]
                self.daily_table.insertRow(row)
                for column in range(column_count):
                        value = tuple_value[column]

                        self.daily_table.setItem(row, column, self.table_item(value,
                                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled))

            print("The total amount value is ", self.total_amount)
            print("The total amount recieved value is ", self.amount_recieved)
            print("The total due amount value is ", self.due_amount)

            self.total_le.setText(str(round(float(self.total_amount), 2)))
            self.recieved_le.setText(str(round(float(self.amount_recieved), 2)))
            self.due_le.setText(str(round(float(self.due_amount), 2)))

            print("The count values are",count_result)
            bill_count = str(count_result[0])
            due_count = str(count_result[1])

            self.total_order_label_value.setText(bill_count)
            self.total_due_label_value.setText(due_count)

    def table_item(self, text, flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def exportbtn(self):

        if self.daily_table.rowCount() >=1:
                file_path =QFileDialog.getSaveFileName(self, 'Export to Excel', "Daily_Bill_Report_"+self.table_from_date.strftime("%d_%b_%Y")+ "_to_"+self.table_to_date.strftime("%d_%b_%Y")+".xlsx", 'Excel files (.xlsx) ;; All Files ()')

                if file_path != ('', ''):

                    print("File path is",file_path)

                    excel_book_name  = file_path[0]

                    workbook = xlsxwriter.Workbook(excel_book_name)
                    worksheet = workbook.add_worksheet("Today Report")

                    title_format = workbook.add_format({'bold' : True})
                    title_format.set_bg_color('yellow')
                    title_format.set_font_color('brown')
                    title_format.set_border()
                    data = self.data_result


                    cell_format = workbook.add_format()
                    cell_format.set_border()

                    money_format = workbook.add_format()
                    money_format.set_border()
                    money_format.set_num_format('#,##0.00')


                    print("The first data is ",data)
                    print("check value",data[0][0])
                    data_modified =[]
                    list_value = []

                    data_modified = [tuple(str(item) for item in i) for i in data]



                    print ( "The workbook Name is ",excel_book_name)


                    title =["BILL_NO","SL_NO","DATE","CATEGORY","FRAME_SIZE","RATE","QTY","AMOUNT","TOTAL_AMOUNT","AMOUNT_RECIEVED",
                            "AMOUNT_DUE","CUSTOMER_NAME","PHONE_NO"]
                    title_size =[len(i) for i in title]
                    print('the  title size is',title_size)

                    for col in range(0,len(title)):

                        worksheet.write(0,col,title[col],title_format)

                    for row_level in range(len(data_modified)):
                        for col_level in range(len(data_modified[0])):
                            col_list =[5,7,7,9,10]

                            if col_level in col_list:
                                value = int(float(data_modified[row_level][col_level]))
                                worksheet.write(row_level + 1, col_level, value, money_format)
                            else:
                                value = data_modified[row_level][col_level]
                                worksheet.write(row_level+1,col_level,value,cell_format)

                    print ( " the row number value is",row_level)



                    footer_list =["Total Order Amount :","Total Recieved :","Due Amount :"]

                    total = int(float(self.total_amount))
                    recieved = int(float(self.amount_recieved))
                    due =int(float(self.due_amount))

                    footer_amt_list =[total,recieved,due]

                    footer_format = workbook.add_format()
                    footer_format.set_border()
                    footer_format.set_bold(True)
                    footer_format.set_font_size(14)

                    footer_money_format = workbook.add_format()
                    footer_money_format.set_border()
                    footer_money_format.set_bold(True)
                    footer_money_format.set_num_format('#,##0.00')
                    footer_money_format.set_font_color('green')
                    footer_money_format.set_font_size(14)


                    footer_money_format_due = workbook.add_format()
                    footer_money_format_due.set_border()
                    footer_money_format_due.set_bold(True)
                    footer_money_format_due.set_num_format('#,##0.00')
                    footer_money_format_due.set_font_color('red')
                    footer_money_format_due.set_font_size(14)




                    row_num =row_level +6
                    for i in range(3):
                        footer_format.set_font_color('black')
                        worksheet.merge_range(row_num,0,row_num,2,footer_list[i],footer_format)
                        if i==2:
                            worksheet.set_column(row_num,3,12)
                            worksheet.write(row_num, 3, footer_amt_list[i], footer_money_format_due)

                        else:
                            worksheet.set_column(row_num, 3, 12)
                            worksheet.write(row_num, 3, footer_amt_list[i], footer_money_format)

                        row_num+=1
                    worksheet.set_column(0,2,10)


                    workbook.close()

                    QMessageBox.information(self,"File Export","Daily Report Exported Successfully...")
        else:
                QMessageBox.warning(self,"Warning", "Please click show button to get data and then select Export")


    def closebtn(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    daily_report = QtWidgets.QDialog()
    #ui = Ui_daily_report()
    #ui.setupUi(daily_report)
    #daily_report.show()
    ui =Daily_Report_Page()
    ui.show()
    sys.exit(app.exec_())