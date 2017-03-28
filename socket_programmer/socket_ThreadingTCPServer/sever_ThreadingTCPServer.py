#!/usr/bin/env python
# _*_ coding: utf-8 -*-

'socket of multithreading'
import SocketServer
import time, socket, threading

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall('accept connect')
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                print "server recv exit"
                Flag = False
            else:
                print "server recv data %s"%data
                conn.sendall('server recv data %s'%data)

if __name__ == '__main__':
	IP = '127.0.0.1'
	PORT = 9999
	server = SocketServer.ThreadingTCPServer((IP,PORT),MyServer)
	server.serve_forever()