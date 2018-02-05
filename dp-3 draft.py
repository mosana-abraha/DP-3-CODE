'''
DP-3 CODE DRAFT


'''

import time
import math
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

listValues=[]
#I need to append the values that the sensor is getting into "listValues)

def checkAverage(listValues):
    total = 0
    for value in listValues:
        total += value
    average = total/len(listValues)
    return(average)

def ActivateBuzzer(#arguement?):
    if checkAverage()<#ourtestednumber:
##       activate Buzzer pins on pi
    else:
##        buzzer pins should be off

   return()

def DeActivateBuzzer(variable):
    
    
    
        

