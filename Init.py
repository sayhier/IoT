import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="password")
cursor = conn.cursor()
cursor.execute('CREATE DATABASE test13')

conn = mysql.connector.connect(user='root', password='password', database='test13')
cursor = conn.cursor()
#cursor.execute('create table datasource (sendtime char(19) primary key, sensorID_1 char(20), data_1 real)')
cursor.execute('create table datasource (sendtime datetime NOT NULL primary key, sensorID_1 char(20), data_1 real, sensorID_2 char(20), data_2 real, sensorID_3 char(20), data_3 real, sensorID_4 char(20), data_4 real, sensorID_5 char(20), data_5 real)')

conn.commit()
cursor.close()
