data_frame = [
    {'node_id':"123", 'time':"", 'humidity':"", 'temperature':"", 'thermal':""},
    {'node_id':"456", 'time':"", 'humidity':"", 'temperature':"", 'thermal':""}
]
data_format = {'node_id':"789", 'time':"", 'humidity':"", 'temperature':"", 'thermal':""}

data_frame.insert(2,data_format)
data_format['node_id']="qwe"
print(data_frame)