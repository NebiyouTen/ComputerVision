'''
    Sunglasses filter using open cv
    Nebiyou Yismaw
'''
import cv2
import numpy as np
import sys


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
    blob = cv2.dnn.blobFromImage(
        frameOpencvDnn, 1, (300, 300),  (104.0, 177.0, 123.0), True, False)
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
    return frameOpencvDnn, bboxes, blob[0, 0]


def detect_face(img):
    '''
        Detect faces
    '''
    MODEL_PATH = "../models/"
    modelFile = MODEL_PATH + "res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = MODEL_PATH + "deploy.prototxt"
    # create a Caffe2 model
    face_detector = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    return detectFaceOpenCVDnn(face_detector, img, 0.65)


def norm_to_float(img):
    return (img.astype(np.float) - img.min()) / (img.max() - img.min())


def norm_to_int(img):
    return (((img - img.min()) / (img.max() - img.min()))* 255).astype(np.uint8)

def main(arg):
    '''
        @main
    '''
    # Read images
    musk_img = cv2.imread("musk.jpg")
    sunglass_img = cv2.imread("sunglass.png",-1)
    flower_garden = cv2.imread("flower-garden.jpg", cv2.IMREAD_GRAYSCALE)
    print(f"Musk image: {musk_img.shape} Sunglass image: {sunglass_img.shape}")
    # Detect face
    output_img, boxes, blob = detect_face(musk_img)
    print("BOxes are ", boxes)
    # Find eye regions
    eye_center_x, eye_center_y = (
        boxes[0][0] + boxes[0][2]) // 2, int(boxes[0][1] * 0.6 + boxes[0][3] * 0.4)
    # Scale Sunglasses
    h, w = sunglass_img.shape[:2]
    face_width = boxes[0][2] - boxes[0][0]
    face_height = boxes[0][3] - boxes[0][1]
    print("Size of glasses is ", h, w, "face width ",face_width)
    # put sung Sunglasses
    print ("output shape is ",eye_center_x - h // 2, eye_center_x + (h + 1) // 2)
    print ("outptu shape 2 is ", eye_center_y - w // 2,eye_center_y + (w + 1) // 2)
    scale_w = face_width / w
    sunglass_img = cv2.resize(sunglass_img, (0,0), fx =scale_w, fy =scale_w)
    h, w = sunglass_img.shape[:2]
    print ("Shape after resizing is ", sunglass_img.shape)
    slice_x = slice(eye_center_y - h // 2, eye_center_y + (h + 1) // 2)
    slice_y = slice(eye_center_x - w // 2, eye_center_x + (w + 1) // 2)
    final_img = norm_to_float(output_img.copy())
    mask = cv2.merge((sunglass_img[:,:,3],sunglass_img[:,:,3],sunglass_img[:,:,3]))
    # print (mask.max())
    mask_1 = mask.astype(np.float) / 255.0 * 0.7
    # print (mask.max(), mask.min())
    final_img[slice_x, slice_y] = cv2.multiply(norm_to_float(sunglass_img[:,:,:3]).astype(np.float), mask_1)
    final_img[slice_x, slice_y] += cv2.multiply(norm_to_float(output_img[slice_x, slice_y]),  (1 -mask_1))
    # do some processing to sun glasese to make it look more realistic
    # Apply reflection
    mask_2 = mask.astype(np.float) / 255.0 * 0.5

    flower_garden = cv2.merge((flower_garden, flower_garden, flower_garden))
    flower_garden = flower_garden[:h,:w]
    print ("Mask and garden",flower_garden.shape, mask_2.shape)
    cv2.multiply(norm_to_float(flower_garden), mask_1)
    final_img[slice_x, slice_y] += cv2.multiply(norm_to_float(flower_garden).astype(np.float), mask_2)
    cv2.imshow("Face detection", norm_to_int(final_img))
    cv2.waitKey()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv)
