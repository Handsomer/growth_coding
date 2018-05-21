#!/usr/bin/env python
# _*_ coding: utf-8 -*-
import socket

import select

sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #端口重用
#SOL_SOCKET，意思是正在使用的socket选项，
#socket.SO_REUSEADDR,当socket关闭后，
#本地端用于该socket的端口号立刻就可以被重用。
#通常来说，只有经过系统定义一段时间后，才能被重用。
#最后一个 1，表示将SO_REUSEADDR标记为TRUE，
#操作系统会在服务器socket被关闭或服务器进程终止后
#马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
sk1.bind(('127.0.0.1',9999))
sk1.listen(5)
sk1.setblocking(0)

inputs = [sk1,]
while True:
    readable_list, writeable_list, error_list = select.select(inputs, [], inputs, 1) #监听inputs列表所含的所有元素，一有变化，就放入readalbe_list, 第四个参数 1 代表，阻塞1秒，然后就往下走
    for r in readable_list:
        # 当客户端第一次连接服务端时
        if sk1 == r:
            print('accept')
            request, address = r.accept()
            request.sendall('receive data connect')
            request.setblocking(0)
            inputs.append(request)  #将此次的连接放入inputs 的监听队列
        # 当客户端连接上服务端之后，再次发送数据时
        else:
            received = r.recv(1024)
            # 当正常接收客户端发送的数据时
            if received != 'exit':
                print('received data:', received)
                r.sendall('recv data:%s'%received)
            # 当客户端关闭程序时，会发送过来空数据
            else:
                inputs.remove(r)
sk1.close()