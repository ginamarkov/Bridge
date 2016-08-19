dictionary={"Brooklyn":["Prospect Park", "Brooklyn Bridge", "Bagels"], "Upper West Side":["AMNH"], "West Village":["Independent Film Theater", "Cones Ice Cream"]}
for location in dictionary:
	sentence = "I like "
	places = dictionary[location]
	for place in places:
		if len(places) == 1:
			sentence += place + " in " + location + "."
		elif len(places) ==2 and places.index(place) == 0:
			sentence += place + ""
		elif (places.index(place) != len(places) -1):
			sentence += place + ", "
		else:
			sentence += " and " + place + " in " + location + "."

	print sentence
