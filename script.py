#!/usr/bin/python
import sys
import Adafruit_DHT
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("F*CK THIS WORLD", 1)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    mylcd.lcd_display_string('Temp: {0:0.1f} C'.format(temperature),1)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))



