# bme680
MQTT bus producer for Adafruit QtPy ESP32-C3 and Adafruit BME680 sensor 

Adafruit driver for their BME680 board supports CircuitPython but CircuitPython isn't on this ESP32C3 board of theirs, just like it isn't on the one from 01space. The BME680 interface uses a few Adafruit libraries and, unsurprisingly, it didn't install or run cleanly in Micropython.  Just use https://github.com/robert-hh/BME680-Micropython port.

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
sensor/bme680/QTPY_000000000000 temp=26.77;hum=52.9152;press=1015.945;gas=18982
```

# Drivers
- https://github.com/robert-hh/BME680-Micropython
- import net.py
- upip.install("umqtt.simple", "lib")

# References
- https://microcontrollerslab.com/micropython-bme680-esp32-esp8266-gas-pressure-temperature-humidity/
- https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board
- https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main
- https://github.com/adafruit/Adafruit-QT-Py-ESP32-C3-PCB/blob/main/Adafruit%20QT%20Py%20ESP32-C3%20Pinout.pdf
- https://bhave.sh/micropython-mqtt/
- https://micropython.org/pi/umqtt.simple/umqtt.simple-1.3.4.tar.gz
- https://forum.micropython.org/viewtopic.php?t=12109&p=65771#p65868 "OSError: \[Errno 113\] ECONNABORTED"
