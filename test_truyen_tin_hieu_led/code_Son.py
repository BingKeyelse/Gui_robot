# import serial
# import time
# import sys
# with serial.Serial('COM3', 115200, timeout=1) as ser:
#         if not ser.isOpen():
#             ser.open()    
#         print('com3 is open', ser.isOpen())
#         # time.sleep(0.5)
#         a=0;b=0;
#         while True:
#             theta = float(input('Value of Desired Angle: '))
#             t_on  = int(input('Timming LED ON (milisecond): '))
#             t_off = int(input('Timming LED OFF (milisecond): '))
#             # theta = 90.0
#             # ser.write("{0},{1},{2}".format(theta,t_on,t_off).encode())
#             data_send = str("{0},{1},{2}".format(theta,t_on,t_off).encode())
#             ser.write("{0},{1},{2}".format(theta,t_on,t_off).encode())
#             print(data_send)
            
#             b= abs(theta-a)
#             a=theta
#             count = 0
#             while ser.isOpen() and count<b+1:
#                 strdata = ser.readline().decode()
#                 ser.flushInput()
#                 sys.stdout.write('\r'+strdata)
#                 count+=1
txt = "hello,my name is Peter,I am 26 years old"

# x = txt.split(", ").strip()
x=txt.strip("\r\n").split(",")
print(x)
print(x[0])
print(x[1])
print(x[2])
