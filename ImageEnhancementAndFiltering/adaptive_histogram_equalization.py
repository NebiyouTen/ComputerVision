'''
    Author: Nebiyou Yismaw

    This is a python code that uses opencv to perform adaptive historgram
    equalization

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
    filename = "night-sky.jpg"
    im = cv2.imread(filename)

    # Convert to HSV
    imhsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    imhsvCLAHE = imhsv.copy()

    # Perform histogram equalization only on the V channel
    imhsv[:,:,2] = cv2.equalizeHist(imhsv[:,:,2])

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    imhsvCLAHE[:,:,2] = clahe.apply(imhsvCLAHE[:,:,2])

    # Convert back to BGR format
    imEq = cv2.cvtColor(imhsv, cv2.COLOR_HSV2BGR)
    imEqCLAHE = cv2.cvtColor(imhsvCLAHE, cv2.COLOR_HSV2BGR)

    #Display images
    plt.figure(figsize=(40,40))

    ax = plt.subplot(1,3,1)
    plt.imshow(im[:,:,::-1], vmin=0, vmax=255)
    ax.set_title("Original Image")
    ax.axis('off')

    ax = plt.subplot(1,3,2)
    plt.imshow(imEq[:,:,::-1], vmin=0, vmax=255)
    ax.set_title("Histogram Equalized")
    ax.axis('off')

    ax = plt.subplot(1,3,3)
    plt.imshow(imEqCLAHE[:,:,::-1], vmin=0, vmax=255)
    ax.set_title("CLAHE")
    ax.axis('off')
    plt.show()



if __name__ == '__main__':
    main(sys.argv)
