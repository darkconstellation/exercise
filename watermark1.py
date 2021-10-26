from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt


file = 'C:\MDT\images\ktp.jpeg'

image = Image.open(file)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 50)
draw.text((0, 0), "puppy", (0, 0, 0), font=font)
image.show()
# plt.imshow(image)
plt.show()

