'''
    Author: Nebiyou Yismaw

    This is a python code has implementations of basic morphological operations
    namely erotion and dilation

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
    A function to return a simple binary image, it takes in a size tuple.

'''


def get_simple_image(size):
    # create an empty image
    img = np.zeros(size, dtype='uint8')
    # assign some pixel values
    img[0, 1] = 1
    img[-1, 0] = 1
    img[-2, -1] = 1
    img[2, 2] = 1
    img[5:8, 5:8] = 1
    return img


def dilation_method_1(image, kernel):
    # get image and kenel size
    kernel_size = kernel.shape[0]
    height, width = image.shape[:2]
    # get border size, required for padding.
    border = kernel_size // 2
    # create the passed image array
    padded_img = np.zeros((height + border * 2, width + border * 2))
    # let's copy the src image to our padded array
    padded_img = cv2.copyMakeBorder(
        image, border, border, border, border, cv2.BORDER_CONSTANT, value=0)
    for h_i in range(border, height + border):
        for w_i in range(border, width + border):
            # When you find a white pixel
            if image[h_i - border, w_i - border]:
                padded_img[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1] = \
                    cv2.bitwise_or(
                        padded_img[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1], kernel)
                # Print the intermediate result
                # print(padded_img)
    # return the dilated image
    return padded_img[border:border+height,border:border+width]

'''
    A different approach to dilation
'''
def dilation_method_2(im, element):
    # get width, hights and shapes
    ksize = element.shape[0]
    height,width = im.shape[:2]
    border = ksize//2
    # create a padded matrix
    paddedIm = np.zeros((height + border*2, width + border*2))
    # create a border of values zero around the image and copy it to the padded matrix
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
    # copy the padded image, on which the dilation operation will be operated on
    paddedDilatedIm = paddedIm.copy()
    # Create a VideoWriter object
    frame_width   = 50
    frame_height  = 50
    fps           = 10
    outavi = cv2.VideoWriter('dilationScratch.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
    # move around the non-padded region
    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            # do a bitwise between the region of interset and the kernel bit
            dil_mat = cv2.bitwise_and(
                            paddedIm[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1], element)
            # for a given pixel, find a maximum bit value. As dilation or putting a bit at
            # pixel can happen if there is a bit in the region of intrest
            paddedDilatedIm[h_i, w_i] = np.max(dil_mat)
            # Resize output to 50x50 before writing it to the video
            resized_img = cv2.resize(paddedDilatedIm, (50,50))
            # Convert resizedFrame to BGR before writing
            merged_img  = cv2.cvtColor(resized_img*255, cv2.COLOR_GRAY2BGR)
            outavi.write(merged_img)
            cv2.waitKey(10)
    # Release the VideoWriter object
    outavi.release()
    # return the non padded image in the dilated image
    return paddedDilatedIm[border:border+height,border:border+width]

'''
    A different approach to erosion
'''
def erosion_method_2(im, element):
    # get width, hights and shapes
    ksize = element.shape[0]
    height,width = im.shape[:2]
    border = ksize//2
    # create a padded matrix
    paddedIm = np.zeros((height + border*2, width + border*2))
    # create a border of values zero around the image and copy it to the padded matrix
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 1)
    # copy the padded image, on which the erosion operation will be operated on
    paddedErodedIm = paddedIm.copy()
    # Create a VideoWriter object
    frame_width   = 50
    frame_height  = 50
    fps           = 10
    outavi = cv2.VideoWriter('dilationScratch.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
    # move around the non-padded region
    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            # do a bitwise between the region of interset and the kernel bit
            # since dilation removes white pixels, if there is a black pixel in our center pixel
            # we will set our pixel value to 0. So we can flip our ROI, meaning black pixels will
            # have a value of 1 and white pixel will have a value of 0. We can then AND these flipped
            # bits with our kernel.
            erod_mat = cv2.bitwise_and(
                        cv2.bitwise_not(paddedIm[h_i - border: (h_i + border) + 1, w_i - border: (w_i + border) + 1])
                        , element)
            #  if we
            paddedErodedIm[h_i, w_i] = 1 - np.max(erod_mat)
            # Resize output to 50x50 before writing it to the video
            resized_img = cv2.resize(paddedErodedIm, (50,50))
            # Convert resizedFrame to BGR before writing
            merged_img  = cv2.cvtColor(resized_img*255, cv2.COLOR_GRAY2BGR)
            outavi.write(merged_img)
            cv2.waitKey(10)
    # Release the VideoWriter object
    outavi.release()
    # return the non padded image in the dilated image
    return paddedErodedIm[border:border+height,border:border+width]

'''
    @main
'''
def main(argv):
    # get sample image
    image = get_simple_image((10, 10))
    # get structuring element
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # dilate image using method 1
    dil_img_1 = dilation_method_1(image, element)
    cv2.namedWindow('Dilated image 1', cv2.WINDOW_NORMAL)
    cv2.imshow("Dilated image 1", dil_img_1*255)
    cv2.resizeWindow('Dilated image 1', 600,600)
    cv2.waitKey()
    # dilate image using method 2
    dil_img_2 = dilation_method_1(image, element)
    cv2.namedWindow('Dilated image 2', cv2.WINDOW_NORMAL)
    cv2.imshow("Dilated image 2", dil_img_2*255)
    cv2.resizeWindow('Dilated image 2', 600,600)
    cv2.waitKey()
    # erode an image using method 2
    erod_img_2 = erosion_method_2(image, element)
    cv2.namedWindow('Eroded image 2', cv2.WINDOW_NORMAL)
    cv2.imshow("Eroded image 2", erod_img_2*255)
    cv2.resizeWindow('Eroded image 2', 600,600)
    cv2.waitKey()


    # destory windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv)
