#!/usr/bin/env python
import socket
import subprocess
import sys
import pdb
from datetime import datetime
import threading


def tryConn(ip, myIP, port):
    #print "Trying IP: {}".format(ip)
    try:
		#for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((ip, port))
		if result == 0:
			lock.acquire()
			try:
				print "IP: {} Port {}: \t Open".format(ip, port)
			finally:
				lock.release()
			openIPs.append(ip)
			#pdb.set_trace()
			sock.send(myIP)
			msg = sock.recv(1024)
			msg = sock.recv(1024)
			if msg == "Ready for query.":
				sock.send('select')
			msg = sock.recv(1024)
			print msg
		sock.close()
    except socket.gaierror:
        print 'Hostname for {} could not be resolved. Exiting'.format(ip)
    except socket.error:
        print "Couldn't connect to IP: {}".format(ip)
    
# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
myIP = raw_input("What is your IP? ")
#remoteServer    = raw_input("Enter a template IP to scan (ex. \"10.11.7. \" --> note the space): ")

subNet = myIP.split('.')
remoteServer = subNet[0] + '.' + subNet[1] + '.' + subNet[2] + '.' 

serverIPs = []
counter = 2;
while counter < 256:

#counter = 15
#while counter < 24:
    #make a bunch of ip addresses
    newServerIP = remoteServer + `counter`
    serverIPs.append(newServerIP)
    counter = counter + 1

serverHostNames = []
for ip in serverIPs:
    serverHostNames.append(socket.gethostbyname(ip))

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote hosts"
print "-" * 60

# Check what time the scan started
t1 = datetime.now()
#set the default timout to be 0.5 to reduce wait time
socket.setdefaulttimeout(0.3)

#the port to scan
portToCheck = 12345
openIPs = []
lock = threading.Lock()
for ip in serverHostNames:
    try:
        #pdb.set_trace()
        threading.Thread(target=tryConn, args=(ip, myIP, portToCheck))
		
    except:
        print "Error: unable to start new thread    IP: " + ip
        
# Checking the time again

t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
