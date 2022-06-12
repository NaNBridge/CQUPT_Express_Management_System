import cv2
import dlib
import numpy as np

image = cv2.imread("./dataset/lfw-deepfunneled/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")

detector = dlib.get_frontal_face_detector()  # 切割器
boundarys = detector(image, 2)

rectangles = list(boundarys)

draw = image.copy()
for rectangle in rectangles:
    top = np.int(rectangle.top())  # idx = 1
    bottom = np.int(rectangle.bottom())  # idx = 3
    left = np.int(rectangle.left())  # idx = 0
    right = np.int(rectangle.right())  # idx = 2

    W = -int(left) + int(right)  # 获取人脸框体的宽度
    H = -int(top) + int(bottom)  # 获取人脸框体的高度
    paddingH = 0.01 * W
    paddingW = 0.02 * H
    # 将人脸的图片单独“切割出来”
    crop_img = image[int(top + paddingH):int(bottom - paddingH), int(left - paddingW):int(right + paddingW)]
    # 进行人脸框体描绘
    cv2.rectangle(draw, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), 1)

    cv2.imshow("test", draw)
    c = cv2.waitKey(0)
