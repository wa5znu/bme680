import network

import secrets

sta_if = network.WLAN(network.STA_IF)

# Now, you can check to see if they are active:
if not sta_if.active():
    sta_if.active(True)

#If you're not sure what your Wi-Fi network is, you can scan to remind yourself.
# sta_if.scan()

sta_if.connect(WIFI_NAME, WIFI_PASS)

sta_if.isconnected()
#True
