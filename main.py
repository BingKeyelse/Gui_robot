################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
# pyuic5 -x loggui_complete.ui -o loggui_complete.py
# pyuic5 -x main.ui -o ui_main.py  
# pyuic5 -x splash_screen.ui -o ui_splash_screen.py 
# pyuic5 -x Sum_gui.ui -o Sum_gui.py 
'''
Ý nghĩa các nút nhấn trong Sum Gui:
- 

'''


import sys
import platform
import matplotlib
import os
import serial
import serial.tools.list_ports
import numpy as np
import threading

from matplotlib import cm
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
# from matplotlib.animation import FuncAnimation

from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication,QMainWindow

## ==> GLOBALS
counter = 0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

import warnings
warnings.filterwarnings('ignore')
from app_modules import *

# Setup không gian vẽ liên kết với Gui
class Display(FigureCanvas):
    def __init__(self,parent=None, width = 70, height = 50,dpi=75):
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#343b48')
        figure.suptitle('3D Robotics Simulation',color='white',fontsize=15)
        self.axes = figure.gca(projection='3d')
        figure.tight_layout()
        super(Display, self).__init__(figure)
    def config_display(self,widget):
        widget.axes.set_facecolor('#343b48')
        widget.axes.grid(True)
        widget.axes.set_xlim(-25,25)
        widget.axes.set_ylim(-25,25)
        widget.axes.set_zlim(-25,25)


        widget.axes.set_xlabel('X',color='pink',fontsize=15)
        widget.axes.set_ylabel('Y',color='pink',fontsize=15)
        widget.axes.set_zlabel('Z_axis',color='pink',fontsize=10)
        widget.axes.tick_params(axis='x', colors='pink')
        widget.axes.tick_params(axis='y', colors='pink')
        widget.axes.tick_params(axis='z', colors='pink')

class Display_2D_thelta1(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.patch.set_facecolor('#343b48')
        fig.tight_layout()
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)
        self.axes.xaxis.set_ticklabels([])
        super(Display_2D_thelta1, self).__init__(fig)

        #matplotlib.pyplot.style.use("seaborn-notebook")
    def config_display(self,widget):
        widget.axes.grid(True)
        widget.axes.set_xlim(-5,15)
        widget.axes.set_ylim(-150,150)
        widget.axes.tick_params(axis='y', colors='white')

        #fig.tight_layout()

class Display_2D_thelta2(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.patch.set_facecolor('#343b48')
        fig.tight_layout()
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)
        self.axes.xaxis.set_ticklabels([])
        super(Display_2D_thelta2, self).__init__(fig)
        #matplotlib.pyplot.style.use("seaborn-notebook")
    def config_display(self,widget):
        widget.axes.grid(True)
        widget.axes.set_xlim(-5,15)
        widget.axes.set_ylim(-150,150)
        widget.axes.tick_params(axis='y', colors='white')

class Display_2D_thelta3(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.patch.set_facecolor('#343b48')
        fig.tight_layout()
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)
        self.axes.xaxis.set_ticklabels([])
        super(Display_2D_thelta3, self).__init__(fig)
        #matplotlib.pyplot.style.use("seaborn-notebook")
    def config_display(self,widget):
        widget.axes.grid(True)
        widget.axes.set_xlim(-5,15)
        widget.axes.set_ylim(-150,150)
        widget.axes.tick_params(axis='y', colors='white')     

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # phần thêm vào
        self.ui = uic.loadUi('Sum_gui.ui',self)
        self.setMinimumSize(QtCore.QSize(1290,725))
        self.setMaximumSize(QtCore.QSize(1290,725))
        # self.ui.setupUi(self)
        print('System: '+platform.system()+" of Nhóm 4") # có thể sửa được nè    
        print('Version: '+platform.release()) # có thể sửa được nè
        UIFunctions.uiDefinitions(self)
        ## initializing Threading Core
        self.threadpool = QtCore.QThreadPool()
        # initialize parameter:
        self.link = [float(self.length1.text()),
                     float(self.length2.text()),
                     float(self.length3.text())]
        Userfunctions.initialize_robot(self,self.link) # Khởi tạo robot

        self.screen = Display(self,width=50, height=50, dpi=70)
        self.screen.config_display(self.screen)
        self.ui.screen_form.addWidget(self.screen)

        self.theta1 = Display_2D_thelta1(self, width=5, height=4, dpi=70)
        self.theta1.config_display(self.theta1)
        self.ui.screen_thelta1.addWidget(self.theta1)

        self.theta2 = Display_2D_thelta2(self, width=5, height=4, dpi=70)
        self.theta2.config_display(self.theta2)
        self.ui.screen_thelta2.addWidget(self.theta2)
        
        self.theta3 = Display_2D_thelta3(self, width=5, height=4, dpi=70)
        self.theta3.config_display(self.theta3)
        self.ui.screen_thelta3.addWidget(self.theta3)

        self.ser =  serial.Serial()
        self.ui.but_logout.clicked.connect(lambda: UIFunctions.logout(self))
        self.ui.but_cancer.clicked.connect(self.close)
        # Ẩn màn hình F_I
        self.ui.choose_F_I.setText("N")
        self.ui.choose_F_I.hide()
        self.ui.but_trans_angle.hide()
        self.ui.but_trans_position.hide()
        self.ui.textEdit.setText('0.2')
        self.ui.btn_closescreen_display2D.hide()
        self.ui.mode_arduino.hide()
        self.ui.mode_arduino.setText('Non')
        self.ui.btn_notification.hide()
        self.ui.led_mode_PID.hide()
        self.ui.led_mode_FUZZY.hide()
        self.ui.mode_PF.setText("0")
        self.ui.mode_PF.hide()
        self.ui.button_mode_PID.hide()
        self.ui.button_mode_FUZZY.hide()

        #Nút nhấn plus or minus thanh giá trị
        self.ui.but_plus_the1_adjust.clicked.connect(lambda: UIFunctions.Plus_the1_adjust(self))
        self.ui.but_plus_the2_adjust.clicked.connect(lambda: UIFunctions.Plus_the2_adjust(self))
        self.ui.but_plus_the3_adjust.clicked.connect(lambda: UIFunctions.Plus_the3_adjust(self))
        self.ui.but_minus_the1_adjust.clicked.connect(lambda: UIFunctions.Minus_the1_adjust(self))
        self.ui.but_minus_the2_adjust.clicked.connect(lambda: UIFunctions.Minus_the2_adjust(self))
        self.ui.but_minus_the3_adjust.clicked.connect(lambda: UIFunctions.Minus_the3_adjust(self))

       

        # Nút chon mode PID và Fuzzy
        self.ui.button_mode_PID.clicked.connect(lambda: UIFunctions.PID(self))
        self.ui.button_mode_FUZZY.clicked.connect(lambda: UIFunctions.Fuzzy(self))        
        # Nút set chạy thuận nghịch và pause
        self.ui.but_forward.clicked.connect(lambda: UIFunctions.forward(self))
        self.ui.but_inverse.clicked.connect(lambda: UIFunctions.inverse(self))
        self.ui.but_inverse.clicked.connect(lambda: Userfunctions.inverse(self))
        self.ui.but_pause.clicked.connect(lambda: UIFunctions.pause(self))
        # Setup thanh chỉnh 
        self.ui.the1_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the1_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        # Setup mode hand
        self.ui.btn_left.clicked.connect(lambda: Userfunctions.left_signal(self))
        self.ui.btn_right.clicked.connect(lambda: Userfunctions.right_signal(self))
        self.ui.btn_for.clicked.connect(lambda: Userfunctions.forward_signal(self))
        self.ui.btn_back.clicked.connect(lambda: Userfunctions.backward_signal(self))
        self.ui.btn_up.clicked.connect(lambda: Userfunctions.up_signal(self))
        self.ui.btn_down.clicked.connect(lambda: Userfunctions.down_signal(self))
        #Set nút nhấn liên quan thời gian
        self.ui.btn_plustime.clicked.connect(lambda: UIFunctions.timechange_plus(self))
        self.ui.btn_minustime.clicked.connect(lambda: UIFunctions.timechange_minus(self))
        #Set cập nhập độ dài link
        self.ui.btn_reset.clicked.connect(lambda: Userfunctions.link_adjustment(self))
        #Set expand place of work
        # self.ui.btn_openscreen_display2D.clicked.connect(lambda: UIFunctions.expand_place(self)) cai này là cái chính
        # self.ui.btn_openscreen_display2D.clicked.connect(lambda: Userfunctions.test_plot(self))
        # self.ui.btn_closescreen_display2D.clicked.connect(lambda: UIFunctions.close_place(self)) cái này cũng là cái chinhs
        #Check Mode
        self.ui.mode_check.stateChanged.connect(lambda: UIFunctions.simulation_check(self))
        #Set up connect Arduino
        self.ui.btnconnect_arduino.clicked.connect(lambda: Communication.connect(self))
        self.ui.btn_disconnect_arduino.clicked.connect(lambda: Communication.disconnect(self))
        #Truyền và gửi tín hiệu đi 
        self.ui.btn_start.clicked.connect(lambda: Communication.sending(self))
        self.ui.btn_start.clicked.connect(lambda: Communication.receive(self))  
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(lambda: Communication.receive(self))
        # time = self.ui.time_respond.text().split()
        # T = int(time[0])
        self.timer.start(80)

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # CLOSE SPLASH SCREEN
            self.hide()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            

        # INCREASE COUNTER
        counter += 1

# Log Screen
class Log_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_Log_screen()
        self.uic.setupUi(self)
        self.uic.button_cancer.clicked.connect(self.close)
        self.uic.button_login.clicked.connect(self.login)
        self.uic.button_show.clicked.connect(self.showpass)
        self.uic.button_pass.clicked.connect(self.hidepass)
        self.uic.button_error.clicked.connect(self.error)
        # self.uic.button_show.show()
        self.uic.button_pass.hide()
        self.uic.button_error.hide()
        

    def login(self):
        ID = self.uic.screen_user.text()
        password = self.uic.screen_pass.text()
        if ID=="MAGICIAN" and password=='12345':
            self.close()
            self.main = SplashScreen()
            self.main.show()
        else:
            Log_screen.login_plus(self)
            
    def login_plus(self):
        self.uic.button_error.show()
        self.uic.button_login.hide()

    def error(self):
        self.uic.button_error.hide()
        self.uic.button_login.show()
                
    def showpass(self):
        self.uic.screen_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uic.button_show.hide()
        self.uic.button_pass.show()
    def hidepass(self):
        self.uic.screen_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uic.button_show.show()
        self.uic.button_pass.hide()
        

# class Worker(QtCore.QRunnable):

#     def __init__(self, function, *args, **kwargs):
#         super(Worker, self).__init__()
#         self.function = function
#         self.args = args
#         self.kwargs = kwargs

#     @pyqtSlot()
#     def run(self):

#         self.function(*self.args, **self.kwargs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Log_screen()
    window.show()
    sys.exit(app.exec_())

