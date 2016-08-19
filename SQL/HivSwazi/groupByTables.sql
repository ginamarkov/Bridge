SELECT BigTable.Population_Subgroup, Virus.Virus_Type, Geo.Geo_Area, COUNT (Virus.Virus_Type) FROM BigTable
LEFT JOIN Virus ON BigTable.V_ID = Virus.V_ID
LEFT JOIN Geo ON BigTable.G_ID = Geo.G_ID
GROUP BY Population_Subgroup, Geo_Area