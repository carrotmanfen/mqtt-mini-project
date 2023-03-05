import paho.mqtt.client as mqtt
import time
import pymysql

flag_connected = 0

data_frame = [
    # {'node_id':"", 'time':"", 'humidity':"", 'temperature':"", 'thermal':""}
]
data_format = {'node_id':"", 'time':"", 'humidity':"", 'temperature':"", 'thermal':""}

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
    global data_format
    global data_frame
    checkDataFrame = True
    data = str(message.payload.decode("utf-8"))
    dataSplit = data.split(";")
    dataNode = dataSplit[0]
    dataMessage = dataSplit[1]
    # if start set variable
    if str(message.topic)=="SENSOR_DATA/START":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                data_frame[i]['time']=""
                data_frame[i]['humidity']=""
                data_frame[i]['temperature']=""
                data_frame[i]['thermal']=""
                checkDataFrame = False
                
        if checkDataFrame:
            data_frame.insert(len(data_frame),{'node_id':dataNode, 'time':"", 'humidity':"", 'temperature':"", 'thermal':""})
            print(data_frame)

    # if time get data in variable
    elif str(message.topic)=="SENSOR_DATA/TIME":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                data_frame[i]['time'] = data_frame[i]['time'] + str(dataMessage)

    # if humidity get data in variable
    elif str(message.topic)=="SENSOR_DATA/HUMIDITY":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                data_frame[i]['humidity'] = data_frame[i]['humidity'] + str(dataMessage)

    # if temperature get data in variable
    elif str(message.topic)=="SENSOR_DATA/TEMPERATURE":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                data_frame[i]['temperature'] = data_frame[i]['temperature'] + str(dataMessage)

    # if thermal get data in variable 
    elif str(message.topic)=="SENSOR_DATA/THERMAL":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                data_frame[i]['thermal'] = data_frame[i]['thermal'] + str(dataMessage)

    # if end send all data on variable to database
    elif str(message.topic)=="SENSOR_DATA/END":
        for i in range(len(data_frame)):
            if data_frame[i]['node_id']==dataNode:
                print(data_frame[i])
                connection = pymysql.connect(host="localhost",user="root",password="",database="network2" )
                cursor = connection.cursor()
                insert = "INSERT INTO sensor_data(Time,NodeID,Humidity,Temperature,Thermal) VALUES('"+data_frame[i]['time']+"','"+data_frame[i]['node_id']+"','"+data_frame[i]['humidity']+"','"+data_frame[i]['temperature']+"','"+data_frame[i]['thermal']+"');"
                cursor.execute(insert)
                connection.commit()
                connection.close()
                data_frame[i]['time']=""
                data_frame[i]['humidity']=""
                data_frame[i]['temperature']=""
                data_frame[i]['thermal']=""

        
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
