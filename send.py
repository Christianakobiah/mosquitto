import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  
        Connected = True  

    else:
        print("Connection failed")
        
        Connected = False

client = mqtt.Client()
client.on_connect = on_connect
client.connect("10.10.3.221", 4000, 60)
client.loop_start()

try:
    while True:
        message = input('Your message: ')
        client.publish("Ucc/Christiana", message)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()