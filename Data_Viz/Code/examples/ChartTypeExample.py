import matplotlib.pyplot as plt
import numpy as np
years = [2012,2013,2014]
allyears = list(range(2012,2015))
values = [2,5,9]
plt.xticks (allyears,allyears)
plt.bar(years, values, align="center")
plt.savefig('/Users/ginamarkov/Documents/BridgeUp/Data_Viz/Figures/barChartExample.png')
plt.show()
plt.close()