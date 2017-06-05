import socket
import json
import sys
import time

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(('127.0.0.1', 8000))
b = {}
b['hp'] = {'Id': '3',
'Name': 'Pradha',
'Uname': 'HP',
'Password':'hello'}

a = json.dumps(b)
with open("/home/hari/Desktopjson1.txt","w") as f:
     f.write(a)
     print "File Write Successful"

sc.send(str(a))
print "Client 1 connected to server"
print "Time when client1 connected to server",time.ctime(time.time())
d = sc.recv(1024)
print d
