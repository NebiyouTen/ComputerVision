'''
    Author: Nebiyou Yismaw

    This is a python code has implementation of simple thresholding techniques
    on a gray scale image.

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
    A naive thresholding function that will set pixel values at a certan
    coordiante to max_val if ( pixel value > thresh ), otherwise to 0. This is
    a naive approach because it iterates through each pixel elemnts, hence
    not efficient.
'''
def navive_thresholding(img, thresh, max_val):
    dst = img.copy()
    height, width = img.shape[:2]
    # Loop over rows
    for i in range(height):
        # Loop over columns
        for j in range(width):
            if img[i, j] > thresh:
                dst[i, j] = max_val
            else:
                dst[i, j] = 0
    return dst

'''
    A better vectorized approch to thresholding
'''
def threshold_using_vectors(src, thresh, maxValue):
    # Create a black output image ( all zeros )
    dst = np.zeros_like(src)
    # Find pixels which have values>threshold value
    thresholdedPixels = src>thresh
    # Assign those pixels maxValue
    dst[thresholdedPixels] = maxValue
    return dst

'''
    @main
'''


def main(argv):
    # Read an image in grayscale
    src = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE)
    # Set threshold and maximum value
    thresh = 100
    maxValue = 255
    # time the navie thresholding method
    t = time.time()
    dst_naive = navive_thresholding(src, thresh, maxValue)
    print("Time taken naive = {} seconds".format(time.time() - t))
    # time the vectorized thresholding method
    t = time.time()
    dst_vectorized = threshold_using_vectors(src, thresh, maxValue)
    print("Time taken vectorized = {} seconds".format(time.time() - t))
    # time the opencv thresholding method
    t = time.time()
    th, dst_cv = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    print("Time taken vectorized = {} seconds".format(time.time() - t))
    # plot the output of the thresholding alg and the origional image
    # show image
    cv2.imshow("Original image", src)
    cv2.waitKey()
    cv2.imshow("Thresholded image", dst_naive)
    cv2.waitKey()
    cv2.imshow("Thresholded image", dst_vectorized)
    cv2.waitKey()
    cv2.imshow("Thresholded image", dst_cv)
    cv2.waitKey()
    '''
        other thresholding algorithms provided by ppencv
    '''
    thresh = 100
    maxValue = 150
    # binary thresholding
    th, dst_bin = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    # inverse binary thresholding
    th, dst_bin_inv = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)
    # truncate thresholding
    th, dst_trunc = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TRUNC)
    # treshold to zero
    th, dst_to_zero = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO)
    # inverted treshold to zero
    th, dst_to_zero_inv = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO_INV)
    # display thresholded images
    cv2.imshow("binary thresholding", dst_bin)
    cv2.waitKey()
    cv2.imshow("inverse binary thresholding", dst_bin_inv)
    cv2.waitKey()
    cv2.imshow("truncate thresholding", dst_trunc)
    cv2.waitKey()
    cv2.imshow("treshold to zero", dst_to_zero)
    cv2.waitKey()
    cv2.imshow("inverted treshold to zero", dst_to_zero_inv)
    cv2.waitKey()
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
