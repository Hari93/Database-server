import socket
import sys
import time

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(('127.0.0.1', 8000))
sc.send("Hello World")
print "Client 2 connected to server"
print "Time when client2 connected to server",time.ctime(time.time())

