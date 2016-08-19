def starbucksCoffeeOrder (temp, size, flavor):
	if temp == "iced":
		if size == "small":
			if flavor == "vanilla":	
					print ("You get a small, vanilla, iced coffee!")
			elif flavor == "caramel":
					print ("You  get a small, caramel, iced coffee!")
			else:
				print ("You get a small iced, coffee!")
		else:
			if flavor == "vanilla":	
				print ("You get a large, vanilla, iced coffee!")
			elif flavor == "caramel":
				print ("You  get a large, caramel, iced coffee!")
			else:
				print ("You get a large, plain, iced coffee!")

	elif temp == "hot":
		if size == "small":
			if flavor == "vanilla":	
					print ("You get a small, vanilla, hot coffee!")
			elif flavor == "caramel":
					print ("You  get a small, caramel, hot coffee!")
			else:
				print ("You get a small, hot, plain coffee!")
		else:
			if flavor == "vanilla":	
				print ("You get a large, vanilla, hot coffee!")
			elif flavor == "caramel":
				print ("You  get a large, caramel, hot coffee!")
			else:
				print ("You get a large, plain, hot coffee!")
	else:
		print ("Not available, sorry!")
print("Hello! We have large or small, hot or iced, and caramel, vanilla, or plain coffee.")
starbucksCoffeeOrder (raw_input("What temperature would you like?"), raw_input("What size would you like?"), raw_input("What flavor would you like?"))


