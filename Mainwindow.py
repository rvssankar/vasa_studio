from PyQt5.QtWidgets import QApplication,QMainWindow,QAction, QMessageBox,QLabel,QVBoxLayout, QWidget,QDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from Admin_login import Admin_Login_User
from Staff_Login import Staff_Login_User
from Admin_changepassword import Admin_Password_Change
from Staff_changepassword import Staff_Password_Change
from Add_Staff import Add_Staff_Window
from Add_Product import Add_Product_window
from Add_Function_Product import Add_Function_Product_window
from Daily_Bill import Add_Daily_Bill
from Update_Daily_Bill import Update_Daily_Bill
from New_Function_Bill import Add_Function_Bill
from Update_Function_Bill import Update_Function_Bill
from Expenses import Add_Expenses
from Work_Allocate import  Work_Allocate_Page
from Work_Finish import  Work_Finish_Window
from Work_complete import Work_Complete_Page
from Today_Report import Today_Report_Page
from Daily_Report import Daily_Report_Page
from Function_Report import Function_Report_Page
from Expense_Report import Expense_Report_Page
from Reminder import Reminder_Page

from Dummy_Bill import  Add_Dummy_Bill
import VASA_IMAGE
import sys
import os





class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'VASA STUDIO'
        self.left = 600
        self.top = 200
        self.width = 400
        self.height = 300



        self.setWindowTitle(self.title)
        self.windowpage()



        self.centralWidget()
        self.show()


    def windowpage(self):

        config_name = 'myapp.cfg'

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)

        icon_image = os.path.join(application_path, "images", "VASA_ICON.png")
        self.main_image = os.path.join(application_path, 'images', 'VASA_MAIN.jpg')

        self.exit_image = os.path.join(application_path, "images", "exit.png")


        self.setWindowIcon(QtGui.QIcon(icon_image))

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
        Add_daily_product = QAction('Add Daily Product',self)
        Add_function_product = QAction('Add Function Product', self)
        exit = QAction('Exit',self)
        logout = QAction('Logout',self)
        dailybill = QAction('Daily Bill',self)
        updatedaily=QAction('Update Daily Bill',self)
        functionbill = QAction('Function Bill',self)
        updatefuncbill = QAction('Update Function Bill',self)
        add_expense = QAction('Add Expense',self)
        work_allocate = QAction('Allocate Work Orders',self)
        work_pending = QAction('Pending Work Orders',self)
        work_complete = QAction('Completed Work Orders',self)
        today_report = QAction("Today's Report",self)
        daily_bill_report = QAction("Daily Bill Report",self)
        function_bill_report = QAction('Function Bill Report',self)
        expense_report =QAction('Expense Report',self)
        reminders = QAction("Reminders",self)

        dummy_bill = QAction("Add Dummy Bill",self)



        self.loginmenu.addAction(admin)
        self.loginmenu.addAction(staff)

        chgpwdmenu.addAction(admin_change)
        chgpwdmenu.addAction(staff_change)

        custbillmenu.addAction(dailybill)
        custbillmenu.addAction(updatedaily)
        custbillmenu.addAction(functionbill)
        custbillmenu.addAction(updatefuncbill)
        expensemenu.addAction(add_expense)

        addstaffmenu.addAction(Add_staff)

        workstatsmenu.addAction(work_allocate)
        workstatsmenu.addAction(work_pending)
        workstatsmenu.addAction(work_complete)

        reportsmenu.addAction(today_report)
        reportsmenu.addAction(daily_bill_report)
        reportsmenu.addAction(function_bill_report)
        reportsmenu.addAction(expense_report)

        remindermenu.addAction(reminders)

        exitmenu.addAction(exit)
        logoutmenu.addAction(logout)
        prodcostmenu.addAction(Add_daily_product)
        prodcostmenu.addAction(Add_function_product)

        prodcostmenu.addAction(dummy_bill)

        admin.triggered.connect(self.adminpage)
        staff.triggered.connect(self.staffpage)
        admin_change.triggered.connect(self.admin_change_password)
        staff_change.triggered.connect(self.staff_change_password)
        Add_staff.triggered.connect(self.add_staff)
        Add_daily_product.triggered.connect(self.add_product)
        Add_function_product.triggered.connect(self.add_function_product)
        dailybill.triggered.connect(self.daily_bill)
        updatedaily.triggered.connect(self.update_daily)
        functionbill.triggered.connect(self.new_function)
        updatefuncbill.triggered.connect(self.update_function)
        add_expense.triggered.connect(self.add_expense)
        work_allocate.triggered.connect(self.work_allocate)
        work_pending.triggered.connect(self.work_pending)
        work_complete.triggered.connect(self.work_complete)
        today_report.triggered.connect(self.today_report)
        daily_bill_report.triggered.connect(self.daily_report)
        function_bill_report.triggered.connect(self.function_report)
        expense_report.triggered.connect(self.expense_report)
        reminders.triggered.connect(self.reminders)
        exit.triggered.connect(self.close)
        logout.triggered.connect(self.logout)

        dummy_bill.triggered.connect(self.dummybill)


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

        reminder = Reminder_Page()

        self.result_count = reminder.result_count

        print("the result count is", self.result_count)




    def adminpage(self):
        dialog = Admin_Login_User()
        dialog.exec_()


        print("The username logged in is :"+dialog.username)
        self.loginmenu.setDisabled(True)
        for menu in self.menulist:
            menu.setDisabled(False)

        if self.result_count >=1 :
            Reminder_Page().exec_()





    def staffpage(self):
        dialog = Staff_Login_User()
        dialog.exec_()

        '''if dialog.exec_() == 1 and dialog.usercheck:
            print("The username logged in is :"+dialog.username)'''
        self.loginmenu.setDisabled(True)
        for menu in self.staffmenu:
            menu.setDisabled(False)

        if self.result_count >=1 :
            Reminder_Page().exec_()

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

    def add_function_product(self):
        dialog = Add_Function_Product_window()
        dialog.exec_()

    def daily_bill(self):
        dialog =Add_Daily_Bill()
        dialog.exec_()

    def update_daily(self):
        dialog =Update_Daily_Bill()
        dialog.exec_()

    def new_function(self):
        dialog =Add_Function_Bill()
        dialog.exec_()

    def update_function(self):
        dialog = Update_Function_Bill()
        dialog.exec_()

    def add_expense(self):
        dialog = Add_Expenses()
        dialog.exec_()

    def work_allocate(self):
        dialog = Work_Allocate_Page()
        dialog.exec_()

    def work_pending(self):
        dialog = Work_Finish_Window()
        dialog.exec_()

    def work_complete(self):
        dialog = Work_Complete_Page()
        dialog.exec_()

    def today_report(self):
        dialog = Today_Report_Page()
        dialog.exec_()

    def daily_report(self):
        dialog =Daily_Report_Page()
        dialog.exec_()

    def function_report(self):
        dialog = Function_Report_Page()
        dialog.exec_()

    def expense_report(self):
        dialog = Expense_Report_Page()
        dialog.exec_()

    def reminders(self):
        dialog = Reminder_Page()
        dialog.exec_()

    def dummybill(self):
        dialog = Add_Dummy_Bill()
        #dialog.exec_()









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





