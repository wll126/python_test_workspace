#  使用pyqt5,纯代码实现一个简单的GUI程序
import sys
from PyQt5 import QtCore,QtGui,QtWidgets

app=QtWidgets.QApplication(sys.argv)   # 创建app ，用QApplication 类
widgetHello=QtWidgets.QWidget()   # 创建窗体
widgetHello.resize(280,150) # 设置窗体的宽度和高度
widgetHello.setWindowTitle('Demo title')    # 设置窗体标题文字

labHello=QtWidgets.QLabel(widgetHello)  # 创建标签，父容器为widHello
labHello.setText(" 设置标签文字")
font=QtGui.QFont()      # 创建字体对象
font.setPointSize(12)
font.setBold(True)
labHello.setFont(font)
size=labHello.sizeHint()
labHello.setGeometry(70,60,size.width(),size.height())

widgetHello.show()      # 显示对话框
sys.exit(app.exec_())   # 运行应用程序




