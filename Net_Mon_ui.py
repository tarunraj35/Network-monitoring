# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Net_Mon.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import nmap3
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 400, 86, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_ip)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 400, 86, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Exit)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 470, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.reassign_ip)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 100, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 100, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 100, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 20, 161, 31))
        self.label_7.setObjectName("label_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 130, 171, 171))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(310, 130, 171, 171))
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_3.setText(_translate("MainWindow","Reassign"))
        self.label_4.setText(_translate("MainWindow", "Active Hosts"))
        self.label_5.setText(_translate("MainWindow", "Breached ips"))
        self.label_7.setText(_translate("MainWindow", "NETWORK MONITORING"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "\n""\n""\n""\n"""))

    def breached_ip(self):
        import capture_ip
        self.plainTextEdit_2.appendPlainText(capture_ip.res)
    def reassign_ip(self):
        import reassign

    def get_ip(self):
        nmap=nmap3.Nmap()
        results=nmap.scan_top_ports("172.25.1.0/24",args="-sn")
        ip=list(results.keys())
        ip=ip[:-2]
        for i in ip:
            self.plainTextEdit.appendPlainText(i)
            
        self.breached_ip()
    ''' def breached_ip(self):
        print("before imp")
        import capture_ip
        print("after imp")
        self.plainTextEdit_2.appendPlainText(res)'''
    def Exit(self):
        sys.exit(0)

app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())
