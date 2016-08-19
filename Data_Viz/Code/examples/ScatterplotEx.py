import matplotlib.pyplot as plt

csfont = {'fontname' : 'Comic Sans MS'}
timeOnSubway= [15,50,0,35,26,18]
instaLikes= [8,22,5,16,18,5]
#x, y, color, marker, size of the marker
plt.scatter(timeOnSubway,instaLikes, color='#FF0000', marker='*', s=150)
# label, font
plt.xlabel('Time (minutes)', **csfont) #syntax for including cs font
plt.ylabel('Instagram Photos Liked', **csfont)
# label, size, font
plt.title('Does Commute Time Influence Social Media Engagement?', fontsize=20, **csfont)
# which sets appearance parameters for ticks and ticklabels- can be "major", "minor", "both"
plt.grid(which='major', color='pink',linestyle=':')
plt.show()
plt.close()

'''
(saved as simpleScatter.py) 
Documentation on style http://www.mathworks.com/help/matlab/ref/plot.html?requestedDomain=www.mathworks.com
'''