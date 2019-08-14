'''
    Author: Nebiyou Yismaw

    This is a python code read an RGB image, just to show the RGB color space

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


'''
    @main
'''
def main(argv):
    # read the RGB image
    rgb_image = cv2.imread("capsicum.jpg")
    cv2.imshow("RGB image ",rgb_image)
    cv2.waitKey()
    # now let's split the channels and view all of them
    b, g, r = cv2.split(rgb_image)
    cv2.imshow("R-channel ",r)
    cv2.waitKey()
    cv2.imshow("G-channel ",g)
    cv2.waitKey()
    cv2.imshow("B-channel",b)
    cv2.waitKey()

    '''
        Looking at the channel image, we can see the intensity of each color in
        each channel. All the three channels have brightness and color information.
        Color component is knows as Chrominance, brightness info is known as
        Luminance. Other color space might have these inforation in a separate
        channels.
    '''


if __name__ == '__main__':
    main(sys.argv)
