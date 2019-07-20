'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Bitwise AND, OR, NOT and NOR operations

'''
# import requried libraries
import sys
import cv2
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
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
    image_path_musk      = "./data/images/musk.jpg"
    image_path_glasses   = "./data/images/sunglass.png"
    image_musk           = read_image(image_path_musk)
    # -1 flag indicates that we read the image as it is. As this image has
    # an additional alpha channel
    image_glasses        = read_image(image_path_glasses, -1)
    # Resize the image to fit over the eye region
    image_glasses        = resize_image(image_glasses, size= (300,100), interp = cv2.INTER_LINEAR)
    # get glasses BGR data
    image_glasses_bgr    = image_glasses[:,:,:3]
    # get glasses alpha data. This will be a while image for regions inside the
    # glass and black else where.
    image_glasses_a      = image_glasses[:,:,3]
    # get eye region
    eye_region           = image_musk[150:250,140:440]
    # merge mask to make a 3 channel image
    image_glasses_a_3    = merge_channels((image_glasses_a,image_glasses_a,image_glasses_a))
    # get musk eye image wth regions inside the glassses as black
    musk_eye             = cv2.bitwise_and(eye_region, cv2.bitwise_not(image_glasses_a_3))
    # get boundary less glasses image
    glass_boundary_less  = cv2.bitwise_and(image_glasses_bgr, image_glasses_a_3)
    # final image
    musk_final           = cv2.bitwise_or(musk_eye, glass_boundary_less)
    display_image(musk_final)


if __name__ == '__main__':
    main(sys.argv)
