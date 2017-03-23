import threading
import socket
import time
import sqlite3
import mysql.connector

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 8082))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send((data.decode('utf-8')).encode('utf-8'))
        data = data.decode('utf-8').split(',')
        data1 = (data[0])
        print(data1)
        data2 = float(data[1])
        print(data2)

        sendtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        print ('Time:', sendtime)
        print('Received:', data)

        senddata = (sendtime, data1, data2)
        #conn = sqlite3.connect('customer-01.db')
        #conn.execute('CREATE TABLE IF NOT EXISTS datasource (sendtime CHAR(19) PRIMARY KEY, data1 REAL, data2 REAL)')
        #conn.execute("INSERT INTO datasource VALUES (?, ?, ?)", senddata)

        conn = mysql.connector.connect(user='root', password='password', database='test13')
        cursor = conn.cursor()

        #cursor.execute("INSERT INTO datasource VALUES (?, ?, ?)", senddata)
        #cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
        #cursor.execute('insert into datasource (sendtime, sensorID_1, data_1) values (%s, %s, %s)', [sendtime, data1, data2])
        cursor.execute('insert into datasource (sendtime, sensorID_1, data_1, sensorID_2, data_2, sensorID_3, data_3, sensorID_4, data_4, sensorID_5, data_5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',[sendtime, data1, data2, data1, data2, data1, data2, data1, data2, data1, data2])
        conn.commit()
        conn.close()

        

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()