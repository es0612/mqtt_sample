import paho.mqtt.client as mqtt


def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("/test")


def on_disconnect(client, userdata, flag, rc):
  print("Disconnected with result code " + str(rc))


def on_message(client, userdata, msg):
  print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))


client = mqtt.Client()

client.on_connect = on_connect         
client.on_disconnect = on_disconnect   
client.on_message = on_message         

client.connect("broker.emqx.io")
client.loop_forever()