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

# callback function on connect when connect/disconnect then print
def on_connect(client, userdata, flags, rc):
    global flag_connected
    flag_connected = flag_connected+1
    print("Connecting from", str(client)) 

def on_disconnect(client, userdata, rc):
    global flag_connected
    flag_connected = flag_connected-1
    print("Disconnecting from", str(client)) 

# callback function on message do something when got the message
def on_message(client, userdata, message):
    global data_time 
    global data_node_id 
    global data_humidity 
    global data_temperature 
    global data_thermal
    
    data = str(message.payload.decode("utf-8"))
    # if start set variable
    if str(message.topic)=="SENSOR_DATA/START":
        data_time = ""
        data_node_id = data
        data_humidity = ""
        data_temperature = ""
        data_thermal = ""

    # if time get data in variable
    elif str(message.topic)=="SENSOR_DATA/TIME":
        data_time = str(data_time) + str(data)

    # if humidity get data in variable
    elif str(message.topic)=="SENSOR_DATA/HUMIDITY":
        data_humidity = str(data_humidity) + str(data)

    # if temperature get data in variable
    elif str(message.topic)=="SENSOR_DATA/TEMPERATURE":
        data_temperature = str(data_temperature) + str(data)

    # if thermal get data in variable 
    elif str(message.topic)=="SENSOR_DATA/THERMAL":
        data_thermal = str(data_thermal) + str(data)

    # if end send all data on variable to database
    elif str(message.topic)=="SENSOR_DATA/END":
        print(data_thermal)
        connection = pymysql.connect(host="localhost",user="root",password="",database="network2" )
        cursor = connection.cursor()
        insert = "INSERT INTO sensor_data(Time,NodeID,Humidity,Temperature,Thermal) VALUES('"+data_time+"','"+data_node_id+"','"+data_humidity+"','"+data_temperature+"','"+data_thermal+"');"
        cursor.execute(insert)
        connection.commit()
        connection.close()
        
    # if print something when publisher connect or disconnect
    if str(message.topic)=="SENSOR_DATA/CONNECT":
        print("Connecting from : ", str(message.payload.decode("utf-8")) )
    else:
        print("Received message: ",str(client), str(message.topic), str(message.payload.decode("utf-8")) )

# connent to broker
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Database")
client.connect(mqttBroker)

# subscribe all the topic and end program when pass 3000 second
while True:
    client.on_connect = on_connect
    client.loop_start()
    client.subscribe("SENSOR_DATA/START")
    client.subscribe("SENSOR_DATA/CONNECT")
    client.subscribe("SENSOR_DATA/TIME")
    client.subscribe("SENSOR_DATA/HUMIDITY")
    client.subscribe("SENSOR_DATA/TEMPERATURE")
    client.subscribe("SENSOR_DATA/THERMAL")
    client.subscribe("SENSOR_DATA/END")
    client.on_message = on_message
    # time.sleep(300000)
    # client.disconnect()
    # client.on_disconnect = on_disconnect
    # time.sleep(1)
    # client.loop_end()
