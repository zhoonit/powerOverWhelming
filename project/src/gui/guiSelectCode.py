import sys

import signal
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic 

from . import guiStart
from . import guiCompileSuccess
# sys.path.insert(1, 'C:/Users/GuSan/Desktop/powerOverWhelming/project/src/comp_exec')
from ..comp_exec import validation
from . import guiErrorCode

class GuiSelectCode(QtWidgets.QMainWindow) :

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

      def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.setupUi(self)
         self.initUi()

      def initUi(self) :
        self.btn_compile_start.clicked.connect(self.compile_click)
        self.opt_select_code_1.setChecked(True)
        #window_start = guiStart.GuiStart(self)
        #self.txt_select_code_1.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[0])
        #self.txt_select_code_2.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[1])
        #self.txt_select_code_3.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[2])
        

      def compile_click(self) :
        global window_compile_success
        global window_compile_fail
        window_compile_success = guiCompileSuccess.GuiCompileSuccess()
        window_compile_fail = guiErrorCode.GuiErrorCode()
        self.completed = 0
        while self.completed<100 :
            self.completed+=0.001
            self.progress.setValue(self.completed)
            QtWidgets.QApplication.processEvents()

        tupleCompile = validation.validation(self.loadText(), 'cpp')
        print(tupleCompile[0])
        if(tupleCompile[1]==1) :
           msg = QtWidgets.QMessageBox()
           msg.setText("컴파일 에러")
           msg.setWindowTitle("컴파일 에러")
           msg.show()
           msg.exec_()
           window_compile_fail.txt_error_code.setPlainText(self.loadText())
           window_compile_fail.txt_error_context.setPlainText(tupleCompile[0])
           window_compile_fail.show()
           return window_compile_fail
        else :
            window_compile_success.txt_code_complete.setPlainText(self.loadText())
            window_compile_success.txt_output_test.setPlainText(tupleCompile[0])
            window_compile_success.show()
            return window_compile_success
        

      def loadText(self) :
         if(self.opt_select_code_1.isChecked()) :
             print("radioButton 1 is toggled")
             return self.txt_select_code_1.toPlainText()
         elif(self.opt_select_code_2.isChecked()) :
             print("radioButton 2 is toggled")
             return self.txt_select_code_2.toPlainText()
         else :
             print("radioButton 3 is toggled")
             return self.txt_select_code_3.toPlainText()


       