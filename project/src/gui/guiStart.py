import sys, time
from PyQt5 import QtCore, QtGui
import guiSelectCode
sys.path.insert(0, 'C:/Users/GuSan/Desktop/powerOverWhelming/project/src/keyword')
sys.path.insert(1, 'C:/Users/GuSan/Desktop/powerOverWhelming/project/src/crawling')
import crawling_controller
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
import synonym_search

class GuiStart(QtWidgets.QMainWindow):
    
     def setupUi(self, Start):
        Start.setObjectName("Start")
        Start.resize(640, 560)
        self.centralwidget = QtWidgets.QWidget(Start)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 171, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 181, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edit_keyword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_keyword.setGeometry(QtCore.QRect(20, 170, 601, 121))
        self.edit_keyword.setObjectName("edit_keyword")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(250, 460, 131, 41))
        self.btn_submit.setObjectName("btn_submit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 380, 561, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.opt_c = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_c.setFont(font)
        self.opt_c.setObjectName("opt_c")
        self.horizontalLayout.addWidget(self.opt_c)
        self.opt_cpp = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_cpp.setFont(font)
        self.opt_cpp.setObjectName("opt_cpp")
        self.horizontalLayout.addWidget(self.opt_cpp)
        self.opt_cs = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_cs.setFont(font)
        self.opt_cs.setObjectName("opt_cs")
        self.horizontalLayout.addWidget(self.opt_cs)
        self.opt_java = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_java.setFont(font)
        self.opt_java.setObjectName("opt_java")
        self.horizontalLayout.addWidget(self.opt_java)
        self.opt_py = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_py.setFont(font)
        self.opt_py.setObjectName("opt_py")
        self.horizontalLayout.addWidget(self.opt_py)
        self.opt_ruby = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_ruby.setFont(font)
        self.opt_ruby.setObjectName("opt_ruby")
        self.horizontalLayout.addWidget(self.opt_ruby)
        Start.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Start)
        self.statusbar.setObjectName("statusbar")
        Start.setStatusBar(self.statusbar)

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

     def retranslateUi(self, Start):
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("Start", "Start"))
        self.label_2.setText(_translate("Start", "Write your keyword."))
        self.label_3.setText(_translate("Start", "Select your language"))
        self.label.setText(_translate("Start", "Coding Helper"))
        self.btn_submit.setText(_translate("Start", "Submit"))
        self.opt_c.setText(_translate("Start", "C"))
        self.opt_cpp.setText(_translate("Start", "C++"))
        self.opt_cs.setText(_translate("Start", "C#"))
        self.opt_java.setText(_translate("Start", "Java"))
        self.opt_py.setText(_translate("Start", "Python"))
        self.opt_ruby.setText(_translate("Start", "Ruby"))


     def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.setupUi(self)
         self.initUi()

     def initUi(self) :
         self.opt_c.setChecked(True)
         self.btn_submit.clicked.connect(self.on_click)

     def on_click(self) :

        if(self.edit_keyword.toPlainText()=="") :
            self.showDialogKeyWord()
        else :
            
            if(self.opt_cpp.isChecked() or self.opt_py.isChecked()) :
                self.listCrawling()
            else :
                self.showDialogOption()

     def listCrawling(self) :
          
          global window_select
          window_select = guiSelectCode.GuiSelectCode()
          replacedString = self.convertToKeyword(self.edit_keyword.toPlainText())
          if(self.opt_cpp.isChecked()) :
              checkedOption = 'cpp'
          else :
              checkedOption = 'python'
          print(replacedString)
          try :
              msg = QtWidgets.QMessageBox()
              msg.setText("잠시만 기다려주세요. 30초의 시간이 소요됩니다.")
              msg.setWindowTitle("로딩중")
              msg.show()
              msg.exec_()
              QGuiApplication.setOverrideCursor(Qt.BusyCursor)

              list_crawling = crawling_controller.search(replacedString, 'cpp')
              QGuiApplication.restoreOverrideCursor()
              self.close()
              window_select.txt_select_code_1.setPlainText(list_crawling[0])
              window_select.txt_select_code_2.setPlainText(list_crawling[1])
              window_select.txt_select_code_3.setPlainText(list_crawling[2])
              window_select.show()
                
          except(BaseException) :
              QGuiApplication.restoreOverrideCursor()
              msg = QtWidgets.QMessageBox()
              msg.setText("검색결과가 없습니다.")
              msg.setWindowTitle("알림")
              msg.show()
              msg.exec_()
            
     def showDialogKeyWord(self) :
        msg = QtWidgets.QMessageBox()
        msg.setText("키워드를 입력하세요.")
        msg.setWindowTitle("경고")
        msg.show()
        msg.exec_()

     def showDialogOption(self) :
         msg = QtWidgets.QMessageBox()
         msg.setText("미구현")
         msg.setWindowTitle("미구현")
         msg.show()
         msg.exec_()

     def convertToKeyword(self, qString) :
         replacer = synonym_search.CsvWordReplacer('../keyword/synonym_test.csv')
         qSplited = qString.split(' ')
         qReplaced=''
         for i in qSplited :
             qReplaced += replacer.replace(i)
             qReplaced += ' '
         return qReplaced

     #def inputOutput(self, keyword) :
     #    list_crawling = crawling_controller.search('quick sort', 'cpp')
     #    return [crawling_controller.search('quick sort', 'cpp')[0], crawling_controller.search('quick sort', 'cpp')[1], crawling_controller.search('quick sort', 'cpp')[2]]



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = guiSelectCode.GuiSelectCode()
    window = w.show()
    sys.exit(app.exec_())