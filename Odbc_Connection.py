import pyodbc

class Add_Odbc_Connection(object):
    def __init__(self):
        super(Add_Odbc_Connection,self).__init__()



        #self.odbc_connection = self.connectdb()
        self.connect = connect

        print("The connection is successfully created")



    def connectdb(self):
        global cur
        global connect



        connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=DHANALAKSHMI_PC\SQLEXPRESS;'
                                 'Database=VASADB;'
                                 'Trusted_Connection=yes;')
        cur = connect.cursor()
        return cur,connect

if __name__ == "__main__":
    import sys
    #ui = Ui_function_report()
    #ui.setupUi(function_report)
    #function_report.show()
    ui =Add_Odbc_Connection()
    #ui.show()
    #sys.exit(app.exec_())