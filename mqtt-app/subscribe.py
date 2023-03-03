import paho.mqtt.client as mqtt
import time
import pymysql

flag_connected = 0

data_time = None
data_node_id = None
data_humidity = None
data_temperature = None
data_thermal = None
first_send = True

def on_connect(client, userdata, flags, rc):
    global flag_connected
    flag_connected = flag_connected+1
    print("Connecting from", str(client)) 

def on_disconnect(client, userdata, rc):
    global flag_connected
    flag_connected = flag_connected-1
    print("Disconnecting from", str(client)) 

def on_message(client, userdata, message):
    global data_time 
    global data_node_id 
    global data_humidity 
    global data_temperature 
    global data_thermal
    global first_send
    data = str(message.payload.decode("utf-8"))
    if str(message.topic)=="START":
        first_send = True
        data_time = None
        data_node_id = data
        data_humidity = None
        data_temperature = None
        data_thermal = ""
    elif str(message.topic)=="TIME":
        data_time = data
    elif str(message.topic)=="HUMIDITY":
        data_humidity = data
    elif str(message.topic)=="TEMPERATURE":
        data_temperature = data
    elif str(message.topic)=="THERMAL":
        if(first_send):
            data_thermal = data
            first_send = False
        else:
            data_thermal = str(data_thermal) + str(data)
    elif str(message.topic)=="END":
        print(data_thermal)
        connection = pymysql.connect(host="localhost",user="root",password="",database="network2" )
        cursor = connection.cursor()
        insert = "INSERT INTO sensor_data(Time,NodeID,Humidity,Temperature,Thermal) VALUES('"+data_time+"','"+data_node_id+"','"+data_humidity+"','"+data_temperature+"','"+data_thermal+"');"
        cursor.execute(insert)
        connection.commit()
        connection.close()
        
    print("Received message: ",str(client), str(message.topic), str(message.payload.decode("utf-8")) )
    

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Database")
client.connect(mqttBroker)

while True:
    client.on_connect = on_connect
    client.loop_start()
    client.subscribe("START")
    client.subscribe("CONNECT")
    client.subscribe("TIME")
    client.subscribe("HUMIDITY")
    client.subscribe("TEMPERATURE")
    client.subscribe("THERMAL")
    client.subscribe("END")
    client.on_message = on_message
    time.sleep(30)
    client.disconnect()
    client.on_disconnect = on_disconnect
    time.sleep(1)
    client.loop_end()
