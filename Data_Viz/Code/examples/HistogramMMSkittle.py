import matplotlib.pyplot as plt
import numpy as np
colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
color_values = [4,10,7,5,5,3,5]
plt.xlabel("Colors")
plt.ylabel("Frequency")
plt.title("Frequency of Different Colors in Skittles and M&Ms")
plt.hist(color_values)

plt.show() 
plt.close()
