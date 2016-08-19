
def menu_for_moon_functions (choice):
	if choice == "A":
		weight_on_moon(int(raw_input("What is your weight?")))
	elif choice == "B":
		moonsbtwnearthandmoon ()
	elif choice == "C":
		distance_of_moon_travel(int(raw_input("How many hours would you like?")))
		
	
def weight_on_moon(kgs):
	b = (0.16*kgs)
	print "Your weight on the moon is " +str(b) + " pounds"


def moonsbtwnearthandmoon ():
	distance_btwn_earth_and_moon = 238900
	diameter_of_moon = 2159
	print (distance_btwn_earth_and_moon/diameter_of_moon)


def distance_of_moon_travel (time):
	speed_of_moon = 2288
	a = (speed_of_moon*time)
	print "The moon travels",a, "miles in" ,time, "hours"


userInput=raw_input ("If you want to know your weight on the moon, choose A. If you want to know the number of moons between earth and moon, choose B. Finally, if you want to know how far the moon travels in a specific amount of time, choose C").upper()
while(userInput != "QUIT"):
	menu_for_moon_functions(userInput)
	userInput = raw_input ("If you want to know your weight on the moon, choose A. If you want to know the number of moons between earth and moon, choose B. Finally, if you want to know how far the moon travels in a specific amount of time, choose C").upper()







