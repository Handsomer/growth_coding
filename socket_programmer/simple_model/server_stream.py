#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(9)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        print 'recv msg is:'+data
        #接收的为退出信息那么就退出。
        if data == 'exit' or not data:
            sock.close()
            exit()
        #接收的为非退出信息，那么就往客户端发送信息。
        sock.send('Hello, %s!' % data)
        sock.close()
    print 'Connection from %s:%s closed.' % addr
