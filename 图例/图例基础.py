import numpy as np
import matplotlib.pyplot as plt

fig= plt.figure()
ax = fig.add_subplot(111)

t = np.arange(0., 5., 0.2)

## 方法一
# ax.plot(t, t, t, t**2, t, t**3)
# ax.legend(['A simple line','Square line','Cube line'])

## 方法二
# ax.plot(t, t)
# ax.plot(t, t**2)
# ax.plot(t, t**3)
# ax.legend(['A simple line','Square line','Cube line'])

## 方法三
# ax.plot(t, t, label='A simple line')
# ax.plot(t, t**2, label='Square line')
# ax.plot(t, t**3, label='Cube line')
# ax.legend()

## 方法四
# line1,= ax.plot(t, t)
# line1.set_label('A simple line')
# line2,= ax.plot(t, t**2)
# line2.set_label('Square line')
# line3,= ax.plot(t, t**3)
# line3.set_label('Cube line')
# ax.legend()

## 方法五
# line1,= ax.plot(t, t)
# line2,= ax.plot(t, t**2)
# line3,= ax.plot(t, t**3)
# ax.legend([line1,line2,line3][::-1],
#     ['A simple line','Square line','Cube line'][::-1])

plt.show()