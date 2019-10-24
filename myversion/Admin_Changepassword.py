from PyQt5.QtWidgets import QDialog,QLabel,QLineEdit,QPushButton,QFrame,QApplication
from PyQt5 import QtCore, QtGui
import sys
import pyodbc

class admin_chng_password(QDialog):
    def __init__(self):
        super().__init__()
        self.admin_change()

    def admin_change(self):

        self.resize(680,615)
        self.setStyleSheet("background-color: rgb(255, 244, 224);")
        self.title_label = QLabel('Change Admin Password')
        self.title_label.setGeometry(QtCore.QRect(60, 5, 551, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color:rgb(6, 51, 255);\n"
                                       "")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        self.username_label = QLabel('User Name          :')
        self.username_label.setGeometry(QtCore.QRect(130, 190, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color:rgb(0, 170, 0)")
        self.username_label.setWordWrap(False)
        self.username_label.setIndent(-1)

        self.cur_pass_label = QLabel('Current Password  :')
        self.cur_pass_label.setGeometry(QtCore.QRect(129, 247, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cur_pass_label.setFont(font)
        self.cur_pass_label.setStyleSheet("color:rgb(0, 170, 0)")
        self.cur_pass_label.setWordWrap(True)

        self.new_pass_lbl = QLabel('New Password      :')
        self.new_pass_lbl.setGeometry(QtCore.QRect(130, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.new_pass_lbl.setFont(font)
        self.new_pass_lbl.setStyleSheet("color:rgb(0, 170, 0)")
        self.new_pass_lbl.setWordWrap(True)

        self.username_le = QLineEdit()
        self.username_le.setGeometry(QtCore.QRect(310, 200, 221, 31))
        self.username_le.setStyleSheet("border-radius:10px;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-color:black;")

        self.cur_pass_le = QLineEdit()
        self.cur_pass_le.setGeometry(QtCore.QRect(310, 250, 221, 31))
        self.cur_pass_le.setStyleSheet("border-radius:10px;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-color:black;")

        self.new_pass_le = QLineEdit()
        self.new_pass_le.setGeometry(QtCore.QRect(310, 300, 221, 31))
        self.new_pass_le.setStyleSheet("border-radius:10px;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-color:black;")

        self.change_btn = QPushButton('Change')
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

        self.clr_btn = QPushButton('Clear')
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

        self.cncl_btn = QPushButton('Cancel')
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

        self.page_frame = QFrame()
        self.page_frame.setGeometry(QtCore.QRect(80, 110, 501, 411))
        self.page_frame.setStyleSheet("border-radius:8px;\n"
                                      "border-style:outset;\n"
                                      "border-width:3px;\n"
                                      "border-color:green;\n"
                                      "")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)

        self.h_line = QFrame()
        self.h_line.setGeometry(QtCore.QRect(0, 74, 671, 16))
        self.h_line.setFrameShape(QFrame.HLine)
        self.h_line.setFrameShadow(QFrame.Sunken)

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



        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = admin_chng_password()


    sys.exit(app.exec_())