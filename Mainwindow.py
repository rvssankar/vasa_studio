from PyQt5.QtWidgets import QApplication,QMainWindow,QAction, QMessageBox,QLabel,QVBoxLayout, QWidget,QDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from Admin_login import Admin_Login_User
from Staff_Login import Staff_Login_User
from Admin_changepassword import Admin_Password_Change
from Staff_changepassword import Staff_Password_Change
from Add_Staff import Add_Staff_Window
from Add_Product import Add_Product_window
import sys




class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'VASA STUDIO'
        self.left = 600
        self.top = 200
        self.width = 400
        self.height = 300

        icon_image = 'images\VASA_ICON.png'
        self.main_image = 'images\VASA_MAIN.jpg'

        self.setWindowTitle(self.title)
        self.windowpage()
        self.setWindowIcon(QtGui.QIcon(icon_image))


        self.centralWidget()
        self.show()


    def windowpage(self):

        menubar = self.menuBar()
        menubar.setStyleSheet(('font: 10 14pt "Calibri" bold'))
        self.loginmenu = menubar.addMenu('Login')
        chgpwdmenu = menubar.addMenu('Change Password')
        addstaffmenu = menubar.addMenu('Add Staffs')
        custbillmenu = menubar.addMenu('Customer Billing')
        prodcostmenu = menubar.addMenu('Product Cost')
        expensemenu = menubar.addMenu('Expense')
        workstatsmenu= menubar.addMenu('Work Status')
        reportsmenu = menubar.addMenu('Reports')
        remindermenu = menubar.addMenu('Reminders')
        logoutmenu = menubar.addMenu('Log Out')
        exitmenu =menubar.addMenu('Exit')


        admin = QAction('Admin Login',self)
        staff = QAction('Staff Login',self)
        admin_change = QAction('Admin Password',self)
        staff_change = QAction('Staff Password',self)
        Add_staff = QAction('Add Staff',self)
        Add_product = QAction('Add Product',self)
        exit = QAction('Exit',self)
        logout = QAction('Logout',self)
        dailybill = QAction('Daily Bill',self)
        updatedaily=QAction('Update Daily Bill',self)
        functionbill = QAction('Function Bill',self)
        updatefuncbill = QAction('Update Function Bill',self)
        print('Hello')


        self.loginmenu.addAction(admin)
        self.loginmenu.addAction(staff)

        chgpwdmenu.addAction(admin_change)
        chgpwdmenu.addAction(staff_change)

        custbillmenu.addAction(dailybill)
        custbillmenu.addAction(updatedaily)
        custbillmenu.addAction(functionbill)
        custbillmenu.addAction(updatefuncbill)

        addstaffmenu.addAction(Add_staff)

        exitmenu.addAction(exit)
        logoutmenu.addAction(logout)
        prodcostmenu.addAction(Add_product)

        admin.triggered.connect(self.adminpage)
        staff.triggered.connect(self.staffpage)
        admin_change.triggered.connect(self.admin_change_password)
        staff_change.triggered.connect(self.staff_change_password)
        Add_staff.triggered.connect(self.add_staff)
        Add_product.triggered.connect(self.add_product)
        exit.triggered.connect(self.close)
        logout.triggered.connect(self.logout)


        self.menulist = [chgpwdmenu,addstaffmenu,custbillmenu,prodcostmenu,expensemenu,workstatsmenu,reportsmenu,remindermenu,logoutmenu]
        self.staffmenu =[custbillmenu,reportsmenu,remindermenu,logoutmenu,exitmenu]

        for menu in self.menulist:
            menu.setDisabled(True)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        vbox = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        pixmap = QPixmap(self.main_image)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.resize(pixmap.width(),pixmap.height())

        vbox.addWidget(self.label)

    def adminpage(self):
        dialog = Admin_Login_User()
        dialog.exec_()


        print("The username logged in is :"+dialog.username)
        self.loginmenu.setDisabled(True)
        for menu in self.menulist:
            menu.setDisabled(False)



    def staffpage(self):
        dialog = Staff_Login_User()
        dialog.exec_()

        '''if dialog.exec_() == 1 and dialog.usercheck:
            print("The username logged in is :"+dialog.username)'''
        self.loginmenu.setDisabled(True)
        for menu in self.staffmenu:
            menu.setDisabled(False)

    def admin_change_password(self):
        dialog = Admin_Password_Change()
        dialog.exec_()

    def staff_change_password(self):
        dialog = Staff_Password_Change()
        dialog.exec_()

    def add_staff(self):
        dialog = Add_Staff_Window()
        dialog.exec_()

    def add_product(self):
        dialog = Add_Product_window()
        dialog.exec_()







    def closeEvent(self, event):
        close = QMessageBox.question(self,'Quit','Are you sure to exit the application',QMessageBox.Yes|QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def logout(self):
        reply=QMessageBox.question(self,'Logout','Are you sure want to logout?',QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.loginmenu.setDisabled(False)
            for menu in self.menulist:
                menu.setDisabled(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.showMaximized()
    sys.exit(app.exec_())





