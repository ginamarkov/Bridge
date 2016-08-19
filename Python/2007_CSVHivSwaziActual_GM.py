import csv
hiv_in = open ("hiv_swazi.csv", "rU")
stats_in = csv.reader(hiv_in)

column_headers = stats_in.next()

year_index = column_headers.index("Year")

def find_data_for_year (year):
	hiv_out = open ("hiv_swazi_new.csv", "w")
	writeData = csv.writer(hiv_out)
	writeData.writerow(column_headers)
	
	for data in stats_in:
		if data[year_index] == str(year):
			writeData.writerow(data)

	hiv_out.close()	
find_data_for_year((raw_input("Enter a year ")))
hiv_in.close()