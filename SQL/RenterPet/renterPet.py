#Use Python to create database of apartment-pet info

import sqlite3
import csv 


conn = sqlite3.connect("RenterPet.db")
c = conn.cursor()

data_in = open("RenterPet.csv", "rU")
data_reader = csv.reader(data_in)

#The column headers are Renter_Name, Apt_No, Renter_SSN, Pet_Type, Pet_Name, Pet_ID
column_headers = data_reader.next()



#creates big table and puts in all the values 
'''
c.execute('CREATE TABLE BigTable ('
	+column_headers[0]+' TEXT,'
	+column_headers[1]+' TEXT,' 
	+column_headers[2]+' TEXT,'
	+column_headers[3]+' TEXT,' 
	+column_headers[4]+' TEXT,' 
	+column_headers[5]+' INTEGER)')


for row in data_reader:
	c.execute("INSERT INTO BigTable VALUES (?,?,?,?,?,?)", row)

'''


#creates the table Renter info, selects distinct, then inserts values
'''

c.execute('CREATE TABLE Renter_Info ('
	+column_headers[0]+' TEXT,'
	+column_headers[1]+' TEXT,' 
	+column_headers[2]+' TEXT)')


query = 'SELECT DISTINCT '+\
column_headers[0]+', '+\
column_headers[1]+', '+\
column_headers[2]+ \
' FROM BigTable'


renter_info = list(c.execute(query))


for row in renter_info:
	bigList = []
	for item in row:
		if type(item) == type(u"hi"):
			bigList.append(item.encode("ascii"))
		else:
			bigList.append(item)
	c.execute("INSERT INTO Renter_Info VALUES (?,?,?)",bigList)

'''


#creates the table Pet info, adds SSN, selects distinct, then inserts values

'''

c.execute('CREATE TABLE Pet_Info ('
	+column_headers[2]+' TEXT,'
	+column_headers[3]+' TEXT,'
	+column_headers[4]+' TEXT,' 
	+column_headers[5]+' INTEGER)')


query = 'SELECT DISTINCT '+\
column_headers[2]+', '+\
column_headers[3]+', '+\
column_headers[4]+', '+\
column_headers[5]+ \
' FROM BigTable'


pet_info = list(c.execute(query))


for row in pet_info:
	bigList = []
	for item in row:
		if type(item) == type(u"hi"):
			bigList.append(item.encode("ascii"))
		else:
			bigList.append(item)
	c.execute("INSERT INTO Pet_Info VALUES (?,?,?,?)",bigList)


'''

conn.commit()
conn.close()
data_in.close()
