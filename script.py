#!/usr/bin/python
import sys
import Adafruit_DHT
import I2C_LCD_driver
import time
mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()

mylcd.lcd_display_string("GATHER DATA", 1)

def read_print():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        mylcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature,),1)
        mylcd.lcd_display_string('Humidity: {1:0.1f} %'.format(temperature,humidity), 2)

        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))


read_print()
