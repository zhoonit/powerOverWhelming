# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GuSan\Desktop\pyqt\gui_select_code.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectCode(object):

    def __init__(self, widget):
        Ui_SelectCode.__init__(self)
        self.setupUi(widget)
        self.initUi()

    def setupUi(self, SelectCode):
        SelectCode.setObjectName("SelectCode")
        SelectCode.resize(1300, 1000)
        self.centralwidget = QtWidgets.QWidget(SelectCode)
        self.centralwidget.setObjectName("centralwidget")
        self.opt_select_code_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.opt_select_code_3.setGeometry(QtCore.QRect(970, 100, 21, 22))
        self.opt_select_code_3.setText("")
        self.opt_select_code_3.setObjectName("opt_select_code_3")
        self.txt_select_code_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_select_code_1.setGeometry(QtCore.QRect(150, 140, 320, 721))
        self.txt_select_code_1.setObjectName("txt_select_code_1")
        self.opt_select_code_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.opt_select_code_1.setGeometry(QtCore.QRect(310, 100, 21, 22))
        self.opt_select_code_1.setText("")
        self.opt_select_code_1.setObjectName("opt_select_code_1")
        self.txt_select_code_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_select_code_3.setGeometry(QtCore.QRect(810, 140, 320, 721))
        self.txt_select_code_3.setObjectName("txt_select_code_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_compile_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_compile_start.setGeometry(QtCore.QRect(980, 890, 151, 51))
        self.btn_compile_start.setObjectName("btn_compile_start")
        self.opt_select_code_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.opt_select_code_2.setGeometry(QtCore.QRect(640, 100, 21, 22))
        self.opt_select_code_2.setText("")
        self.opt_select_code_2.setObjectName("opt_select_code_2")
        self.txt_select_code_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_select_code_2.setGeometry(QtCore.QRect(480, 140, 320, 721))
        self.txt_select_code_2.setObjectName("txt_select_code_2")
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(150, 910, 791, 31))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        SelectCode.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SelectCode)
        self.statusbar.setObjectName("statusbar")
        SelectCode.setStatusBar(self.statusbar)

        self.retranslateUi(SelectCode)
        QtCore.QMetaObject.connectSlotsByName(SelectCode)

    def retranslateUi(self, SelectCode):
        _translate = QtCore.QCoreApplication.translate
        SelectCode.setWindowTitle(_translate("SelectCode", "Select Code"))
        self.label.setText(_translate("SelectCode", "Select Code"))
        self.btn_compile_start.setText(_translate("SelectCode", "Compile!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectCode = QtWidgets.QMainWindow()
    ui = Ui_SelectCode()
    ui.setupUi(SelectCode)
    SelectCode.show()
    sys.exit(app.exec_())

