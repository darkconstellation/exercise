from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
text = input('Masukkan Text: ')
warna = input('Warna Text: ')
font_name = input('Font apa (1,2,3): ')

im = Image.open('ktp.jpeg')

img_width, img_height = im.size  # Get resolution of image in pixel
print('lebar x panjang foto: %s x %s' %(img_width, img_height))

draw = ImageDraw.Draw(im)  #Prepare canvas for adding text

# if-then-else untuk memilih font
font_used = ''
if font_name == '1':
    font_used == 'arial.ttf'
elif font_name == '2':
    font_used == 'Fruktur-Regular.ttf'
elif font_name == '3':
    font_used == 'ZenKurenaido-Regular.ttf'

font = ImageFont.truetype('Fruktur-Regular.ttf', 36)  # Init object text
text_width, text_height = draw.textsize(text, font)

# if-then-else untuk memilih warna #RGBA 0-255
if warna == 'merah':
    warna_text = (255,0,0,60)
elif warna == 'biru':
    warna_text = (0,0,255,60)
elif warna == 'hijau':
    warna_text = (0,255,0,60)
else:
    warna_text = (255,255,255,60)

# loop sebanyak 10x text yg di-inginkan
jumlah_text = 10
img_height_index = text_height - (text_height //2) 
img_height_avg = img_height//jumlah_text
for i in range(jumlah_text):    # 0-9
    x = (img_width//2) - (text_width//2)        # ini untuk horizontal
    y = img_height_index - (text_height //2)    # ini untuk vertical
    draw.text((x, y), text, font=font, fill=warna_text) 
    img_height_index = img_height_index+img_height_avg    
im.show()

#Save watermarked image
im.save('ktp_watermark.jpg')

