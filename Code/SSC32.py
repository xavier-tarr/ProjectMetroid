#!/user/bin/python
import serial
import sys
import numpy as np

class SSC32:
    
    def __init__(self):
        self.serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0)
        self.cur_servo_vals = np.zeros(18)
        
    def __init__(self, BAUDRATE):
        self.serial = serial.Serial('/dev/ttyUSB0', BAUDRATE, timeout=1.0)
        self.cur_servo_vals = np.zeros(18)

    def __init__(self,BAUDRATE,VAL):
	if(VAL==0): 
		self.serial = serial.Serial('/dev/ttyUSB0',BAUDRATE,timeout=1.0)
		self.cur_servo_vals =np.zeros(18)
	else:
		self.serial=serial.Serial('/dev/ttyUSB1',BAUDRATE,timeout=1.0)
		self.cur_servo_vals=np.zeros(18)

    def write(self,FRAME,JOINTS,TIME):
        if len(FRAME) != len(JOINTS):
            raise ValueError('Size of Frame and joints does not match')
        else:
            string = ""
            for i in range(0, len(JOINTS)):
                string = string + '#'+str(JOINTS[i])+' P'+str(FRAME[i])+'T'+TIME+' \r'
                self.cur_servo_vals[JOINTS[i]] = FRAME[i]
            self.serial.write(string)

    def write_Frame(self,FRAME):
        string = ""
        for i in range(0, 18):
            string = string + '#'+str(i)+' P'+str(FRAME[i])+'T10 \r'
            self.cur_servo_vals[i] = FRAME[i]
        self.serial.write(string)
        
    def write_ALL(self,position):
        string = ""
        for i in range(0, 18):
            string = string + '#'+str(i)+' P'+str(position)+'T10 \r'
            self.cur_servo_vals[i] = position
        self.serial.write(string)

    def print_servos(self):
        for i in range(0, 18):
            print("Sevo " + str(i) + ": " + str(self.cur_servo_vals[i]))
        print


    def center(self):
	string = ""
	for i in range(0,18):
		string = string +'#' + str(i) + 'P' +str(1500) + 'T3\r'
		self.cur_servo_vals[i] = 1500
	self.serial.write(string)

	        
    def close_com(self):
        self.serial.close()

    def open_com(self):
        self.serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0)

