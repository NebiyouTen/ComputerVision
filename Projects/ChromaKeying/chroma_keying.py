'''
    An OpenCV implementation of the matting/chroma keying algorithm

    Nebiyou Yismaw
'''

# import requried libraries
import sys
import cv2
import numpy as np

# let's define global variables
input_img_1 = []
input_img_2 = []
backing_color_1_xy = []
backing_color_2_xy = []
backing_color_index = 0

def compute_alpha():
    '''

    '''

    global backing_color_1_xy
    global backing_color_2_xy
    global backing_color_index
    global input_img
    x,y = backing_color_1_xy
    cf_1 = np.ones_like(input_img) * input_img[x,y]
    x,y = backing_color_2_xy
    cf_2 = np.ones_like(input_img) * input_img[x,y]



    print ( cf_1[0,0,:])
    print ( cf_2[0,0,:])

def callback(action, y, x, flags, userdata):
    '''
        Mouse event callback function
    '''
    global backing_color_1_xy
    global backing_color_2_xy
    global backing_color_index
    global input_img
    # if mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        # get all the candidate patches
        if backing_color_index:
            backing_color_2_xy = [x,y]
            print ("selecting second backing color ", backing_color_2_xy)
            compute_alpha()
        else:
            backing_color_1_xy = [x,y]
            print ("selecting first backing color ", backing_color_1_xy)
        backing_color_index = (backing_color_index + 1) % 2



def main(argv):
    '''
        @main
    '''
    global backing_color_1_xy
    global backing_color_2_xy
    global input_img
    input_img = cv2.imread("greenscreen-demo.jpg")
    input_img_cpy = input_img.copy()
    print (input_img.shape)
    # crete a named window
    cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Window', input_img.shape[0]//2, input_img.shape[0]//2)
    # let's add mouse event handler for our named window
    cv2.setMouseCallback("Window", callback, input_img)
    # exit if esc key is pressed
    k = 0
    while k != 27:
        cv2.imshow("Window", input_img)
        cv2.putText(input_img, 'Press ESC to exit and c to clear',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 0), 2)
        # wait for key
        k = cv2.waitKey(20) & 0xFF
        # if key c is pressed, create the a copy of the original image and
        # pass that to the mouse event callback, which has no circles drawn
        # on it
        if k == 99:
            input_img = input_img_cpy.copy()
    # destroy windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv)
