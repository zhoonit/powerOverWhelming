# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GuSan\Desktop\pyqt\gui_error_code.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from . import guiSelectCode

class GuiErrorCode(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(415, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_error_context = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_error_context.setGeometry(QtCore.QRect(690, 90, 270, 750))
        self.txt_error_context.setObjectName("txt_error_context")
        self.txt_error_code = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_error_code.setGeometry(QtCore.QRect(50, 90, 630, 880))
        self.txt_error_code.setObjectName("txt_error_code")
        self.btn_prev = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_prev.setGeometry(QtCore.QRect(690, 880, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_prev.setFont(font)
        self.btn_prev.setObjectName("btn_prev")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Error Code"))
        self.btn_prev.setText(_translate("MainWindow", "Select Another Code"))

    def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.setupUi(self)
         self.btn_prev.clicked.connect(self.goPrev)
    
    def goPrev(self) :
        global window_select_code

        self.close()
        
