#!/usr/bin/env python
import socket
import subprocess
import sys
import pdb
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
myIP = raw_input("What is your IP? ")
#remoteServer    = raw_input("Enter a template IP to scan (ex. \"10.11.7. \" --> note the space): ")

subNet = myIP.split('.')

if len(subNet) == 4:
	remoteServer = subNet[0] + '.' + subNet[1] + '.' + subNet[2] + '.'
else: 
	print "Incorrect IP format. Stop using IPv6 or stop being dumb!!!"
	sys.exit()

serverIPs = []
#counter = 2;
#while counter < 256:

counter = 2
while counter < 256:
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
for ip in serverHostNames:
    #print "Trying IP: {}".format(ip)
    try:
        #for port in range(1,1025):
		#pdb.set_trace()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, portToCheck))
        if result == 0:
			print "IP: {} Port {}: \t Open".format(ip, portToCheck)
			openIPs.append(ip)
			
			# protocol start
			
			sock.send(myIP)
			#pdb.set_trace()
			msg = sock.recv(1024)
			print msg
			
			# protocol end
			
			#print msg
        sock.close()
    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()
    except socket.gaierror:
        print 'Hostname for {} could not be resolved. Exiting'.format(ip)
    except socket.error:
        print "Couldn't connect to IP: {}".format(ip)

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
