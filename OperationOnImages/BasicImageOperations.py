'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Read,write and display an image
        - Get image properties (color, channels, shape, image structure)
        - Creating new images, accessing pixels and region of interest (ROI)
'''
# import requried libraries
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
# configure matplot lib
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
# import image_utils which contains all required
from image_utils import *

'''
    @main
'''
def main(argv):
    # read simple image and display it
    image_path_zero = "./data/images/number_zero.jpg"
    image_path_musk = "./data/images/musk.jpg"
    image_arr  = read_image(image_path_zero, 0)
    print (image_arr)
    # print image props
    print_image_props(image_arr)
    # display image
    display_image(image_arr)
    # save the image
    save_image(image_arr, "./data/images/test_image.jpg")
    # read color image
    color_image = read_image(image_path_musk)
    # display image
    display_image(color_image)
    # split image
    B, G, R    = split_image(color_image)
    merged_img = merge_channels((B,G,R))
    display_image(B)
    display_image(G)
    display_image(R)
    display_image(merged_img)


if __name__ == '__main__':
    main(sys.argv)
