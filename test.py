# https://microcontrollerslab.com/micropython-bme680-esp32-esp8266-gas-pressure-temperature-humidity/

from machine import Pin, SoftI2C
from time import sleep

# ESP32 Pins for SoftI2C 
i2c = SoftI2C(scl=Pin(6), sda=Pin(5))

bme = Adafruit_BME680_I2C(i2c=i2c)

while True:
  try:
    temperature = str(round(bme.temperature, 2)) + ' C'
    #temp = (bme.temperature) * (9/5) + 32
    #temp = str(round(temp, 2)) + 'F'
    
    humidity = str(round(bme.humidity, 2)) + ' %'
    
    pressure = str(round(bme.pressure, 2)) + ' hPa'
    
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'

    print('Temperature:', temperature)
    print('Humidity:', humidity)
    print('Pressure:', pressure)
    print('Gas:', gas)
    print('-------')
  except OSError as e:
    print('Failed to read bme680 sensor.')
 
  sleep(5)