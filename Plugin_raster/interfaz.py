# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 471, 371))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.cmb1 = QtWidgets.QComboBox(self.groupBox)
        self.cmb1.setGeometry(QtCore.QRect(20, 50, 221, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmb1.setFont(font)
        self.cmb1.setObjectName("cmb1")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(250, 50, 41, 23))
        self.btn1.setObjectName("btn1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lb1 = QtWidgets.QLabel(self.groupBox)
        self.lb1.setGeometry(QtCore.QRect(20, 130, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.btn2 = QtWidgets.QPushButton(self.groupBox)
        self.btn2.setGeometry(QtCore.QRect(20, 320, 93, 28))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.groupBox)
        self.btn3.setGeometry(QtCore.QRect(150, 320, 93, 28))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.groupBox)
        self.btn4.setGeometry(QtCore.QRect(280, 320, 93, 28))
        self.btn4.setObjectName("btn4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 161, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 200, 351, 87))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Módulo ráster"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos de entrada"))
        self.label.setText(_translate("MainWindow", "Selecciona el archivo "))
        self.btn1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Sistema de referencia geoespacial"))
        self.lb1.setText(_translate("MainWindow", "SRG"))
        self.btn2.setText(_translate("MainWindow", "Ayuda"))
        self.btn3.setText(_translate("MainWindow", "Empezar"))
        self.btn4.setText(_translate("MainWindow", "Cerrar"))
        self.label_3.setText(_translate("MainWindow", "Datos de información:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

