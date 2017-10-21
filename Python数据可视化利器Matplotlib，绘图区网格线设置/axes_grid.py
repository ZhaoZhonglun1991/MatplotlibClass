import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.image as img
import os

mpl.rcParams['ytick.color']='white'
mpl.rcParams['xtick.color']='white'
mpl.rcParams['ytick.labelsize']='large'
mpl.rcParams['xtick.labelsize']='large'
mpl.rcParams['axes.edgecolor']='white'

fn=os.path.dirname(os.path.realpath(__file__))+'/picture.png'
bgimg = img.imread(fn)

np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))


def plota(fig):
    fig.figimage(bgimg)
    ax = fig.add_subplot(111)
    ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
    ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
    ax.plot(X, Y3, linewidth=0,
            marker='o', markerfacecolor='w', markeredgecolor='k')
    ax.set_facecolor('None')
    ax.xaxis.set_major_locator(ticker.IndexLocator(0.4,-0.1))
    ax.xaxis.set_minor_locator(ticker.IndexLocator(0.2,-0.1))
    return ax

fig1= plt.figure(1)
ax= plota(fig1)
ax.grid(True)
ax.set_title("ax.grid(True)",size=20,color='w')

fig2= plt.figure(2)
ax= plota(fig2)
ax.grid(False)
ax.set_title("ax.grid(False)",size=20,color='w')

fig3= plt.figure(3)
ax= plota(fig3)
ax.grid(alpha= 0.5)
ax.set_title("ax.grid(alpha= 0.5)",size=20,color='w')

fig4= plt.figure(4)
ax= plota(fig4)
ax.grid(which='major')
ax.set_title("ax.grid(which='major')",size=20,color='w')

fig5= plt.figure(5)
ax= plota(fig5)
ax.grid(which='minor')
ax.set_title("ax.grid(which='minor')",size=20,color='w')

fig6= plt.figure(6)
ax= plota(fig6)
ax.grid(which='both')
ax.set_title("ax.grid(which='both')",size=20,color='w')

fig7= plt.figure(7)
ax= plota(fig7)
ax.grid(axis='both')
ax.set_title("ax.grid(axis='both')",size=20,color='w')

fig8= plt.figure(8)
ax= plota(fig8)
ax.grid(axis='x')
ax.set_title("ax.grid(axis='x')",size=20,color='w')

fig9= plt.figure(9)
ax= plota(fig9)
ax.grid(axis='y')
ax.set_title("ax.grid(axis='y')",size=20,color='w')

fig10= plt.figure(10)
ax= plota(fig10)
ax.grid(color='skyblue')
ax.set_title("ax.grid(color='skyblue')",size=20,color='w')

fig11= plt.figure(11)
ax= plota(fig11)
ax.grid(linestyle='--')
ax.set_title("ax.grid(linestyle='--')",size=20,color='w')

fig12= plt.figure(12)
ax= plota(fig12)
ax.grid(linewidth=2)
ax.set_title("ax.grid(linewidth=2)",size=20,color='w')
plt.show()