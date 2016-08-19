import sqlite3
conn = sqlite3.connect("StudentSchedule.db")
c = conn.cursor()

c.execute('''CREATE TABLE S_Info
			(S_Name text, S_Dorm text, S_ID text)''')

c.execute('''INSERT INTO S_Info VALUES)


c.execute('''CREATE TABLE C_Info
			(C_Name text, C_Credits text, C_ID text)''')

c.execute('''CREATE TABLE Schedule
			(S_Name text, S_Dorm text, S_ID text)''')


conn.commit()
conn.close()
