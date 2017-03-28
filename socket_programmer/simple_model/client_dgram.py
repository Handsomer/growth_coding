import socket

obj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

obj.sendto('haha 666',('localhost',8080))
