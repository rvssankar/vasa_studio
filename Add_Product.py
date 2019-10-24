
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QInputDialog,QLineEdit,QMessageBox
import pyodbc
from decimal import Decimal
import Vasa


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
        self.frame_size_label = QtWidgets.QLabel(self.Add_prod_frame)
        self.frame_size_label.setGeometry(QtCore.QRect(30, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_size_label.setFont(font)
        self.frame_size_label.setStyleSheet("font: 75 14pt \"Cambria\";\n"
"font:bold;\n"
"color: rgb(11, 19, 175);\n"
"")
        self.frame_size_label.setWordWrap(False)
        self.frame_size_label.setIndent(-1)
        self.frame_size_label.setObjectName("frame_size_label")
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
        self.combo_box = QtWidgets.QComboBox(self.Add_prod_frame)
        self.combo_box.setGeometry(QtCore.QRect(210, 90, 221, 41))
        self.combo_box.setStyleSheet("border-radius:5px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold;")
        self.combo_box.setEditable(False)
        self.combo_box.setIconSize(QtCore.QSize(20, 20))
        self.combo_box.setObjectName("combo_box")
        self.frame_size_le = QtWidgets.QLineEdit(self.Add_prod_frame)
        self.frame_size_le.setGeometry(QtCore.QRect(210, 150, 221, 41))
        self.frame_size_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.frame_size_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.frame_size_le.setObjectName("frame_size_le")
        self.rate_le = QtWidgets.QLineEdit(self.Add_prod_frame)
        self.rate_le.setGeometry(QtCore.QRect(211, 220, 221, 41))
        self.rate_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"font: 11pt \"Cambria\";\n"
"font:bold")
        self.rate_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rate_le.setObjectName("rate_le")
        self.save_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.save_btn.setGeometry(QtCore.QRect(200, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(26, 204, 57, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.save_btn.setObjectName("save_btn")
        self.clear_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.clear_btn.setGeometry(QtCore.QRect(368, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(204, 188, 26, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.clear_btn.setObjectName("clear_btn")
        self.add_btn = QtWidgets.QPushButton(self.Add_prod_frame)
        self.add_btn.setGeometry(QtCore.QRect(20, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 120, 204, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.add_btn.setObjectName("add_btn")
        self.toolButton = QtWidgets.QToolButton(self.Add_prod_frame)
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
        self.toolButton.setIconSize(QtCore.QSize(140, 140))
        self.toolButton.setObjectName("toolButton")
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
        self.category_label.setText(_translate("New_product_dialog", "Category           :"))
        self.frame_size_label.setText(_translate("New_product_dialog", "Frame Size       :"))
        self.rate_label.setText(_translate("New_product_dialog", "Rate (Rs.)          :"))
        self.save_btn.setText(_translate("New_product_dialog", "Save"))
        self.clear_btn.setText(_translate("New_product_dialog", "Clear"))
        self.add_btn.setText(_translate("New_product_dialog", "Add New"))
        self.toolButton.setText(_translate("New_product_dialog", "..."))
        self.toolButton_2.setText(_translate("New_product_dialog", "New Product"))

class Add_Product_window(QDialog,Ui_New_product_dialog):
    def __init__(self,parent=None):
        super(Add_Product_window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Add Products")

        self.onlydouble = QtGui.QIntValidator()
        self.rate_le.setValidator(self.onlydouble)

        self.combo_box.currentIndexChanged['QString'].connect(self.comboindexchanged)



        self.combovalue()




        self.add_btn.clicked.connect(self.newprod)
        self.save_btn.clicked.connect(self.savebtn)
        self.clear_btn.clicked.connect(self.clearbtn)

    def comboindexchanged(self):
        current_value =self.combo_box.currentText()
        print(current_value)
        if current_value =='FRAME':
            self.frame_size_le.setEnabled(True)
            self.frame_size_le.setStyleSheet("border-radius:10px;\n"
                                             "border-style:outset;\n"
                                             "border-width:2px;\n"
                                             "border-color:black;\n"
                                             "font: 11pt \"Cambria\";\n"
                                             "font:bold")

        else:
            self.frame_size_le.setEnabled(False)
            self.frame_size_le.setStyleSheet('QPushButton: disabled{background - color:grey}')



    def connectdb(self):
        global cur
        global connect

        connect = pyodbc.connect('Driver={SQL SERVER};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur
    def newprod(self):
        text,okpressed = QInputDialog.getText(self,'Add Produt','Product Name :',QLineEdit.Normal,"")
        if okpressed and text!='':
                value = str.upper(text)
                self.connectdb()
                ins_query = 'INSERT INTO dbo.PROD_DETAILS VALUES (NEXT VALUE FOR dbo.seq_prod,?)'
                cur.execute(ins_query,value)
                connect.commit()
                connect.close()
                QMessageBox.information(self,'Information','Product '+value+' added successfully')
                self.combo_box.clear()
                self.combovalue()

    def combovalue(self):
        self.combolist = set('',)

        sel_query ='SELECT PROD_NAME from dbo.PROD_DETAILS'
        self.connectdb()
        cur.execute(sel_query)
        result= cur.fetchall()

        for i in result:

                x=i[0]
                self.combolist.add(x)



        self.combo_box.addItems(self.combolist)


    def savebtn(self):
        cat_value  = str(self.combo_box.currentText())


        frame_size = self.frame_size_le.text()

        if self.rate_le.text().isnumeric():
            price = int(self.rate_le.text())
        else:
            QMessageBox.information(self,'Alert Window','Please enter the Rate details')
            price=0

        self.connectdb()

        if price != 0 and cat_value !='FRAME':

            upd_query ='UPDATE dbo.PROD_DETAILS SET SIZE=?, PRICE=? WHERE PROD_NAME=?'
            data =(frame_size,price,cat_value)
            cur.execute(upd_query,data)
            connect.commit()
            connect.close()
            QMessageBox.information(self,'Information','Prod information added successfully')
            self.rate_le.clear()


        elif cat_value =='FRAME' and frame_size !='' and price != 0 :

            ins_query ='INSERT INTO dbo.PROD_DETAILS VALUES (NEXT VALUE FOR dbo.seq_prod, ?,?,?)'
            data = (cat_value,frame_size,price)
            cur.execute(ins_query,data)
            connect.commit()
            connect.close()
            QMessageBox.information(self, 'Information', 'Prod information added successfully')
            self.rate_le.clear()
            self.frame_size_le.clear()
        elif frame_size =='' and cat_value=='FRAME':

            QMessageBox.information(self, 'Alert Window', 'Frame size is mandatory')

    def clearbtn(self):
        self.rate_le.clear()
        self.frame_size_le.clear()




















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_product_dialog = QtWidgets.QDialog()
    #ui = Ui_New_product_dialog()
    #ui.setupUi(New_product_dialog)
    #New_product_dialog.show()
    ui = Add_Product_window()
    ui.show()
    sys.exit(app.exec_())
