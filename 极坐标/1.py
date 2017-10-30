import matplotlib.pyplot as plt
import numpy as np
import math

theta=np.arange(0,2*np.pi,0.02)

def creatAx(fig):
    ax1= fig.add_subplot(121, projection='polar')
    ax2= fig.add_subplot(122, projection='polar')
    ax1.plot(theta,theta/6,'--',lw=2)
    ax2.plot(theta,theta/6,'--',lw=2)    
    return ax1,ax2

fig = plt.figure(1)    
ax1 = fig.add_subplot(121, projection='polar')
ax2 = fig.add_subplot(122)
ax1.plot(theta,theta/6,'--',lw=2)
ax2.plot(theta,theta/6,'--',lw=2)

fig = plt.figure(2)
ax1,ax2= creatAx(fig)
ax2.set_theta_direction(-1)

fig = plt.figure(3)
ax1,ax2= creatAx(fig)
ax2.set_theta_zero_location('N')

fig = plt.figure(4)
ax1,ax2= creatAx(fig)
ax2.set_thetagrids(np.arange(0.0, 360.0, 30.0))

fig = plt.figure(5)
ax1,ax2= creatAx(fig)
ax2.set_theta_offset(np.pi)

fig = plt.figure(6)
ax1,ax2= creatAx(fig)
ax2.set_rgrids(np.arange(0.2,1.0,0.4))

fig = plt.figure(7)
ax1,ax2= creatAx(fig)
ax2.set_rlabel_position('90')

fig = plt.figure(8)
ax1,ax2= creatAx(fig)
ax2.set_rlim(0.6,1.2)

fig = plt.figure(9)
ax1,ax2= creatAx(fig)
ax2.set_rmax(0.6)

fig = plt.figure(10)
ax1,ax2= creatAx(fig)
ax2.set_rmin(0.6)

fig = plt.figure(11)
ax1,ax2= creatAx(fig)
ax2.set_rlim(math.pow(10,-1),math.pow(10,0))
ax1.set_rscale('linear')
ax2.set_rscale('symlog')

fig = plt.figure(12)
ax1,ax2= creatAx(fig)
ax2.set_rticks(np.arange(0.1, 0.9, 0.2))

plt.show()



