import sys

from PyQt5 import QtWidgets
from PyQt5 import uic 

from . import guiCompiling
from . import guiStart
from . import guiCompileSuccess


class GuiSelectCode(QtWidgets.QMainWindow) :
     def __init__(self, parent=None):
        super(GuiSelectCode, self).__init__(parent)
        uic.loadUi('c:/cGit/project/src/GUI/gui_select_code.ui', self)
        self.initUi()

     def initUi(self) :
        self.btn_compile_start.clicked.connect(self.compile_click)
        self.opt_select_code_1.setChecked(True)
        #window_start = guiStart.GuiStart(self)
        #self.txt_select_code_1.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[0])
        #self.txt_select_code_2.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[1])
        #self.txt_select_code_3.setPlainText(window_start.inputOutput(window_start.edit_keyword.toPlainText())[2])
        

     def compile_click(self) :
        self.hide()
        self.window_compile_success = guiCompileSuccess.GuiCompileSuccess(self)
        #if(self.opt_select_code_1.isChecked()) :
        #    window_compile_success.txt_code_complete.setPlainText(self.loadText())
        #elif(self.opt_select_code_2.isChecked()) :
        #    window_compile_success.txt_code_complete.setPlainText(self.loadText())
        #else : 
        #    window_compile_success.txt_code_complete.setPlainText(self.loadText())
        #self.completed = 0
        #while self.completed<100 :
        #    self.completed+=0.001
        #    self.progress.setValue(self.completed)
        #    QtWidgets.QApplication.processEvents()

       
        self.window_compile_success.show()            

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


       