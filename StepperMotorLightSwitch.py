#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
myStepper.setSpeed(50)  		# RPM

while True:
	
	command = input("Hit 1 for lights on or 2 for off and press enter to turn motor.")	
	
	while(command):
		#command = input("Hit 1 or 2 and press enter to turn motor.")
		
		#myStepper.step(150, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
	
	
		if (command==1):
			#1 is lights ON
			myStepper.step(175, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
			myStepper.step(175, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
			turnOffMotors()
			command=False
		
		
		if (command==2):
			#2 is lights OFF
			myStepper.step(175, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.INTERLEAVE)
			myStepper.step(175, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
			turnOffMotors()
			command=False
