import matplotlib.pyplot as plt
slices = [7,2,4,10]
activities = ['Eat', 'Poo', 'Sleep', 'School']
cols = ['blue', 'green', 'yellow', 'red']

#with pie charts, you should always set the figure size to two of the same values, otherwise it is distorted
plt.figure(figsize =(4,4))

#autopct puts the values on the chart for easy readability!
plt.pie(slices, labels = activities, colors = cols, startangle = 180, 
autopct = '%1.1f%%')
#(more info on autopct at http://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct?rq=1)

plt.title('Time Spent on Daily Activities')
plt.savefig('/Users/ginamarkov/Documents/BridgeUp/Data_Viz/Figures/pieExample.png')
plt.show()
