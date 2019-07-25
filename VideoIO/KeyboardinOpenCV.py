'''
    Author: Nebiyou Yismaw

    This is a python code that will explore the use keyboards in OPenCV


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
        # while there is a frame to read
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Wait for 25 ms before moving on to the next frame
                # This will slow down the video
                # Exit if key pressed is 27 (ascii for ESC)
                k = cv2.waitKey(1000) & 0xFF
                # Identify if 'ESC' is pressed or not
                if(k==27):
                	break
                txt = "Key pressed is " + chr(k)
                cv2.putText(frame, txt, (100,180), cv2.FONT_HERSHEY_SIMPLEX,
                                  1, (0,255,0), 3);
                # Display the frame
                cv2.imshow("Frame", frame)
            else:
                break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
