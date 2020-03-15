#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import os
import time

import numpy


def create_image(width=1920, height=1080, num_of_images=100):
    width = int(width)
    height = int(height)
    num_of_images = int(num_of_images)

    current = time.strftime("%Y%m%d%H%M%S")
    os.mkdir(current)

    for n in range(num_of_images):
        filename = '{0}/{0}_{1:03d}.jpg'.format(current, n)
        rgb_array = numpy.random.rand(height, width, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
        image.save(filename)

def text_on_img(text="Hello", size=12):
    current = time.strftime("%Y%m%d%H%M%S")
    os.mkdir(current)
    filename = '{0}/{0}_{1:03d}.jpg'.format(current, 1)
    "Draw a text on an Image, saves it, show it"
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', size)
    # create image
    image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = "red")
    draw = ImageDraw.Draw(image)
    # draw text
    draw.text((10,10), text, font=fnt, fill=(255,255,0))
    # save file
    image.save(filename)
    # show file
    #os.system(filename)

def main(args):
    #create_image(width=args[0], height=args[1], num_of_images=args[2])
    text_on_img(text=args[0], size=100)
    return 0


if __name__ == '__main__':
    import sys

    status = main(sys.argv[1:])
    sys.exit(status)
