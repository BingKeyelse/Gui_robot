import numpy as np
import math as m
import time
from Libs.Magician_Robotics_Libs import *
from main import *


class Userfunctions(MainWindow):
    # Truy cập vào hàm Magician để lấy độ dài 
    def initialize_robot(self, length):
        self.Robot = Magician(length)
        if self.ui.the1_set.text() != "":
            self.the = [
                np.deg2rad(float(self.ui.the1_set.text())),
                np.deg2rad(float(self.ui.the2_set.text())),
                np.deg2rad(float(self.ui.the3_set.text())),
            ]

    #Hàm chuyển đổi radian sang góc với việc làm tròn 2 số 
    def convert_to_Deg(value):
        return np.round(np.rad2deg(value), 2)


    # Code để vẽ chính display trên màn hình ,  quy định một số hình ảnh cấu trúc 
    def Geometry_display(self):
        mode_1 = self.ui.choose_F_I.text()
        if mode_1=="F" :
            try:
                #self vì đây là biến toàn class khi muốn xử dụng def trong class
                self.the = [
                    np.deg2rad(float(self.ui.the1_set.text())),
                    np.deg2rad(float(self.ui.the2_set.text())),
                    np.deg2rad(float(self.ui.the3_set.text())),
                ]
                T01 = self.Robot.initial_parameters(self.the, 1)
                T02 = self.Robot.initial_parameters(self.the, 2)
                T03 = self.Robot.initial_parameters(self.the, 3)
                T0E = self.Robot.initial_parameters(self.the, 4)
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
                self.screen.axes.scatter(0, 0, 0, marker="D", color="k", s=200)
                self.screen.axes.scatter(x[0], y[0], z[0], marker="D", color="r", s=100)
                self.screen.axes.scatter(x[1], y[1], z[1], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[2], y[2], z[2], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[3], y[3], z[3], marker="D", color="c", s=200)
                self.screen.axes.scatter(no_x, no_y, z[3], marker="D", color="c", s=50)
                self.screen.axes.scatter(no_x, no_y, no_z, marker="D", color="c", s=50)


                self.ui.x_position.setText(str(np.round(no_x, 2)))
                self.ui.y_position.setText(str(np.round(no_y, 2)))
                self.ui.z_position.setText(str(np.round(no_z, 2)))
                # self.ui.x_position.setText(str(np.round(x[3], 2)))
                # self.ui.y_position.setText(str(np.round(y[3], 2)))
                # self.ui.z_position.setText(str(np.round(z[3], 2)))
                self.screen.draw()
            except:
                print("loading....")
        else:
            pass
    #hàm vẽ riêng cho nút nhấn 
    def Geometry_display_inver(self,theta):
        mode_1 = self.ui.choose_F_I.text()
        if  mode_1=="I":
            self.the=theta
            T01 = self.Robot.initial_parameters(self.the, 1)
            T02 = self.Robot.initial_parameters(self.the, 2)
            T03 = self.Robot.initial_parameters(self.the, 3)
            T0E = self.Robot.initial_parameters(self.the, 4)
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
            # # Joints syntaxis plot
            self.screen.axes.scatter(0, 0, 0, marker="D", color="k", s=100)
            self.screen.axes.scatter(x[0], y[0], z[0], marker="D", color="r", s=100)
            self.screen.axes.scatter(x[1], y[1], z[1], marker="D", color="c", s=200)
            self.screen.axes.scatter(x[2], y[2], z[2], marker="D", color="c", s=200)
            self.screen.axes.scatter(x[3], y[3], z[3], marker="D", color="c", s=200)
            self.screen.axes.scatter(no_x, no_y, z[3], marker="D", color="c", s=50)
            self.screen.axes.scatter(no_x, no_y, no_z, marker="D", color="c", s=50)
            self.screen.draw()
        else:
            return
    #Ve riêng cho cap nhap
    def Geometry_display_change(self):
        mode_1 = self.ui.choose_F_I.text()
        if mode_1=="F" or mode_1=='I':
            try:
                #self vì đây là biến toàn class khi muốn xử dụng def trong class
                self.the = [
                    np.deg2rad(float(self.ui.the1_set.text())),
                    np.deg2rad(float(self.ui.the2_set.text())),
                    np.deg2rad(float(self.ui.the3_set.text())),
                ]
                T01 = self.Robot.initial_parameters(self.the, 1)
                T02 = self.Robot.initial_parameters(self.the, 2)
                T03 = self.Robot.initial_parameters(self.the, 3)
                T0E = self.Robot.initial_parameters(self.the, 4)
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
                self.screen.axes.scatter(x[0], y[0], z[0], marker="D", color="r", s=100)
                self.screen.axes.scatter(x[1], y[1], z[1], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[2], y[2], z[2], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[3], y[3], z[3], marker="D", color="c", s=200)
                self.screen.axes.scatter(no_x, no_y, z[3], marker="D", color="c", s=50)
                self.screen.axes.scatter(no_x, no_y, no_z, marker="D", color="c", s=50)

                self.ui.x_position.setText(str(np.round(no_x, 2)))
                self.ui.y_position.setText(str(np.round(no_y, 2)))
                self.ui.z_position.setText(str(np.round(no_z, 2)))
                # self.ui.x_position.setText(str(np.round(x[3], 2)))
                # self.ui.y_position.setText(str(np.round(y[3], 2)))
                # self.ui.z_position.setText(str(np.round(z[3], 2)))
                self.screen.draw()
            except:
                print("loading....")
        else:
            pass
    # Hàm cho nghich
    def inverse(self):
        mode_1 = self.ui.choose_F_I.text()
        if mode_1=='I'and self.ui.y_position.text()!="Error":
            x = np.round(float(self.ui.x_position.text()),2)
            y = np.round(float(self.ui.y_position.text()),2)
            z = np.round(float(self.ui.z_position.text()),2)
            # print(x)
            # print(y)
            # print(z)
            #tinh toan diem cuoi cung
            anpha = round(y/x,10)
            # Phương trình bậc 2 có các hệ số 
            a= 1+anpha**2
            b= -2*((x**2+y**2)/x)
            c= x**2+y**2-9
            # Giải phương trình bậc 2 
            delta = b**2-4*a*c
            delta=round(delta,3)
            # print(delta)
            no_x1= (-b+np.sqrt(delta))/(2*a)
            no_x2= (-b-np.sqrt(delta))/(2*a)
            if(abs(no_x1)>abs(no_x2)): no_x = no_x2
            else: no_x=no_x1
            no_y=anpha*no_x

            no_x00=np.round(no_x,10)
            no_y00=np.round(no_y,10)
            no_z00=np.round(z+3,10)

            position = [no_x00, no_y00, z+3]
            # position = [x, y, z]

            # print(position)
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            # print(thelta)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
                breakpoint
            else:
                Userfunctions.set_joint_angle(self, thelta)
                self.the=thelta
                T01 = self.Robot.initial_parameters(self.the, 1)
                T02 = self.Robot.initial_parameters(self.the, 2)
                T03 = self.Robot.initial_parameters(self.the, 3)
                T0E = self.Robot.initial_parameters(self.the, 4)
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
                delta=round(delta,5)
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
                self.screen.axes.scatter(x[0], y[0], z[0], marker="D", color="r", s=100)
                self.screen.axes.scatter(x[1], y[1], z[1], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[2], y[2], z[2], marker="D", color="c", s=200)
                self.screen.axes.scatter(x[3], y[3], z[3], marker="D", color="c", s=200)
                self.screen.axes.scatter(no_x, no_y, z[3], marker="D", color="c", s=50)
                self.screen.axes.scatter(no_x, no_y, no_z, marker="D", color="c", s=50)

                self.ui.x_position.setText(str(np.round(no_x, 2)))
                self.ui.y_position.setText(str(np.round(no_y, 2)))
                self.ui.z_position.setText(str(np.round(no_z, 2)))
                # self.ui.x_position.setText(str(np.round(x[3], 2)))
                # self.ui.y_position.setText(str(np.round(y[3], 2)))
                # self.ui.z_position.setText(str(np.round(z[3], 2)))
                self.screen.draw()
        else:
            pass

        
        
    def set_joint_angle(self, thelta):
        thelta1 = str(int(np.rad2deg(thelta[0])))
        thelta2 = str(int(np.rad2deg(thelta[1])))
        thelta3 = str(int(np.rad2deg(thelta[2])))
        self.ui.the1_set.setText(thelta1)
        self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
        self.ui.the2_set.setText(thelta2)
        self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
        self.ui.the3_set.setText(thelta3)
        self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))

    def set_joint_angle_inver(self, thelta):
        thelta1 = str(int(np.rad2deg(thelta[0])))
        thelta2 = str(int(np.rad2deg(thelta[1])))
        thelta3 = str(int(np.rad2deg(thelta[2])))
        self.ui.the1_set.setText(thelta1)
        self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
        self.ui.the2_set.setText(thelta2)
        self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
        self.ui.the3_set.setText(thelta3)
        self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))

    def valuechange(self):
        value_the1 = str(self.ui.the1_adjust.value())
        value_the2 = str(self.ui.the2_adjust.value())
        value_the3 = str(self.ui.the3_adjust.value())
        self.ui.the1_set.setText(value_the1)
        self.ui.the2_set.setText(value_the2)
        self.ui.the3_set.setText(value_the3)
    # Tạo nên giá trị mới cho độ dài giữa các thanh 
    def link_adjustment(self):
        self.link = [
            float(self.length1.text()),
            float(self.length2.text()),
            float(self.length3.text()),
        ]
        self.ui.the1_adjust.setValue(int(0))
        self.ui.the2_adjust.setValue(int(90))
        self.ui.the3_adjust.setValue(int(-90))
        self.Robot.ChangeValue(self.link)
        Userfunctions.valuechange(self)
        Userfunctions.Geometry_display_change(self)

    
    # Hàm góc liên kết

    # Nút nhấn home khai báo vị trí đặt trước
    def Home_position(self):
        self.the1_set.setText("162")
        self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
        self.the2_set.setText("23")
        self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
        self.the3_set.setText("-75")
        self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))
        self.the = [
            np.deg2rad(float(self.uic.the1_set.text())),
            np.deg2rad(float(self.uic.the2_set.text())),
            np.deg2rad(float(self.uic.the3_set.text())),
        ]
        position = np.round_(self.Robot.Forward_kinematis(self.the), 3)
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        if self.ui.mode_check.isChecked():
            self.stop_simulation_mode()
            self.start_simulation_mode()
        else:
            Userfunctions.Geometry_display(self)

    def forward_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()) -step,2)
            y = round(float(self.ui.y_position.text()),2)
            z = round(float(self.ui.z_position.text()),2)
            position = [x, y, z]
            print(position)
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

    def backward_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()) + step,2)
            y = round(float(self.ui.y_position.text()),2)
            z = round(float(self.ui.z_position.text()),2)
            position = [x, y, z]
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

    def left_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()),2)
            y = round(float(self.ui.y_position.text()) - step,2)
            z = round(float(self.ui.z_position.text()),2)
            position = [x, y, z]
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

    def right_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()),2)
            y = round(float(self.ui.y_position.text()) + step,2)
            z = round(float(self.ui.z_position.text()),2)
            position = [x, y, z]
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

    def up_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()),2)
            y = round(float(self.ui.y_position.text()),2)
            z = round(float(self.ui.z_position.text()) + step,2)
            position = [x, y, z]
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

    def down_signal(self):
        self.ui.choose_F_I.setText("I")
        if self.ui.x_position.text() != 'Error' :
            step=round(float(self.ui.textEdit.text()),2)
            x = round(float(self.ui.x_position.text()),2)
            y = round(float(self.ui.y_position.text()),2)
            z = round(float(self.ui.z_position.text()) - step,2)
            position = [x, y, z]
            self.ui.x_position.setText(str(position[0]))
            self.ui.y_position.setText(str(position[1]))
            self.ui.z_position.setText(str(position[2]))
            sol= int(self.ui.solution.text())
            thelta = self.Robot.Inverse_kinematics(position, sol)
            if thelta =='error':
                self.ui.x_position.setText("Error")
                self.ui.y_position.setText("Error")
                self.ui.z_position.setText("Error")
            else:
                Userfunctions.set_joint_angle_inver(self, thelta)
                Userfunctions.Geometry_display_inver(self,thelta)

        # self.stop_simulation_mode()
        # self.start_simulation_mode()

