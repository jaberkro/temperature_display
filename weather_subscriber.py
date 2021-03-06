import paho.mqtt.client as mqtt
import serial

ser = serial.Serial('/dev/ttyACM0')

MQTT_SERVER = "<ip_address_of_your_mqtt_server>" # change this with your IP address
MQTT_PATHS = {"weather"}
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for path in MQTT_PATHS:
        client.subscribe(path)
        print("subscribed to topic: " + path)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode()))
    if msg.topic == "weather":
        ser.write(str(msg.payload.decode()).encode())
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
