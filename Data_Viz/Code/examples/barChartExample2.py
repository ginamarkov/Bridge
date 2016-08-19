import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012,2015)

category1_values = [2, 5, 9]
category2_values = [7, 6, 3]

plt.bar(years - 0.2,
        category1_values,
        color='blue',
        edgecolor='none',
        width=0.4,
        align='center',
        label='y1')
plt.bar(years + 0.2,
        category2_values,
        color='orange',
        edgecolor='none',
        width=0.4,
        align='center',
        label='y2')

plt.xticks(years, [str(year) for year in years])
plt.ylabel('Units')
plt.xlabel('Years')
plt.title('This is a bar graph')
plt.legend()
#can change location with loc='lower right' or 'upper left' etc

plt.show()
plt.close()
