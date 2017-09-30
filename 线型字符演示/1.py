import matplotlib.pyplot as plt
import numpy as np

markers=['-','--','-.',':','.','o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']
yticklabels=['"'+a+'"' for a in markers]
points=np.ones(6)

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.1,right=0.95,top=0.95,bottom=0.05)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

for y, marker in enumerate(markers):    
    ax.plot(y * points,'b'+marker,markersize=10)

ax.set_yticks(np.arange(0,len(markers)))
ax.set_yticklabels(yticklabels,size=15)
plt.show()