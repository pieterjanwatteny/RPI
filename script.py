#!/usr/bin/python
import sys
import I2C_LCD_driver
from time import*
import Adafruit_DHT

mylcd = I2C_LCD_driver.lcd()

mylcd = I2C_LCD_driver.lcd()
print("Plantz monitor script running")
mylcd.lcd.display_string('TEST',1);
while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))



