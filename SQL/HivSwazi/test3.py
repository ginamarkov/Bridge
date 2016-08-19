import sqlite3
conn = sqlite3.connect("HivSwazi.db")
c = conn.cursor()

c.execute ("SELECT * FROM Virus")



bigList = [[str(item) for item in results] for results in c.fetchall()]
for item in bigList:
	print item
	
'''
for results in c.fetchall():
	bigList= []
	bigList.append(str(results))
	for item in results:
		innerLists = []
		str(item)
		innerLists.append(item)
print bigList

'''

conn.close()