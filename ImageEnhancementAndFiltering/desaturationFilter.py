'''
    Author: Nebiyou Yismaw

    This is a python code read an RGB image and perform desaturation

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


'''
    @main
'''
def main(argv):
    img = cv2.imread("girl.jpg")
    # Specify scaling factor
    saturationScale = 0.01
    # Convert to HSV color space
    hsvImage = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Convert to float32
    hsvImage = np.float32(hsvImage)
    # Split the channels
    H, S, V = cv2.split(hsvImage)
    # Multiply S channel by scaling factor and clip the values to stay in 0 to 255
    S = np.clip(S * saturationScale , 0, 255)
    # Merge the channels and show the output
    hsvImage = np.uint8( cv2.merge([H, S, V]) )
    imSat = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
    cv2.imshow("Original Image",img)
    cv2.waitKey(0)
    cv2.imshow("Desaturated Image", imSat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
