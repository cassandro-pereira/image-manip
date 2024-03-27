#Demo for Image manipulation using Pillow
from PIL import Image

width = 500
height = 500

image = Image.new (mode = "RGB", size = (width, height), color = (1, 1, 100))

#Adding pixel to split the image generated
for x in range (height):
    image.putpixel((x ,x), (255, 255, 255, 240))

image.save("manipulated1.png")

image.show()