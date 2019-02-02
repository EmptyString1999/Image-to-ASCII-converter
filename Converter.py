from __future__ import print_function
from PIL import Image

filename = input("Enter file name including extension: ")
w = input("Enter width of final image: ")
h = input("Enter height of final image: ")
size = (int(w), int(h))

im = Image.open(filename).convert('L')
im.rotate(270, expand=True).transpose(Image.FLIP_LEFT_RIGHT).resize(size[::-1]).save("grayscale.png")
im.close()

img = Image.open("grayscale.png")
width, height = img.size




px = img.load()

# binary mode 1s & 0s

# file = open("Result.txt", "w")
# prevX = 0
# for x in range(width):
#     for y in range(height):
        
#         if x > prevX:
#             file.write("\n")
#             prevX += 1
#         else:
#             if px[x, y] < 127:
#                 txt = "0"
#             else:
#                 txt = "1"
#             file.write(txt)



# Attempt at ASCII mode

file = open("Result.txt", "w")
prevX = 0
for x in range(width):
    for y in range(height):

        if x > prevX:
            file.write("\n")
            prevX += 1
        else:
            if px[x, y] < 255 and px[x, y] > 225:
                txt = '='
            elif px[x, y] < 225 and px[x, y] > 195:
                txt = ':'
            elif px[x, y] < 195 and px[x, y] > 165:
                txt = ';'
            elif px[x, y] < 165 and px[x, y] > 105:
                txt = '+'
            elif px[x, y] < 105 and px[x, y] > 75:
                txt = '$'
            elif px[x, y] < 75 and px[x, y] > 45:
                txt = '@'
            elif px[x, y] < 45 and px[x, y] >= 0:
                txt = '#'
            file.write(txt)
