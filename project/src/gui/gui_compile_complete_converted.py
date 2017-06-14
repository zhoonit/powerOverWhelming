# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GuSan\Desktop\pyqt\gui_compile_complete.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_output_test = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_output_test.setGeometry(QtCore.QRect(690, 130, 271, 751))
        self.txt_output_test.setObjectName("txt_output_test")
        self.txt_code_complete = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_code_complete.setGeometry(QtCore.QRect(30, 90, 631, 881))
        self.txt_code_complete.setObjectName("txt_code_complete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_copy_code = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy_code.setGeometry(QtCore.QRect(770, 900, 131, 31))
        self.btn_copy_code.setObjectName("btn_copy_code")
        self.btn_test_compile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test_compile.setGeometry(QtCore.QRect(770, 940, 131, 31))
        self.btn_test_compile.setObjectName("btn_test_compile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compile Complete"))
        self.label.setText(_translate("MainWindow", "Compile Complete"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.btn_copy_code.setText(_translate("MainWindow", "Copy Code"))
        self.btn_test_compile.setText(_translate("MainWindow", "Test Compile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

