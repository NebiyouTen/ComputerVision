'''
    Author: Nebiyou Yismaw

    This is a python code that uses opencv to perform historgram equalization

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
    # read an image in grayscale
    im = cv2.imread("dark-flowers.jpg", cv2.IMREAD_GRAYSCALE)
    # display
    cv2.imshow("Imput image", im)
    cv2.waitKey()
    # Equalize histogram
    imEq = cv2.equalizeHist(im)
    # display
    cv2.imshow("Equalized image", imEq)
    cv2.waitKey()
    # now let's print the histogram
    plt.figure(figsize=(30,10))
    plt.subplot(1,2,1)
    plt.hist(im.ravel(),256,[0,256]);

    plt.subplot(1,2,2)
    plt.hist(imEq.ravel(),256,[0,256]);
    plt.show()

    '''
        Now let's perform histogram equalization on color images.
        histogram shouldn' be perfromed on RGB space, as we don't want
        to modify any color information but only the intensity values.
        Hence, we can convert the image to HSV space and equalizae the V
        channel, which only contains intensity information
    '''
    # read the iamge
    im = cv2.imread("dark-flowers.jpg")
    cv2.imshow("Input image", im)
    cv2.waitKey()
    # Convert to HSV
    imhsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # Perform histogram equalization only on the V channel
    imhsv[:,:,2] = cv2.equalizeHist(imhsv[:,:,2])
    # Convert back to BGR format
    imEq = cv2.cvtColor(imhsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("Final image", imEq)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
