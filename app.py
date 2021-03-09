#!/usr/bin/env python
import click

from skimage.io import imread
from skimage.color import rgba2rgb, rgb2gray
from skimage.exposure import rescale_intensity
from skimage.transform import downscale_local_mean

ascii_greyscale = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


@click.command()
@click.option('--path', type = str, help='path to the image file.', prompt='path to image')
@click.option('--cols', type = int, default=120, help='width of the ascii art.')
@click.option('--font_scale', type = float, default=0.43, help='the most appropriate scale for your terminal font.')
def generate_ascii(path, cols, font_scale):
    img = imread(path)
    asciimge = image2ascii(img, cols, font_scale)
    print()
    for row in asciimge:
        print(row)
    print()

def pxl2ascii(pxl):
    global ascii_greyscale
    return ascii_greyscale[round(pxl*69)]


def image2ascii(img, cols=240, font_scale=0.43):
    if (img.shape[-1] == 4):
        grey_img = rgb2gray(rgba2rgb(img))
    else:
        grey_img = rgb2gray(img)

    grey_img = rescale_intensity(grey_img)
    h, w = grey_img.shape
    block_width = int(grey_img.shape[1]/cols)
    block_height = int(block_width/font_scale)
    downsampled_img = downscale_local_mean(grey_img, (block_height, block_width))
    h, w = downsampled_img.shape
    asciimg = []
    for i in range(h-1): 
        asciimg.append("")  
        for j in range(w-1): 
            pxl = downsampled_img[i,j]
            asciimg[i] += pxl2ascii(pxl)
    return asciimg



if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    generate_ascii()