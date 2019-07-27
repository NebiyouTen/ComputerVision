'''
    Author: Nebiyou Yismaw

    This is a python code that will explore the face annotation using mouse
    callbacks in OPenCV


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

COORD_1 = "p1"
COORD_2 = "p2"
# dictionary to store coordiantes
rect_coords = {}
# flag for program exit
image_saved = False
'''
    Function to save an image
    Args: image     : image array
          file_name : output file name
'''


def save_image(image, file_name):
    cv2.imwrite(file_name, image)


'''
    Function to crop an image
    Args: image: image array
          h1   : crop boundary start height
          h2   : crop boundary end height
          w1   : crop boundary start width
          w2   : crop boundary end width
    Ret:  cropped image array
'''


def crop_image(image, h1, h2, w1, w2):
    return np.copy(image[h1:h2, w1:w2])


'''
    Mouse event callback function to draw face annotation
'''


def face_annotate(action, x, y, flags, userdata):
    # Referencing global variables
    global rect_coords, image_saved
    # when mouse button is pressed, mark the start of the rectangle
    if action == cv2.EVENT_LBUTTONDOWN:
        rect_coords[COORD_1] = (x, y)
        # mark the first coorindates
        cv2.circle(userdata, (x, y), 1, (239, 191, 53), 2, cv2.LINE_AA)
    # when mouse button is released, mark the second points, draw a rectangle
    # crop the image and finally save it to an output file.
    elif action == cv2.EVENT_LBUTTONUP:
        rect_coords[COORD_2] = (x, y)
        # crop the image and save it to an output file before drawing a rectangle
        # this way the bouding box will not be present in the output image
        cropped_img = crop_image(
            userdata, rect_coords[COORD_1][1], rect_coords[COORD_2][1], rect_coords[COORD_1][0], rect_coords[COORD_2][0])
        save_image(cropped_img, "face.png")
        # Draw the rectangle
        cv2.rectangle(userdata, rect_coords[COORD_1], rect_coords[COORD_2],
                      (239, 191, 53), thickness=2, lineType=cv2.LINE_8)
        # show image
        cv2.imshow("Window", userdata)
        # set image saved falg
        image_saved = True
        # remvoe callback so that any further mouse events won't invoke this
        # call back
        cv2.setMouseCallback("Window", lambda *args: None)


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
    cv2.setMouseCallback("Window", face_annotate, src_img)
    # exit if esc key is pressed or if image is saved
    k = 0
    while k != 27 and not image_saved:
        # show image
        cv2.imshow("Window", src_img)
        cv2.putText(src_img, '''Choose center, and drag,
                            Press ESC to exit and c to clear''',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2)
        # wait for key
        k = cv2.waitKey(20) & 0xFF
        # if key c is pressed, create the a copy of the original image and
        # pass that to the mouse event callback, which has no circles drawn
        # on it
        if k == 99:
            src_img = src_img_cpy.copy()
    # wait for 1 sec before exiting
    cv2.waitKey(1000)
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
