'''
    Author: Nebiyou Yismaw

    This is a python code has implementations of basic morphological operations
    namely erotion and dilation

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
    A function to return a simple binary image, it takes in a size tuple.

'''


def get_simple_image(size):
    # create an empty image
    img = np.zeros(size, dtype='uint8')
    # assign some pixel values
    img[0, 1] = 1
    img[-1, 0] = 1
    img[-2, -1] = 1
    img[2, 2] = 1
    img[5:8, 5:8] = 1
    return img


def dilation_method_1(image, kernel):
    # get image and kenel size
    kernel_size = kernel.shape[0]
    height, width = image.shape[:2]
    # get border size, required for padding.
    border = kernel_size // 2
    # create the passed image array
    padded_img = np.zeros((height + border * 2, width + border * 2))
    # let's copy the src image to our padded array
    padded_img = cv2.copyMakeBorder(
        image, border, border, border, border, cv2.BORDER_CONSTANT, value=0)
    for h_i in range(border, height + border):
        for w_i in range(border, width + border):
            # When you find a white pixel
            if image[h_i - border, w_i - border]:
                print("White Pixel Found @ {},{}".format(h_i, w_i))
                padded_img[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1] = \
                    cv2.bitwise_or(
                        padded_img[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1], kernel)
                # Print the intermediate result
                # print(padded_img)
    # return the dilated image
    return padded_img[border:border+height,border:border+width]
'''
    @main
'''


def main(argv):
    # get sample image
    image = get_simple_image((10, 10))
    # get structuring element
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    dil_img = dilation_method_1(image, element)
    print (dil_img)
    cv2.namedWindow('Dilated image', cv2.WINDOW_NORMAL)
    cv2.imshow("Dilated image", dil_img*255)
    cv2.resizeWindow('Dilated image', 600,600)
    cv2.waitKey()


    # destory windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv)
