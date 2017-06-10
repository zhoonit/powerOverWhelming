import GUI.guiStart
import sys

app = GUI.guiStart.QtWidgets.QApplication(sys.argv)
w = GUI.guiStart.guiSelectCode.GuiSelectCode()
w.show()
sys.exit(app.exec_())