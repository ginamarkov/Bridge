UPDATE BigTable
SET V_ID = (SELECT V_ID from Virus WHERE BigTable.Sequence = Virus.Sequence AND BigTable.Virus_Type = Virus.Virus_Type AND BigTable.Specimen_Type = Virus.Specimen_Type);

UPDATE BigTable
SET G_ID = (SELECT G_ID from Geo WHERE BigTable.Country_Code = Geo.Country_Code AND BigTable.Geo_Area = Geo.Geo_Area AND BigTable.Site_Name = Geo.Site_Name);


UPDATE BigTable
SET P_ID = (SELECT P_ID from Pub WHERE BigTable.Author = Pub.Author AND BigTable.Title = Pub.Title AND BigTable.Year = Pub.Year);

UPDATE BigTable
SET R_ID = (SELECT R_ID from Rates WHERE BigTable.NO_CASES = Rates.NO_CASES AND BigTable.NO_DEATHS = Rates.NO_DEATHS AND BigTable.PREV_RATE = Rates.PREV_RATE);


#join 3 tables
SELECT Geo.Geo_Area, Virus.Sequence
FROM BigTable 
LEFT JOIN Geo ON BigTable.G_ID = Geo.G_ID  
LEFT JOIN Virus ON BigTable.V_ID = Virus.V_ID


#group by sex
SELECT Geo.Geo_Area, BigTable.Sex, COUNT(BigTable.Sex) FROM Geo JOIN BigTable WHERE Geo_Area = "National" GROUP BY Sex;

#group by 3 tables
SELECT BigTable.Population_Subgroup, Virus.Virus_Type, Geo.Geo_Area, COUNT (Virus.Virus_Type) FROM BigTable
LEFT JOIN Virus ON BigTable.V_ID = Virus.V_ID
LEFT JOIN Geo ON BigTable.G_ID = Geo.G_ID
GROUP BY Population_Subgroup, Geo_Area;