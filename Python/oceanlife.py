import csv
import wikipedia as w
import sys

ocean_data_in = open("ocean_life_data.csv", "rU")
data_in = list(csv.reader(ocean_data_in))
 

def menu ():
	print("Hello! Welcome to Ocean Life! You can learn about the Deep Sea, Estuaries, the Polar Seas, the Continental Shelf, or Coral Reefs.")
	choice = (raw_input("Please choose a region to learn about. If you want to quit, type quit").lower())

	while choice != "quit":
		if choice == "deep sea":
			DeepSea()
		elif choice == "estuaries":
			Estuaries()
		elif choice == "polar seas":
			PolarSeas()
		elif choice == "continental shelf":
			ContinentalShelf()
		elif choice == "coral reefs":
			CoralReef()
		else:
			choice = (raw_input("Choice not available. Please choose a region to learn about. If you want to quit, type quit").lower())
	sys.exit(0)

def DeepSea ():
	print("Welcome to the Deep Sea!")
	print("You can learn about the environment, the animals or their adaptaions, threats in the environment, and the regions the Deep Sea is found in. If you want to learn more, type more info.")
	userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit").lower())
	
	while userinput != "quit": 
		if userinput == "environment":
			print ("The deep sea has " + (str(data_in[1][1])) + ".")
		elif userinput == "animals":
			print ("Examples of animals in the deep sea include " + str(data_in[1][2]) + ".")
		elif userinput == "adaptations":
			print ("Examples of adaptations in the deep sea include " + (str(data_in[1][3])) + ".")
		elif userinput == "threats":
			print ("Examples of threats to the deep sea include " + (str(data_in[1][4])) + ".")
		elif userinput == "regions":
			print ("The deep sea is " + (str(data_in[1][5])) + ".")
		elif userinput == "more info":
			print w.summary ("Deep Sea")
		userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	menu()



def Estuaries():
	print("Welcome to Estuaries!")
	print("You can learn about the environment, the animals or their adaptaions, threats in the environment, and the regions Estuaries are found in. If you want to learn more, type more info.")
	userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	
	while userinput != "quit": 
		if userinput == "environment":
			print ("Estuaries have " + (str(data_in[2][1])) + ".")
		elif userinput == "animals":
			print ("Examples of animals in estuaries include " + str(data_in[2][2]) + ".")
		elif userinput == "adaptations":
			print ("Examples of adaptations in estuaries include " + (str(data_in[2][3])) + ".")
		elif userinput == "threats":
			print ("Examples of threats to estuaries include " + (str(data_in[2][4])) + ".")
		elif userinput == "regions":
			print ("Estuaries are found in the " + (str(data_in[2][5])) + ".")
		elif userinput == "more info":
			print w.summary ("Estuaries")
		userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	menu()



def PolarSeas():
	print("Welcome to the Polar Seas!")
	print("You can learn about the environment, the animals or their adaptaions, threats in the environment, and the regions Polar Seas are found in. If you want to learn more, type more info.")
	userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	
	while userinput != "quit": 
		if userinput == "environment":
			print ("Polar Seas have " + (str(data_in[3][1])) + ".")
		elif userinput == "animals":
			print ("Examples of animals in the Polar Seas include " + str(data_in[3][2]) + ".")
		elif userinput == "adaptations":
			print ("Examples of adaptations in the Polar Seas include " + (str(data_in[3][3])) + ".")
		elif userinput == "threats":
			print ("Examples of threats to the Polar Seas include " + (str(data_in[3][4])) + ".")
		elif userinput == "regions":
			print ("Polar Seas include the " + (str(data_in[3][5])) + ".")
		elif userinput == "more info":
			print w.summary ("Polar Seas")
		userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	menu()




def ContinentalShelf():
	print("Welcome to the Continental Shelf!")
	print("You can learn about the environment, the animals or their adaptaions, threats in the environment, and the regions the Continental Shelf is found in. If you want to learn more, type more info.")
	userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	
	while userinput != "quit": 
		if userinput == "environment":
			print ("The Continental Shelf has " + (str(data_in[4][1])) + ".")
		elif userinput == "animals":
			print ("Examples of animals in the Continental Shelf include " + (str(data_in[4][2])) + ".")
		elif userinput == "adaptations":
			print ("Examples of adaptations in the Continental Shelf include " + (str(data_in[4][3])) + ".")
		elif userinput == "threats":
			print ("Examples of threats to the Continental Shelf include " + (str(data_in[4][4])) + ".")
		elif userinput == "regions":
			print ("The Continental Shelf can be found in " + (str(data_in[4][5])) + ".")
		elif userinput == "more info":
			print w.summary ("The Continental Shelf")
		userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	menu()



def CoralReef():
	print("Welcome to Coral Reefs!")
	print("You can learn about the environment, the animals or their adaptaions, threats in the environment, and the regions Coral Reefs are found in. If you want to learn more, type more info.")
	userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	
	while userinput != "quit": 
		if userinput == "environment":
			print ("Coral Reefs have " + (str(data_in[5][1])) + ".")
		elif userinput == "animals":
			print ("Examples of animals in Coral Reefs include " + (str(data_in[5][2])) + ".")
		elif userinput == "adaptations":
			print ("Examples of adaptations in Coral Reefs include " + (str(data_in[5][3])) + ".")
		elif userinput == "threats":
			print ("Examples of threats to Coral Reefs include " + (str(data_in[5][4])) + ".")
		elif userinput == "regions":
			print ("Coral Reefs can be found in the " + (str(data_in[5][5])) + ".")
		elif userinput == "more info":
			print w.summary ("Coral Reef")
		userinput = (raw_input("Enter what you want to know. If you want to go back to the main menu, type quit.").lower())
	menu()

menu()
data_in.close()
		