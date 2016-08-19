import sqlite3
conn = sqlite3.connect("HivSwazi.db")
c = conn.cursor()

c.execute('''SELECT BigTable.Population_Subgroup, Virus.Virus_Type, Geo.Geo_Area, COUNT (Virus.Virus_Type) FROM BigTable 
			JOIN Virus ON BigTable.V_ID = Virus.V_ID 
			JOIN Geo ON BigTable.G_ID = Geo.G_ID 
			GROUP BY Population_Subgroup, Geo_Area''')
bigList = [[str(item) for item in results] for results in c.fetchall()]


for item in bigList:
	print item[0] + " in the " +item[2] + " region were infected with " +item[3]+ " case(s)of " +item[1]

conn.close()