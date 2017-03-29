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
        sendtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        print('Received data string:')
        print(data)
        conn = mysql.connector.connect(user='root', password='password', database='test13')
        cursor = conn.cursor()
        try:
            sensorID_1 = (data[0]); data1 = (data[1])
            sensorID_2 = (data[2]); data2 = (data[3])
            sensorID_3 = (data[4]); data3 = (data[5])
            sensorID_4 = (data[6]); data4 = (data[7]);
            sensorID_5 = (data[8]); data5 = (data[9]);
            cursor.execute('insert into datasource (sendtime, sensorID_1, data_1, sensorID_2, data_2, sensorID_3, data_3, sensorID_4, data_4, sensorID_5, data_5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',[sendtime, sensorID_1, data1, sensorID_2, data2, sensorID_3, data3, sensorID_4, data4, sensorID_5, data5])
        except:
            sensorID_1 = ' '; data1 = 0.0
            sensorID_2 = ' '; data2 = 0.0
            sensorID_3 = ' '; data3 = 0.0
            sensorID_4 = ' '; data4 = 0.0
            sensorID_5 = ' '; data5 = 0.0
            cursor.execute('insert into datasource (sendtime, sensorID_1, data_1, sensorID_2, data_2, sensorID_3, data_3, sensorID_4, data_4, sensorID_5, data_5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',[sendtime, sensorID_1, data1, sensorID_2, data2, sensorID_3, data3, sensorID_4, data4, sensorID_5, data5])
            print('************exception')

        conn.commit()
        conn.close()

        break

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()