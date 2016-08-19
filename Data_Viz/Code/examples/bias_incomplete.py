
''' WORD BANK
matplotlib.pyplot
plt
2006
xlabel
plt
show
year
title
2007371
label
2550000

year
dirverless_cars
plot
2014
legend
Driverless Cars on the road 
ylabel
Total Number
2350000
'''


import matplotlib.pyplot as plt
car_injuries = [2550000,2350000]
year = [2006,2014]
driverless_cars = [0,10000]
allYears = list(range(2006,2014))
plt.plot(year, car_injuries, label= 'Car Injuries in the U.S.')
plt.plot(year, driverless_cars, label= 'Driverless Cars on the Road')
plt.xlabel('Year')
plt.ylabel('Total Number')
plt.xticks(allYears, allYears)
plt.title('Comparison of Car Accident Injuries and \n Driverless Cars On The Road')
plt.legend()
plt.show()
