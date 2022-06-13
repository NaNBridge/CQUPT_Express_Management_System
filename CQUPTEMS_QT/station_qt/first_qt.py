"""使用qt纯代码化一个简单的gui"""
import sys

#from qtpy import PYQT6
from PyQt5 import QtCore, QtGui, QtWidgets

# app = qtwidgets.qApplication(sys.argv)  # 创建APP
# widgetHello = qtwidgets.qWidget()  # 创建窗体
# # 设置窗体的宽度和高度
# widgetHello.resize(280, 150)
# # 设置窗体的标题文字
# widgetHello.setWindowTitle("My First QT")
# # 创建标签
# LabHello = qtwidgets.QLabel(widgetHello)
# # 设置标签文字
# LabHello.setText("Hello World,PyQt5")
# font = QtGui.QFont()
# font.setPointSize(12)
# font.setBold(True)  # 设置字体为粗体

# LabHello.setFont(font)
# size = LabHello.sizeHint()
# LabHello.setGeometry(70, 60, size.width(), size.height())
# widgetHello.show()
# sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)  # 创建app， 用QApplication类 
widgetHello = QtWidgets.QWidget() #创建窗体， 用QWidget类 
widgetHello.resize(280*2,2*150) #设置窗体的 宽度和高度 
widgetHello.setWindowTitle("My First QT") #设置窗体的 标题文字 
LabHello = QtWidgets.QLabel(widgetHello) #创建标签， 父容器为widgetHello 
LabHello.setText("Hello World,PyQt5") #设置标签文 字
font = QtGui.QFont() #创建字体对象font，用QFont类 
font.setPointSize(12) #设置字体大小 ]]
font.setBold(True) #设置为粗体
# 设置为标签LabHello的字体 
size=LabHello.sizeHint() #获取LabHello的合适大小，返回 值是QSize类对象 
LabHello.setGeometry(70*2, 60*2, size.width(), size.height()) 
widgetHello.show() #显示对话框 sys.exit(app.exec_())
LabHello.setFont(font)
widgetHello.show()
sys.exit(app.exec_())