import sys, time
sys.path.insert(0, 'c:/cGit/project/src/crawling')
import crawling_controller
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from . import guiSelectCode

class GuiStart(QtWidgets.QMainWindow):
     def __init__(self, parent=None):
         super(GuiStart, self).__init__(parent)
         uic.loadUi('c:/cGit/project/src/GUI/gui_start.ui', self)
         self.initUi()

     def initUi(self) :
         self.opt_c.setChecked(True)
         self.btn_submit.clicked.connect(self.on_click)

     def on_click(self) :

        if(self.edit_keyword.toPlainText()=="") :
            self.showDialogKeyWord()           
        else :
            self.close()
            window_select = guiSelectCode.GuiSelectCode(self)
            list_crawling = crawling_controller.search(self.edit_keyword.toPlainText(), 'python')
            window_select.txt_select_code_1.setPlainText(list_crawling[0])
            window_select.txt_select_code_2.setPlainText(list_crawling[1])
            window_select.txt_select_code_3.setPlainText(list_crawling[2])
            window_select.show()

     def showDialogKeyWord(self) :
        msg = QtWidgets.QMessageBox()
        msg.setText("키워드를 입력하세요.")
        msg.setWindowTitle("경고")
        msg.show()
        msg.exec_()

     #def inputOutput(self, keyword) :
     #    list_crawling = crawling_controller.search('quick sort', 'cpp')
     #    return [crawling_controller.search('quick sort', 'cpp')[0], crawling_controller.search('quick sort', 'cpp')[1], crawling_controller.search('quick sort', 'cpp')[2]]



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = guiSelectCode.GuiSelectCode()
    w.show()
    sys.exit(app.exec_())