#!/usr/bin/python
import sys
import Adafruit_DHT
import I2C_LCD_driver
import time
from time import sleep
import RPi.GPIO as GPIO

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

mylcd.lcd_display_string("NOMNOM DATA", 1)
mylcd.lcd_display_string("PLS STAND BY...", 2)


def buttonPress(channel):
    print("Button pushed")
    print("Initiate Blinky")
    blink()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(10,GPIO.RISING,buttonPress, bouncetime=200)


def readPrint():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        mylcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature,),1)
        mylcd.lcd_display_string('Humidity: {1:0.1f} %'.format(temperature,humidity), 2)
        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))


def blink():
        while True: # Run forever
            GPIO.output(11, GPIO.HIGH) # Turn on
            sleep(0.5)                  # Sleep for 1 second
            GPIO.output(11, GPIO.LOW)  # Turn off
            sleep(0.5)                  # Sleep for 1 second


readPrint()



