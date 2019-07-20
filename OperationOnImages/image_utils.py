'''
    Author: Nebiyou Yismaw

    This is a python code that will have different image utilties. These are
    mainly wrappers around functions provided by OpenCV.
'''
# import requried libraries
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
# configure matplot lib
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

'''
    Function to read an image:
        Args: path: path to the image
              flag: flag for image foramt. default = 1
        Ret : image numpy array
'''
def read_image(path, flag = 1):
    return cv2.imread(path, flag)

'''
    Function to print image properties
        Args: image: image array
'''
def print_image_props(image):
    print("Data type = {}".format(image.dtype))
    print("Object type = {}".format(type(image)))
    print("Image Dimensions = {}".format(image.shape))

'''
    Function to display an image
    Args: image     : image array
          use_matlib: flag param used to use opencv or matlib for display
'''
def display_image(image, use_matlib = False):
    if use_matlib:
        plt.imshow(image)
        plt.colorbar()
    else:
        cv2.imshow("Image", image )
        cv2.resizeWindow('Image', 600,600)
        # wait for a key input
        cv2.waitKey()
        # then destory images
        cv2.destroyAllWindows()

'''
    Function to save an image
    Args: image     : image array
          file_name : output file name
'''
def save_image(image, file_name):
    cv2.imwrite(file_name, image)

'''
    Function to split an image
    Args: split_image: image array
    Ret:  B, G, R image channels
'''
def split_image(image):
    return cv2.split(image)

'''
    Function to merge image channles
    Args: split_image: image array
    Ret:  B, G, R image channels
'''
def merge_channels(image):
    return cv2.merge(image)


'''
    Function to crop an image
    Args: image: image array
          h1   : crop boundary start height
          h2   : crop boundary end height
          w1   : crop boundary start width
          w2   : crop boundary end width
    Ret:  cropped image array
'''
def crop_image(image, h1, h2, w1, w2):
    return np.copy(image[h1:h2, w1:w2])


'''
    Function to resize an image
    Args: image: image to be resized
    return: Resized image
'''
def resize_image(image, size = None, scale_h = 0, scale_w = 0, interp = None):
    return np.copy(cv2.resize(image, size, fx =scale_w, fy =scale_h, interpolation = interp))

'''
    Function to enhance contrast
    Args: image: image array
          alpha: scale to enhance contrast.
'''
def enhance_contrast(image, alpha):
    return np.uint8(np.clip(image * alpha, 0, 255))

'''
    Function to enhance brightness
    Args: image: image array
          beta : scale to enhance brightness.
'''
def enhance_brightness(image, beta):
    beta_array = beta * np.ones_like(image)
    return np.copy(cv2.add(image, beta_array.astype(np.uint8)))
