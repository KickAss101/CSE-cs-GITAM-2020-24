# Write a program to create a server that listens to port 5005 using stream sockets. 
# Write a simple client program to connect to the server.
# The client should request for a text file and the server should return the file 
# before terminating the connection.

import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = 'localhost'
port = 5005

s.bind((addr,port))
s.listen()

conn, c_addr = s.accept()

print("Name of the file:")

f = s.recv(1024)
files = os.listdir()

if f in files:
    conn.sendfile(f)
else:
    conn.send("file not found".encode())

s.close()