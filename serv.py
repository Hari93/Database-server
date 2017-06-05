# Database-server
# Importing libraries in python
import socket
from threading import Thread
import time
import sqlite3
import json

# Allows multiple clients to connect to server 
def clienthandler():
    c, addr = s.accept()
    print addr, "is connected to server"
    #while :
    data = c.recv(1024)
    # Printing messages received from the client's end
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

    

# Creating a socket and binding it to port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',8000))
s.listen(600)
print "Server is connected"

#Connection to database
def database():
     
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
        con.commit()
        cur.execute("SELECT * FROM Users")
        data = cur.fetchall()
        for row in data:
              print row
        #Updating record in a databse and printing it
        cur.execute('''UPDATE Users SET Id = ? WHERE Name = ?''',(4,'Srik'))
        con.commit()
        a = cur.execute("SELECT * FROM Users WHERE Name = 'Srik'")
        d1 = a.fetchone()
        print d1
        # Selecting a record from the database
        s = cur.execute("SELECT * FROM USERS WHERE Name = 'Hari'")
        d2 = s.fetchone() 
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

def write():
    
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

def read():
     f = open("/home/hari/Desktop/json1.txt", "r")
     e = f.read()
     print e
    

def Main():
    # Starting threads that allow multiple clients to connect to server 
    for i in range(600):
        t1 = Thread(target = clienthandler)
        t1.start()
    # Starting database thread
    t2 = Thread(target = database)
    t2.start()
    #Starting write json parsers
    t3 = Thread(target = write)
    t3.start()
    #Starting read json parsers
    t4 = Thread(target = read)
    t4.start()
    # Closing down socket connection
    s.close()

if __name__ == '__main__':
    Main()
