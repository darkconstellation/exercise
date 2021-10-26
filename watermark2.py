# importing the library
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# read image
file = 'C:\MDT\images\ktp.jpeg'
image=Image.open(file)
image.show()
plt.imshow(image)
