import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("I AM THE ONE", 1)
mylcd.lcd_display_string("DONT WEIGH A TON", 2)
