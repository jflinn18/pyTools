import socket
import sys
import pdb
import random

import portscan
import ourDB

#connection is working for localhost

#PORT = 12345
#HOST = '10.28.34.61'
#HOST = '127.0.0.1'

#HOST = raw_input("Enter server IP: " )
PORT = 12345

def addData(mySock, ip, data):
	try:
		mySock.connect((ip, PORT))
	except:
		print 'Connection failed.'
		
		
	print "Connection Complete"
	#pdb.set_trace()

	# protocol start

	mySock.send(portscan.myIP) # sends your ip address

	msg = mySock.recv(128)

	if msg == "hello: " + portscan.myIP:
		mySock.send("insert into data (name, age) values ('" + data[0] + "', " + str(data[1])+ ");")
		#mySock.send('select * from data')
	else:
		print 'Incorrect Server response! Next server...'
		return
		
		
	msg = mySock.recv(1024)
	print msg

	mySock.close()


#myIP = '10.28.34.80'


#pdb.set_trace()
#socket.setdefaulttimeout(None)
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

netSize = len(portscan.openIPs)

# assuming a 33.3% disconnection rate (see paper)

R = 2

for n in ourDB.db:
	while n[2] <= R:
		ip = portscan.openIPs[random.randint(0, netSize-1)]
		if ip not in n[3]:
			n[3].append(ip)
			n[2] += n[2]
			
			addData(mySock, ip, (n[0], n[1]))