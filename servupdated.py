# Importing libraries in python
import socket
from threading import Thread
import time
import sqlite3
import json

# Allows multiple clients to connect to server 
class server:
    def __init__(self):
        # Initializing socket
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def connections(self,ip,port):
        # Server and client binding
        self.socket.bind(('',port))
        self.socket.listen(600)
        print "Server is connected"
        while True:
            
       # Accepting client connections
            c, addr = self.socket.accept()
            print addr, "is connected to server"
            data = c.recv(1024)
    #Printing messages received from the client's end
            print "Received message from client"
            print data
            print "Time when client connects to server:", time.ctime(time.time())
            a = {}
            a['hr'] = {'Id': '5',
                       'Name': 'Human',
                       'Uname': 'HR',
                       'Password': 'abcd'}   

            b = json.dumps(a)
            c.send(str(b))
       #Connecting to an existing database
            try:
                    con = sqlite3.connect('d1.db')
                    cur = con.cursor()
                    cur.execute("DROP TABLE IF EXISTS Users")
        # Creating a table
                    cur.execute("CREATE TABLE Users(Id INT,Name Text,Uname Text,Password Text)")
                    print "Table Created"
        # Inserting records into database
                    cur.execute("INSERT INTO Users VALUES(1,'Hari','hs','hari')")
                    cur.execute("INSERT INTO Users VALUES(2,'Srik','sr','kan')")
                    cur.execute("INSERT INTO Users VALUES(3,'New','us','user')")
                    con.commit()
                    cur.execute("SELECT * FROM Users")
                    da = cur.fetchall()
                    for row in da:
                        print row
       # Deleting a record from database
                    cur.execute("DELETE FROM Users where Id = '3'")
                    con.commit()
                    cur.execute("SELECT * FROM Users")
                    dc = cur.fetchall()
                    for i in dc:
                        print i
        #Updating record in a databse and printing it
                    cur.execute('''UPDATE Users SET Id = ? WHERE Name = ?''',(4,'Srik'))
                    con.commit()
                    a = cur.execute("SELECT * FROM Users WHERE Name = 'Srik'")
                    d1 = a.fetchone()
                    print d1
        # Selecting a record from the database
                    f = cur.execute("SELECT * FROM USERS WHERE Name = 'Hari'")
                    d2 = f.fetchone() 
                    print d2

            except sqlite3.Error, e:
                    if con:
              # Printing errors if exist
                       con.rollback()
                       print "There is error"
                       print str(e)
            finally:
                    if con:
              # Closing connection
                       con.close()

            # Writing to a json file
    
            d = {}
            d['srik'] ={'Id': '4',
                            'Name': 'Srik',
                            'Uname': 'sr',
                            'Password': 'kan'}

            d['hari'] = {'Id': '1',
                               'Name': 'Hari',
                               'Uname': 'hs',
                               'Password': 'hari'}

            a = json.dumps(d)
            with open("/home/hari/Desktop/json1.txt", "w") as f:
                     f.write(a)
                     print "Successfully written in file"

            # Reading from a file using json
            f = open("/home/hari/Desktop/json1.txt", "r")
            e = f.read()
            print e

    def close(self):
        self.socket.close()

def Main():
     
    # Strating client connection
    s = server()
    # Setting up connections with server
    s.connections('127.0.0.1',8080)
    # Closing socket connection
    s.close()

if __name__ == '__main__':
    Main()
