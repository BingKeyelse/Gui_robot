# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loggui_complete.ui'
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

class Ui_Log_screen(object):
    def setupUi(self, Log_screen):
        if not Log_screen.objectName():
            Log_screen.setObjectName(u"Log_screen")
        Log_screen.resize(450, 550)
        self.centralwidget = QWidget(Log_screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
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
"}\n"
"QPushButton#button_pass:pressed{\n"
"	padding-left:5px;\n"
"	padding-stop:5px;\n"
"	background-color: rgba(105,118,132,200);\n"
"}\n"
"QPushButton#button_error{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#button_error:hover{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#button_erroe:pressed{\n"
"	padding-left:5px;\n"
"	padding-stop:5px;\n"
"	background-color: rgba(105,118,132,200);\n"
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 300, 420))
        self.label.setStyleSheet(u"border-image: url(:/images/background.png);\n"
"border-radius:20px;\n"
"\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 280, 390))
        self.label_2.setStyleSheet(u"background-color: rgba(0,0,0,100);\n"
"border-radius:20px;")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(135, 95, 101, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgba(255,255,255,210);\n"
"")
        self.label_6.setScaledContents(False)
        self.screen_user = QLineEdit(self.widget)
        self.screen_user.setObjectName(u"screen_user")
        self.screen_user.setGeometry(QRect(80, 165, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.screen_user.setFont(font1)
        self.screen_user.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.screen_pass = QLineEdit(self.widget)
        self.screen_pass.setObjectName(u"screen_pass")
        self.screen_pass.setGeometry(QRect(80, 230, 200, 40))
        self.screen_pass.setFont(font1)
        self.screen_pass.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom: 2px solid rgba(10,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom : 7px;")
        self.screen_pass.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton(self.widget)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(80, 280, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.button_login.setFont(font2)
        self.button_cancer = QPushButton(self.widget)
        self.button_cancer.setObjectName(u"button_cancer")
        self.button_cancer.setGeometry(QRect(80, 330, 200, 40))
        self.button_cancer.setFont(font2)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 380, 181, 21))
        font3 = QFont()
        font3.setFamily(u"Poor Richard")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 85, 127);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 430, 91, 16))
        self.label_8.setStyleSheet(u"color:rgba(255,255,255,140);")
        self.button_show = QPushButton(self.widget)
        self.button_show.setObjectName(u"button_show")
        self.button_show.setGeometry(QRect(260, 240, 51, 28))
        self.button_show.setAutoFillBackground(False)
        self.button_show.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255,255,0);")
        icon = QIcon()
        icon.addFile(u"eye (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_show.setIcon(icon)
        self.button_pass = QPushButton(self.widget)
        self.button_pass.setObjectName(u"button_pass")
        self.button_pass.setGeometry(QRect(260, 240, 51, 28))
        self.button_pass.setAutoFillBackground(False)
        self.button_pass.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255,255,0);")
        icon1 = QIcon()
        icon1.addFile(u"eye-crossed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pass.setIcon(icon1)
        self.button_error = QPushButton(self.widget)
        self.button_error.setObjectName(u"button_error")
        self.button_error.setGeometry(QRect(80, 280, 200, 40))
        self.button_error.setFont(font2)
        self.button_error.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.screen_user.raise_()
        self.screen_pass.raise_()
        self.button_cancer.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.button_show.raise_()
        self.button_pass.raise_()
        self.button_error.raise_()
        self.button_login.raise_()
        Log_screen.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Log_screen)
        self.statusbar.setObjectName(u"statusbar")
        Log_screen.setStatusBar(self.statusbar)

        self.retranslateUi(Log_screen)

        QMetaObject.connectSlotsByName(Log_screen)
    # setupUi

    def retranslateUi(self, Log_screen):
        Log_screen.setWindowTitle(QCoreApplication.translate("Log_screen", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("Log_screen", u"Log in", None))
        self.screen_user.setPlaceholderText(QCoreApplication.translate("Log_screen", u" User Name", None))
        self.screen_pass.setPlaceholderText(QCoreApplication.translate("Log_screen", u" Password", None))
        self.button_login.setText(QCoreApplication.translate("Log_screen", u"L O G  I N", None))
        self.button_cancer.setText(QCoreApplication.translate("Log_screen", u"C A N C E R", None))
        self.label_7.setText(QCoreApplication.translate("Log_screen", u"MAGICIAN ROBOT", None))
        self.label_8.setText(QCoreApplication.translate("Log_screen", u"Creted by H\u01b0ng", None))
        self.button_show.setText("")
        self.button_pass.setText("")
        self.button_error.setText(QCoreApplication.translate("Log_screen", u"A G A I N", None))
    # retranslateUi

