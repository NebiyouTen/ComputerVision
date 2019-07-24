'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and do the following
        - Anotate an image with Line, Circle, Rectangle, Ellipse and Text

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
# import image_utils which contains all required
from image_utils import *

'''
    @main
'''
def main(argv):
    # read simple image and display it
    image_path_boy      = "./data/images/boy.jpg"
    image_boy           = read_image(image_path_boy)
    display_image(image_boy)
    # draw a line on the boy image and display it
    image_boy_line      = cv2.line(image_boy.copy(), (200, 80), (280, 80), (0, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    display_image(image_boy_line)
    # draw a circle on the boy image and display it
    image_boy_circle    = cv2.circle(image_boy.copy(), (250, 125), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)
    display_image(image_boy_circle)
    # draw a filled circle on the boy image and display it
    image_boy_circle_f  = cv2.circle(image_boy.copy(), (250, 125), 100, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)
    display_image(image_boy_circle_f)
    # draw a elipses circle on the boy image and display them
    image_boy_ellipse   = image_boy.copy()
    cv2.ellipse(image_boy_ellipse, (250, 125), (100, 50), 0, 0, 360, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
    cv2.ellipse(image_boy_ellipse, (250, 125), (100, 50), 90, 0, 360, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
    display_image(image_boy_ellipse)
    # draw a rectangle on the boy image and display it
    image_boy_rectangle = cv2.rectangle(image_boy.copy(), (170, 50), (300, 200), (255, 0, 255), thickness=5, lineType=cv2.LINE_8)
    display_image(image_boy_rectangle)
    # put sample text on the image and display it
    text      = "Sample text "
    fontScale = 1.5
    fontFace  = cv2.FONT_HERSHEY_COMPLEX
    fontColor = (250, 10, 10)
    fontThickness = 2
    pixelHeight   = 20
    # get fontscale from height
    fontScale     = cv2.getFontScaleFromHeight(fontFace, pixelHeight, fontThickness)
    image_boy_text  = image_boy.copy()
    cv2.putText(image_boy_text, text, (20, 350), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
    display_image(image_boy_text)

if __name__ == '__main__':
    main(sys.argv)
