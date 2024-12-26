# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loggui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 550)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 370, 480))
        self.widget.setStyleSheet(u"QPushButton#button_login{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#button_login:hover{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#button_login:pressed{\n"
"	padding-left:5px;\n"
"	padding-stop:5px;\n"
"	background-color: rgba(105,118,132,200);\n"
"}\n"
"QPushButton#button_cancer{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#button_cancer:hover{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPush"
                        "Button#button_cancer:pressed{\n"
"	padding-left:5px;\n"
"	padding-stop:5px;\n"
"	background-color: rgba(105,118,132,200);\n"
"}\n"
"QPushButton#button_show:pressed{\n"
"	padding-left:5px;\n"
"	padding-stop:5px;\n"
"	background-color: rgba(105,118,132,200);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 300, 420))
        self.label.setStyleSheet(u"border-image: url(:/images/background.png);\n"
"border-radius : 20px;\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 280, 390))
        self.label_2.setStyleSheet(u"background-color: rgba(0,0,0,100);\n"
"border-radius: 20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(135, 95, 101, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgba(255,255,255,210);\n"
"")
        self.label_3.setScaledContents(False)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 165, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 230, 200, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton(self.widget)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(80, 290, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.button_login.setFont(font2)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 420, 91, 16))
        self.label_4.setStyleSheet(u"color:rgba(255,255,255,140);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 400, 181, 21))
        font3 = QFont()
        font3.setFamily(u"Poor Richard")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 85, 127);")
        self.button_cancer = QPushButton(self.widget)
        self.button_cancer.setObjectName(u"button_cancer")
        self.button_cancer.setGeometry(QRect(80, 340, 200, 40))
        self.button_cancer.setFont(font2)
        self.button_show = QPushButton(self.widget)
        self.button_show.setObjectName(u"button_show")
        self.button_show.setGeometry(QRect(270, 240, 51, 28))
        self.button_show.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255,255,0);")
        icon = QIcon()
        icon.addFile(u":/icon/icons/20x20/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_show.setIcon(icon)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Log in", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u" User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u" Password", None))
        self.button_login.setText(QCoreApplication.translate("Form", u"L O G  I N", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Creted by H\u01b0ng", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"MAGICIAN ROBOT", None))
        self.button_cancer.setText(QCoreApplication.translate("Form", u"C A N C E R", None))
        self.button_show.setText("")
    # retranslateUi

