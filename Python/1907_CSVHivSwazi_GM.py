import csv
f = open ("hiv_swazi.csv", "rU")
data = csv.reader(f)


dataOut = open ("hiv_swazi_out.csv", "w")
writeData = csv.writer(dataOut)
for line in data:
	print writeData.writerow(line)


f.close()
dataOut.close()
'''
#prints all lines 

for item in data:
	print item

#prints first 2 lines

for i in range (2):
	print (str(i) + "    " + data.next())


#prints lines 3 4 and 5

for i in range (3,6):
	print (data.next())


'''
