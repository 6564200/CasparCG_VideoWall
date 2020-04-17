# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import glob, os
import sys
import chardet

import datetime
from datetime import datetime, timedelta
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem, QDateTimeEdit, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime
 
from GUI import Ui_MainWindow
import sys

color_index = {7: QColor(40,50,180), 1: QColor(80,30,80), 2: QColor(40,100,50), 3: QColor(200,50,50), 4: QColor(40,180,20), 5: QColor(180,30,80), 6: QColor(0,10,10)}



class mywindow(QtWidgets.QMainWindow):
    files = ""

    CURENT = 0
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        
        self.ui.pushB_Init2.clicked.connect(self.pushB_Init2)
        self.ui.pushB_Init12.clicked.connect(self.pushB_Init12)
        self.ui.pushB_Connect.clicked.connect(self.pushB_Connect)
        
        self.ui.pushB_Restart.clicked.connect(self.pushB_Restart)
        
        #self.ui.actionSend.triggered.connect(self.MenuSendClicked)
        
        #self.ui.label_1.clicked.connect(self.label_1)
        #self.ui.actionExit.triggered.connect(self.MenuExitClicked)
        #self.ui.pushButtonExit.clicked.connect(self.MenuExitClicked)
        #self.ui.pushButton.clicked.connect(self.InsertProg)
        #self.ui.tableWidget.cellClicked[int, int].connect(self.clickedRowColumn)

    def pushB_Init12(self):
        print("pushB_Init12")
        
        return True

    def pushB_Init2(self):
        print("pushB_Init2")
        
        return True

    def pushB_Connect(self):
        print("pushB_Connect")
        return True

    def pushB_Restart(self):
        print("pushB_Restart")
        return True
        
    
    def label_1(self):
        print("label_1")
        return True


    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        f = e.mimeData().urls()
        mywindow.files = f[0].toString()
        print(mywindow.files)
        if mywindow.files[-3:] == "mp4":
            print("кто это?")


            
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
