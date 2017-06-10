import sys
from PyQt5 import QtWidgets
from PyQt5 import uic 
#import guiSelectCode

class GuiCompileSuccess(QtWidgets.QMainWindow) :
    def __init__(self, parent=None):
        super(GuiCompileSuccess, self).__init__(parent)
        uic.loadUi('c:/cGit/project/src/GUI/gui_compile_complete.ui', self)
        #codeCompleteText = guiSelectCode.GuiSelectCode.loadText(guiSelectCode.GuiSelectCode(self))
        #self.txt_code_complete.setPlainText(codeCompleteText)