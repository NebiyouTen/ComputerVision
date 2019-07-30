'''
    Author: Nebiyou Yismaw

    This is a python code that will explore the use of trackbars as controllers

'''
# import requried libraries
import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# maximum scale for the trackbar scaler
maxScaleUp = 100
# scaling factor
scaleFactor = 1
# scaling type
scaleType = 0
# maximum type
maxType = 1
# load an image
im = cv2.imread("truth.png")
# window name for image resizing
windowName = "Resize Image"
#
SCALE_FACTOR_TRACK_BAR = "scale_factor_track_bar"
SCALE_TYPE_TRACK_BAR   = "scale_type_track_bar"
MIN_SCALE_TRESH        = 1e-1

'''
    A function to get scaling factor by taking type into consideration
'''
def get_scaling_factor (factor, type ):
    if type == 0:
        # if type is scale up, return a scale factor greater than one
        return 1 + factor / 100.0
    else:
        # if type is scale down, return a scale factor less than one
        # set the minimum treshold scale to 0.1
        return max(1 - factor / 100.0, MIN_SCALE_TRESH)

'''
    A Callback function for the trackbars
'''
def scaleImage(val, type):
    global scaleFactor
    global scaleType
    # check if value is form the type or factor trackbar, and then assign
    # the correct value 
    if type == SCALE_TYPE_TRACK_BAR:
        scaleType   = val
    else:
        scaleFactor = get_scaling_factor(val, scaleType)
    scaledImage = cv2.resize(im, None, fx=scaleFactor,
                             fy=scaleFactor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


'''
    @main
'''
def main(argv):
    # track bar name for scaling
    trackbarValue = "Scale"
    # track bar name for scale type
    trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

    # Create a window to display results, note the autoresize flag
    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
    # Create trackbars and assign a callback
    # We can similar callback, and use the help of a lambda experssion to
    # pass the type of trackbar, since in our callback we need to differenciate
    # between values from our two callbakcs
    cv2.createTrackbar(trackbarValue, windowName,
                       scaleFactor, maxScaleUp, lambda x: scaleImage(x, SCALE_FACTOR_TRACK_BAR))
    cv2.createTrackbar(trackbarType, windowName,
                       scaleType, maxType, lambda x: scaleImage(x, SCALE_TYPE_TRACK_BAR))
    # initial call to scaling function
    scaleImage(25, SCALE_FACTOR_TRACK_BAR)
    while True:
        c = cv2.waitKey(20)
        # exit if esc is pressed, exit
        if c == 27:
            break
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
