# https://github.com/robert-hh/BME680-Micropython/blob/master/bmetest.py
# install his bme280 or bme280i (not tried) library first.
# below are pins needed.

from bme680 import *
from machine import SoftI2C, Pin
import time
bme = BME680_I2C(SoftI2C(scl=Pin(6), sda=Pin(5)))

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)


