# 单绘图区
import matplotlib.pyplot as plt

def example_plot(ax, fontsize=12):
     ax.plot([1, 2])
     ax.locator_params(nbins=3)
     ax.set_xlabel('x-label', fontsize=fontsize)
     ax.set_ylabel('y-label', fontsize=fontsize)
     ax.set_title('Title', fontsize=fontsize)

fig1, ax = plt.subplots()
example_plot(ax,fontsize=40)

fig2, ax = plt.subplots()
example_plot(ax,fontsize=40)
fig2.tight_layout()

plt.show()