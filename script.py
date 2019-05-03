#!/usr/bin/python
import sys
import Adafruit_DHT
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

mylcd.lcd_display_string("GATHERING DATA", 1)
mylcd.lcd_display_string("PLEASE STAND BY..", 2)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
def buttonPres():
    while True:
        if GPIO.input(10)==GPIO.HIGH:
            mylcd.lcd_display_string("BUTTON PRESS", 2)
            mylcd.lcd_clear()

def readPrint():
     while True:
         humidity, temperature = Adafruit_DHT.read_retry(11, 4)
         mylcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature,),1)
         mylcd.lcd_display_string('Humidity: {1:0.1f} %'.format(temperature,humidity), 2)

         print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))


readPrint()
buttonPres()
