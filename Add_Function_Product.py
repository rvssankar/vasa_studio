from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QInputDialog,QLineEdit,QMessageBox
import pyodbc
from decimal import Decimal
import Vasa
import os
import sys


class Ui_New_product_dialog(object):
    def setupUi(self, New_product_dialog):
        New_product_dialog.setObjectName("New_product_dialog")
        New_product_dialog.resize(691, 614)
        New_product_dialog.setStyleSheet("#New_product_dialog{background-image: url(:/Images/pexels-photo-949587.jpeg);}")
        self.Add_prod_frame = QtWidgets.QFrame(New_product_dialog)
        self.Add_prod_frame.setGeometry(QtCore.QRect(54, 90, 581, 451))
        self.Add_prod_frame.setStyleSheet("#Add_prod_frame{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 183, 204, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"border-radius:25px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;}")
        self.Add_prod_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Add_prod_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Add_prod_frame.setObjectName("Add_prod_frame")
        self.category_label = QtWidgets.QLabel(self.Add_prod_frame)
        self.category_label.setGeometry(QtCore.QRect(30, 80, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.category_label.setFont(font)
        self.category_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(11, 19, 175);\n"
"")
        self.category_label.setWordWrap(False)
        self.category_label.setIndent(-1)
        self.category_label.setObjectName("category_label")
        self.package_name_label = QtWidgets.QLabel(self.Add_prod_frame)
        self.package_name_label.setGeometry(QtCore.QRect(30, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.package_name_label.setFont(font)
        self.package_name_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(11, 19, 175);\n"
"")
        self.package_name_label.setWordWrap(False)
        self.package_name_label.setIndent(-1)
        self.package_name_label.setObjectName("package_name_label")
        self.rate_label = QtWidgets.QLabel(self.Add_prod_frame)
        self.rate_label.setGeometry(QtCore.QRect(30, 220, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rate_label.setFont(font)
        self.rate_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(11, 19, 175);\n"
"")
        self.rate_label.setWordWrap(False)
        self.rate_label.setIndent(-1)
        self.rate_label.setObjectName("rate_label")
        self.category_combo_box = QtWidgets.QComboBox(self.Add_prod_frame)
        self.category_combo_box.setGeometry(QtCore.QRect(239, 90, 221, 41))
        self.category_combo_box.setStyleSheet("border-radius:5px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold;")
        self.category_combo_box.setEditable(False)
        self.category_combo_box.setIconSize(QtCore.QSize(20, 20))
        self.category_combo_box.setObjectName("category_combo_box")
        self.rate_le = QtWidgets.QLineEdit(self.Add_prod_frame)
        self.rate_le.setGeometry(QtCore.QRect(240, 220, 221, 41))
        self.rate_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.rate_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rate_le.setObjectName("rate_le")
        self.save_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.save_btn.setGeometry(QtCore.QRect(90, 360, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("#save_btn{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(26, 204, 57, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#save_btn:pressed{border-style:solid;border-width:6px}"                                    )
        self.save_btn.setObjectName("save_btn")
        self.clear_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.clear_btn.setGeometry(QtCore.QRect(330, 360, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("#clear_btn{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(204, 188, 26, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#clear_btn:pressed{border-style:solid;border-width:6px}"                                     )
        self.clear_btn.setObjectName("clear_btn")
        self.add_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.add_btn.setGeometry(QtCore.QRect(30, 290, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("#add_btn{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 120, 204, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#add_btn:pressed{border-style:solid;border-width:6px}"                                   )
        self.add_btn.setObjectName("add_btn")
        '''self.toolButton = QtWidgets.QToolButton(self.Add_prod_frame)
        self.toolButton.setGeometry(QtCore.QRect(435, 110, 141, 141))
        self.toolButton.setStyleSheet("\n"
"border-radius:50px;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-color:white;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 140))
        self.toolButton.setObjectName("toolButton")'''
        self.package_combo_box = QtWidgets.QComboBox(self.Add_prod_frame)
        self.package_combo_box.setEnabled(False)
        self.package_combo_box.setGeometry(QtCore.QRect(240, 152, 221, 41))
        self.package_combo_box.setStyleSheet("border-radius:5px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold;")
        self.package_combo_box.setEditable(False)
        self.package_combo_box.setIconSize(QtCore.QSize(20, 20))
        self.package_combo_box.setObjectName("package_combo_box")
        self.add_btn_2 = QtWidgets.QPushButton(self.Add_prod_frame)
        self.add_btn_2.setGeometry(QtCore.QRect(290, 290, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_btn_2.setFont(font)
        self.add_btn_2.setStyleSheet("#add_btn_2{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(100, 9, 85, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;} \n"
"#add_btn_2:pressed{border-style:solid;border-width:6px}"                                     )
        self.add_btn_2.setObjectName("add_btn_2")
        self.toolButton_2 = QtWidgets.QToolButton(New_product_dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 50, 371, 81))
        self.toolButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(125, 37, 37, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 16pt \"Cambria\";\n"
"font: Bold;\n"
"color: rgb(34, 48, 170);\n"
"border-radius:40px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;")
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(New_product_dialog)
        QtCore.QMetaObject.connectSlotsByName(New_product_dialog)

    def retranslateUi(self, New_product_dialog):
        _translate = QtCore.QCoreApplication.translate
        New_product_dialog.setWindowTitle(_translate("New_product_dialog", "Dialog"))
        self.category_label.setText(_translate("New_product_dialog", "Category             :"))
        self.package_name_label.setText(_translate("New_product_dialog", "Package Name  :"))
        self.rate_label.setText(_translate("New_product_dialog", "Rate (Rs.)            :"))
        self.save_btn.setText(_translate("New_product_dialog", "Save"))
        self.clear_btn.setText(_translate("New_product_dialog", "Clear"))
        self.add_btn.setText(_translate("New_product_dialog", "New Product"))
        #self.toolButton.setText(_translate("New_product_dialog", "..."))
        self.add_btn_2.setText(_translate("New_product_dialog", "New Package"))
        self.toolButton_2.setText(_translate("New_product_dialog", "New Function Product"))

class Add_Function_Product_window(QDialog,Ui_New_product_dialog):
    def __init__(self,parent=None):
        super(Add_Function_Product_window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Add Function Products")

        self.onlydouble  = QtGui.QIntValidator()
        self.rate_le.setValidator(self.onlydouble)

        self.combovalue()

        self.category_combo_box.currentIndexChanged['QString'].connect(self.comboindexchanged)

        self.add_btn.clicked.connect(self.newprod)
        self.add_btn_2.clicked.connect(self.newpackage)
        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)

        config_name = 'function_product.cfg'

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

    def newprod(self):
        text,okpressed = QInputDialog.getText(self,'Add Product','Product Name :',QLineEdit.Normal,"")
        if okpressed and text!='':
                value = str.upper(text)
                self.connectdb()
                query_value =(value,'FUNCTION')
                ins_query = 'INSERT INTO dbo.PROD_DETAILS (PROD_ID,PROD_NAME,PROD_TYPE) VALUES (NEXT VALUE FOR dbo.seq_prod,?,?)'
                cur.execute(ins_query,query_value)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Information','Product '+value+' added successfully')
                self.category_combo_box.clear()
                self.combovalue()


    def newpackage(self):
        text,okpressed = QInputDialog.getText(self,'Add Package','Package Name :',QLineEdit.Normal,"")
        if okpressed and text!='':
                value = str.upper(text)
                self.connectdb()

                ins_query = 'INSERT INTO dbo.PACKAGE_DETAILS (PACKAGE_ID,PACKAGE_NAME) VALUES (NEXT VALUE FOR dbo.seq_package,?)'
                cur.execute(ins_query,value)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Information','Package '+value+' added successfully')
                self.package_combo_box.clear()
                #self.combovalue()
    def combovalue(self):
        self.combolist = set('',)

        sel_query ="SELECT PROD_NAME from dbo.PROD_DETAILS WHERE PROD_TYPE ='FUNCTION'"
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

                x=i[0]
                self.combolist.add(x)
        self.category_combo_box.addItems(self.combolist)

    def combopackagevalue(self):
        self.combolist = set('',)

        sel_query ="SELECT PACKAGE_NAME from dbo.PACKAGE_DETAILS"
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

                x=i[0]
                self.combolist.add(x)
        self.package_combo_box.addItems(self.combolist)


    def comboindexchanged(self):
        current_value =self.category_combo_box.currentText()
        print("The category combo box current value is ",current_value)
        if current_value =='MARRIAGE':
            self.package_combo_box.setEnabled(True)
            self.package_combo_box.setStyleSheet("border-radius:10px;\n"
                                             "border-style:outset;\n"
                                             "border-width:2px;\n"
                                             "border-color:black;\n"
                                             "font: 11pt \"Cambria\";\n"
                                             "font:bold")
            self.combopackagevalue()

        else:
            self.package_combo_box.setEnabled(False)
            self.package_combo_box.setStyleSheet('QPushButton: disabled{background - color:grey}')


    def packageid(self,name):
        sel_query ='SELECT PACKAGE_ID FROM dbo.PACKAGE_DETAILS WHERE PACKAGE_NAME=?'
        cur.execute(sel_query, name)
        result =cur.fetchone()
        package_id =result[0]
        return package_id
        print('the package id value for '+name+' is ',result)

    def savebtn(self):
        cat_value  = str(self.category_combo_box.currentText())
        package_name = str(self.package_combo_box.currentText())

        if self.rate_le.text().isnumeric():
            price = int(self.rate_le.text())
        else:
            QMessageBox.information(self,'Alert Window','Please enter the Rate details')
            price=0

        self.connectdb()

        if price != 0 and cat_value !='MARRIAGE':

            upd_query ="UPDATE dbo.PROD_DETAILS SET PRICE=? WHERE PROD_NAME=? AND PROD_TYPE='FUNCTION'"
            data =(price,cat_value)
            cur.execute(upd_query,data)
            connect.commit()
            connect.close()
            QMessageBox.information(self,'Information','Prod information added successfully')
            self.rate_le.clear()

        elif cat_value =='MARRIAGE' and package_name !='' and price != 0 :
            package_id_value = self.packageid(package_name)

            sel_query = "SELECT * FROM dbo.PROD_DETAILS WHERE PROD_NAME=? AND PACKAGE_ID =? AND PROD_TYPE='FUNCTION'"
            sel_data =(cat_value,package_id_value)

            cur.execute(sel_query,sel_data)
            sel_value = cur.fetchall()

            if len(sel_value)>0:
                update_query  = 'UPDATE dbo.PROD_DETAILS SET PRICE =? WHERE PROD_NAME=? AND PACKAGE_ID=?'
                upd_data =(price,cat_value,package_id_value)
                cur.execute(update_query,upd_data)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Information','PROD details updated successfully')
                self.rate_le.clear()
                self.frame_size_le.clear()
            else:

                ins_query ='INSERT INTO dbo.PROD_DETAILS(PROD_ID,PROD_NAME,PACKAGE_ID,PRICE,PROD_TYPE) VALUES (NEXT VALUE FOR dbo.seq_prod, ?,?,?,?)'
                prod_type ='FUNCTION'
                data = (cat_value,package_id_value,price,prod_type)
                cur.execute(ins_query,data)
                connect.commit()
                connect.close()
                QMessageBox.information(self, 'Information', 'Prod information added successfully')
                self.rate_le.clear()
                self.package_combo_box.clear()
        elif package_name =='' and cat_value=='MARRIAGE':

            QMessageBox.information(self, 'Alert Window', 'PACKAGE NAME is mandatory')

    def clearbtn(self):
        self.rate_le.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_product_dialog = QtWidgets.QDialog()
    #ui = Ui_New_product_dialog()
    #ui.setupUi(New_product_dialog)
    #New_product_dialog.show()
    ui = Add_Function_Product_window()
    ui.show()
    sys.exit(app.exec_())
