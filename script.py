#!/usr/bin/python
import sys
import Adafruit_DHT
import I2C_LCD_driver
from time import*
mylcd = I2C_LCD_driver.lcd()

print("Plantz monitor script running")

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    mylcd.lcd.display_string('Temp: {0:0.1f} C'.format(temperature))


