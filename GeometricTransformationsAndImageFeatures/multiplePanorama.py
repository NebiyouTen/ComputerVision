'''
    This pythons script will use OpenCV to sticth different images to create
    a panorama

    Nebiyou Yismaw

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def main(argv):
    images = []
    dirName = "scene"
    imagefiles = [DATA_PATH + "images/{}/".format(dirName) + f for f in os.listdir(
        DATA_PATH + "images/" + dirName) if f.endswith(".jpg")]
    imagefiles.sort()
    destination = "{}_result.png".format(dirName)
    plt.figure(figsize=[20, 15])
    i = 1
    for filename in imagefiles:
        img = cv2.imread(filename)
        images.append(img)
    # let's create a stitcher class
    stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
    # pass the list of images to our stitcher object
    _, result = stitcher.stitch(images)


if __name__=="__main__":
    main(sys.argv)
