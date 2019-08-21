'''
    Author: Nebiyou Yismaw

    This is a python code that has color transformation implemnetation

'''
# import requried libraries
import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


def convertBGRtoGray(image):
    '''
        This function accepts an image in the BGR color spae and converts it
        to a gray scale image.

        Reference or conversion formula can be found here

        https://docs.opencv.org/4.1.0/de/d25/imgproc_color_conversions.html

    '''
    conv_mat = np.array([0.114, 0.587, 0.299]).reshape(3, 1)
    dtype = image.dtype
#     print (np.min(np.round(np.matmul(image.astype(float), conv_mat).squeeze())))
    return np.round(np.matmul(image.astype(float), conv_mat).squeeze()).astype(np.int32)


def convertBGRtoHSV(image):
    '''
        This function will convert an image in BGR color space an HSV color space. 

    '''
    __image__ = image
    height, width, c = image.shape
    dtype    = image.dtype
    image = image / 255.0
    b, g, r = cv2.split(image)

    v = np.max(image, axis=2).squeeze()
    v_flat = v.flatten()
    v_non_zero = v_flat[v_flat!=0]

    image_min = np.min(image, axis=2).squeeze()
    image_min_flat = image_min.flatten()

    s_flat = np.zeros_like(v_flat).astype(np.float)
    s_flat[v_flat!=0] = np.divide( v_non_zero - image_min_flat[v_flat!=0] , v_non_zero)
    s = s_flat.reshape(height, width)

    H_comp = np.zeros_like(image).astype(np.float16)
    diff_mat = v - image_min

    H_comp[:,:,2] =   0 + np.divide( 60 * (g - b), diff_mat )
    H_comp[:,:,1] = 120 + np.divide( 60 * (b - r), diff_mat )
    H_comp[:,:,0] = 240 + np.divide( 60 * (r - g), diff_mat )

    H_comp = np.nan_to_num(H_comp)
    temp = np.argmax(image, axis=2)
    max_mat = (np.arange(temp.max()+1) == temp[...,None]).astype(np.float)

    mat_mul = np.multiply(H_comp, max_mat)

    h = np.ceil(mat_mul.sum(axis=2))
    h_flat = h.flatten()
    h_flat[h_flat<0] = h_flat[h_flat<0] + 360.0
    h = h_flat.reshape(height, width)

    return np.round(cv2.merge([h / 2, s * 255, v * 255])).astype(np.int32)
