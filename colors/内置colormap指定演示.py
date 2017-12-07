
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.randn(N)
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, cmap='Accent', alpha=0.5)
plt.colorbar()
plt.show()

