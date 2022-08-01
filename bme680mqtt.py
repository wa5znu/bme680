# From https://github.com/robert-hh/BME680-Micropython/blob/master/bmetest.py
# and https://bhave.sh/micropython-mqtt/
# install robert-hh bme280 library first.
# bme280i gave different readings, unsure of which to use
# For Adafruit ESP32C3 QT thing, SCL=6, SDA=5

from machine import SoftI2C, Pin, unique_id
from ubinascii import hexlify
from umqtt.simple import MQTTClient
from utime import sleep

from bme680 import *
import mynet

class BME680MQTT(object):
    CLIENT_NAME = f"QTPY_{hexlify(unique_id()).decode()}"
    TOPIC = f"sensor/bme680/{CLIENT_NAME}"

    def __init__(self, broker_addr):
       SCL_PIN=6
       SDA_PIN=5
       self.broker_addr = broker_addr
       self.bme = BME680_I2C(SoftI2C(scl=Pin(SCL_PIN), sda=Pin(5)))
       self.connect()
       
    def connect(self):
        mynet.connect()        
        self.mqttc = MQTTClient(self.CLIENT_NAME, self.broker_addr, keepalive=60)
        self.mqttc.connect()

    def disconnect(self):
        try:
            self.mqttc.disconnect()
        except OSError:
            pass
        mynet.disconnect()

    def loop(self):
        temp = self.bme.temperature
        hum = self.bme.humidity
        press = self.bme.pressure
        gas = self.bme.gas
        MESSAGE = f"temp={temp:.2f};hum={hum:.2f};press={press:.3f};gas={gas}"
        print(f"{self.TOPIC} {MESSAGE}")
        try:
            self.mqttc.publish(self.TOPIC, MESSAGE)
            #mynet.disconnect() # inject fault
        except OSError as e:
            print(f"Exception {e} ERRNO={e.errno}")
            print("MQTT Publish failed; reconnecting")
            self.disconnect()
            sleep(10)
            self.connect()
        else:
            sleep(60)

def main(broker_addr):
    app = BME680MQTT(broker_addr)
    while True:
        app.loop()

if __name__ == "__main__":
    import secrets
    main(secrets.BROKER_ADDR)

    
