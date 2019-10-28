
# coding: utf-8

# # <font style = "color:rgb(50,120,229)">Skin Smoothing</font>
# 
# In previous modules we have seen how we can use grabcut for detecting skin region given the image of a face. The detected skin can then be smoothened and applied back to the original image, thereby resulting in a skin smoothened image. 
# 
# In this project, you will be implementing **Skin Smoothing** but this time the image will contain regions other than face as well and will have to be completely automated.
# 
# You can use the following steps to approach this problem:
# 
# 1. Detect the faces in the image using Deep Learning or HAAR Cascades
# 2. Iterate over the detected faces and apply smoothing filter. You can experiment with the filter type and size to see which one (or combination) gives the best result.

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from dataPath import DATA_PATH
get_ipython().magic('matplotlib inline')


# In[2]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0,6.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# In[3]:


# Read image
img = cv2.imread(DATA_PATH + "images/hillary_clinton.jpg")


# In[4]:


plt.imshow(img[:,:,::-1])
plt.title("Input Image")
plt.show()


# In[5]:


# get the model path 
MODEL_PATH = "resource/lib/publicdata/models/"
modelFile = MODEL_PATH + "res10_300x300_ssd_iter_140000_fp16.caffemodel"
configFile = MODEL_PATH + "deploy.prototxt"
# create a Caffe2 model
face_detector = cv2.dnn.readNetFromCaffe(configFile, modelFile)
img.shape


# ### Detector function
# 

# In[6]:


def detectFaceOpenCVDnn(net, frame, conf_threshold):
    '''
        This detector function accepts a pre-trained model and an image. 
        It returnes boudning boxes and the original image with the boudning 
        box drawn on it
    '''
    # copy the image
    frameOpencvDnn = frame.copy()
    # get image height and width
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    # create a bolb image to pass it to the detector
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1, (300, 300),  (104.0, 177.0, 123.0), True, False)
    # do a forward pass on our network
    net.setInput(blob)
    detections = net.forward()
    # get the best bounding box, since we know we already have on 
    # face in the image
    i = np.argmax(detections[0, 0, :, 2])
    bboxes = []
    confidence = detections[0, 0, i, 2]
    if confidence > conf_threshold:
        x1 = int(detections[0, 0, i, 3] * frameWidth)
        y1 = int(detections[0, 0, i, 4] * frameHeight)
        x2 = int(detections[0, 0, i, 5] * frameWidth)
        y2 = int(detections[0, 0, i, 6] * frameHeight)
        bboxes.append([x1, y1, x2, y2])
        cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)))
    return frameOpencvDnn, bboxes, blob[0,0]


# ## Detect face and show bounding box

# In[7]:


output_img, boxes, blob = detectFaceOpenCVDnn(face_detector, img, 0.65)
plt.imshow(output_img[:,:,::-1])
plt.title("Image with face detected")
plt.show()
print (boxes)
# print (np.divide(boxes[1],boxes[0]))


# ## Get skin mask (skin detection)

# In[8]:


def get_skin_mask(image, bbox):
    '''
        function to return a face mask
    '''
    forhead_loc = [ bbox[1] + 100, (bbox[0] + bbox[2]) // 2  ]
    cheeck_loc = [(bbox[1] + bbox[3])//2, bbox[0] + 50 ]
    
    forehead_region = img[forhead_loc[1] - 10 : forhead_loc[1] + 10, forhead_loc[0] - 10: forhead_loc[0]+10,  :] 
    cheeck_region = img[cheeck_loc[0] - 10 : cheeck_loc[0] + 10, cheeck_loc[1] - 10: cheeck_loc[1] + 10, :]
    
    max_f, min_f = np.amax(forehead_region, axis =  (0,1)), np.min(forehead_region, axis = (0,1))
    max_c, min_c = np.amax(cheeck_region, axis = (0,1)), np.min(cheeck_region, axis = (0,1))
    _max_, _min_ = np.mean([max_f, max_c], axis=0) + 25, np.mean([min_c, min_f], axis=0) - 25
    print ( _min_, _max_, min_c, max_c )
    mask = cv2.inRange(image, _min_, _max_)
   
    return mask
    
    
mask = get_skin_mask(img, boxes[0])
# apply a series of erosions and dilations to the mask
# using an elliptical kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask = cv2.erode(mask, kernel, iterations = 1)
mask = cv2.dilate(mask, kernel, iterations = 1)
# mask = cv2.dilate(mask, kernel, iterations = 2)

# blur the mask to help remove noise, then apply the
# mask to the frame
mask = cv2.GaussianBlur(mask, (3, 3), 0)
mask[mask>0] = 1
mask[mask<=0] = 0


# ## Skin smoothing

# In[9]:


# Defining the kernel size
kernelSize = 7
# Performing Median Blurring and store it in numpy array "medianBlurred"
medianBlurred = cv2.medianBlur(img, kernelSize)
final_img = medianBlurred * mask[:,:,None] + img * (1 - mask[:,:,None])
f, axarr = plt.subplots(1,2,figsize=(15,15))
axarr[0].imshow(img[:,:,::-1])
axarr[0].title.set_text("Original image")
axarr[1].imshow(final_img[:,:,::-1])
axarr[1].title.set_text("Revised image")

