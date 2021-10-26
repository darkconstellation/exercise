import os,sys
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def contrast(image, contrast_factor):
    enhancer = ImageEnhance.Contrast(image)
    image_result = enhancer.enhance(contrast_factor)
    return image_result

def contrast(image, bright_factor):
    enhancer = ImageEnhance.Brightness(image)
    image_result = enhancer.enhance(bright_factor)
    return image_result    


if __name__ == "__main__":    
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    python_file_path = os.path.dirname(os.path.realpath(__file__))
    file = 'C:\MDT\images\ktp.jpeg'

    if "-contrast" in opts:
        image_original = Image.open(file)
        plt.figure('Original')
        plt.imshow(image_original, cmap='gray')
        
        image1 = contrast(image_original, 1.5)
        plt.figure('After Contrast')
        plt.imshow(image1, cmap='gray')

        image2 = contrast(image1, 1.5)
        plt.figure('After Brightness')
        plt.imshow(image2, cmap='gray')
        plt.show()