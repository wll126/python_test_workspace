import sys
from PyQt5 import QtWidgets
from com.ll.gui import ui_form

app=QtWidgets.QApplication(sys.argv)
baseWidget=QtWidgets.QWidget()

ui=ui_form.Ui_Form()
ui.setupUi(baseWidget)

baseWidget.show()
sys.exit(app.exec_())