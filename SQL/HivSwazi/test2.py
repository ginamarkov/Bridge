import sqlite3
conn = sqlite3.connect("HivSwazi.db")
c = conn.cursor()

for row in c.execute ("SELECT * FROM Virus"):
	rowASCII = []
	for item in row:
		rowASCII.append(item.encode("ascii"))
	print rowASCII






conn.close()