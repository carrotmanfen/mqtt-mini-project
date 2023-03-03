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
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("iot node1")
client.connect(mqttBroker)
client.on_connect = on_connect
client.publish("SENSOR_DATA/CONNECT","IP: 123:123:123:1")
print("Connecting to server")


# Read the Excel file and extract the sensor data
df = pd.read_excel('SampleInput.xlsx')

# publish data to broker for data that read in file
for i, row in df.iterrows():
    # publish data start (max 250byte)
    client.publish("SENSOR_DATA/START", "Node1")
    print("Just Starting Publishing")

    # publish data time (max 250byte)
    
    # you can use these code to generate current time if you want 

    # currentTime = time.time()
    # result = time.localtime(currentTime)
    # stringTime = str(result.tm_year)+"-"+str(result.tm_mon)+"-"+str(result.tm_mday)+" "+str(result.tm_hour)+":"+str(result.tm_min)+":"+str(result.tm_sec)
    
    row.Time = str(row.Time)
    while(len(row.Time)>250):
        buffer = row.Time[0:250]
        client.publish("SENSOR_DATA/TIME", buffer)
        print("Just published to Topic TIME",buffer)
        row.Time = row.Time[250:len(row.Time)]

    client.publish("SENSOR_DATA/TIME", row.Time)
    print("Just published to Topic TIME", row.Time)

    # publish data Humidity (max 250byte)
    row.Humidity = str(row.Humidity)
    while(len(row.Humidity)>250):
        buffer = row.Humidity[0:250]
        client.publish("SENSOR_DATA/HUMIDITY", buffer)
        print("Just published to Topic HUMIDITY",buffer)
        row.Humidity = row.Humidity[250:len(row.Humidity)]

    client.publish("SENSOR_DATA/HUMIDITY", row.Humidity)
    print("Just published to Topic HUMIDITY", row.Humidity)

    # publish data temperature (max 250byte)
    row.Temperature = str(row.Temperature)
    while(len(row.Temperature)>250):
        buffer = row.Temperature[0:250]
        client.publish("SENSOR_DATA/TEMPERATURE", buffer)
        print("Just published to Topic TEMPERATURE",buffer)
        row.Temperature = row.Temperature[250:len(row.Temperature)]

    client.publish("SENSOR_DATA/TEMPERATURE", row.Temperature)
    print("Just published to Topic TEMPERATURE", row.Temperature)

    # publish data thermalArray (max 250byte)
    while(len(row.ThermalArray)>250):
        buffer = row.ThermalArray[0:250]
        client.publish("SENSOR_DATA/THERMAL", buffer)
        print("Just published to Topic THERMAL",buffer)
        row.ThermalArray = row.ThermalArray[250:len(row.ThermalArray)]
    
    client.publish("SENSOR_DATA/THERMAL", row.ThermalArray)
    print("Just published to Topic THERMAL",row.ThermalArray)

    # publish data end (max 250byte)
    client.publish("SENSOR_DATA/END","Ending publish data")
    print("Just Ending Publishing")
    client.on_disconnect = on_disconnect
    time.sleep(180)

