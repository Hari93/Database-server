# Creating a multi threaded server
Server application that can handle 500-600 requests per second.
Connects to multiple clients using multi threading
It manages a database application such as sqlite3
Tasks such as inserting a record in the database and updating a record and selecting a particular entry from the database are done.
***For Optimizing time***
Data Structures such as dictionary are used.
The advantage of using data structure is it optimizes time and performance
**Json parsers**
Json parsers are used to parse the information and send the data between server and multiple clients.
In my code , i have shown a simple json parsing between server and single client
**What I have done**
I have created a web server application that manages database and uses json parsers to present a scalable system and for my demo, 
i have written code for 2 clients , one client uses json library to send information to and from the server.
The other client just interacts with server and passes message
