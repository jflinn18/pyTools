# Echo server program
import socket
import sqlite3
import os
import pdb
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 12345              # Arbitrary non-privileged port


#class to allow exiting the connection
class exitConn(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#end exitConn

print "Starting server. Please wait."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
while 1:
    try:
        msg = conn.recv(128)
        conn.sendall("hello: "+ msg)
        if msg: break;
    except KeyboardInterrupt:
        sys.exit()
conn.close()

localDatabase = sqlite3.connect('localDB.db')
cursor = localDatabase.cursor()
cursor.execute("drop table if exists DATA")
#remove the current data table if it already exists
cursor.execute("create table DATA(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL)")

while 1:
    try:
        conn, addr = s.accept()
        print 'Connected by', addr
        data = conn.recv(128)
        conn.send("hello: " + data)
        #data is the SQL statement
        data = conn.recv(1024)
        print data
        if data == "finished":
            break
        #pdb.set_trace()
        conn.sendall("Got it.")
        conn.close()
        cursor.execute(data)
        localDatabase.commit()
    except KeyboardInterrupt:
        sys.exit()
    #except exitConn:
    #    print "Data transfer finished"
    #    break;

#close the database
localDatabase.close()
#close the socket
s.close()

#check if database exists already --> if it does, delete it
#if(os.path.exists("release\localDB.db")):
#    os.system("del release\localDB.db")
#move the database file to the folder where the P2PNetworkFinal.exe is located
#os.rename("localDB.db", "release\localDB.db")
#run the P2PNetworkFinal.exe
#os.system("release\P2PNetworkFinal.exe")
