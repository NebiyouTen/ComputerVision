'''
    An OpenCV implementation of the matting/chroma keying algorithm

    Nebiyou Yismaw
'''

# import requried libraries
import sys
import cv2
import numpy as np
import time

# let's define global variables
backing_color_1_xy = None
cb = [1,0,0]
beta = 0.5
tolerance = 100
smoothness = 18
defringe = 18
maxScaleUp = 100



'''
    A function that will normaliz an image so that the pixels will be in the [0, 255]
    range and will return a unit8 version
'''
def normalize_img(image):
    return np.uint8( 255 *  (image - np.min(image)) / (np.max(image) - np.min(image)) )

def compute_alpha(input_img_1):
    '''

    '''

    global backing_color_1_xy
    global tolerance
    global smoothness
    global defringe

    img_ycrcb = cv2.cvtColor(input_img_1, cv2.COLOR_BGR2YCR_CB).astype(np.float64)

    x, y = backing_color_1_xy
    cr_k, cb_k = img_ycrcb[x, y, 1:]

    dis = np.sum((img_ycrcb[:, :, 1:] - img_ycrcb[x, y, 1:][None,None,:])**2, axis=-1)

    alpha = np.zeros_like(dis).astype(np.float64)

    tol_low =  max(tolerance / 100 * dis.max(), 10)
    alpha[dis > tol_low] = 1#(dis[dis > tol_low] - tol_low) / (dis.max() - tol_low)

    return alpha

def get_new_img(src_img, alpha):
    '''

    '''
    global backing_color_1_xy

    x, y = backing_color_1_xy
    src_img = (src_img.astype(np.float64) - src_img.min()) / ( src_img.max() - src_img.min() )
    alpha = (1-alpha)[:,:,None]
    co = src_img - alpha * src_img[x, y, :]
    co[co<0] = 0
    c = co + alpha * cb
    print ("co",co.max(), co.min())
    return normalize_img(c)


def callback(action, y, x, flags, userdata):
    '''
        Mouse event callback function
    '''
    global backing_color_1_xy
    # if mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        backing_color_1_xy = [x, y]


def get_track_bar_data(val, type):
    '''

    '''
    global tolerance
    global smoothness
    global defringe
    if type == 0:
        tolerance = val
    elif type == 1:
        smoothness = val
    else:
        defringe = val
    print ("Values are ",tolerance, smoothness, defringe, val, type )




def main(argv):
    '''
        @main
    '''
    global backing_color_1_xy, tolerance, smoothness, defringe
    # crete a named window
    cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow(
        'Window', 720, 720)
    cv2.putText(None,'''Click anywhere to pick a color''' ,
                (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                1,(255,255,255), 2 );
    # let's add mouse event handler for our named window
    cv2.setMouseCallback("Window", callback, None)
    # create a video capture object by passing a file name
    cap = cv2.VideoCapture('greenscreen-demo.mp4')
    cv2.createTrackbar("Tolerance", "Window",
                       tolerance, maxScaleUp, lambda x: get_track_bar_data(x, 0))
    cv2.createTrackbar("Smoothness", "Window",
                       smoothness, maxScaleUp, lambda x: get_track_bar_data(x, 1))
    cv2.createTrackbar("Defringe", "Window",
                      defringe, maxScaleUp, lambda x: get_track_bar_data(x, 2))
    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
    else: # if capture object is opened successfully
        # while capture object is opened
        i = 0
        while(cap.isOpened()):
          # Capture frame-by-frame
          ret, input_img_1 = cap.read()
          if ret == True:
              if backing_color_1_xy is not None:
                  alpha = compute_alpha(input_img_1)
                  img = get_new_img(input_img_1, alpha)
                  cv2.putText(img,'''Click anywhere to pick a color''' ,
                              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                              1.5,(123,53,202), 2 );
                  cv2.imshow('Window', img)

              else:
                  cv2.putText(input_img_1,'''Click anywhere to pick a color''' ,
                              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                              1.5,(123,53,202), 2 );
                  cv2.imshow('Window',input_img_1)
              if cv2.waitKey(25) & 0xFF == 27:
                  break
              # Display the resulting frame

    # destroy windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv)
