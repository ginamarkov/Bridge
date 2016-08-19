import matplotlib.pyplot as plt
csfont = {'fontname':'Lato'}
allTimes = list(range(1,5))
num_insta =[1,0,0,0]
num_snaps = [10,12,7,9]
time_of_day = [1, 2, 3, 4]
plt.scatter(time_of_day,num_snaps, label= "Snapchat", color='#FF0000', marker='*', s=150)
plt.scatter(time_of_day,num_insta, label = "Instagram", color='#00FF00', marker='*', s=150)

plt.xlabel("Time of Day", **csfont)
plt.ylabel("Number of Posts", **csfont)

plt.xticks(allTimes, allTimes)



plt.title("Social Media Use", fontsize = 20, **csfont)
plt.savefig('/Users/ginamarkov/Documents/BridgeUp/Data_Viz/Figures/snapUse.png')

plt.legend()
plt.show()
plt.close()
