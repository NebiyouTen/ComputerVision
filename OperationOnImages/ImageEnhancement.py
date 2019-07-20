'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Contrat Enhancement
        - Brightness Enhancement

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
    image_path_boy      = "./data/images/boy.jpg"
    image_boy           = read_image(image_path_boy)
    # enhance contrast
    enhanced_contrast   = enhance_contrast(image_boy, 1.3)
    # enhance brightness
    enhanced_brightness = enhance_brightness(image_boy, 50)
    # display images
    display_image(image_boy)
    # display_image(enhanced_contrast)
    display_image(enhanced_brightness)
    brightnessOffset = 50
    brightHighInt32 = np.int32(image_boy)+brightnessOffset
    brightHighInt32Clipped = np.clip(brightHighInt32,0,255)
    print (type(brightHighInt32Clipped))
    cv2.imshow("Int32 Clipped",brightHighInt32Clipped.astype(np.uint8))
    cv2.waitKey()
    cv2.destroyAllWindows()

    print (image_boy[0,0], enhanced_brightness[0,0])

if __name__ == '__main__':
    main(sys.argv)
