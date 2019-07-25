'''
    Author: Nebiyou Yismaw

    This is a python code that will that will use OPenCV and write frames bufers
    to a video file.

    List of video code codes can be found here https://www.fourcc.org/codecs.php

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
    # create a video capture object by opening a camera
    cap = cv2.VideoCapture(0)
    # Check if camera opened successfully
    if (cap.isOpened()== False):
          print("Error opening video stream or file")
    else:
        # get camera video resolution
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Define the codec and create VideoWriter object.
        # create avi and mp4 video writers. In doing so, first argument is
        # file name, the second argument is a 4 character code of codec,
        # the thrid argument is frames per second and finally the video resolution
        outavi = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        outmp4 = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width,frame_height))
        # while there is a frame to read
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Write the frame into output files
                outavi.write(frame)
                outmp4.write(frame)
                # Display the frame
                cv2.imshow("Frame",frame)
                # Wait for 25 ms before moving on to the next frame
                # This will slow down the video
                # Exit if key pressed is 27 (ascii for ESC)
                k = cv2.waitKey(25)
                if k == 27:
                  break
                # Break the loop
            else:
                break


if __name__ == '__main__':
    main(sys.argv)
