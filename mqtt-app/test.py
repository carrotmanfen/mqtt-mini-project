import pandas as pd

# Read the Excel file and extract the sensor data
df = pd.read_excel('SampleInput.xlsx')
humidity_data = df['Humidity'].tolist()
temperature_data = df['Temperature'].tolist()
thermal_data = df.iloc[:, 2:].values.tolist()

# Convert the sensor data into a dictionary
sensor_data = {
    'Humidity': humidity_data,
    'Temperature': temperature_data,
    'ThermalArray': thermal_data
}
sensor_data['Humidity'][0] = 12
data = None
data = str(data)+"hello"
print(sensor_data['Humidity'][0])
print(data)