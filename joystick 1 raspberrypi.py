import Rpi.Gpio as Gpio
from time import sleep
import pygame

pygame.init()
pygame.joystick.init()
joystick=pygame.joystick.Joystick(0)

#setup the gpio pins
Gpio.setmode(Gpio.borad)
#Gpio.setmode(Gpio.BCM)
Gpio.setwarnings(False)

#declare  the pins off frist  motors
motorA1=2
motorA2=3
motorA3=4
#declare  the pins offsecond  motors
motorB1=5
motorB2=6
motorB3=7
#declare  the pins offthrid motors
motorC1=2
motorC2=3
motorC3=4
#declare  the pins off four  motors
motorD1=2
motorD2=3
motorD3=4

#declare  the pins off fifth  motors
motorE1=2
motorE2=3
motorE3=4

#declare  the pins off Sixthly  motors
motorF1=2
motorF2=3
motorF3=4

#declare  the pins off VII  motors
motorG1=2
motorG2=3
motorG3=4

#declare  the pins off Eighth  motors
motorZ1=2
motorZ2=3
motorZ3=4


#set the pins as output
Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)
Gpio.setup(motorA3,Gpio.OUT)

Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)


Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)

Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)

Gpio.setup(motorE1,Gpio.OUT)
Gpio.setup(motorE2,Gpio.OUT)
Gpio.setup(motorE3,Gpio.OUT)

Gpio.setup(motorF1,Gpio.OUT)
Gpio.setup(motorF2,Gpio.OUT)
Gpio.setup(motorF3,Gpio.OUT)

Gpio.setup(motorG1,Gpio.OUT)
Gpio.setup(motorG2,Gpio.OUT)
Gpio.setup(motorG3,Gpio.OUT)

Gpio.setup(motorZ1,Gpio.OUT)
Gpio.setup(motorZ2,Gpio.OUT)
Gpio.setup(motorZ3,Gpio.OUT)

#set the pwm pins
# We have set our PWM frequency to 150.
R1=Gpio.PWM(motorA3,150)
R2=Gpio.PWM(motorB3,150)
R3=Gpio.PWM(motorC3,150)
R4=Gpio.PWM(motorD3,150)
R5=Gpio.PWM(motorE3,150)
R6=Gpio.PWM(motorF3,150)
R7=Gpio.PWM(motorG3,150)
R8=Gpio.PWM(motorZ3,150)

#The main code
while(1):
   
   pygame.event.pump()
   Yvert=joystick.get_axis(1)
   Xhorz=joystick.get_axis(0)
   Yvert1=joystick.get_axis(2)
#HHorizontally mounted motors that move Motors counterclockwise forward
   if Yvert<0:
    print('Forward')
    y=abs(Yvert*100)
    print(y)
    Gpio.output(motorA1,Gpio.LOW)
    Gpio.output(motorA2,Gpio.HIGH)
    Gpio.output(motorA3,Gpio.HIGH)
    R1.start(y)                         # That's the maximum value 100 %.
   

    Gpio.output(motorB1,Gpio.LOW)
    Gpio.output(motorB2,Gpio.HIGH)
    Gpio.output(motorB3,Gpio.HIGH)
    R2.start(y)

    Gpio.output(motorC1,Gpio.LOW)
    Gpio.output(motorC2,Gpio.HIGH)
    Gpio.output(motorC3,Gpio.OUT)
    R3.start(y)

    Gpio.output(motorD1,Gpio.LOW)
    Gpio.output(motorD2,Gpio.HIGH)
    Gpio.output(motorD3,Gpio.HIGH)
    R4.start(.8*y)
#HHorizontally mounted motors that move Motors clockwise backward
   elif Yvert>0 :
     print('backWard')
     y=abs(Yvert*100)
     print(y)
     Gpio.output(motorA1,Gpio.HIGH)
     Gpio.output(motorA2,Gpio.LOW)
     Gpio.output(motorA3,Gpio.HIGH)
     R1.start(y)

     Gpio.output(motorB1,Gpio.HIGH)
     Gpio.output(motorB2,Gpio.LOW)
     Gpio.output(motorB3,Gpio.HIGH)
     R2.start(y)

     Gpio.output(motorC1,Gpio.HIGH)
     Gpio.output(motorC2,Gpio.LOW)
     Gpio.output(motorC3,Gpio.HIGH)
     R3.start(y)

     Gpio.setup(motorD1,Gpio.HIGH)
     Gpio.setup(motorD2,Gpio.LOW)
     Gpio.setup(motorD3,Gpio.HIGH)
     R4.start(y)

#vertically mounted motors that move motors counterclockwise forward
   elif Yvert1<0:
     print('up')
     y=abs(Yvert1*100)
     print(y)
     Gpio.output(motorE1,Gpio.LOW)
     Gpio.output(motorE2,Gpio.HIGH)
     Gpio.output(motorE3,Gpio.HIGH)
     R5.start(y)

     Gpio.output(motorF1,Gpio.LOW)
     Gpio.output(motorF2,Gpio.HIGH)
     Gpio.output(motorF3,Gpio.HIGH)
     R6.start(y)

     Gpio.output(motorG1,Gpio.LOW)
     Gpio.output(motorG2,Gpio.HIGJ)
     Gpio.output(motorG3,Gpio.HIGH)
     R7.start(y)

     Gpio.output(motorZ1,Gpio.LOW)
     Gpio.output(motorZ2,Gpio.LOW)
     Gpio.output(motorZ3,Gpio.HIGH)
     R8.start(y)

#vertically mounted motors that move motors clockwise Down
   elif Yvert1>0 :
     print('Down')
     y=abs(Yvert1*100)
     print(y)
     Gpio.output(motorE1,Gpio.HIGH)
     Gpio.output(motorE2,Gpio.LOW)
     Gpio.output(motorE3,Gpio.HIGH)
     R5.start(y)

     Gpio.output(motorF1,Gpio.HIGH)
     Gpio.output(motorF2,Gpio.LOW)
     Gpio.output(motorF3,Gpio.HIGH)
     R6.start(y)
     Gpio.output(motorG1,Gpio.HIGH)
     Gpio.output(motorG2,Gpio.LOW)
     Gpio.output(motorG3,Gpio.HIGH)
     R7.start(y)

     Gpio.output(motorZ1,Gpio.HIGH)
     Gpio.output(motorZ2,Gpio.LOW)
     Gpio.output(motorZ3,Gpio.HIGH)
     R8.start(y)
#Motors installed horizontally and in a right direction
   elif Xhorz>0 :
     print('right')
     y=abs(Yvert*100)
     print(y)
    #Motors installed on the left side in an anti-clockwise direction
     Gpio.output(motorA1,Gpio.LOW)
     Gpio.output(motorA2,Gpio.HIGH)
     Gpio.output(motorA3,Gpio.HIGH)
     R1.start(y)
     
     Gpio.output(motorB1,Gpio.LOW)
     Gpio.output(motorB2,Gpio.HIGH)
     Gpio.output(motorB3,Gpio.HIGH)
     R2.start(y)
    #Motors installed on the right side that  an clockwise direction
     Gpio.output(motorC1,Gpio.HIGH)
     Gpio.output(motorC2,Gpio.low)
     Gpio.output(motorC3,Gpio.HIGH)
     R3.start(y)

     Gpio.output(motorD1,Gpio.HIGH)
     Gpio.output(motorD2,Gpio.low)
     Gpio.output(motorD3,Gpio.HIGH)
     R4.start(y)
#Motors installed horizontally and in a Lfet direction
   elif Xhorz<0 :
     print('LEFT')
     y=abs(Yvert*100)
     print(y)
    #Motors installed on the left side in an clockwise direction
    
     Gpio.output(motorA1,Gpio.HIGH)
     Gpio.output(motorA2,Gpio.LOW)
     Gpio.output(motorA3,Gpio.HIGH)
     R1.start(y)                         
    
     Gpio.output(motorB1,Gpio.HIGH)
     Gpio.output(motorB2,Gpio.LOW)
     Gpio.output(motorB3,Gpio.HIGH)
     R2.start(y)
    #Motors installed on the right side in an anti-clockwise direction
    
     Gpio.output(motorC1,Gpio.LOW)
     Gpio.output(motorC2,Gpio.HIGH)
     Gpio.output(motorC3,Gpio.HIGH)
     R3.start(y)

     Gpio.output(motorD1,Gpio.LOW)
     Gpio.output(motorD2,Gpio.HIGH)
     Gpio.output(motorD3,Gpio.HIGH)
     R4.start(y)
    
#Stop motors
   else:
     print('stop')
     Gpio.output(motorA1,Gpio.LOW)
     Gpio.output(motorA2,Gpio.LOW)
     Gpio.output(motorA3,Gpio.LOW)
     Gpio.output(motorB1,Gpio.LOW)
     Gpio.output(motorB2,Gpio.LOW)
     Gpio.output(motorB3,Gpio.LOW)
     Gpio.output(motorC1,Gpio.LOW)
     Gpio.output(motorC2,Gpio.LOW)
     Gpio.output(motorC3,Gpio.LOW)
     Gpio.output(motorD1,Gpio.LOW)
     Gpio.output(motorD2,Gpio.LOW)
     Gpio.output(motorD3,Gpio.LOW)
     Gpio.output(motorE1,Gpio.LOW)
     Gpio.output(motorE2,Gpio.LOW)
     Gpio.output(motorE3,Gpio.LOW)
     Gpio.output(motorF1,Gpio.LOW)
     Gpio.output(motorF2,Gpio.LOW)
     Gpio.output(motorF3,Gpio.LOW)
     Gpio.output(motorG1,Gpio.LOW)
     Gpio.output(motorG2,Gpio.LOW)
     Gpio.outputp(motorG3,Gpio.LOW)
     Gpio.output(motorZ1,Gpio.LOW)
     Gpio.output(motorZ2,Gpio.LOW)
     Gpio.output(motorZ3,Gpio.LOW)
   sleep(0.3)
Gpio.cleanup()
