# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_MainWindow(object):
    def setupUi(self, Ui_MainWindow):
        Ui_MainWindow.setObjectName("Ui_MainWindow")
        Ui_MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonMostrar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMostrar.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.buttonMostrar.setObjectName("buttonMostrar")
        self.buttonAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAgregar.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.buttonAgregar.setObjectName("buttonAgregar")
        self.buttonModificar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonModificar.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.buttonModificar.setObjectName("buttonModificar")
        self.buttonEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEliminar.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.buttonEliminar.setObjectName("buttonEliminar")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(200, 60, 461, 321))
        self.tableView.setObjectName("tableView")
        Ui_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Ui_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Ui_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow)

    def retranslateUi(self, Ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow.setWindowTitle(_translate("Ui_MainWindow", "MainWindow"))
        self.buttonMostrar.setText(_translate("Ui_MainWindow", "Mostrar"))
        self.buttonAgregar.setText(_translate("Ui_MainWindow", "Agregar"))
        self.buttonModificar.setText(_translate("Ui_MainWindow", "Modificar"))
        self.buttonEliminar.setText(_translate("Ui_MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Ui_MainWindow()
    ui.setupUi(Ui_MainWindow)
    Ui_MainWindow.show()
    sys.exit(app.exec_())
