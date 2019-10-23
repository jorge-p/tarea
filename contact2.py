import sys
from time import sleep

from PyQt5 import QtCore, QtWidgets

#Cambia el nombre de Video2_base_SQL por el de tu archivo convertido
from contact import Ui_Ui_MainWindow
from PyQt5 import QtSql

import sqlite3
from pprint import pprint
                                    

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        self.create_DB()
        #Cambia el button_SQL_view_data por el nombre que le pongas al boton de ver
        self.ui.buttonMostrar.clicked.connect(self.print_data)
        self.model = None
        #Cambia el button_SQL_view_data por el nombre que le pongas al boton de ver
        self.ui.buttonMostrar.clicked.connect(self.sql_tableview_model)
        #Cambia el button_SQL_add por el nombre que le pongas al boton de agregar
        self.ui.buttonAgregar.clicked.connect(self.sql_add_row)
        #Cambia el button_SQL_delete por el nombre que le pongas al boton de eliminar
        self.ui.buttonEliminar.clicked.connect(self.sql_delete_row)
        
        
        #-------------------------- 
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #Cambias este nombre
        db.setDatabaseName('CONTACT.db')
        
        tableview = self.ui.tableView
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('contacts')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "contacto")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "nombre")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "apellido")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "email")
        

    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'CONTACT.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'contacts' ORDER BY ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('CONTACT.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table contacts(ID int primary key, "
                    "contacto varchar(20), nombre varchar(20),"
                    "apellido varchar(20), email varchar(20),tel int)")
        
        #query.exec_("insert into contacts values(1, 'Leonel', 'Messi','messi@joto.com','4181167906')")
        #query.exec_("insert into contacts values(1, 'jorge', 'ponce','ponce@joto.com','4181167906')")
        
if __name__ == "__main__":
    MainWindow_EXEC()
