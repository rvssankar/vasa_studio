
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 615)
        Dialog.setStyleSheet("background-color: rgb(255, 244, 224);")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(60, 5, 551, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color:rgb(6, 51, 255);\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(130, 190, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color:rgb(0, 170, 0)")
        self.username_label.setWordWrap(False)
        self.username_label.setIndent(-1)
        self.username_label.setObjectName("username_label")
        self.cur_pass_label = QtWidgets.QLabel(Dialog)
        self.cur_pass_label.setGeometry(QtCore.QRect(129, 247, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cur_pass_label.setFont(font)
        self.cur_pass_label.setStyleSheet("color:rgb(0, 170, 0)")
        self.cur_pass_label.setWordWrap(True)
        self.cur_pass_label.setObjectName("cur_pass_label")
        self.new_pass_lbl = QtWidgets.QLabel(Dialog)
        self.new_pass_lbl.setGeometry(QtCore.QRect(130, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.new_pass_lbl.setFont(font)
        self.new_pass_lbl.setStyleSheet("color:rgb(0, 170, 0)")
        self.new_pass_lbl.setWordWrap(True)
        self.new_pass_lbl.setObjectName("new_pass_lbl")
        self.username_le = QtWidgets.QLineEdit(Dialog)
        self.username_le.setGeometry(QtCore.QRect(310, 200, 221, 31))
        self.username_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.username_le.setObjectName("username_le")
        self.cur_pass_le = QtWidgets.QLineEdit(Dialog)
        self.cur_pass_le.setGeometry(QtCore.QRect(310, 250, 221, 31))
        self.cur_pass_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.cur_pass_le.setObjectName("cur_pass_le")
        self.new_pass_le = QtWidgets.QLineEdit(Dialog)
        self.new_pass_le.setGeometry(QtCore.QRect(310, 300, 221, 31))
        self.new_pass_le.setStyleSheet("border-radius:10px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.new_pass_le.setObjectName("new_pass_le")
        self.change_btn = QtWidgets.QPushButton(Dialog)
        self.change_btn.setGeometry(QtCore.QRect(119, 400, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("background-color:rgb(85, 170, 0);\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.change_btn.setObjectName("change_btn")
        self.clr_btn = QtWidgets.QPushButton(Dialog)
        self.clr_btn.setGeometry(QtCore.QRect(266, 400, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clr_btn.setFont(font)
        self.clr_btn.setStyleSheet("background-color:rgb(255, 170, 127);\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.clr_btn.setObjectName("clr_btn")
        self.cncl_btn = QtWidgets.QPushButton(Dialog)
        self.cncl_btn.setGeometry(QtCore.QRect(413, 400, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cncl_btn.setFont(font)
        self.cncl_btn.setStyleSheet("background-color:rgb(255, 155, 162);\n"
"border-radius:20px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:black;\n"
"font:bold;")
        self.cncl_btn.setObjectName("cncl_btn")
        self.page_frame = QtWidgets.QFrame(Dialog)
        self.page_frame.setGeometry(QtCore.QRect(80, 110, 501, 411))
        self.page_frame.setStyleSheet("border-radius:8px;\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-color:green;\n"
"")
        self.page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_frame.setObjectName("page_frame")
        self.h_line = QtWidgets.QFrame(Dialog)
        self.h_line.setGeometry(QtCore.QRect(0, 74, 671, 16))
        self.h_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line.setObjectName("h_line")
        self.page_frame.raise_()
        self.title_label.raise_()
        self.username_label.raise_()
        self.cur_pass_label.raise_()
        self.new_pass_lbl.raise_()
        self.username_le.raise_()
        self.cur_pass_le.raise_()
        self.new_pass_le.raise_()
        self.change_btn.raise_()
        self.clr_btn.raise_()
        self.cncl_btn.raise_()
        self.h_line.raise_()

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "Change Admin Password"))
        self.username_label.setText(_translate("Dialog", "User Name          :"))
        self.cur_pass_label.setText(_translate("Dialog", "Current Password  :"))
        self.new_pass_lbl.setText(_translate("Dialog", "New Password      :"))
        self.change_btn.setText(_translate("Dialog", "Change"))
        self.clr_btn.setText(_translate("Dialog", "Clear"))
        self.cncl_btn.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Dialog()




    sys.exit(app.exec_())