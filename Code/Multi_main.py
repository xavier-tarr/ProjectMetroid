from SSC32 import SSC32
import multiprocessing
import sys
import numpy as np
import time
import tty, termios

hex1 = SSC32(9600,0)
All_Shoulders = [0,3,6,9,12,15]
All_Elbows =    [1,4,7,10,13,16]
All_Wrists =    [2,5,8,11,14,17]

Tri_1_El = [1,7,13]
Tri_2_El = [4,10,16]
Tri_1_Sh = [0,6,12]
Tri_2_Sh = [3,9,15]
Tri_1_Wr = [2,8,14]
Tri_2_Wr = [5,11,17]


def tripod_walk(Time):
    while True:
        tim = str(Time.value*1000/9)
        hex1.write([1400,1400,1600],Tri_1_Sh,tim)
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([2200,2200,2200],Tri_1_El,tim)
        hex1.write([2500,2500,2500],Tri_1_Wr,tim)
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([1500,1500,1500],Tri_2_El,tim)
	hex1.write([2000,2000,2000],Tri_2_Wr,tim) #Bring Wrists Down
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([1600,1600,1400],Tri_1_Sh,tim)
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([1400,1600,1600],Tri_2_Sh,tim)
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([2200,2200,2200],Tri_2_El,tim)
	hex1.write([2500,2500,2500],Tri_2_Wr,tim) #Bring Wrists Up
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([1500,1500,1500],Tri_1_El,tim)
	hex1.write([2000,2000,2000],Tri_1_Wr,tim) #Bring Wrists Down
        time.sleep(float(tim)/1000)

	tim = str(Time.value*1000/9)
        hex1.write([1600,1400,1400],Tri_2_Sh,tim)
        time.sleep(float(tim)/1000)

def getchar():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

if __name__ == "__main__":
    
    Time = multiprocessing.Value('d',1.0)
    
    p_walk = multiprocessing.Process(target=tripod_walk, args=(Time,))
    p_walk.start()
    
    while True:
        char = getchar()
        if char == 'w':
            Time.value *= 1.1
	    print(str(Time.value))
        elif char == 's':
            Time.value *= .9
	    print(str(Time.value))
        elif char == 'e':
            print("BYE!!")
            break
    hex1.close_com
