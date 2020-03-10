from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QTableWidgetItem,QTableWidget,QFileDialog,QMessageBox
from PyQt5.QtCore import Qt
import pyodbc
import datetime
import xlsxwriter
import os
import sys



class Ui_today_report_window(object):
    def setupUi(self, today_report_window):
        today_report_window.setObjectName("today_report_window")
        today_report_window.resize(1365, 855)
        today_report_window.setStyleSheet("#today_report_window{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.179104 rgba(62, 94, 125, 255), stop:0.661692 rgba(161, 255, 255, 255));}")
        self.frame = QtWidgets.QFrame(today_report_window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1371, 81))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(340, 20, 601, 51))
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
        self.today_frame = QtWidgets.QFrame(today_report_window)
        self.today_frame.setGeometry(QtCore.QRect(20, 200, 1321, 411))
        self.today_frame.setStyleSheet("#today_frame{border-width:1.5px;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-width:4px;}\n"
"")
        self.today_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.today_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.today_frame.setObjectName("today_frame")
        self.today_table = QtWidgets.QTableWidget(self.today_frame)
        self.today_table.setGeometry(QtCore.QRect(20, 20, 1281, 371))
        self.today_table.setStyleSheet("#finish_table{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));}")
        self.today_table.setObjectName("today_table")
        self.today_table.setColumnCount(12)
        self.today_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.today_table.setHorizontalHeaderItem(11, item)
        self.due_label = QtWidgets.QLabel(today_report_window)
        self.due_label.setGeometry(QtCore.QRect(40, 770, 281, 41))
        self.due_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);")
        self.due_label.setObjectName("due_label")
        self.due_le = QtWidgets.QLineEdit(today_report_window)
        self.due_le.setEnabled(True)
        self.due_le.setGeometry(QtCore.QRect(350, 772, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.due_le.setFont(font)
        self.due_le.setStyleSheet("color:red;")
        self.due_le.setObjectName("due_le")
        self.total_label = QtWidgets.QLabel(today_report_window)
        self.total_label.setGeometry(QtCore.QRect(40, 650, 281, 41))
        self.total_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.total_label.setObjectName("total_label")
        self.total_le = QtWidgets.QLineEdit(today_report_window)
        self.total_le.setEnabled(True)
        self.total_le.setGeometry(QtCore.QRect(349, 650, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.total_le.setFont(font)
        self.total_le.setStyleSheet("color:brown;")
        self.total_le.setObjectName("total_le")
        self.recieved_le = QtWidgets.QLineEdit(today_report_window)
        self.recieved_le.setEnabled(True)
        self.recieved_le.setGeometry(QtCore.QRect(350, 711, 241, 41))
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
        self.recieved_label = QtWidgets.QLabel(today_report_window)
        self.recieved_label.setGeometry(QtCore.QRect(40, 710, 281, 41))
        self.recieved_label.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(55, 55, 166);\n"
"")
        self.recieved_label.setObjectName("recieved_label")
        self.export_btn = QtWidgets.QPushButton(today_report_window)
        self.export_btn.setGeometry(QtCore.QRect(40, 120, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.export_btn.setFont(font)
        self.export_btn.setStyleSheet("#export_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(37, 125, 40, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 18pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#export_btn:pressed{border-style:solid;border-width:6px}")
        self.export_btn.setObjectName("export_btn")
        self.close_btn = QtWidgets.QPushButton(today_report_window)
        self.close_btn.setGeometry(QtCore.QRect(990, 720, 141, 71))
        self.close_btn.setStyleSheet("#close_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(159, 173, 84, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Calibri\";\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#close_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(today_report_window)
        QtCore.QMetaObject.connectSlotsByName(today_report_window)

    def retranslateUi(self, today_report_window):
        _translate = QtCore.QCoreApplication.translate
        today_report_window.setWindowTitle(_translate("today_report_window", "Dialog"))
        self.title_label.setText(_translate("today_report_window", "Today\'s Report"))
        item = self.today_table.horizontalHeaderItem(0)
        item.setText(_translate("today_report_window", "Bill No"))
        item = self.today_table.horizontalHeaderItem(1)
        item.setText(_translate("today_report_window", "Sno"))
        item = self.today_table.horizontalHeaderItem(2)
        item.setText(_translate("today_report_window", "Category"))
        item = self.today_table.horizontalHeaderItem(3)
        item.setText(_translate("today_report_window", "Frame Size"))
        item = self.today_table.horizontalHeaderItem(4)
        item.setText(_translate("today_report_window", "Rate"))
        item = self.today_table.horizontalHeaderItem(5)
        item.setText(_translate("today_report_window", "Qty"))
        item = self.today_table.horizontalHeaderItem(6)
        item.setText(_translate("today_report_window", "Amount"))
        item = self.today_table.horizontalHeaderItem(7)
        item.setText(_translate("today_report_window", "Total Amount"))
        item = self.today_table.horizontalHeaderItem(8)
        item.setText(_translate("today_report_window", "Amt Recieved"))
        item = self.today_table.horizontalHeaderItem(9)
        item.setText(_translate("today_report_window", "Amt Due"))
        item = self.today_table.horizontalHeaderItem(10)
        item.setText(_translate("today_report_window", "Cust Name"))
        item = self.today_table.horizontalHeaderItem(11)
        item.setText(_translate("today_report_window", "Phone No"))
        self.due_label.setText(_translate("today_report_window", "Total Due Amount (Rs.)              :"))
        self.total_label.setText(_translate("today_report_window", "Total Order Amount (Rs.)         :"))
        self.recieved_label.setText(_translate("today_report_window", "Total Amount Recieved (Rs.)  :"))
        self.export_btn.setText(_translate("today_report_window", "Export"))
        self.close_btn.setText(_translate("today_report_window", "Close"))

class Today_Report_Page(QDialog,Ui_today_report_window):
    def __init__(self,parent=None):
        super(Today_Report_Page,self).__init__(parent)
        self.setupUi(self)


        self.table_population()

        self.export_btn.clicked.connect(self.exportbtn)
        self.close_btn.clicked.connect(self.closebtn)

        self.setWindowTitle("Today's Bill Report")

        config_name = 'today_report.cfg'

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

        self.export_btn.setIcon(QtGui.QIcon(excel_image))
        self.export_btn.setIconSize(QtCore.QSize(40, 40))

        self.close_btn.setIcon(QtGui.QIcon(close_image))
        self.close_btn.setIconSize(QtCore.QSize(40, 40))





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
        self.today_table.setRowCount(0)
        self.today_table.verticalHeader().setVisible(False)
        header = self.today_table.horizontalHeader()
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

    def table_population(self):
        self.table_records()

        today = datetime.date.today()
        self.todaydate = today

        print ("The todays date is ",self.todaydate)

        self.connectdb()

        select_query ="SELECT BILL.BILL_NO,ROW_NUMBER() OVER( PARTITION BY BILL.BILL_NO ORDER BY CATEGORY) SLNO,\
                        CATEGORY,ORD.SIZE,ORD.RATE,ORD.QTY,ORD.TOTAL_AMOUNT,BILL.TOTAL_AMOUNT,BILL.AMOUNT_RECIEVED,\
                        BILL.AMOUNT_DUE,BILL.CUSTOMER_NAME,BILL.PHONE_NO \
                        FROM DBO.ORDER_DETAILS ORD INNER JOIN DBO.BILLING_TABLE BILL ON \
                        ORD.BILL_NO = BILL.BILL_NO \
                        WHERE BILL_TYPE ='DAILY' AND BILLING_DATE =? ORDER BY BILL.BILL_NO"

        cur.execute(select_query, self.todaydate)

        result = cur.fetchall()

        self.today_result = [data for data in result]



        result_check = len(result)
        self.result_chk =result_check
        self.total_amount =0
        self.amount_recieved =0
        self.due_amount =0
        self.prev_row_bill_no=None

        if result_check >= 1:
            new_result = []
            column_count = self.today_table.columnCount()
            for row in range(result_check):
                tuple_value = list(result[row])
                tuple_value = [str(value) for value in tuple_value if type(value) != 'str']
                # tuple_value.extend(self.work_finish)
                print('the modified tuple value is ', tuple_value)
                current_row_bill_no = tuple_value[0]

                if (current_row_bill_no != self.prev_row_bill_no) or self.prev_row_bill_no== None:
                    self.total_amount = self.total_amount+int(float(tuple_value[7]))
                    self.amount_recieved = self.amount_recieved + int(float(tuple_value[8]))
                    self.due_amount = self.due_amount+ int(float(tuple_value[9]))

                self.prev_row_bill_no =tuple_value[0]

                self.today_table.insertRow(row)
                for column in range(column_count):

                    value = tuple_value[column]

                    self.today_table.setItem(row, column, self.table_item(value,
                                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled))

            print("The total amount value is ",self.total_amount)
            print("The total amount recieved value is ", self.amount_recieved)
            print("The total due amount value is ",self.due_amount)

            self.total_le.setText(str(round(float(self.total_amount),2)))
            self.recieved_le.setText(str(round(float(self.amount_recieved),2)))
            self.due_le.setText(str(round(float(self.due_amount),2)))

    def table_item(self, text, flag):

        tablewidgetitem = QTableWidgetItem(text)
        tablewidgetitem.setFlags(flag)
        return tablewidgetitem

    def exportbtn(self):

        if self.result_chk >=1:

            file_path =QFileDialog.getSaveFileName(self, 'Export to Excel', "Daily_Bill_Report_"+self.todaydate.strftime("%d_%m_%Y")+".xlsx", 'Excel files (.xlsx) ;; All Files ()')

            if file_path != ('', ''):

                print("File path is",file_path)

                excel_book_name  = file_path[0]

                workbook = xlsxwriter.Workbook(excel_book_name)
                worksheet = workbook.add_worksheet("Today Report")

                title_format = workbook.add_format({'bold' : True})
                title_format.set_bg_color('yellow')
                title_format.set_font_color('brown')
                title_format.set_border()
                data = self.today_result


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


                title =["BILL_NO","SL_NO","CATEGORY","FRAME_SIZE","RATE","QTY","AMOUNT","TOTAL_AMOUNT","AMOUNT_RECIEVED",
                        "AMOUNT_DUE","CUSTOMER_NAME","PHONE_NO"]
                title_size =[len(i) for i in title]
                print('the  title size is',title_size)

                for col in range(0,len(title)):

                    worksheet.write(0,col,title[col],title_format)

                for row_level in range(len(data_modified)):
                    for col_level in range(len(data_modified[0])):
                        col_list =[4,6,7,8,9]

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


                workbook.close()

                QMessageBox.information(self,"File Export","Today's Report Exported Successfully...")
        else:
            QMessageBox.warning(self, "Warning", "No results found")


    def closebtn(self):
        self.close()










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    #Dialog.show()
    ui =Today_Report_Page()
    ui.show()
    sys.exit(app.exec_())
