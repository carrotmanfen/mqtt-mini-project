import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import pandas as pd

# callback function on connect when connect/disconnect then print
def on_connect(client, userdata, flags, rc):
    print("Connecting from", str(client)) 

def on_disconnect(client, userdata, rc):
    print("Disconnecting from", str(client)) 

# connect to mqtt broker
node_id = "Node2;"
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("iot node2")
client.connect(mqttBroker)
client.on_connect = on_connect
client.publish("SENSOR_DATA/CONNECT",node_id+"IP: 123:123:123:2")
print("Connecting to server")


# Read the Excel file and extract the sensor data
df = pd.read_excel('SampleInput.xlsx')

# publish data to broker for data that read in file
for i, row in df.iterrows():
    # publish data start (max 250byte)
    client.publish("SENSOR_DATA/START", node_id)
    print("Just Starting Publishing")

    # publish data time (max 250byte)
    
    # you can use these code to generate current time if you want 

    # currentTime = time.time()
    # result = time.localtime(currentTime)
    # stringTime = str(result.tm_year)+"-"+str(result.tm_mon)+"-"+str(result.tm_mday)+" "+str(result.tm_hour)+":"+str(result.tm_min)+":"+str(result.tm_sec)
    
    row.Time = str(row.Time)
    while(len(row.Time)>250-len(node_id)):
        buffer = node_id+row.Time[0:250-len(node_id)]
        client.publish("SENSOR_DATA/TIME", buffer)
        print("Just published to Topic TIME",buffer)
        row.Time = row.Time[250-len(node_id):len(row.Time)]

    client.publish("SENSOR_DATA/TIME", node_id+row.Time)
    print("Just published to Topic TIME", node_id+row.Time)

    # publish data Humidity (max 250byte)
    row.Humidity = str(row.Humidity)
    while(len(row.Humidity)>250-len(node_id)):
        buffer = node_id+row.Humidity[0:250]
        client.publish("SENSOR_DATA/HUMIDITY", buffer)
        print("Just published to Topic HUMIDITY",buffer)
        row.Humidity = row.Humidity[250-len(node_id):len(row.Humidity)]

    client.publish("SENSOR_DATA/HUMIDITY", node_id+row.Humidity)
    print("Just published to Topic HUMIDITY", node_id+row.Humidity)

    # publish data temperature (max 250byte)
    row.Temperature = str(row.Temperature)
    while(len(row.Temperature)>250-len(node_id)):
        buffer = node_id+row.Temperature[0:250]
        client.publish("SENSOR_DATA/TEMPERATURE", buffer)
        print("Just published to Topic TEMPERATURE",buffer)
        row.Temperature = row.Temperature[250-len(node_id):len(row.Temperature)]

    client.publish("SENSOR_DATA/TEMPERATURE", node_id+row.Temperature)
    print("Just published to Topic TEMPERATURE", node_id+row.Temperature)

    # publish data thermalArray (max 250byte)
    while(len(row.ThermalArray)>250-len(node_id)):
        buffer = node_id+row.ThermalArray[0:250]
        client.publish("SENSOR_DATA/THERMAL", buffer)
        print("Just published to Topic THERMAL",buffer)
        row.ThermalArray = row.ThermalArray[250-len(node_id):len(row.ThermalArray)]
    
    client.publish("SENSOR_DATA/THERMAL", node_id+row.ThermalArray)
    print("Just published to Topic THERMAL",node_id+row.ThermalArray)

    # publish data end (max 250byte)
    client.publish("SENSOR_DATA/END",node_id+"Ending publish data")
    print(node_id+"Just Ending Publishing")
    client.on_disconnect = on_disconnect
    time.sleep(180)
    if(i == 15):
        client.disconnect()
    else:
        time.sleep(180)
        client.connect(mqttBroker)

