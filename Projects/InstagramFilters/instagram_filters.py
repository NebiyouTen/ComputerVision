''''

    Nebiyou Yismaw

    Pencil scketch and cartoonify filters using OpenCV
    
''''

import cv2
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')


# In[2]:


import matplotlib
import matplotlib.cm as cm
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# In[3]:


def pencilSketch(image, arguments=0):
    # convert color to Gray
    image_GRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Applying a gaussian blur
    image_Blur = cv2.GaussianBlur(image_GRAY,(3,3),0,0)
    # Applying laplacian
    lap = cv2.Laplacian(image_Blur, -1, ksize=5)
    # inverse threshold image
    _, output = cv2.threshold(lap, 100, 255, cv2.THRESH_BINARY_INV)
    return cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

lowThreshold = 150
highThreshold = 160
apertureSize = 3
blur_amt = 1

def cartoonify(image, arguments=0):
    img = image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9,2)

    color = cv2.bilateralFilter(img, 9, 0, 250)

    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


imagePath = "trump.jpg"
image = cv2.imread(imagePath)

cartoonImage = cartoonify(image)
pencilSketchImage = pencilSketch(image)

plt.figure(figsize=[20,10])
plt.subplot(131);plt.imshow(image[:,:,::-1]);
plt.subplot(132);plt.imshow(cartoonImage[:,:,::-1]);
plt.subplot(133);plt.imshow(pencilSketchImage[:,:,::-1]);
