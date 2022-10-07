from PIL import Image
import numpy as np
from math import sin, cos
from math import radians

def great_replacer(i, color = (255, 255, 255, 255)):
    data = np.array(i)
    data[(data == color).all(axis = -1)] = (0,0,0,0)
    return Image.fromarray(data, mode='RGBA')

single = great_replacer(Image.open("single.png").convert('RGBA'))
single = single.resize((int(single.width/2), int(single.height/2)))
zero = Image.open("zero.png").convert('RGBA')

canvas = Image.new("RGBA", (zero.width*2, zero.height*2))

for deg in range(0, 360*2, 10):
    r = 70 + (deg/4)

    modx = int(cos(radians(deg))*r)
    mody = -1*int(sin(radians(deg))*r)

    print(modx, mody)
    rsingle = single.rotate(270+deg)

    canvas.paste(rsingle, box=(118+modx+int(zero.width/2)-int(rsingle.width/2), 84+mody+int(zero.height/2)-int(rsingle.height/2)), mask=rsingle)

canvas.paste(zero, (114, 104), mask=zero)

canvas.show()