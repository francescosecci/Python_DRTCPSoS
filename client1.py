'''
Programma Echo_Client
'''

import socket 
import time

HOST = "localhost"
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
time.sleep(1)
s.send("Hello World!")

data = s.recv(1024)

s.close()

print "Received from Server: ", data




