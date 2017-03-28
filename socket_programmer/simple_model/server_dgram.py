import socket 

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sk.bind(("",8080))
print sk
print 'waiting accept'
conn,address = sk.recvfrom(1024)
print conn,address

print 'dgram socket end'

