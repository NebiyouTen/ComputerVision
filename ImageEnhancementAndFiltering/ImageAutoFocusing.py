'''
    Author: Nebiyou Yismaw

    This is a python code will use convolution to find sharpness of an image.
    It uses appriximations of laplacian of image to compute second derivates
    to compute sharpness of an image. This technique can be used to get the
    sharpest image in a sequence of image frames.

    Two methods will be used to compute image sharpness
    1. Variance of absolute values of Laplacian  http://optica.csic.es/papers/icpr2k.pdf
    2. Sum Modified Laplacian (SML) http://www1.cs.columbia.edu/CAVE/publications/pdfs/Nayar_TR89.pdf

'''


def get_lap_app_kernel():
    '''
        A function to return an approximate kernel mask for the Laplacian operator
    '''
    return np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]).astype(np.float32) / 6

def get_app_kernel_x():
    '''
        A function to return an approximate kernel mask for the x second order derivative for modfied Laplaican
    '''
    return np.array([[0,0,0],[-1,2,-1],[0,0,0]]).astype(np.float32)

def get_app_kernel_y():
    '''
        A function to return an approximate kernel mask for the y second order derivative for modfied Laplaican
    '''
    return np.array([[0,-1,0],[0,2,0],[0,-1,0]]).astype(np.float32)


def var_abs_laplacian(image):
    '''
        Variance of absolute values of Laplacian - Method 1
        Input: image
        Output: Floating point number denoting the measure of sharpness of image
    '''
    # convert image to gray
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # get approximating kernel
    kernel     = get_lap_app_kernel()
    # gaussian blurring
    image_blur = cv2.GaussianBlur(image_gray,(3,3),0,0)
    # calculate L(m,n), which is the output of the convolution of our image with
    # the laplacian approximate mask
    L = cv2.filter2D(image_blur, cv2.CV_32F, kernel, (-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)
    # Calculate the variance of the absolute values
    LAP_VAR = np.square(np.abs(L) - np.mean(np.abs(L)))
    # return the sum of LAP_VAR
    return np.sum(LAP_VAR)


def sum_modified_laplacian(im):
    '''
        Implement Sum Modified Laplacian - Method 2
        Input: image
        Output: Floating point number denoting the measure of sharpness of image
    '''
    # convert image to gray
    image_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # get approximating kernel for x derivative
    kernel_x     = get_app_kernel_x()
    # get approximating kernel for y derivative
    kernel_y     = get_app_kernel_y()
    # gaussian blurring
    image_blur = cv2.GaussianBlur(image_gray,(3,3),0,0)
    # get 2nd or derivative in x and y
    L_x = cv2.filter2D(image_blur, cv2.CV_32F, kernel_x, (-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)
    L_y = cv2.filter2D(image_blur, cv2.CV_32F, kernel_y, (-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)
    ML  = np.abs(L_x) + np.abs(L_y)
    return np.sum(ML)
