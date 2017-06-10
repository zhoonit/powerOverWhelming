import sys
from PyQt5 import QtWidgets
from PyQt5 import uic 
#import guiCompileSuccess
from . import guiSelectCode

class GuiCompiling(QtWidgets.QMainWindow) :
    def __init__(self, parent=None):
        super(GuiCompiling, self).__init__(parent)
        uic.loadUi('C:\\Users\\GuSan\\Desktop\\pyqt\\gui_compiling.ui', self)
        #self.show()
        #self.initUi()
        self.download()

    #def initUi(self) :
    #    self.txt_compiling.setPlainText(guiSelectCode.GuiSelectCode.loadText(guiSelectCode.GuiSelectCode(self)))
            

    #def loadText(self) :
    #    if(guiSelectCode.GuiSelectCode(self).opt_select_code_1.isChecked()) :
    #       self.txt_compiling.setPlainText(guiSelectCode.GuiSelectCode(self).txt_select_code_1.toPlainText())
    #    elif(guiSelectCode.GuiSelectCode(self).opt_select_code_2.isChecked()) :
    #       self.txt_compiling.setPlainText(guiSelectCode.GuiSelectCode(self).txt_select_code_2.toPlainText())
    #    else :
    #       self.txt_compiling.setPlainText(guiSelectCode.GuiSelectCode(self).txt_select_code_3.toPlainText())