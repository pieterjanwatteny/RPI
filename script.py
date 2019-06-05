#!/usr/bin/bash python
import sys
import Adafruit_DHT
import I2C_LCD_driver
import time
import requests

from time import sleep
import RPi.GPIO as GPIO

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
sleep(10)
mylcd.lcd_display_string("NOMNOM DATA", 1)
mylcd.lcd_display_string("PLS STAND BY...", 2)

def buttonPress(channel):
    print("Button pushed")
    setServoAngle(90)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,buttonPress, bouncetime=1500)

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)


def setServoAngle(angle):
    duty= angle/18+2
    GPIO.output(12,True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(12,False)
    pwm.ChangeDutyCycle(0)


def readPrint():
    while True:
		blink()
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        mylcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature,),1)
        mylcd.lcd_display_string('Humidity: {1:0.1f} %'.format(temperature,humidity), 2)
        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

        payload= {"Temp":temperature,"Humid":humidity}
        r = requests.post("https://ibiome.herokuapp.com/api/data",json=payload)
        print(r.text)
        print(payload)

        if temperature > 27:
            setServoAngle(180)
			sleep(0.2)
			setServoAngle(90)
			
def blink():
        while True: # Run forever
            GPIO.output(11, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(11, GPIO.LOW)
            sleep(0.1)


readPrint()




