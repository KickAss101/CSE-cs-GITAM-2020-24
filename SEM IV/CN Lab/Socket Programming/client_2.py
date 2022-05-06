# Write a program to create a server that listens to port 5005 using stream sockets. 
# Write a simple client program to connect to the server. 
# The client should request for a text file and the server should return the file 
# before terminating the connection.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = 'localhost'
port = 5005
f = 'test.txt'

s.connect((addr,port))

s.send(f.encode())


    
