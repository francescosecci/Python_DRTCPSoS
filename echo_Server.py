'''
Programma Echo_Server
'''

import socket 

HOST = "localhost"
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

while 1:
	conn, addr = s.accept()

	print "Connected by", addr

	data = conn.recv(1024)

	if data == "ko": 
		print "Received ko command."
		print "Connection Closed (ko command received)."
		conn.close()
		break
	else:
		print "Re-Send message received from Client: ", data
		conn.send(data)




