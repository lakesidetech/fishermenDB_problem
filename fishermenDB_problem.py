#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python==8.0.17


# In[2]:


import mysql.connector
import csv


# In[3]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth"
)

mycursor = mydb.cursor()


# In[4]:


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE FisheriesDB")
print(mydb)


# In[5]:


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[4]:


mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()
#instantiate cursor
mySql_Create_station_tbl = """CREATE TABLE IF NOT EXISTS Station ( 
                             Station_id int(11) NOT NULL,
                             Station_Name varchar(250) NOT NULL,
                             Station_address varchar(100),
                             PRIMARY KEY (Station_id)) """

result = mycursor.execute(mySql_Create_station_tbl)
mydb.commit
print("The Station Table created successfully ")


# In[8]:


mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()
#instantiate cursor
mySql_Create_owner_tbl = """CREATE TABLE IF NOT EXISTS Boat_Owner ( 
                             Owner_id int(11) NOT NULL,
                             Owner_Name varchar(250) NOT NULL,
                             Phone_Num varchar(100),
                             Owner_Email varchar(100),
                             Boat_id int(11),
                             PRIMARY KEY (Owner_id)) """

result = mycursor.execute(mySql_Create_owner_tbl)
mydb.commit
print("The Boat Owner Table created successfully ")


# In[13]:


mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()
#instantiate cursor
mySql_Create_boat_tbl = """CREATE TABLE IF NOT EXISTS Boat ( 
                             Boat_id int(11) NOT NULL,
                             Boat_Name varchar(250) NOT NULL,
                             Boat_Size int(11),
                             Boat_length int(11),
                             Boat_Capacity int(11),
                             Station_id int,
                             Owner_id int,
                             PRIMARY KEY (Boat_id)) """

result = mycursor.execute(mySql_Create_boat_tbl)
mydb.commit
print("The Boat Table created successfully ")


# In[15]:


mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()
#instantiate cursor
mySql_Create_boat_tbl = """CREATE TABLE IF NOT EXISTS Fishermen ( 
                             Fishermen_id int(11) NOT NULL,
                             Fishermen_Name varchar(250) NOT NULL,
                             Boat_id int(11),
                             Phone_Num varchar(100),
                             Fishermen_email varchar(100),
                             Age int,
                             PRIMARY KEY (Fishermen_id)) """

result = mycursor.execute(mySql_Create_boat_tbl)
mydb.commit
print("The Fishermen Table created successfully ")


# In[5]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()

#  Insert college1 records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\Fishery_station.csv', 'r') as stationrec:
    c_reader = csv.reader(stationrec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO Station(station_id, Station_Name, station_Address) VALUES(%s, %s,%s)", rec)
        mydb.commit()
print("Fisheries Station records added")


# In[10]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()

#  Insert boat owner records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\owner_info.csv', 'r') as Boat_Ownerec:
    c_reader = csv.reader(Boat_Ownerec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO Boat_Owner(Owner_id, Owner_Name, Phone_Num,Owner_email,Boat_id) VALUES(%s,%s,%s,%s,%s)", rec)
        mydb.commit()
print("Fisheries Boat Owner records added")


# In[14]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()

#  Insert boat records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\boat_info.csv', 'r') as boat_rec:
    c_reader = csv.reader(boat_rec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO Boat(boat_id, boat_Name, boat_size,boat_length,boat_capacity,Station_id,owner_id) VALUES(%s, %s,%s,%s,%s, %s,%s)", rec)
        mydb.commit()
print("Fisheries boat records added")


# In[16]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="FisheriesDB"
)

mycursor=mydb.cursor()

#  Insert boat records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\fishermen_info.csv', 'r') as fmen_rec:
    c_reader = csv.reader(fmen_rec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO fishermen(fishermen_id, fishermen_Name, boat_id,phone_num,fishermen_email,age) VALUES(%s,%s,%s,%s, %s,%s)", rec)
        mydb.commit()
print("Fisheries boat records added")


# In[ ]:




