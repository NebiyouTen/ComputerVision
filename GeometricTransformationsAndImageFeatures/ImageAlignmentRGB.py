'''
    Author: Nebiyou Yismaw

    This is a python code that will do feature matching using OpenCV


'''

import cv2
import numpy as np
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'


def main(argv):
    # Read 8-bit color image.
    # This is an image in which the three channels are
    # concatenated vertically.
    im =  cv2.imread("emir.jpg", cv2.IMREAD_GRAYSCALE)
    # Find the width and height of the color image
    sz = im.shape
    print(sz)
    height = int(sz[0] / 3);
    width = sz[1]
    # Extract the three channels from the gray scale image
    # and merge the three channels into one color image
    im_color = np.zeros((height,width,3), dtype=np.uint8 )
    for i in range(0,3):
        im_color[:,:,i] = im[ i * height:(i+1) * height,:]
    blue = im_color[:,:,0]
    green = im_color[:,:,1]
    red = im_color[:,:,2]
    # Initiate ORB detector
    MAX_FEATURES = 5000
    GOOD_MATCH_PERCENT = 0.015
    orb = cv2.ORB_create(MAX_FEATURES)
    keypointsBlue, descriptorsBlue = orb.detectAndCompute(blue,None)
    keypointsGreen, descriptorsGreen = orb.detectAndCompute(green,None)
    keypointsRed, descriptorsRed = orb.detectAndCompute(red,None)
    plt.figure(figsize=[30,20])
    img2 = cv2.drawKeypoints(blue, keypointsBlue, None, color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.subplot(131);plt.imshow(img2[...,::-1])

    img2 = cv2.drawKeypoints(green, keypointsGreen, None, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.subplot(132);plt.imshow(img2[...,::-1])

    img2 = cv2.drawKeypoints(red, keypointsRed, None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.subplot(133);plt.imshow(img2[...,::-1])
    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matchesBlueGreen = matcher.match(descriptorsBlue, descriptorsGreen, None)

    # Match features between blue and Green channels
    # Sort matches by score
    matchesBlueGreen.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matchesBlueGreen) * GOOD_MATCH_PERCENT)
    matchesBlueGreen = matchesBlueGreen[:numGoodMatches]

    # Draw top matches
    imMatchesBlueGreen = cv2.drawMatches(blue, keypointsBlue, green, keypointsGreen, matchesBlueGreen, None)
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matchesRedGreen = matcher.match(descriptorsRed, descriptorsGreen, None)
    # Match features between Red and Green channels
    ###
    ### YOUR CODE HERE
    ###

    # Sort matches by score
    matchesRedGreen.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matchesRedGreen) * GOOD_MATCH_PERCENT)
    matchesRedGreen = matchesRedGreen[:numGoodMatches]

    # Draw top matches
    imMatchesRedGreen = cv2.drawMatches(red, keypointsRed, green, keypointsGreen, matchesRedGreen, None)
    # Extract location of good matches
    pts1 = np.zeros((len(matchesBlueGreen), 2), dtype=np.float32)
    pts2 = np.zeros((len(matchesBlueGreen), 2), dtype=np.float32)

    for i, match in enumerate(matchesBlueGreen):
        pts1[i, :] = keypointsBlue[match.queryIdx].pt
        pts2[i, :] = keypointsGreen[match.trainIdx].pt

    # Find homography
    hBlueGreen, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)
    pts1 = np.zeros((len(matchesRedGreen), 2), dtype=np.float32)
    pts2 = np.zeros((len(matchesRedGreen), 2), dtype=np.float32)

    for i, match in enumerate(matchesRedGreen):
        pts1[i, :] = keypointsRed[match.queryIdx].pt
        pts2[i, :] = keypointsGreen[match.trainIdx].pt

    # Find homography
    hRedGreen, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)
    # Use homography to find blueWarped and RedWarped images
    blueWarped = cv2.warpPerspective(blue, hBlueGreen, (width, height))
    redWarped = cv2.warpPerspective(red, hRedGreen, (width, height))
    colorImage = cv2.merge((blueWarped,green,redWarped))
    originalImage = cv2.merge((blue,green,red))




if __name__ == "__main__":
    main(sys.argv)
