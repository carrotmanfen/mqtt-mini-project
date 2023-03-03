import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", password="", database="network2")
cursor = connection.cursor()

# queries for sql command all rows
query = "Select * from sensor_data;"

#executing the quires
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()