# Write a program to create a chat server that listens to port 5004 using stream sockets. 
# Write a simple client program to connect to the server. Send multiple text messages from 
# the client to the server and vice versa. When either party types “Bye”, close the connection.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = 'localhost'
port = 5004

s.bind((addr,port))
s.listen()

conn, c_addr = s.accept()