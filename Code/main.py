from SSC32 import SSC32
import sys
import numpy as np
import time

print("Main has started")
hex1 = SSC32(9600,0)
hex2 = SSC32(9600,1)
All_Shoulders = [0,3,6,9,12,15]
All_Elbows =    [1,4,7,10,13,16]
All_Wrists =    [2,5,8,11,14,17]

Tri_1_El = [1,7,13]
Tri_2_El = [4,10,16]
Tri_1_Sh = [0,6,12]
Tri_2_Sh = [3,9,15]
Tri_1_Wr = [2,8,14]
Tri_2_Wr = [5,11,17]

hex1.write([2400,2400,2400,2400,2400,2400],All_Wrists,"3")
hex1.write([2300,2300,2300,2300,2300,2300],All_Elbows,"3")
hex1.write([1500,1500,1500,1500,1500,1500],All_Shoulders,"3")
hex2.write([2000,2000,2000,2000,2000,2000],All_Wrists,"3")
hex2.write([2500,2500,2500,2500,2500,2500],All_Elbows,"3")
hex2.write([1500,1500,1500,1500,1500,1500],All_Shoulders,"3")
time.sleep(1)
while 1:
    print("Enter speed of 1 double step:")
    TIME = float(raw_input())
    Time = str(int(TIME*1000/9))
    print(Time)
    hex1.write([1500,1500,1500],Tri_1_El,Time)
    hex1.write([1500,1500,1500],Tri_1_Wr,Time) #Bring Wrists down
    time.sleep(float(Time)/1000)
    for i in range(0,4):
        hex1.write([1450,1450,1550],Tri_1_Sh,Time)
        time.sleep(float(Time)/1000)

        hex1.write([2200,2200,2200],Tri_1_El,Time)
	hex1.write([2200,2200,2200],Tri_1_Wr,Time) #Bring Wrists Up
	
        time.sleep(float(Time)/1000)
        
	hex1.write([1500,1500,1500],Tri_2_El,Time)
	hex1.write([1500,1500,1500],Tri_2_Wr,Time) #Bring Wrists Down
	time.sleep(float(Time)/1000)
        
	hex1.write([1550,1550,1450],Tri_1_Sh,Time)
	time.sleep(float(Time)/1000)
        
	hex1.write([1450,1550,1550],Tri_2_Sh,Time)
	time.sleep(float(Time)/1000)
        
	hex1.write([2200,2200,2200],Tri_2_El,Time)
	hex1.write([2200,2200,2200],Tri_2_Wr,Time) #Bring Wrists Up
	time.sleep(float(Time)/1000)
        
	hex1.write([1500,1500,1500],Tri_1_El,Time)
	hex1.write([1500,1500,1500],Tri_1_Wr,Time) #Bring Wrists Down
	time.sleep(float(Time)/1000)
        
	hex1.write([1550,1450,1450],Tri_2_Sh,Time)
	time.sleep(float(Time)/1000)
        
    hex1.write([1500,1500,1500],Tri_1_Sh,Time)
    time.sleep(float(Time)/1000)
    hex1.write([2200,2200,2200],Tri_1_El,Time)
    hex1.write([2100,2100,2200],Tri_1_Wr,Time)
    time.sleep(float(Time)/1000)
    hex1.write([1500,1500,1500],Tri_2_El,Time)
    hex1.write([2000,2000,2000],Tri_2_Wr,Time)
    time.sleep(float(Time)/1000)
    hex1.write([1500,1500,1500],Tri_2_Sh,Time)
    time.sleep(float(Time)/1000)
    hex1.write([2200,2200,2200],Tri_2_El,Time)
    hex1.write([2100,2100,2100],Tri_2_Wr,Time)
    time.sleep(float(Time)/1000)

time.sleep(1)
hex1.print_servos()
hex1.write_ALL(1500)
hex1.close_com
hex2.print_servos()
hex2.write_ALL(1500)
hex2.close_com
print("Ended all communication between SSC and raspi!")
