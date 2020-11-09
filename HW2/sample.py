# object representation

from PIL import Image, ImageDraw
import math
import csv
import array as arr




img = Image.new('RGB', (600, 600))

# this list hold all vertices
# you can use append() to add all x, y, z
# into it. the format could be like this:
# [[x1, y1, z1], [x2, y2, z2],......]
vertices = []


#read in face vertices
with open('face-vertices.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:    
        print float(row[0]), float(row[1]), float(row[2])
    
    for index in csv_reader:
        #a = float((index[0]*0)+(index[1]*0) + (index[2] * 1))
        #b = float((index[0]*0)+(index[1]*1) + (index[2] * 0))
        c = [index[2],index[1]]
        vertices.append(c)
    
    print vertices[0]

    #for index in vertices:
       # print vertices
    
pixels = img.load()
def draw_pixel(x,y, color):
    pixels[x,y] = (color,0,0)

#read index
with open('face-index.txt') as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0

    for index in reader:
        #print int(index[0]), int(index[1]), int(index[2])


        draw = ImageDraw.Draw(img)
        #draw.point((a,b),(0,255,0))
        draw.line((0,0,200,200), fill=255)

    for index in vertices:
        draw.point((vertices[0]),(0,255,0))
img.show()
