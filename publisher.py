import paho.mqtt.client as mqtt
import time
import datetime


client = mqtt.Client()
client.connect("broker.emqx.io")


while True:
    time.sleep(2)
    current_time = str(datetime.datetime.now())
    print(current_time)

    message = current_time + " publish from pyton code."
    client.publish("/test", payload=message, qos=1)
    