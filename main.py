from typing import Any

from PIL import Image, ImageDraw
image = Image.open("1.bmp")
draw = ImageDraw.Draw(image)
pixel = image.load()
width = image.size[0]
height = image.size[1]
maximum = -10
for i in range(width):
    for j in range(height):
        if pixel[i, j][0] + pixel[i, j][1] + pixel[i, j][2] >= maximum:
            maximum = pixel[i, j][0] + pixel[i, j][1] + pixel[i, j][2]
            r = 255 - pixel[i, j][0]
            g = 255 - pixel[i, j][1]
            b = 255 - pixel[i, j][2]
print(r)
print(g)
print(b)
for i in range(width):
    for j in range(height):
        newr = pixel[i, j][0]
        newb = pixel[i, j][1]
        newc = pixel[i, j][2]
        draw.point((i, j), (newr+r, newb+g, newc+b))
image.save("2.bmp")
del draw
