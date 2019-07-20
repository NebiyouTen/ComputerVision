'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Copying and creating new images
        - Cropping an image section
        - Resizing an Image
        - Creating binary masks for images

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
    image_path_boy = "./data/images/boy.jpg"
    image_boy      = read_image(image_path_boy)
    # display cropped image
    display_image(crop_image(image_boy,40, 200, 170, 320))
    # scale image by providing hXw and then display
    display_image(resize_image(image_boy, size= (300, 200), interp = cv2.INTER_LINEAR))
    # scale image by scaling factor and then display
    display_image(resize_image(image_boy, scale_h= 0.6, scale_w = 0.6, interp = cv2.INTER_LINEAR))


if __name__ == '__main__':
    main(sys.argv)
