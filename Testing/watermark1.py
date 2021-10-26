from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt


file = 'images\ktp.jpeg'

image = Image.open(file)
p, l = image.size
print('Resolusi gambar: %s x %s '%(p, l) )
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 50)
draw.text((p // 2 , l // 1.2), "Watermark\nTesting", (128, 128, 128), font=font)
image.show()
# plt.imshow(image)
plt.show()

