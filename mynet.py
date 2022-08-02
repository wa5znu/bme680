# https://forum.micropython.org/viewtopic.php?t=12109&p=65771#p65868

import network
from umqtt.simple import MQTTClient
import time

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def isconnected():
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.isconnected()

def connect():
    from secrets import WIFI_NAME, WIFI_PASS
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_NAME, WIFI_PASS) 
        while not sta_if.isconnected():
            print('wifi connecting...')
            time.sleep(1)
    print('network config:', sta_if.ifconfig())
    return True

def disconnect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.disconnect()

def main(server="test.mosquitto.org"):
    if connect():
        print('WiFi connected...')
        time.sleep(1)
        c = MQTTClient("umqtt_client", server, keepalive=60)
        c.connect()
        if False:
            c.publish(b"asdf/asdf/123", b"hello_esp_S2")
        c.disconnect()


if __name__ == "__main__":
    main()
