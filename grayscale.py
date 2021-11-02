import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def grayscale_use_pil():
    img=np.array(Image.open('ktp.jpeg')) #Input - Color image
    gray_img=img.copy()
    for clr in range(img.shape[2]):
        gray_img[:,:,clr]=img.mean(axis=2) #Take mean of all 3 color channels of each pixel and assign it back to that pixel(in copied image)
    # gray_img.imshow()

    plt.figure('After Processing')
    plt.imshow(gray_img)
    plt.show()

# grayscale_use_pil()