# Write a program to create a server that listens to port 5003 using stream sockets. 
# Write a simple client program to connect to the server. 
# Send a simple text message “Hello” from the client to the server 
# and the server to the client and close the connection.

import socket

addr = 'localhost'
port = 5003
msg = 'Hello'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((addr,port))
s.listen()

conn, c_addr = s.accept()
conn.send(msg.encode())

data = ''
while True:
    d = conn.recv(8)

    if len(d) <= 0:
        break
    
    data += d.decode()

print(data)
conn.close()