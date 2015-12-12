import socket	
import pdb

uphosts = []

subNet = raw_input("Enter your gateway address (ex. 192.168.0.1): ")
port = int(raw_input("Enter the port number: "))

subNetParts = subNet.split('.')

rawSubNet = subNetParts[0] + '.' + subNetParts[1] + '.' + subNetParts[2] + '.'

loclnet = 2

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while loclnet < 255:
	try:
		host = rawSubNet+str(loclnet)
		#host = '10.28.34.23'
		pdb.set_trace()
		mySock.connect((host, port))
	
		print "-----Host up: " + rawSubNet + str(loclnet) + "-----"
		uphosts.append(rawSubNet+str(loclnet))
		mySock.close()
	except socket.error:
		print socket.error
	except:
		print "No connection: " + rawSubNet + str(loclnet)
		mySock.close()
	
	loclnet += 1
	
print '\n\n'

for n in uphosts:
	print "Host up: " + n