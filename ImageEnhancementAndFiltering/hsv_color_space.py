'''
    Author: Nebiyou Yismaw

    This is a python code will explore the HSV colorspace.
        - Hue : indicates color
        - Saturation: purity of the color
        - Value: brightness of the pixel

'''
# import requried libraries
import sys
import cv2
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt
# configure matplot lib
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


def value_test():
    '''
        Value channel tells us how bright or dark a pixel is. In order to test
        this we will create an image with zero hue and saturation and gradually
        increase the value channel value and see the effect.
        We will see that the image eventaully gets brighter and brighter
    '''
    # value will be 40 * i, where i in [0,7)
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
        # Set Hue = 0, Saturation = 0, Value = i x 40
        v = i * 40
        imhsv[:,:,:] = (0, 0, v)
        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)
        cv2.imshow("value %d"%(i),imrgb[:,:,::-1])
        cv2.waitKey()

def saturation_test():
    '''
        Here we will fix value and hue, and change the saturation and see the
        effect
    '''
    # value will be 40 * i, where i in [0,7)
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
        # Set Hue = 0, Saturation = 0, Value = i x 40
        s = i * 40
        imhsv[:,:,:] = (0, s, 128)
        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)
        cv2.imshow("Sat %d"%(i),imrgb[:,:,::-1])
        cv2.waitKey()

def hue_test():
    '''
        Here we will fix value and sat, and change the hue and see the
        effect
    '''
    # value will be 40 * i, where i in [0,7)
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
        # Set Hue = 0, Saturation = 0, Value = i x 40
        h = i * 40
        imhsv[:,:,:] = (h, 128, 128)
        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)
        cv2.imshow("Hue %d"%(i),imrgb[:,:,::-1])
        cv2.waitKey()

'''
    @main
'''
def main(argv):
    # read the RGB image
    rgb_image = cv2.imread("capsicum.jpg")
    # convert from bgr to HSV format
    hsv_Image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    # now let's split the channels and view all of them
    h, s, v = cv2.split(hsv_Image)
    cv2.imshow("H-channel ",h)
    cv2.waitKey()
    cv2.imshow("S-channel ",s)
    cv2.waitKey()
    cv2.imshow("V-channel",v)
    cv2.waitKey()
    # now let's explore more on the HSV values
    # experiment with the V(value) channel
    value_test()
    # experiment with the S(Saturation) channel
    saturation_test()
    # experiment with the H(Hue) channel
    hue_test()

if __name__ == '__main__':
    main(sys.argv)
