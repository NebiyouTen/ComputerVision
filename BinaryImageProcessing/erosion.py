'''
    Author: Nebiyou Yismaw

    This is a python code uses opencv to erode images

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
    # Read the input image to erode
    img_to_erode = cv2.imread("erosion_example.jpg")
    cv2.imshow("img to erode", img_to_erode)
    cv2.waitKey()
    # erode image using a single big kernel
    # Get structuring element/kernel which will be used for erosion
    k_size = (7,7)
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k_size)
    cv2.imshow("kernel 7x7",kernel_1.astype(float))
    cv2.waitKey()
    # apply multile erosions on an input image
    image_erroded_1 = cv2.erode(img_to_erode, kernel_1, iterations=1)
    cv2.imshow("Eroded image 1", image_erroded_1)
    cv2.waitKey()
    image_erroded_2 = cv2.erode(img_to_erode, kernel_1, iterations=2)
    cv2.imshow("Eroded image 2", image_erroded_2)
    cv2.waitKey()
    # destory windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
