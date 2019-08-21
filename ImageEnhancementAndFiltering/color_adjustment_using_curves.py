'''
    Author: Nebiyou Yismaw

    This is a python code that uses opencv to perform color adjustments using
    different curves

'''
# import requried libraries
import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


def main(argv):
    '''
        @main
    '''
    # let's read the girl image and make a copy
    filename = "girl.jpg"
    original = cv2.imread(filename)
    img = np.copy(original)
    '''
        We are using a piece-wise curve to modify color values. These curve will
        be define in a given set of points and interpolation will be used to
        fit the values for the others.
    '''
    # pivot points to define the piece wise function (curve function x values)
    originalValue = np.array([0, 50, 100, 150, 200, 255])
    # The new points (curve function y- values ) or r and b channel
    rCurve = np.array([0, 80, 150, 190, 220, 255])
    bCurve = np.array([0, 20,  40,  75, 150, 255])
    # Create a LookUp Table
    # This look up table will define the corresponding relation between pixel
    # and transformed pixel vaules for the range [0,255]
    fullRange = np.arange(0,256)
    rLUT = np.interp(fullRange, originalValue, rCurve )
    bLUT = np.interp(fullRange, originalValue, bCurve )
    # Get the blue channel and apply the mapping
    bChannel = img[:,:,0]
    bChannel = cv2.LUT(bChannel, bLUT)
    img[:,:,0] = bChannel
    # Get the red channel and apply the mapping
    rChannel = img[:,:,2]
    rChannel = cv2.LUT(rChannel, rLUT)
    img[:,:,2] = rChannel
    # show and save the ouput
    combined = np.hstack([original,img])
    plt.imshow(combined[:,:,::-1])
    plt.title("Warming filter output")
    plt.show()
    '''
        Note different curves can be used to get different results 
    '''



if __name__ == '__main__':
    main(sys.argv)
