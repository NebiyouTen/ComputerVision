'''
    Author: Nebiyou Yismaw

    This is a python code uses opencv to dilate images

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
    # Read the input image to dilate
    img_to_dilate = cv2.imread("dilation_example.jpg")
    cv2.imshow("img to dilate", img_to_dilate)
    cv2.waitKey()
    # dilate image using a single big kernel
    # Get structuring element/kernel which will be used for dilation
    k_size = (7,7)
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k_size)
    # kernel_1 = np.ones_like(kernel_1)
    cv2.imshow("kernel 7x7",kernel_1.astype(float))
    print (type(kernel_1))
    cv2.waitKey()
    # Apply dilate function on the input image
    image_dilated = cv2.dilate(img_to_dilate, kernel_1)
    cv2.imshow("Dilated image 1", image_dilated)
    cv2.waitKey()
    # dilage image using a smaller kernel
    # Get structuring element/kernel which will be used for dilation
    k_size = (3,3)
    kernel_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k_size)
    cv2.imshow("kernel 3x3", kernel_2.astype(float))
    cv2.waitKey()
    # apply multile dilations on an input image
    imageDilated_1 = cv2.dilate(img_to_dilate, kernel_2, iterations=1)
    cv2.imshow("Dilated image 2", imageDilated_1)
    cv2.waitKey()
    imageDilated_2 = cv2.dilate(img_to_dilate, kernel_2, iterations=2)
    cv2.imshow("Dilated image 3", imageDilated_2)
    cv2.waitKey()
    # destory windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
