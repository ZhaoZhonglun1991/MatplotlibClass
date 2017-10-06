import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

picName= os.path.dirname(os.path.realpath(__file__))+'/1.png'
img=mpimg.imread(picName)
plt.imshow(img)

plt.figure(2)
lum_img = img[:,:,0]
plt.imshow(lum_img)

plt.figure(3)
plt.imshow(lum_img, cmap="hot")

plt.figure(4)
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')

plt.figure(5)
plt.imshow(lum_img)
plt.colorbar()

plt.figure(6)
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

plt.figure(7)
plt.subplot(121)
plt.imshow(lum_img)
plt.title('Before')
plt.colorbar(orientation ='horizontal')
plt.subplot(122)
plt.imshow(lum_img, clim=(0.1, 0.99))
plt.title('After')
plt.colorbar(orientation='horizontal')

from PIL import Image
picName= os.path.dirname(os.path.realpath(__file__))+'/1.jpg'
img = Image.open(picName)
img.thumbnail((64, 64), Image.ANTIALIAS)

plt.figure(8)
plt.imshow(img)

plt.figure(9)
plt.imshow(img, interpolation="nearest")

plt.figure(10)
plt.imshow(img, interpolation="bicubic")

plt.show()