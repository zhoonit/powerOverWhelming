import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic 
#import guiSelectCode

class GuiCompileSuccess(QtWidgets.QMainWindow) :

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

        self.btn_prev = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_prev.setGeometry(QtCore.QRect(690, 900, 221, 41))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Compile Complete"))
        self.label.setText(_translate("MainWindow", "Compile Complete"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.btn_prev.setText(_translate("MainWindow", "Select Another Code"))
        #self.btn_copy_code.setText(_translate("MainWindow", "Copy Code"))
        #self.btn_test_compile.setText(_translate("MainWindow", "Test Compile"))

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_prev.clicked.connect(self.goPrev)

    def goPrev(self) :
        global window_select_code

        self.close()

    #    self.btn_test_compile.clicked.connect(self.testCompile)

    #def testCompile(self) :
    #    array = self.txt_input_test.toPlainText().split(',')
    #    array.sort()
    #    i=0
    #    str_arr=""
    #    while(i<len(array)) :
    #        str_arr+=array[i] + ","
    #        i=i+1
    #    self.txt_output_test.setPlainText(str_arr)

        #codeCompleteText = guiSelectCode.GuiSelectCode.loadText(guiSelectCode.GuiSelectCode(self))
        #self.txt_code_complete.setPlainText(codeCompleteText)