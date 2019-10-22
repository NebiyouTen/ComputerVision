'''
    Skin smoothing

    Nebiyou Yismaw
'''


import cv2
import numpy as np


def main():
    '''
        @main
    '''
    img = cv2.imread("hillary_clinton.jpg")
    cv2.imshow("Input Image", img)
    cv2.waitKey()

    MODEL_PATH = "../models/"
    modelFile = MODEL_PATH + "../models/res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = MODEL_PATH + "deploy.prototxt"
    # create a Caffe2 model
    face_detector = cv2.dnn.readNetFromCaffe(configFile, modelFile)

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
        blob = cv2.dnn.blobFromImage(cv2.resize(
            frameOpencvDnn, (300, 300)), 1, (300, 300),  (104.0, 177.0, 123.0), False, False)
        print(blob.shape)
        # do a forward pass on our network
        net.setInput(blob)
        detections = net.forward()
        bboxes = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                print(confidence)
                print(detections[0, 0, i, 3:])
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                bboxes.append([x1, y1, x2, y2])
                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2),
                              (0, 255, 0), int(round(frameHeight / 150)))
        return frameOpencvDnn, bboxes, blob[0, 0]

    output_img, boxes, blob = detectFaceOpenCVDnn(face_detector, img, 0.9999842)
    cv2.imshow("Output image", output_img)
    cv2.waitKey()
    print(boxes)


if __name__ == "__main__":
    main()
