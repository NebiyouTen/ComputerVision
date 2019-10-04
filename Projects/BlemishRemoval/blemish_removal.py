'''
    Blemish removal using OpenCV

    Nebiyou Yismaw

    This program will allow the user to click on a point of an image. It has a
    specified radius and will look for a patch of images centered at point +/-
    the radius. These points are found using the patch_inds list. To find each
    path every element in the patch_inds list will be used. It's found using the
    equation center = (x,y) + i * (radius), where i is each element in the patch_inds
    list. After finding these patches, Fourier transform is used to find the
    smoothest patch. Once it's found, it will be copied to our original image
     using seamless cloning.

'''

import matplotlib
import matplotlib.pyplot as plt
import sys
import cv2
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)
# configure matplot lib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# coordiante for patches relative to belmish, these are realtive to the selected
# point and will be scaled by our radius
patch_inds = [[0, -1], [1, -1], [1, 0],
              [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]


def compute_ft(image):
    '''
        Compute FT. This function will compute the fourier transform of our image
    '''
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dft = cv2.dft(np.float32(image_gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    return magnitude_spectrum


def get_slice(x, a, radius):
    '''
        A fuction to return slice given a point, a direction (slope) and a radius
    '''
    center = x + a * radius
    return slice(center - radius, center + radius)


def get_patches(x, y, radius, image):
    '''
        A function to return a list of patches. Given a specific pixel this
        function will return a list of patches around that point. For each
        element in the patch indices, it will append the corresponding patch
        and append it to our list. Finally returns the list.
    '''
    patches = []
    patches.extend(image[get_slice(x, j, radius), get_slice(
        y, i, radius), :] for j, i in patch_inds)
    return patches


def callback(action, y, x, flags, userdata):
    '''
        Mouse event callback function
    '''
    global src_img
    # define a radious around our given point
    radius = 14
    # if mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        # get all the candidate patches
        pathces = get_patches(x, y, radius, userdata)
        orig = compute_ft(
            userdata[x - radius:x + radius, y - radius: y + radius, :])
        spec_means = np.array([compute_ft(patch).mean() for patch in pathces])
        best_patch = pathces[spec_means.argmin()]
        if orig.mean() > spec_means.min():
            # best_patch = np.zeros_like(best_patch)
            mask = 255 * np.ones(best_patch.shape, best_patch.dtype)
            # img = userdata
            __before__ = np.copy(src_img)
            # src_img[x-radius:x+radius,y-radius:y+radius,:] = best_patch
            src_img = cv2.seamlessClone(
                best_patch, src_img, mask, (y, x), cv2.NORMAL_CLONE)
            # show image
            __after__ = np.copy(src_img)
            cv2.imshow("Window", src_img)


src_img = []


def main(argv):
    '''
        @main
    '''
    # get image source
    global src_img
    src_img = cv2.imread("blemish.png")
    print("Image size is ", src_img.shape)
    # let's copy this iamge
    src_img_cpy = src_img.copy()
    # crete a named window
    cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Window', 720, 720)
    # let's add mouse event handler for our named window
    cv2.setMouseCallback("Window", callback, src_img)
    # exit if esc key is pressed
    # show image
    print(" Starting mean is ", src_img.mean())
    k = 0
    while k != 27:
        cv2.imshow("Window", src_img)
        cv2.putText(src_img, 'Press ESC to exit and c to clear',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 0), 2)
        # wait for key
        k = cv2.waitKey(20) & 0xFF
        # if key c is pressed, create the a copy of the original image and
        # pass that to the mouse event callback, which has no circles drawn
        # on it
        if k == 99:
            src_img = src_img_cpy.copy()
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
