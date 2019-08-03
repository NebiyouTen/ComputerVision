'''
    Author: Nebiyou Yismaw

    This is a python code that uses openCV to do opening and closing on an image

'''
# imports
import matplotlib
import cv2
import time
import numpy as np
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

'''
    @main
'''


def main(argv):
    # Read the input image to do opening and closing operations
    img_to_open = cv2.imread("opening.png", cv2.IMREAD_GRAYSCALE)
    img_to_close = cv2.imread("closing.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("img to open", img_to_open)
    cv2.waitKey()
    cv2.imshow("img to clsoe", img_to_close)
    cv2.waitKey()
    # Method 1
    # do opening by combining erosion and dilation
    # Specify Kernel Size
    kernelSize = 10
    # Create the Kernel
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * kernelSize + 1, 2 * kernelSize + 1),
                                        (kernelSize, kernelSize))
    # Perform Erosion
    imEroded = cv2.erode(img_to_open, element, iterations=1)
    # Perform Dilation
    imOpen = cv2.dilate(imEroded, element, iterations=1)
    # show opened image using method 1
    cv2.namedWindow('opened image 1', cv2.WINDOW_NORMAL)
    cv2.imshow("opened image 1", cv2.cvtColor(imOpen, cv2.COLOR_GRAY2BGR))
    cv2.waitKey()
    # Method 2
    # Use morphologyEx to operate opening
    # Get structuring element/kernel which will be used
    # for opening operation
    openingSize = 3
    # Selecting a elliptical kernel
    element_o = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                          (2 * openingSize + 1,
                                           2 * openingSize + 1),
                                          (openingSize, openingSize))
    imageMorphOpened = cv2.morphologyEx(img_to_open, cv2.MORPH_OPEN,
                                        element_o, iterations=3)
    cv2.namedWindow('opened image 2', cv2.WINDOW_NORMAL)
    cv2.imshow("opened image 2", cv2.cvtColor(
        imageMorphOpened, cv2.COLOR_GRAY2BGR))
    cv2.waitKey()
    # Closing an image
    # MEthod 1 using dilation followed by erosion
    # Perform Dilation
    imDilated = cv2.dilate(img_to_close, element)
    # Perform Erosion
    imClose = cv2.erode(imDilated, element)
    # show closed images using method 1
    cv2.namedWindow('closed image 1', cv2.WINDOW_NORMAL)
    cv2.imshow("closed image 1", cv2.cvtColor(imClose, cv2.COLOR_GRAY2BGR))
    cv2.waitKey()
    # Method 2
    # Use morphologyEx to operate closing
    imageMorphClosed = cv2.morphologyEx(img_to_close, cv2.MORPH_CLOSE, element)
    cv2.namedWindow('closed image 2', cv2.WINDOW_NORMAL)
    cv2.imshow("closed image 2", cv2.cvtColor(
        imageMorphClosed, cv2.COLOR_GRAY2BGR))
    cv2.waitKey()

if __name__ == "__main__":
    main(sys.argv)
