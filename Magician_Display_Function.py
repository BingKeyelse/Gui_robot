import numpy as np
import math as m
import time
from Libs.Magician_Robotics_Libs import *
from main import *



class UIFunctions(MainWindow):
    
    def convert_to_Deg(value):
        return np.round(np.rad2deg(value), 2)

    def logout(self):
        self.close()
        self.main = Log_screen()
        self.main.show()

    def forward(self):
        self.ui.but_trans_position.show()
        self.ui.but_trans_angle.hide()
        self.ui.but_trans_position.setStyleSheet("background-color: rgb(85, 255, 255);"
"border-radius:30px;"
"")
        self.ui.but_trans_angle.setStyleSheet("background-color: rgba(20, 40, 70,150);"
"border-radius:30px;"
"")
        self.ui.choose_F_I.setText("F")


    def inverse(self):
        self.ui.but_trans_angle.show()
        self.ui.but_trans_position.hide()
        self.ui.but_trans_angle.setStyleSheet("background-color: rgb(85, 255, 255);"
"border-radius:30px;"
"")
        self.ui.but_trans_position.setStyleSheet("background-color: rgba(20, 40, 70,150);"
"border-radius:30px;"
"")
        self.ui.choose_F_I.setText("I")

    def pause(self):
        self.ui.but_trans_angle.hide()
        self.ui.but_trans_position.hide()
        self.ui.but_trans_angle.setStyleSheet("background-color: rgba(20, 40, 70,150);"
"border-radius:30px;"
"")
        self.ui.but_trans_position.setStyleSheet("background-color: rgba(20, 40, 70,150);"
"border-radius:30px;"
"")
        self.ui.choose_F_I.setText("N")
        self.ui.x_position.setText("0")
        self.ui.y_position.setText("0")
        self.ui.z_position.setText("0")
        self.ui.the1_set.setText('0')
        self.ui.the1_set.setText('0')
        self.ui.the1_set.setText('0')
        self.ui.the1_adjust.setValue(0)
        self.ui.the2_adjust.setValue(0)
        self.ui.the3_adjust.setValue(0)


    def PID(self):
        if (self.ui.mode_PF.text()!="1"):
            self.ui.led_mode_PID.show()
            self.ui.led_mode_FUZZY.hide()
            self.ui.mode_PF.setText('1')
        else:
            self.ui.led_mode_PID.hide()
            self.ui.led_mode_FUZZY.hide()
            self.ui.mode_PF.setText('0')
    
    def Fuzzy(self):
        if (self.ui.mode_PF.text()!="2"):
            self.ui.led_mode_PID.hide()
            self.ui.led_mode_FUZZY.show()
            self.ui.mode_PF.setText('2')
        else:
            self.ui.led_mode_PID.hide()
            self.ui.led_mode_FUZZY.hide()
            self.ui.mode_PF.setText('0')


    def uiDefinitions(self):
        self.ui.time_respond.setText("2 (s)")
        self.ui.mode_check.setChecked(False)
        self.ui.btn_start.setEnabled(False)
        # initialize parameter:
        self.length1.setText("8")
        self.length2.setText("9")
        self.length3.setText("10")
        self.ui.x_position.setText("0")
        self.ui.y_position.setText("0")
        self.ui.z_position.setText("0")
        self.ui.solution.setText("1")
        # UIFunctions.Update_value(self)
        self.ui.mode_check.setChecked(False)

    def expand_place(self):
        self.setMinimumSize(QtCore.QSize(1645,725))
        self.setMaximumSize(QtCore.QSize(1645,725))
        self.ui.btn_closescreen_display2D.show()
        self.ui.btn_openscreen_display2D.hide()
    
    def close_place(self):
        self.setMinimumSize(QtCore.QSize(1290,725))
        self.setMaximumSize(QtCore.QSize(1290,725))
        self.ui.btn_closescreen_display2D.hide()
        self.ui.btn_openscreen_display2D.show()

    # Giá trị thanh chạy sang 3 ô bên cạnh 
    def valuechange(self):
        value_the1 = str(self.ui.the1_adjust.value())
        value_the2 = str(self.ui.the2_adjust.value())
        value_the3 = str(self.ui.the3_adjust.value())
        self.ui.the1_set.setText(value_the1)
        self.ui.the2_set.setText(value_the2)
        self.ui.the3_set.setText(value_the3)
       


    def timechange_plus(self):
        time = self.ui.time_respond.text().split()
        plus = int(time[0]) + 1
        if 0 < plus and plus < 12:
            self.ui.time_respond.setText(str(plus) + " (s)")
        else:
            pass

    def timechange_minus(self):
        time = self.ui.time_respond.text().split()
        minus = int(time[0]) - 1
        if 0 < minus and minus < 12:
            self.ui.time_respond.setText(str(minus) + " (s)")
        else:
            pass

    # def length_change(self):
    #     self.ui.length1.setText("30")
    #     self.ui.length2.setText("30")
    #     self.ui.length3.setText("30")
    #     self.link = [
    #         float(self.length1.text()),
    #         float(self.length2.text()),
    #         float(self.length3.text()),
    #     ]

    def Update_value(self):
        self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
        self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
        self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))

    def reset(self):
        self.ui.the1_current.clear()
        self.ui.the2_current.clear()
        self.ui.the3_current.clear()

        self.ui.the1_set.clear()
        self.ui.the2_set.clear()
        self.ui.the3_set.clear()

        self.ui.length1.clear()
        self.ui.length2.clear()
        self.ui.length3.clear()

        self.ui.the1_adjust.setValue(0)
        self.ui.the2_adjust.setValue(0)
        self.ui.the3_adjust.setValue(0)

        self.ui.xpos.clear()
        self.ui.ypos.clear()
        self.ui.zpos.clear()

        self.ui.mode_check.setChecked(False)

    def Plus_the1_adjust(self):
        if(self.ui.the1_set.text()!=""):
            giatri=self.ui.the1_adjust.value()+1
            self.ui.the1_adjust.setValue(giatri)
            UIFunctions.valuechange(self)
    
    def Plus_the2_adjust(self):
        if(self.ui.the2_set.text()!=""):
            giatri=self.ui.the2_adjust.value()+1
            self.ui.the2_adjust.setValue(giatri)
            UIFunctions.valuechange(self)

    def Plus_the3_adjust(self):
        if(self.ui.the3_set.text()!=""):
            giatri=self.ui.the3_adjust.value()+1
            self.ui.the3_adjust.setValue(giatri)
            UIFunctions.valuechange(self)

    def Minus_the1_adjust(self):
        if(self.ui.the1_set.text()!=""):
            giatri=self.ui.the1_adjust.value()-1
            self.ui.the1_adjust.setValue(giatri)
            UIFunctions.valuechange(self)

    def Minus_the2_adjust(self):
        if(self.ui.the2_set.text()!=""):
            giatri=self.ui.the2_adjust.value()-1
            self.ui.the2_adjust.setValue(giatri)
            UIFunctions.valuechange(self)
    
    def Minus_the3_adjust(self):
        if(self.ui.the3_set.text()!=""):
            giatri=self.ui.the3_adjust.value()-1
            self.ui.the3_adjust.setValue(giatri)
            UIFunctions.valuechange(self)
        

    def simulation_check(self):
        if self.ui.mode_check.isChecked():
            self.btn_start.setEnabled(True)
        else:
            self.btn_start.setEnabled(False)
            
