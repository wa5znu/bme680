# bme680
BME680 environment multi-sensor MQTT bus producer for ESP32C3

Adafruit driver for their BME680 board supports CircuitPython but CircuitPython isn't on this ESP32C3 board of theirs, just like it isn't on the one from 01space. The BME680 interface uses a few Adafruit libraries and, unsurprisingly, it didn't install or run cleanly in Micropython.  So now trying the @robert-hh library.

Just use https://github.com/robert-hh/BME680-Micropython - it works.

# Hardware
- Adafruit BME680 - STEMMA QT Temperature, Humidity, Pressure and Gas Sensor https://www.adafruit.com/product/3660
- Adafruit QT Py ESP32-C3 WiFi Dev Board with STEMMA QT https://www.adafruit.com/product/5405
- STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm https://www.adafruit.com/product/4399

# MQTT

- Existing traffic
```
sensor/dust/Dust_Wifi_00000000 pm01=1;pm2_5=2;pm10=2;aqi=8;pm2_5raw=2
sensor/bme280/kuzu_00000000 temp=24.6;hum=65;press=1015
```

- Proposed
```
temp=27.39;hum=52;press=1014.321;gas=8859
``` 

- Achieved
```
sensor/bme680/QTPY_000000000000 temp=26.61,hum=51.7866,press=1014.259,gas=6233
```

# Drivers
https://github.com/robert-hh/BME680-Micropython
- upip.install("umqtt.simple", "lib")

# References
- https://microcontrollerslab.com/micropython-bme680-esp32-esp8266-gas-pressure-temperature-humidity/
- https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board
- https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main
- https://github.com/adafruit/Adafruit-QT-Py-ESP32-C3-PCB/blob/main/Adafruit%20QT%20Py%20ESP32-C3%20Pinout.pdf
- https://bhave.sh/micropython-mqtt/
- https://micropython.org/pi/umqtt.simple/umqtt.simple-1.3.4.tar.gz

