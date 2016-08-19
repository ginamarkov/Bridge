import sqlite3

conn = sqlite3.connect("Example.db")
c = conn.cursor()

#print(c.execute("SELECT * FROM Blah"))
#RETRIEVE ALL THE CONTENTS OF Viruses TABLE
for row in c.execute("SELECT * FROM Blah"):
	#Need to format into ASCII to print neatly
	rowASCII = []
	for item in row:
		rowASCII.append(item.encode('ascii')) 
	print(rowASCII) 
	


#ENTER A ROW INTO THE DATABASE
vid="V_203"
v_type="HIV"
s_type = "B"
seq = "99"
c.execute("INSERT INTO Viruses VALUES(?,?,?,?)", [vid,v_type,s_type,seq] )
'''

'''
#DELETE THE ROW WE ENTERED 
c.execute("DELETE FROM Viruses WHERE V_ID='V_203'")
'''

'''
#ENTER MULTIPLE ROWS INTO THE DATABASE
r1 = ["V_900","HIV","BW","9"]
r2 = ["V_901","HIV1","B","22"]
r3 = ["V_902","HIV","B","15"]
c.executemany("INSERT INTO Viruses VALUES(?,?,?,?)", [r1,r2,r3])
'''

'''
#DELETE THE ROWS WE ENTERED that start with V_9...
c.execute("DELETE FROM Viruses WHERE V_ID LIKE 'V_9%'")
'''


'''
#what if we want to generate IDs ? ... we can use a for loop to do so
#EXAMPLE....
for i in range(5):
	vid="V_90" +str(i)
	v_type="HIV"
	s_type = "B"
	seq = "1" + str(i)
	c.execute("INSERT INTO Viruses VALUES(?,?,?,?)", [vid,v_type,s_type,seq] )

'''


#always remember to commit changes and close connection
conn.commit()
conn.close()