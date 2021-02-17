import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

img = Image.open('lena.jpg')
gray = np.mean(img, axis=2)
x = np.linspace(-6,6,60)
fx = norm.pdf(x , loc = 0, scale = 1)

filt = np.outer(fx, fx)

out = convolve2d(gray, filt)

plt.subplot(1,2,1)
plt.imshow(gray, cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(out, cmap = 'gray')
plt.show()
#, plt.imshow(gray)
# plt.show()