'''
    Author: Nebiyou Yismaw

    This is a python code that will explore the mouse scroll in OPenCV


'''
# import requried libraries
import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# Lists to store the points
center=[]
circumference=[]


def resize(action, x, y, flags, userdata):
    '''
        Mouse event callback function
    '''
    # Referencing global variables
    global center, circumference
    # Action to be taken when ctrl key + mouse wheel scrolled forward
    if (action == cv2.EVENT_MOUSEWHEEL) and (flags & cv2.EVENT_FLAG_CTRLKEY):
        print("Inside condition 1 ")
        if (flags > 0):
            print("Resize image up")
        elif (flags < 0):
            print("Resize image down")



'''
    @main
'''
def main(argv):
    # get image source
    src_img = cv2.imread("truth.png", 1)
    # let's copy this iamge
    src_img_cpy = src_img.copy()
    # crete a named window
    cv2.namedWindow("Window")
    # let's add mouse event handler for our named window
    cv2.setMouseCallback("Window", resize, src_img)
    # exit if esc key is pressed
    k = 0
    while k != 27:
        # show image
        cv2.imshow("Window", src_img)
        cv2.putText(src_img,'''Choose center, and drag,
                            Press ESC to exit and c to clear''' ,
                    (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,(255,255,255), 2 );
        # wait for key
        k = cv2.waitKey(20) & 0xFF
        # if key c is pressed, create the a copy of the original image and
        # pass that to the mouse event callback, which has no circles drawn
        # on it
        if k == 99:
            src_img = src_img_cpy.copy()
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
