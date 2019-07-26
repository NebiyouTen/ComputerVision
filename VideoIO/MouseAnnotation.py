'''
    Author: Nebiyou Yismaw

    This is a python code that will explore the mouse annotation in OPenCV


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


def draw_circle(action, x, y, flags, userdata):
    '''
        Mouse event callback function
    '''
    # Referencing global variables
    global center, circumference
    # Action to be taken when left mouse button is pressed
    if action==cv2.EVENT_LBUTTONDOWN:
        center=[(x,y)]
        # Mark the center
        cv2.circle(userdata, center[0], 1, (255,255,0), 2, cv2.LINE_AA );
       # Action to be taken when left mouse button is released
    elif action==cv2.EVENT_LBUTTONUP:
        circumference=[(x,y)]
        # Calculate radius of the circle
        radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+
                            math.pow(center[0][1]-circumference[0][1],2))
        # Draw the circle
        cv2.circle(userdata, center[0], int(radius), (0,255,0),2,
                        cv2.LINE_AA)
        cv2.imshow("Window",userdata)
    # pass


'''
    @main
'''
def main(argv):
    # get image source
    src_img = cv2.imread("sample.jpg", 1)
    # let's copy this iamge
    src_img_cpy = src_img.copy()
    # crete a named window
    cv2.namedWindow("Window")
    # let's add mouse event handler for our named window
    cv2.setMouseCallback("Window", draw_circle, src_img)
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
