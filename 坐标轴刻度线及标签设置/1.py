import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as img
import os

mpl.rcParams['ytick.color']='white'
mpl.rcParams['xtick.color']='white'
mpl.rcParams['ytick.labelsize']='large'
mpl.rcParams['xtick.labelsize']='large'
mpl.rcParams['axes.edgecolor']='white'

x = np.arange(0.0, 2*np.pi, np.pi/100)
y = np.sin(x)
 
fig = plt.figure(figsize=(16, 8))
fn=os.path.dirname(os.path.realpath(__file__))+'/picture.png'
bgimg = img.imread(fn)
fig.figimage(bgimg)

ax = fig.add_subplot(111)
ax.set_facecolor('None')
ax.plot(x, y,'w')
ax.set_xticks([0,np.pi/2,np.pi,2*np.pi])
ax.set_xticks([np.pi/4,3*np.pi/4],minor=True)
ax.set_xticklabels(['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$2\pi$'])
ax.set_xticklabels([r'$\frac{\pi}{4}$',r'$\frac{3\pi}{4}$'],minor=True)
plt.show()
