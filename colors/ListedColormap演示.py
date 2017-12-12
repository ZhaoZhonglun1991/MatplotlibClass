
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
c = np.random.randn(N)
area = np.pi * (15 * np.random.rand(N))**2
cmap = colors.ListedColormap(['#5fd9cd','#eaf786','#ffb5a1','#b8ffb8','#b8f4ff'])
plt.scatter(x, y, s=area, c=c, cmap=cmap, alpha=0.5)
plt.colorbar()
plt.show()

