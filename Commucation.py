import sys
import platform
from main import *
count     = 0
time_rev  =[0]*50
theta1_rev=[0]*50
theta2_rev=[0]*50
theta3_rev=[0]*50

class Communication(MainWindow):
    
    def Serial_connect(self, COM, baudrate):
        self.ser.port = COM
        self.ser.baudrate =  baudrate
        self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.ser.parity = serial.PARITY_NONE #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits            #timeout block read
        self.ser.xonxoff = False     #disable software flow control
        self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 0    #timeout for write
        self.ser.timeout =0
        self.ser.open()
        self.ui.btn_notification.show()

        

    def connect(self):
        if(self.ui.the1_set.text()!=""):
            if not self.ser.isOpen():
                # print(self.ui.the1_set.text()+'HH')
                com=str('COM10')
                baud = self.baud_arduino.currentText()
                if baud =="115200":
                    Communication.Serial_connect(self,com,baud)
                else:
                    pass
        
    def disconnect(self):
        if self.ser.isOpen():
            self.ser.close()
        self.ui.mode_arduino.setText("Non")
        self.ui.btn_notification.hide()

        

    def sending(self):
        self.theta1.axes.clear()
        self.theta1.config_display(self.theta1)
        self.theta2.axes.clear()
        self.theta2.config_display(self.theta2)
        self.theta3.axes.clear()
        self.theta3.config_display(self.theta3)
        if self.ser.isOpen():
            self.ui.mode_arduino.setText("Con")
            theta1 = float(self.ui.the1_set.text())
            theta2 = float(self.ui.the2_set.text())
            theta3 = float(self.ui.the3_set.text())
            time = self.ui.time_respond.text().split()
            T = float(time[0])
            mode_PF= float(self.ui.mode_PF.text())


            if self.ui.mode_arduino.text()=="Con":
                self.ser.flushOutput()
                # data_send = str("{0},{1},{2}".format(theta1,theta2,theta3).encode())
                data_send = str("{0},{1},{2},{3}".format(theta1,theta2,theta3,T).encode())
                # self.ser.write("{0},{1},{2}".format(theta1,theta2,theta3).encode())
                self.ser.write("{0},{1},{2},{3}".format(theta1,theta2,theta3,T).encode())
                print(data_send)
            else:
                pass
        
    def receive(self):
        global count 
        global time_rev
        global theta1_rev
        global theta2_rev
        global theta3_rev

        if  self.ser.isOpen() :
            if self.ui.mode_arduino.text()=="Con":
                strdata = self.ser.readline().decode()
                # print(strdata)
                self.ser.flushInput()
                self.ser.flushOutput()
                # sys.stdout.write('\r'+strdata)
                beta = strdata.strip()
                Value = beta.strip("\r\n").split(",")
                if len(Value)==4:
                    Data=[
                        round(float(Value[0]),2),
                        round(float(Value[1]),2),
                        round(float(Value[2]),2),
                        float(Value[3]),
                    ] 
                    theta_drawing = [
                    np.deg2rad(Data[0]),
                    np.deg2rad(Data[1]),
                    np.deg2rad(Data[2]),
                    ]
                    T01 = self.Robot.initial_parameters(theta_drawing, 1)
                    T02 = self.Robot.initial_parameters(theta_drawing, 2)
                    T03 = self.Robot.initial_parameters(theta_drawing, 3)
                    T0E = self.Robot.initial_parameters(theta_drawing, 4)
                    x = np.array([T01[0, 3], T02[0, 3], T03[0, 3], T0E[0, 3]])
                    y = np.array([T01[1, 3], T02[1, 3], T03[1, 3], T0E[1, 3]])
                    z = np.array([T01[2, 3], T02[2, 3], T03[2, 3], T0E[2, 3]])

                    #tinh toan diem cuoi cung
                    anpha = round(y[3]/x[3],2)
                    # Phương trình bậc 2 có các hệ số 
                    a= 1+anpha**2
                    b= -2*((x[3]**2+y[3]**2)/x[3])
                    c= x[3]**2+y[3]**2-9
                    # Giải phương trình bậc 2 
                    delta = b**2-4*a*c
                    no_x1= (-b+np.sqrt(delta))/(2*a)
                    no_x2= (-b-np.sqrt(delta))/(2*a)
                    if(abs(no_x1)>=abs(no_x2)): no_x = no_x1
                    else: no_x=no_x2
                    no_y=anpha*no_x

                    no_x=np.round(no_x,2)
                    no_y=np.round(no_y,2)
                    no_z=np.round(z[3]-3.00,2)

                    
                    self.screen.axes.clear()
                    self.screen.config_display(self.screen)
                    # line -[link length] plot
                    self.screen.axes.plot([0, x[0]], [0, y[0]], [0, z[0]], linewidth=5)
                    self.screen.axes.plot([x[0], x[1]], [y[0], y[1]], [z[0], z[1]], linewidth=5)
                    self.screen.axes.plot([x[1], x[2]], [y[1], y[2]], [z[1], z[2]], linewidth=5)
                    self.screen.axes.plot([x[2], x[3]], [y[2], y[3]], [z[2], z[3]], linewidth=5)
                    self.screen.axes.plot([x[3], no_x], [y[3], no_y], [z[3], z[3]], linewidth=5)
                    self.screen.axes.plot([no_x, no_x], [no_y, no_y], [z[3], no_z], linewidth=5)
                    # Joints syntaxis plot
                    self.screen.axes.scatter(0, 0, 0, marker="D", color="k", s=100)
                    self.screen.axes.scatter(x[0], y[0], z[0], marker="o", color="r", s=100)
                    self.screen.axes.scatter(x[1], y[1], z[1], marker="o", color="c", s=200)
                    self.screen.axes.scatter(x[2], y[2], z[2], marker="o", color="c", s=200)
                    self.screen.axes.scatter(x[3], y[3], z[3], marker="o", color="c", s=200)
                    self.screen.axes.scatter(no_x, no_y, z[3], marker="D", color="c", s=50)
                    self.screen.axes.scatter(no_x, no_y, no_z, marker="D", color="c", s=50)

                    # self.ui.current_x.setText(str(np.round(x[3], 2)))
                    # self.ui.current_y.setText(str(np.round(y[3], 2)))
                    # self.ui.current_z.setText(str(np.round(z[3], 2)))

                    self.ui.current_x.setText(str(no_x))
                    self.ui.current_y.setText(str(no_y))
                    self.ui.current_z.setText(str(no_z))

                    self.screen.draw()

                    self.ui.the1_current.setText(str(Data[0]))
                    self.ui.the2_current.setText(str(Data[1]))
                    self.ui.the3_current.setText(str(Data[2]))

                    # theta1_rev[count]=  Data[0]  
                    # theta2_rev[count]=  Data[1]  
                    # theta3_rev[count]=  Data[2] 
                    # time_rev[count]  =  Data[3]
                    # # print(time_rev)

                    # self.theta1.axes.clear()
                    # self.theta1.config_display(self.theta1)
                    # self.theta1.axes.plot(time_rev[0:count],theta1_rev[0:count],'go-')
                    # self.theta1.draw()  

                    # self.theta2.axes.clear()
                    # self.theta2.config_display(self.theta2)
                    # self.theta2.axes.plot(time_rev[0:count],theta2_rev[0:count],'go-')
                    # self.theta2.draw()

                    # self.theta3.axes.clear()
                    # self.theta3.config_display(self.theta3)
                    # self.theta3.axes.plot(time_rev[0:count],theta3_rev[0:count],'go-')
                    # self.theta3.draw()    
                    # count+=1
        else:
            # self.theta1.axes.clear()
            # self.theta1.config_display(self.theta1)
            # self.theta2.axes.clear()
            # self.theta2.config_display(self.theta2)
            # self.theta3.axes.clear()
            # self.theta3.config_display(self.theta3)
            # count     = 0
            # time_rev  =[0]*50
            # theta1_rev=[0]*50
            # theta2_rev=[0]*50
            # theta3_rev=[0]*50
            # self.ui.led_mode_PID.hide()
            # self.ui.led_mode_FUZZY.hide()
            pass
    
        
    
