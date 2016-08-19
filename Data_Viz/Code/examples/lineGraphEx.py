import matplotlib.pyplot as plt

time = [0,16,32,48,64,80]
popDens = [.028,.047,.082,.141,.240,.381]
plt.plot(time,popDens, color='#00FF00')
plt.xlabel('Time (minutes)')
plt.ylabel('Population Density')
plt.title('Growth Rate of \nVibrio natriegens Bacteria')
plt.savefig('/Users/ginamarkov/Documents/BridgeUp/Data_Viz/Figures/lineExample.png')
plt.show()
plt.close()
