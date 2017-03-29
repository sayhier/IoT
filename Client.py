import socket
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8082))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

i = 0
while True:
    raw1 = str(round(random.uniform(1, 50),2))
    raw2 = str(round(random.uniform(1, 50), 2))
    sensorID = b'Temperature'
    senddata = sensorID + b',' + raw1.encode() + b',' + sensorID + b',' + raw2.encode() + b',' + sensorID + b',' + raw2.encode() + b',' + sensorID + b',' + raw2.encode() + b',' + sensorID + b',' + raw2.encode()
    print('Sent:',senddata.decode())

    s.send(senddata)
    print('Received:', s.recv(1024).decode('utf-8'))

    time.sleep(10)
    i = i+1
    if i > 1000:
        break

# stop the new thread in server
s.send(b'exit')
s.close()