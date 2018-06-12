#!/usr/bin/env python
# _*_ coding: utf-8 -*-

'a socket example which send echo msg to server'

import socket

#创建一个IPV4，数据流的socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))

#接收服务器传来的MSG
print(s.recv(1024))

#发送数据
for data in ['No1 data','No2 data','No3 data']:
	s.send(data)
	try:
		recv_data = s.recv(1024)
		print(recv_data)
	except:
		print('end')
		s.close()
		exit()

s.send('exit')

#关闭socket
s.close()