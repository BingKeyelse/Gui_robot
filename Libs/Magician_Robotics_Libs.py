# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:11:38 2021

@author: Leonard
"""

from os import error
import numpy as np
import math  as m
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import style

c = lambda x: np.cos(x)
s = lambda x: np.sin(x)
t = lambda x,y: m.atan2(x,y)

class Magician:
    def __init__(self,link_length):
        self.l = link_length

    def ChangeValue(self,new_length):
        self.l = new_length

    def DHmatrix(self,alp,a,d,the):
        '''
        the is called the joint variable
        d is the joint variable
        The geometry of a robotic mechanism is conveniently defined
        by attaching coordinate frames to each link.While these frames
        could be located arbitrarily, it is advantageous both for
        consistency and computational efficiency to
        adhere to a convention for locating the frameson the links.
        '''
        Mdh=np.matrix([[c(the)        , -s(the)       , 0       , a],
                       [s(the)*c(alp) , c(the)*c(alp) ,-s(alp)  ,-d*s(alp)],
                       [s(the)*s(alp) , c(the)*s(alp) , c(alp)  , d*c(alp)],
                       [0             ,      0        , 0       , 1]])
        return Mdh

    def initial_parameters(self,the,option = 1):
        '''
        DHMATRIX Summary of this function goes here
         i      alpha(i-1)          di           a(i-1)        Thelta(i)
       joint    Link twist     Link Offset    Link Leight   Joint variable
         1       0                 0                  0         the1;...       %frame1
         2       pi/2              L1                 0         the2;...       %frame2
         3       0                 L2                 0         the3;...       %frame3
        end      0                 L3                 0           0];          %End-point

         Joint frame with respect to the world coordinates.
        '''
        T01 = np.array([[c(the[0]), -s(the[0]), 0,          0],
                        [s(the[0]),  c(the[0]), 0,          0],
                        [0        ,          0, 1,          0],
                        [0        ,          0, 0,          1]])

        T12 = np.array([[c(the[1]), -s(the[1]),  0,  self.l[0]],
                        [0        ,          0,  -1,  0],
                        [s(the[1]),  c(the[1]),  0,  0],
                        [0        ,          0,  0,  1]])

        T23 = np.array([[c(the[2]), -s(the[2]),  0,  self.l[1]],
                        [s(the[2]),  c(the[2]),  0,        0],
                        [0        ,          0,  1,        0],
                        [0        ,          0,  0,        1]])

        T3E = np.array([[1,0, 0,  self.l[2]],
                        [0,1, 0,         0],
                        [0,0, 1,         0],
                        [0,0, 0,         1]])

        # Tranformation Matrix:
        T02 = np.dot(T01,T12)
        T03 = np.dot(T02,T23)
        T0E = np.dot(T03,T3E)
        if   option == 1:
            return T01
        elif option == 2:
            return T02
        elif option == 3:
            return T03
        elif option == 4:
            return T0E

    def Forward_kinematis(self,the):
        End_Effector_Frame = self.initial_parameters(the,4)
        x = End_Effector_Frame[0,3]
        y = End_Effector_Frame[1,3]
        z = End_Effector_Frame[2,3]
        position = np.array([x,y,z])
        return position

    def basic_01(self,a,b,d):
        anp = t(b,a)
        x1 = anp + t(m.sqrt(a**2+b**2-d**2),d)
        x2 = anp + t(-m.sqrt(a**2+b**2-d**2),d)
        the = [x1 , x2]
        return the

        

    def Inverse_kinematics(self,pos,solution=1):
        #scenario 1:
        #Tính theta1
       

        the11=t( pos[1], pos[0])
        the12=t(-pos[1],-pos[0])
        
        c3_am   = ((-m.sqrt(pos[0]**2+pos[1]**2)-self.l[0])**2+pos[2]**2-self.l[1]**2-self.l[2]**2)/(2*self.l[1]*self.l[2])
        c3_duong= (( m.sqrt(pos[0]**2+pos[1]**2)-self.l[0])**2+pos[2]**2-self.l[1]**2-self.l[2]**2)/(2*self.l[1]*self.l[2])
        if c3_duong  > 1 or c3_duong <-1:
            mode='error'
            return mode
        elif c3_am > 1 or c3_am <-1 :
            the3 = self.basic_01(1,0,c3_duong)
            #Có 2 nghiệm the3[0] và the3[1]
            k11=self.l[2]*c(the3[0])+self.l[1]
            k21=self.l[2]*s(the3[0])
            the21=self.basic_01(k21,k11,pos[2])

            k12=self.l[2]*c(the3[1])+self.l[1]
            k22=self.l[2]*s(the3[1])
            the22=self.basic_01(k22,k12,pos[2])
            if solution == 3:
                solution=1
            if solution == 4:
                solution=2
            if solution==1:
                Sol1 = np.array([the11   ,  the21[1]  ,   the3[0]])
                return Sol1
            elif solution==2:
                Sol2 = np.array([the11   ,  the22[1]  ,   the3[1]])
                return Sol2
        else :
            the3_duong=self.basic_01(1,0,c3_duong)
            the3_am=self.basic_01(1,0,c3_am)
            #i=1
            k11=self.l[2]*c(the3_duong[0])+self.l[1]
            k21=self.l[2]*s(the3_duong[0])
            the21=self.basic_01(k21,k11,pos[2])
            #i=2
            k12=self.l[2]*c(the3_duong[1])+self.l[1]
            k22=self.l[2]*s(the3_duong[1])
            the22=self.basic_01(k22,k12,pos[2])
            #i=3
            k13=self.l[2]*c(the3_am[0])+self.l[1]
            k23=self.l[2]*s(the3_am[0])
            the23=self.basic_01(k23,k13,pos[2])
            #i=4
            k14=self.l[2]*c(the3_am[1])+self.l[1]
            k24=self.l[2]*s(the3_am[1])
            the24=self.basic_01(k24,k14,pos[2])
            if solution==1:
                Sol1 = np.array([the11   ,  the21[1]  ,   the3_duong[0]])
                return Sol1
            elif solution==2:
                Sol2 = np.array([the11   ,  the22[1]  ,   the3_duong[1]])
                return Sol2
            elif solution==3:
                Sol3 = np.array([the12   ,  the23[0]  ,   the3_am[0]])
                return Sol3
            elif solution==4:
                Sol4 = np.array([the12   ,  the24[0]  ,   the3_am[1]])
                return Sol4
 

