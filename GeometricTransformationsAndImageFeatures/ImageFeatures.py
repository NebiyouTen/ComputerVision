'''
    Author: Nebiyou Yismaw

    This is a python code that will extract image features using OpenCV


'''

# import requried libraries
import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
import math


def main():
    # Read input image
    img = cv2.imread("book.jpeg")
    # Convert to grayscale
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image",img)
    cv2.imshow("Gray",imgGray)
    cv2.waitKey(0)

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(imgGray,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(imgGray, kp)

    # draw keypoints location, size and orientation
    img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Keypoints",img2)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    orb = cv2.ORB_create(10)
    kp, des = orb.detectAndCompute(imgGray, None)
    img2 = cv2.drawKeypoints(img, kp, None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("keypoints",img2)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
