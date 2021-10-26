#pip install scikit-image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline
from skimage import data,filters

image = mpimg.imread('images\ktp.jpeg')
# image = data.coins()   # ... or any other NumPy array!
plot1 = plt.figure(1)
plt.imshow(image)

plot1 = plt.figure(2)
edges = filters.sobel(image)  
plt.imshow(edges)

plt.show()