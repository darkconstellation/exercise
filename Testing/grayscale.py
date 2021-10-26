#pip install Pillow
import os,sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import imageio
import matplotlib.image as mpimg


def gray_pil(file):
    img=np.array(Image.open(file)) #Input - Color image
    gray_img=img.copy()
    for clr in range(img.shape[2]):
        gray_img[:,:,clr]=img.mean(axis=2) #Take mean of all 3 color channels of each pixel and assign it back to that pixel(in copied image)
    return gray_img

def gray_numpy1(file):
    pic = imageio.imread(file)
    gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
    gray = gray(pic)  
    return gray
    # plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))

def gray_numpy(file):
    img = mpimg.imread(file)   
    # img = imageio.imread(file)
    # print(img.shape[0])
    grayImage = np.zeros(img.shape)
    
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    R = (R *.299)
    G = (G *.587)
    B = (B *.114)

    # R = (R *.333)
    # G = (G *.333)
    # B = (B *.333)
    

    Avg = (R+G+B)
    # print(Avg)
    grayImage = img.copy()

    for i in range(3):
        grayImage[:,:,i] = Avg
        
    return grayImage      

def sephia_numpy(file):
    img = mpimg.imread(file)   
    # img = imageio.imread(file)
    # print(img.shape[0])
    sepia_img = np.zeros(img.shape)
    
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    # R = (R *.299)
    # G = (G *.587)
    # B = (B *.114)

    # sepia_filter = np.array([[.393, .769, .189], [.349, .686, .168], [.272, .534, .131]])
    # sepia_img = img.dot(sepia_filter.T)
    # sepia_img /= sepia_img.max()



    sepia_r = .393*R + .769*G + .189*B
    sepia_g = .349*R + .686*G + .168*B
    sepia_b = .272*R + .534*G + .131*B

    # Avg = (sepia_r * sepia_g * sepia_b)
    # print(Avg)
    sepia_img = img.copy()
    
    sepia_img[:,:,0] = sepia_r
    sepia_img[:,:,1] = sepia_g
    sepia_img[:,:,2] = sepia_b
    
    # for i in range(3):
    #     sepia_img[:,:,i] = Avg
        
    return sepia_img          

if __name__ == "__main__":    
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    python_file_path = os.path.dirname(os.path.realpath(__file__))
    
    # file = input('Masukkan file gambar: ')
    file = 'tiger.jpg'
    file = os.path.join(python_file_path,'images',file)
    
    if "-gray_pil" in opts:
        plt.figure('Original')
        image_original = Image.open(file)
        plt.imshow(image_original)
        
        image1 = gray_pil(file)
        plt.figure('After Processing')
        plt.imshow(image1)
        plt.show()

    elif "-gray_numpy" in opts:
        plt.figure('Original')
        image_original = Image.open(file)
        plt.imshow(image_original)
        
        image1 = gray_numpy(file)
        plt.figure('After Processing 1')
        plt.imshow(image1)

        image2 = sephia_numpy(file)
        plt.figure('After Processing 2')
        plt.imshow(image2)

        plt.show()