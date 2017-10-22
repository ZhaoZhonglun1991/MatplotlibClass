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

np.random.seed(19680801)

X = np.linspace(0.5, 8, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))

fn=os.path.dirname(os.path.realpath(__file__))+'/picture.png'
bgimg = img.imread(fn)

def plota(ax,facecolor='None'):
    ax.grid(linestyle="--", linewidth=0.5, color='w', zorder=-10)
    ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
    ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
    ax.plot(X, Y3, linewidth=0,
            marker='o', markerfacecolor='w', markeredgecolor='k')
    ax.set_facecolor(facecolor)

fig = plt.figure(1)
fig.figimage(bgimg)
ax = fig.add_subplot(111)
plota(ax, 'k')
ax.set_title("ax.set_facecolor('k')",size=20,color='w')

fig = plt.figure(2)
fig.figimage(bgimg)
ax = fig.add_subplot(111)
plota(ax, 'None')
ax.set_title("ax.set_facecolor('None')",size=20,color='w')

fig = plt.figure(3)
fig.figimage(bgimg)
ax = fig.add_subplot(111)
plota(ax, 'k')
ax.set_frame_on(True)
ax.set_title('ax.set_frame_on(True)',size=20,color='w')

fig = plt.figure(4)
fig.figimage(bgimg)
ax = fig.add_subplot(111)
plota(ax, 'k')
ax.set_frame_on(False)
ax.set_title('ax.set_frame_on(False)',size=20,color='w')

fig = plt.figure(5)
fig.figimage(bgimg)
ax = fig.add_subplot(111)
plota(ax)
ax.axis([2,7,1,3])
ax.set_title('ax.axis([2,7,1,3])',size=20,color='w')

fig = plt.figure(6)
fig.figimage(bgimg)
ax = fig.add_subplot(121)
plota(ax)
ax.axis('on')
ax.set_title("ax.axis('on')",size=20,color='w')
ax = fig.add_subplot(122)
plota(ax)
ax.axis('off')
ax.set_title("ax.axis('off')",size=20,color='w')

fig = plt.figure(7)
fig.figimage(bgimg)
fig.subplots_adjust(left=0.05, right=0.98, wspace=0.15)
ax=fig.add_subplot(241)
plota(ax)
ax.axis('off')
ax.set_title('off',color='w')
ax=fig.add_subplot(242)
plota(ax)
ax.axis('equal')
ax.set_title('equal',color='w')
ax=fig.add_subplot(243)
plota(ax)
ax.axis('scaled')
ax.set_title('scaled',color='w')
ax=fig.add_subplot(244)
plota(ax)
ax.axis('tight')
ax.set_title('tight',color='w')
ax=fig.add_subplot(245)
plota(ax)
ax.axis('auto')
ax.set_title('auto',color='w')
ax=fig.add_subplot(246)
plota(ax)
ax.axis('normal')
ax.set_title('normal',color='w')
ax=fig.add_subplot(247)
plota(ax)
ax.axis('image')
ax.set_title('image',color='w')
ax=fig.add_subplot(248)
plota(ax)
ax.axis('square')
ax.set_title('square',color='w')

fig = plt.figure(8)
fig.figimage(bgimg)
ax = fig.add_subplot(121)
plota(ax)
ax.set_axis_on()
ax.set_title('ax.set_axis_on()',size=20,color='w')
ax = fig.add_subplot(122)
plota(ax)
ax.set_axis_off()
ax.set_title('ax.set_axis_off()',size=20,color='w')

fig = plt.figure(9)
fig.figimage(bgimg)
ax = fig.add_subplot(121)
plota(ax)
ax.grid(linewidth=2)
ax.set_axisbelow(True)
ax.set_title("ax.set_axisbelow(True)",size=20,color='w')
ax = fig.add_subplot(122)
plota(ax)
ax.grid(linewidth=2)
ax.set_axisbelow(False)
ax.set_title("ax.set_axisbelow(False)",size=20,color='w')

plt.show()