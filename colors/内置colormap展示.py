import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import cmap_d

cmap1 = sorted([i for i in cmap_d if i[-2:]!='_r'])
cmap2 = sorted([i for i in cmap_d if i[-2:]=='_r'])

nrows = max(len(cmap1),len(cmap2))
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

fig, axes = plt.subplots(figsize=(8,16),nrows=nrows,ncols=2)
fig.subplots_adjust(top=0.98, bottom=0.01, left=0.13, right=0.99,wspace=0.4)

def plot(ax,cmap):
    ax.imshow(gradient, aspect='auto', cmap=cmap)
    pos = list(ax.get_position().bounds)
    x_text = pos[0] - 0.01
    y_text = pos[1] + pos[3]/2.
    fig.text(x_text, y_text, cmap, va='center', ha='right', fontsize=10)
    ax.set_axis_off()    

for row, ax in enumerate(axes):
    plot(ax[0],cmap1[row])
    plot(ax[1],cmap2[row])

plt.show()
