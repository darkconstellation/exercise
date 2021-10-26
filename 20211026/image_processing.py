#Import required Image library
#OOP --> Object oriented Programming (class)
from PIL import Image, ImageDraw, ImageFont


#Create an Image Object from an Image
im = Image.open('ktp.jpeg')

width, height = im.size  # Get resolution of image in pixel
print('lebar x panjang foto: %s x %s' %(width, height))

draw = ImageDraw.Draw(im)  #Prepare canvas for adding text
text = "KTP ini milik Hariyadi\nDigunakan untuk belajar"  #Assign variable text as string with value "sample water"

font = ImageFont.truetype('arial.ttf', 36)  # Init object text

textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font, fill=(255,0,0,60)) #RGBA 0-255
im.show()

# #Save watermarked image
im.save('ktp_watermark.jpg')