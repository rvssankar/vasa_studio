from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox,QInputDialog,QLineEdit
import pyodbc
import datetime
import os
import sys


class Add_Dummy_Bill(QInputDialog):
    def __init__(self):
        super(Add_Dummy_Bill,self).__init__()

        config_name = 'daily_product.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")

        self.setWindowIcon(QtGui.QIcon(icon_image))

        #self.setFixedSize(800,600)
        today = datetime.date.today()


        text,okpressed = self.getText(self,'Add Dummy Bill','<html style="font-size:12pt;font-weight:bold;">Enter Dummy Bill Number :</html>',QLineEdit.Normal,"")

        if okpressed and text!='':
                bill_value = text
                self.connectdb()
                data =(bill_value,'XXX',00000,today)
                ins_query = 'INSERT INTO dbo.BILLING_TABLE (BILL_NO,CUSTOMER_NAME,PHONE_NO, BILLING_DATE) VALUES (?,?,?,?)'
                cur.execute(ins_query,data)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Information','Dummy Bill Number '+text+' added successfully')

        self.deleteLater()



    def connectdb(self):
        global cur
        global connect

        connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    expense_dialog = QtWidgets.QDialog()
    #ui = Ui_expense_dialog()
    #ui.setupUi(expense_dialog)
    #expense_dialog.show()
    w = Add_Dummy_Bill()
    w.show()
    sys.exit(app.exec_())
