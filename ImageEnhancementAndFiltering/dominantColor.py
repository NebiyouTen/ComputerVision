'''
    Author: Nebiyou Yismaw

    This is a python code read an RGB image, plot a historgram to see the
    dominant color

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
    img = cv2.imread("jersey.jpg")
    cv2.imshow("Messi",img)
    cv2.waitKey(0)

    # Convert to HSV color space
    hsvImage = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Split the channels
    H, S, V = cv2.split(hsvImage)
    # Remove unsaturated (white/gray) pixels
    H_array = H[S > 10].flatten()

    print(H_array.shape)

    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Image");plt.axis('off')
    plt.subplot(122);plt.hist(H_array, bins=180, color='r');plt.title("Histogram")
    plt.show()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
