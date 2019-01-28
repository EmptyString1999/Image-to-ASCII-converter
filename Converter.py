from __future__ import print_function
from PIL import Image

filename = "bird.jpg"
size = (1200, 100)

im = Image.open(filename).convert('L')
im.resize(size).save("grayscale.png")
im.close()
img = Image.open("grayscale.png")
width, height = img.size

px = img.load()

file = open("Result.txt", "w")
prevX = 0
for x in range(width):
    for y in range(height):
        
        if x > prevX:
            file.write("\n")
            prevX += 1
        else:
            if px[x, y] < 127:
                txt = "0"
            else:
                txt = "1"
            file.write(txt)