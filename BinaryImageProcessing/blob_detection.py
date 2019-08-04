'''
    Author: Nebiyou Yismaw

    This is a python code that uses openCV to perform blob detection

'''
# imports
import matplotlib
import cv2
import time
import numpy as np
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


'''
    @main
'''
def main(argv):
    # Read blob image and display
    img_blob = cv2.imread("blob_detection.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Blob image", img_blob)
    cv2.waitKey()
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()
    # get the keypoints from our detector
    keypoints = detector.detect(img_blob)
    # Now let's mark the keypoints
    # Let's convert to RGB so that we can dray colored markers
    img = cv2.cvtColor(img_blob, cv2.COLOR_GRAY2BGR)
    print("Num key points %d"%(len(keypoints)))
    for k in keypoints:
        x,y = k.pt
        x=int(round(x))
        y=int(round(y))
        # Mark center in BLACK
        cv2.circle(img,(x,y),5,(0,0,0),-1)
        # Get radius of blob
        diameter = k.size
        radius = int(round(diameter/2))
        # Mark blob in RED
        cv2.circle(img,(x,y),radius,(0,0,255),2)
    cv2.imshow("Key blobs image default params", img)
    cv2.waitKey()
    # Now lets define different blob params for our filter type
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200
    '''
        Commented below are some filter criterias 
    '''
    # Filter by Area.
    # params.filterByArea = True
    # params.minArea = 1500
    #
    # # Filter by Circularity
    # params.filterByCircularity = True
    # params.minCircularity = 0.1
    #
    # # Filter by Convexity
    # params.filterByConvexity = True
    # params.minConvexity = 0.87
    #
    # # Filter by Inertia
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    # get the keypoints from our detector
    keypoints = detector.detect(img_blob)
    img = cv2.cvtColor(img_blob, cv2.COLOR_GRAY2BGR)
    print("Num key points %d"%(len(keypoints)))
    for k in keypoints:
        x,y = k.pt
        x=int(round(x))
        y=int(round(y))
        # Mark center in BLACK
        cv2.circle(img,(x,y),5,(0,0,0),-1)
        # Get radius of blob
        diameter = k.size
        radius = int(round(diameter/2))
        # Mark blob in RED
        cv2.circle(img,(x,y),radius,(0,0,255),2)
    cv2.imshow("Key blobs image configured params", img)
    cv2.waitKey()


if __name__ == "__main__":
    main(sys.argv)
