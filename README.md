# bme680
BME680 environment multi-sensor MQTT bus producer for ESP32C3

Adafruit driver for their BME680 board supports CircuitPython but CircuitPython isn't on this ESP32C3 board of theirs, just like it isn't on the one from 01space. The BME680 interface uses a few Adafruit libraries and, unsurprisingly, it didn't install or run cleanly in Micropython.  So now trying the @robert-hh library.

# Hardware
- Adafruit BME680 - STEMMA QT Temperature, Humidity, Pressure and Gas Sensor https://www.adafruit.com/product/3660
- Adafruit QT Py ESP32-C3 WiFi Dev Board with STEMMA QT https://www.adafruit.com/product/5405
- STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm https://www.adafruit.com/product/4399

# Drivers
https://github.com/robert-hh/BME680-Micropython

# References
- https://microcontrollerslab.com/micropython-bme680-esp32-esp8266-gas-pressure-temperature-humidity/
- https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board
- https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main
- https://github.com/adafruit/Adafruit-QT-Py-ESP32-C3-PCB/blob/main/Adafruit%20QT%20Py%20ESP32-C3%20Pinout.pdf
