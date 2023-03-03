import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import pandas as pd

def on_connect(client, userdata, flags, rc):
    global flag_connected
    flag_connected = flag_connected+1
    print("Connecting from", str(client)) 

def on_disconnect(client, userdata, rc):
    global flag_connected
    flag_connected = flag_connected-1
    print("Disconnecting from", str(client)) 

 
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Iot node1")
client.connect(mqttBroker)
client.on_connect = on_connect
print("Connecting to server")


# Read the Excel file and extract the sensor data
df = pd.read_excel('SampleInput.xlsx')

for i, row in df.iterrows():
    currentTime = time.time()
    result = time.localtime(currentTime)
    stringTime = str(result.tm_year)+"-"+str(result.tm_mon)+"-"+str(result.tm_mday)+" "+str(result.tm_hour)+":"+str(result.tm_min)+":"+str(result.tm_sec)
    client.publish("START", "Node1")
    print("Just Starting Publishing")
    client.publish("TIME", stringTime)
    print("Just published to Topic TIME",stringTime)
    client.publish("HUMIDITY", row.Humidity)
    print("Just published to Topic HUMIDITY", row.Humidity)
    client.publish("TEMPERATURE", row.Temperature)
    print("Just published to Topic TEMPERATURE", row.Temperature)
    while(len(row.ThermalArray)>250):
        buffer = row.ThermalArray[0:250]
        client.publish("THERMAL", buffer)
        print("Just published to Topic THERMAL",buffer)
        row.ThermalArray = row.ThermalArray[250:len(row.ThermalArray)]
    
    client.publish("THERMAL", row.ThermalArray)
    print("Just published to Topic THERMAL",row.ThermalArray)
    client.publish("END","Ending publish data")
    print("Just Ending Publishing")
    if i==15:
        client.disconnect()
        client.on_disconnect = on_disconnect
    time.sleep(180)

