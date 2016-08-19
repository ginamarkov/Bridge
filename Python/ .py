import csv
import wikipedia as w
import sys

ocean_data_in = open("ocean_life_data.csv", "rU")
data_in = list(csv.reader(ocean_data_in))

 
def menu ():
	print("Hello! Welcome to Ocean Life! You can learn about the Deep Sea, type 1. Estuaries, type 2. the Polar Seas, type 3. the Continental Shelf, type 4. or Coral Reefs, type 5. If you want to search a word, type 7.")
	choice = (int(raw_input("Please choose a region to learn about. If you want to quit, type 6.")))

	while choice != 6:
		if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
			all_regions (choice)
		elif choice == 7:
			keyword()
		else:
			choice = (int(raw_input("Choice not available. Please choose a region to learn about. If you want to quit, type 6")))
	sys.exit(0)



def all_regions (region):

	if region == 1:
		region_name = " Deep Sea"
	elif region == 2:
		region_name = " Estuaries"
	elif region == 3:
		region_name = " Polar Seas"
	elif region == 4:
		region_name = " Continental Shelf"
	elif region == 5:
		region_name = " Coral Reefs"

	print("Welcome to the" +region_name+ "!")
	print("You can learn about the environment (type 1) the animals or their adaptations (type 2 or 3), threats in the environment (type 4), and the regions it is found in (type 5). If you want to learn more, type 7.")
	subcategory = (int(raw_input("Enter what you want to know. If you want to go back to the main menu, type 6.")))
	while subcategory != 6:
		if subcategory == 2:
			print "In the" + region_name + ", the animals are the " +data_in[region][2] +"."
		elif subcategory == 1:
			print "In the" + region_name + ", the environment has " +data_in[region][1] +"."
		elif subcategory == 3:
			print "In the" + region_name + ", the animals have adaptations such as " + data_in[region][3] +"."
		elif subcategory == 4:
			print "The threats in the" +region_name+ "include " + data_in[region][4] +"."
		elif subcategory == 5:
			print "The" +region_name+ "can be found near " + data_in[region][5] +"."
		elif subcategory == 7:
			print w.summary (region_name)
		subcategory = (int(raw_input("Enter what you want to know. If you want to go back to the main menu, type 6.")))
	menu()

def capitalize (phrase):
	capitilized = (phrase[0].upper() + phrase[1:])
	return capitilized



def keyword ():
	word = raw_input("Type in the word you want to find. If you want to quit, type quit.").lower()
	while word != "quit":
		found = False
		for row in data_in:
			for value in row:
				if (word in value):
					found = True
					sentence = capitalize(word)+ " can be found in the "
					headers = data_in[0]
					sentence += capitalize(row[0]) + " and is under the category of " + headers[row.index(value)] + "."
					print sentence
	
		if(found == False):
			print "This word is not in our data."		
						
		word = raw_input("Type in the word you want to find. If you want to quit, type quit.").lower()
		
	menu()


menu()
data_in.close()





