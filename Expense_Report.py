
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox,QFileDialog,QTableWidget,QTableWidgetItem,QCalendarWidget
from PyQt5.QtCore import QDate,Qt
import pyodbc
import datetime
import xlsxwriter
import os
import sys


class Ui_expense_report(object):
    def setupUi(self, expense_report):
        expense_report.setObjectName("expense_report")
        expense_report.resize(1127, 855)
        expense_report.setStyleSheet("#expense_report{\n"
"    \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(169, 98, 130, 249), stop:0.81592 rgba(255, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(expense_report)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1351, 91))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(260, 20, 601, 51))
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
        self.groupBox = QtWidgets.QGroupBox(expense_report)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 691, 111))
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
        self.from_cal_tool_btn.setGeometry(QtCore.QRect(280, 50, 30, 32))
        self.from_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.from_cal_tool_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calendar-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.from_cal_tool_btn.setIcon(icon)
        self.from_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.from_cal_tool_btn.setObjectName("from_cal_tool_btn")
        self.to_cal_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.to_cal_tool_btn.setGeometry(QtCore.QRect(640, 50, 30, 32))
        self.to_cal_tool_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.to_cal_tool_btn.setText("")
        self.to_cal_tool_btn.setIcon(icon)
        self.to_cal_tool_btn.setIconSize(QtCore.QSize(30, 30))
        self.to_cal_tool_btn.setObjectName("to_cal_tool_btn")
        self.from_label = QtWidgets.QLabel(expense_report)
        self.from_label.setGeometry(QtCore.QRect(19, 160, 81, 31))
        self.from_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.from_label.setObjectName("from_label")
        self.to_date = QtWidgets.QLineEdit(expense_report)
        self.to_date.setGeometry(QtCore.QRect(461, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.to_date.setFont(font)
        self.to_date.setObjectName("to_date")
        self.from_date = QtWidgets.QLineEdit(expense_report)
        self.from_date.setGeometry(QtCore.QRect(100, 161, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.from_date.setFont(font)
        self.from_date.setObjectName("from_date")
        self.to_label = QtWidgets.QLabel(expense_report)
        self.to_label.setGeometry(QtCore.QRect(380, 160, 81, 31))
        self.to_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(170, 0, 0);\n"
"")
        self.to_label.setObjectName("to_label")
        self.expense_frame = QtWidgets.QFrame(expense_report)
        self.expense_frame.setGeometry(QtCore.QRect(10, 230, 1101, 491))
        self.expense_frame.setStyleSheet("#expense_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.expense_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.expense_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.expense_frame.setObjectName("expense_frame")
        self.expense_table = QtWidgets.QTableWidget(self.expense_frame)
        self.expense_table.setGeometry(QtCore.QRect(20, 20, 1061, 451))
        self.expense_table.setStyleSheet("#finish_table{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));}")
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
        self.total_le = QtWidgets.QLineEdit(expense_report)
        self.total_le.setEnabled(True)
        self.total_le.setGeometry(QtCore.QRect(329, 750, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setStyleSheet("color:red;")
        self.total_le.setObjectName("total_le")
        self.total_label = QtWidgets.QLabel(expense_report)
        self.total_label.setGeometry(QtCore.QRect(20, 750, 291, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_label.setObjectName("total_label")
        self.show_btn = QtWidgets.QPushButton(expense_report)
        self.show_btn.setGeometry(QtCore.QRect(770, 130, 191, 71))
        self.show_btn.setStyleSheet("#show_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:green;\n"
"font:bold;}\n"
"#show_btn:pressed{border-style:solid;\n"
"border-width:9px}")
        self.show_btn.setObjectName("show_btn")
        self.export_btn = QtWidgets.QPushButton(expense_report)
        self.export_btn.setGeometry(QtCore.QRect(620, 750, 191, 71))
        self.export_btn.setStyleSheet("#export_btn{background-color: qlineargradient(spread:pad, x1:0.0348259, y1:0.085, x2:1, y2:1, stop:0 rgba(235, 107, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:brown;\n"
"font:bold;}\n"
"#export_btn:pressed{border-style:solid;\n"
"border-width:9px}")
        self.export_btn.setObjectName("export_btn")
        self.close_btn = QtWidgets.QPushButton(expense_report)
        self.close_btn.setGeometry(QtCore.QRect(870, 750, 191, 71))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 28, 21, 249), stop:0.81592 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:red;\n"
"font:bold;}\n"
"#close_btn:pressed{border-style:solid;\n"
"border-width:9px}")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(expense_report)
        QtCore.QMetaObject.connectSlotsByName(expense_report)

    def retranslateUi(self, expense_report):
        _translate = QtCore.QCoreApplication.translate
        expense_report.setWindowTitle(_translate("expense_report", "Dialog"))
        self.title_label.setText(_translate("expense_report", "Expense Reports"))
        self.groupBox.setTitle(_translate("expense_report", "Search By Date"))
        self.from_label.setText(_translate("expense_report", "From :"))
        self.to_label.setText(_translate("expense_report", "To  :"))
        item = self.expense_table.horizontalHeaderItem(0)
        item.setText(_translate("expense_report", "Sl No"))
        item = self.expense_table.horizontalHeaderItem(1)
        item.setText(_translate("expense_report", "Expense Details"))
        item = self.expense_table.horizontalHeaderItem(2)
        item.setText(_translate("expense_report", "Amount"))
        item = self.expense_table.horizontalHeaderItem(3)
        item.setText(_translate("expense_report", "Description"))
        item = self.expense_table.horizontalHeaderItem(4)
        item.setText(_translate("expense_report", "Date"))
        self.total_label.setText(_translate("expense_report", "Total Expense Amount (Rs.)       :"))
        self.show_btn.setText(_translate("expense_report", "Show Report"))
        self.export_btn.setText(_translate("expense_report", "Export Report"))
        self.close_btn.setText(_translate("expense_report", "Close"))

class Expense_Report_Page(QDialog,Ui_expense_report):
    def __init__(self,parent=None):
        super(Expense_Report_Page,self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Expense Report")

        self.table_records()

        self.from_cal_tool_btn.clicked.connect(self.from_calender)
        self.to_cal_tool_btn.clicked.connect(self.to_calender)
        self.current_date()

        self.show_btn.clicked.connect(self.table_population)
        self.export_btn.clicked.connect(self.exportbtn)
        self.close_btn.clicked.connect(self.closebtn)

        config_name = 'expense_report.cfg'

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
        self.expense_table.setRowCount(0)
        self.expense_table.verticalHeader().setVisible(False)
        header = self.expense_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
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

        self.expense_table.setRowCount(0)

        from_date = self.from_date.text()
        from_date =datetime.datetime.strptime(from_date,'%d-%b-%Y').date()
        self.table_from_date =from_date
        print("The from date value is ",from_date)
        to_date = self.to_date.text()
        to_date=datetime.datetime.strptime(to_date,'%d-%b-%Y').date()
        self.table_to_date = to_date

        select_query = "SELECT ROW_NUMBER() OVER (ORDER BY EXPENSE_DATE DESC) RNO,EXPENSE_NAME,AMOUNT,DESCRIPTION,EXPENSE_DATE FROM dbo.EXPENSE_DETAILS \
                         WHERE EXPENSE_DATE BETWEEN ? AND ?"



        cur.execute(select_query, (from_date, to_date,))
        result = cur.fetchall()


        print("result is", result)

        self.data_result = [data for data in result]

        result_check = len(result)

        self.total_amount = 0


        if result_check >= 1:
            new_result = []
            column_count = self.expense_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value[4] = tuple_value[4].strftime('%d/%m/%Y')
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                # tuple_value.extend(self.work_finish)
                print('the modified tuple value is ', tuple_value)
                self.total_amount = self.total_amount+int(float(tuple_value[2]))

                self.expense_table.insertRow(row)
                for column in range(column_count):
                        value = tuple_value[column]

                        self.expense_table.setItem(row, column, self.table_item(value,
                                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled))

            print("The total amount value is ", self.total_amount)


            self.total_le.setText(str(round(float(self.total_amount), 2)))



    def table_item(self, text, flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def exportbtn(self):

        if self.expense_table.rowCount() >=1:
                file_path =QFileDialog.getSaveFileName(self, 'Export to Excel', "Expenses_Report_"+self.table_from_date.strftime("%d_%b_%Y")+ "_to_"+self.table_to_date.strftime("%d_%b_%Y")+".xlsx", 'Excel files (.xlsx) ;; All Files ()')

                print("the file path value is ",file_path)

                if file_path != ('', ''):

                    print("File path is",file_path)

                    excel_book_name  = file_path[0]

                    workbook = xlsxwriter.Workbook(excel_book_name)
                    worksheet = workbook.add_worksheet("Expense Report")

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


                    title =["SL_NO","EXPENSE_NAME","AMOUNT","DESCRIPTION","EXPENSE_DATE"]
                    title_size =[len(i) for i in title]
                    print('the  title size is',title_size)

                    for col in range(0,len(title)):

                        worksheet.write(0,col,title[col],title_format)

                    for row_level in range(len(data_modified)):
                        for col_level in range(len(data_modified[0])):


                            if col_level ==2:
                                value = int(float(data_modified[row_level][col_level]))
                                worksheet.write(row_level + 1, col_level, value, money_format)
                            else:
                                value = data_modified[row_level][col_level]
                                worksheet.write(row_level+1,col_level,value,cell_format)

                    print ( " the row number value is",row_level)



                    footer_list =["Total Expense Amount :"]

                    total = int(float(self.total_amount))


                    footer_amt_list =[total]

                    footer_format = workbook.add_format()
                    footer_format.set_border()
                    footer_format.set_bold(True)
                    footer_format.set_font_size(14)

                    footer_money_format = workbook.add_format()
                    footer_money_format.set_border()
                    footer_money_format.set_bold(True)
                    footer_money_format.set_num_format('#,##0.00')
                    footer_money_format.set_font_color('red')
                    footer_money_format.set_font_size(14)

                    row_num =row_level +6
                    for i in range(1):
                        footer_format.set_font_color('black')
                        worksheet.merge_range(row_num,0,row_num,2,footer_list[i],footer_format)
                        worksheet.write(row_num, 3, footer_amt_list[i], footer_money_format)

                        row_num+=1
                    worksheet.set_column(0,0,8)
                    worksheet.set_column(3,3, 22)
                    worksheet.set_column(1,1, 18)
                    worksheet.set_column(2, 2, 10)
                    worksheet.set_column(4, 4, 13)


                    workbook.close()

                    QMessageBox.information(self,"File Export","Expense Report Exported Successfully...")
        else:
                QMessageBox.warning(self,"Warning", "Please click show button to get data and then select Export")


    def closebtn(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    expense_report = QtWidgets.QDialog()
    #ui = Ui_expense_report()
    #ui.setupUi(expense_report)
    #expense_report.show()
    ui =Expense_Report_Page()
    ui.show()
    sys.exit(app.exec_())
