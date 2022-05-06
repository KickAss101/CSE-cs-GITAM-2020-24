# Write a program to create a server that listens to port 5003 using stream sockets. 
# Write a simple client program to connect to the server. 
# Send a simple text message “Hello” from the client to the server 
# and the server to the client and close the connection.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = 'localhost'
port = 5003
msg = 'Hello'

s.connect((addr,port))
s.send(msg.encode())

data = s.recv(1024)

print(data.decode())

s.close()