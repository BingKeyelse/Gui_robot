# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loggui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
'''
pyuic5 -x X.ui -o X.py
pyrcc5 X.qrc -o X.py
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res_rc,icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.widget.setStyleSheet("QPushButton#button_login{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#button_login:hover{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#button_login:pressed{\n"
"    padding-left:5px;\n"
"    padding-stop:5px;\n"
"    background-color: rgba(105,118,132,200);\n"
"}\n"
"QPushButton#button_cancer{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#button_cancer:hover{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#button_cancer:pressed{\n"
"    padding-left:5px;\n"
"    padding-stop:5px;\n"
"    background-color: rgba(105,118,132,200);\n"
"}\n"
"QPushButton#button_show:pressed{\n"
"    padding-left:5px;\n"
"    padding-stop:5px;\n"
"    background-color: rgba(105,118,132,200);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/background.png);\n"
"border-radius : 20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius: 20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(135, 95, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(255,255,255,210);\n"
"")
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.button_login = QtWidgets.QPushButton(self.widget)
        self.button_login.setGeometry(QtCore.QRect(80, 290, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(220, 420, 91, 16))
        self.label_4.setStyleSheet("color:rgba(255,255,255,140);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(90, 400, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 85, 127);")
        self.label_5.setObjectName("label_5")
        self.button_cancer = QtWidgets.QPushButton(self.widget)
        self.button_cancer.setGeometry(QtCore.QRect(80, 340, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancer.setFont(font)
        self.button_cancer.setObjectName("button_cancer")
        self.button_show = QtWidgets.QPushButton(self.widget)
        self.button_show.setGeometry(QtCore.QRect(270, 240, 51, 28))
        self.button_show.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255,255,0);")
        self.button_show.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/20x20/cil-loop-circular.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_show.setIcon(icon)
        self.button_show.setObjectName("button_show")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log in"))
        self.lineEdit.setPlaceholderText(_translate("Form", " User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Password"))
        self.button_login.setText(_translate("Form", "L O G  I N"))
        self.label_4.setText(_translate("Form", "Creted by Hưng"))
        self.label_5.setText(_translate("Form", "MAGICIAN ROBOT"))
        self.button_cancer.setText(_translate("Form", "C A N C E R"))

import icon_rc
import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

