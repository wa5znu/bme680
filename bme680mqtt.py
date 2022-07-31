# From https://github.com/robert-hh/BME680-Micropython/blob/master/bmetest.py
# and https://bhave.sh/micropython-mqtt/
# install robert-hh bme280 library first.
# bme280i gave different readings, unsure of which to use
# For Adafruit ESP32C3 QT thing, SCL=6, SDA=5

from bme680 import *
from machine import SoftI2C, Pin, unique_id
from ubinascii import hexlify
import time


bme = BME680_I2C(SoftI2C(scl=Pin(6), sda=Pin(5)))

#for _ in range(86400):
#    print(bme.temperature, bme.humidity, bme.pressure * 0.029530) # bme.gas
#    time.sleep(1)

from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep

CLIENT_NAME = f"QTPY_{hexlify(unique_id()).decode()}"
BROKER_ADDR = 'mqtt.klotz.me'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

TOPIC = f"sensor/bme680/{CLIENT_NAME}"

while True:
    temp = bme.temperature
    hum = bme.humidity
    press = bme.pressure
    gas = bme.gas
    MESSAGE = f"temp={temp:.2f},hum={hum:0.},press={press:.3f},gas={gas}"
    print(f"{TOPIC} {MESSAGE}")
    mqttc.publish(TOPIC, MESSAGE)
    sleep(60)
