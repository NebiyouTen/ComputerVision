'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and read and display
    a video.

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
    # create a video capture object by passing a file name
    cap = cv2.VideoCapture('chaplin.mp4')
    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
    # while capture object is opened
    while(cap.isOpened()):
      # Capture frame-by-frame
      ret, frame = cap.read()
      if ret == True:
          # Display the resulting frame
          cv2.imshow('Frame',frame)
          # Press esc on keyboard to  exit
          # wait take time to wait before timing out in ms. Here we wait for
          # 25ms before displaying the next frame
          if cv2.waitKey(25) & 0xFF == 27:
              break
      else:
          break


if __name__ == '__main__':
    main(sys.argv)