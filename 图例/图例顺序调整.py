import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
fig, axes = plt.subplots(1,2)
for i in range(0,5):
    axes[0].plot(t,t**i,label='line'+str(i))
    axes[1].plot(t,t**i,label='line'+str(i))

axes[0].legend()
handles, labels = axes[1].get_legend_handles_labels()
axes[1].legend(handles[::-1], labels[::-1])

plt.show()

