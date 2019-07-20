'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Add an atrifact to an image

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
    # display rgb glasses and its alpha channel
    display_image(image_glasses_a)
    display_image(image_glasses_bgr)
    # make a naive copy to musk image
    image_musk_naive     = image_musk.copy()
    image_musk_naive[150:250,140:440] = image_glasses_bgr
    # display the naive approach
    display_image(image_musk_naive)
    # merge mask to make a 3 channel image
    image_glasses_a_3    = merge_channels((image_glasses_a,image_glasses_a,image_glasses_a))
    # Make the values [0,1] since we are using arithmetic operations
    image_glasses_a_3    = np.uint8(image_glasses_a_3/255)
    # make an arithmetic copy to musk image
    image_musk_arith     = image_musk.copy()
    # get eye region
    eye_region           = image_musk_arith[150:250,140:440]
    # masked_eye will be black around the glasses and musk everywhere else
    masked_eye           = cv2.multiply(eye_region, 1 - image_glasses_a_3 )
    # masked glass will be black in areas outside of the sunglass and will have
    # the sunglass RGB image in the region of interest
    masked_glass         = cv2.multiply(image_glasses_bgr, image_glasses_a_3)
    # now lets add the masked eye and masked glass
    image_musk_arith[150:250,140:440]     = cv2.add(masked_eye, masked_glass)
    # display the maskes and final picture
    display_image(eye_region)
    display_image(masked_eye)
    display_image(masked_glass)
    display_image(image_musk_arith)



if __name__ == '__main__':
    main(sys.argv)
