'''
    Author: Nebiyou Yismaw

    This is a python code that uses openCV to perform contour analysis

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
    # Read contour image and display
    # We need to keep the RGB image so that we can display colored contours on
    # top of it.
    img_contour = cv2.imread("Contour.png")
    cv2.imshow("Contour image", img_contour)
    cv2.waitKey()
    # Convert contour image to grayscale and display
    img_contour_gray = cv2.cvtColor(img_contour, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Contour image grayscale", img_contour_gray)
    cv2.waitKey()
    # Find all contours in the image
    contours, hierarchy = cv2.findContours(img_contour_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours found = {}".format(len(contours)))
    print("\nHierarchy : \n{}".format(hierarchy))
    # Now let's dray the contours
    cv2.drawContours(img_contour, contours, -1, (0,255,0), 3);
    cv2.imshow("Contour display all", img_contour)
    cv2.waitKey()
    # Let's display only outer contours
    # First let's reset the RGB image
    img_contour = cv2.imread("Contour.png")
    contours, hierarchy = cv2.findContours(img_contour_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours found = {}".format(len(contours)))
    print("\nHierarchy : \n{}".format(hierarchy))
    # Now let's dray the contours
    cv2.drawContours(img_contour, contours, -1, (0,255,255), 3);
    cv2.imshow("Contour display external", img_contour)
    cv2.waitKey()
    # Let's display only a specific contour
    # First let's reset the RGB image
    img_contour = cv2.imread("Contour.png")
    # Now let's dray the contours
    cv2.drawContours(img_contour, contours[3], -1, (255,255,0), 3);
    cv2.imshow("Contour display specific", img_contour)
    cv2.waitKey()
    # Let's calculate centroid
    # First let's reset the RGB image
    img_contour = cv2.imread("Contour.png")
    contours, hierarchy = cv2.findContours(img_contour_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Draw all the contours
    cv2.drawContours(img_contour, contours, -1, (0,255,0), 3);
    for index, cnt in enumerate(contours):
        # We will use the contour moments
        # to find the centroid
        M = cv2.moments(cnt)
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        # Mark the center
        cv2.circle(img_contour, (x,y), 10, (255,0,0), -1);
        # Mark the contour number
        cv2.putText(img_contour, "{}".format(index + 1), (x+40, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2);
        # Rotated bounding box
        box = cv2.minAreaRect(cnt)
        boxPts = np.int0(cv2.boxPoints(box))
        # Use drawContours function to draw
        # rotated bounding box
        cv2.drawContours(img_contour, [boxPts], -1, (0,255,255), 2)

    cv2.imshow("Bounded Contour centroids", img_contour)
    cv2.waitKey()



if __name__ == "__main__":
    main(sys.argv)
