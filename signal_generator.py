import paho.mqtt.publish as publish
import time
import random

speed = 30
while speed != 0:
    distance = random.randrange(100)
    speed_chanage = random.uniform(-1.5, 1.6)
    print(f"Geschwindigkeitsveränderung: {speed_chanage}")
    print(f"Distanz nach vorne: {distance}")
    if distance == 0:
        speed = 0
    else:
        speed += speed_chanage
    print(f"Neue geschwindigkeit: {speed}")
    publish.single("auto1/geschwindigkeit", speed, hostname="127.0.0.1")
    publish.single("auto1/entfernung_vorne", speed, hostname="127.0.0.1")
    time.sleep(0.5)