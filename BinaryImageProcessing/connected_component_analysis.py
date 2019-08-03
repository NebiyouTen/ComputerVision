'''
    Author: Nebiyou Yismaw

    This is a python code that uses openCV to perform connected component analysis
    on a simple image

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
    A function that will normaliz an image so that the pixels will be in the [0, 255]
    range and will return a unit8 version
'''
def normalize_img(image):
    return np.uint8( 255 *  (image - np.min(image)) / (np.max(image) - np.min(image)) )

'''
    @main
'''
def main(argv):
    img_truth = cv2.imread("../VideoIO/truth.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Truth image", img_truth)
    cv2.waitKey()
    # Threshold Image
    th, imThresh = cv2.threshold(img_truth, 127, 255, cv2.THRESH_BINARY)
    # Find connected components
    _, imLabels = cv2.connectedComponents(imThresh)
    # imLables have pixel values that corresond to each connected component.
    # We can change these vales (1, 2, 3 ... ) so that are with in the range of [0, 255]
    # This normalization is done below
    norm_img = normalize_img(imLabels)
    cv2.imshow("CCA", norm_img)
    cv2.waitKey()
    # Now let's display each image
    num_comps = np.max( imLabels )
    for i in range (num_comps + 1):
        # get pixel values of each connected component
        cv2.imshow("Component " + str(i), normalize_img((imLabels==i).astype(int)) )
        cv2.waitKey()
    # For better display, we can use color maps
    cv2.imshow("Color map " + str(i), cv2.applyColorMap(norm_img, cv2.COLORMAP_JET) )
    cv2.waitKey()

if __name__ == "__main__":
    main(sys.argv)
