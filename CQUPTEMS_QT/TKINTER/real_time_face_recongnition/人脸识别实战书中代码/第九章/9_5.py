import cv2
import dlib
import numpy as np

image = cv2.imread("./dataset/lfw-deepfunneled/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")

detector = dlib.get_frontal_face_detector()  # 切割器
boundarys = detector(image, 2)
print(list(boundarys))

draw = image.copy()

rectangles = list(boundarys)

for rectangle in rectangles:
    top = np.int(rectangle.top())  # idx = 1
    bottom = np.int(rectangle.bottom())  # idx = 3
    left = np.int(rectangle.left())  # idx = 0
    right = np.int(rectangle.right())  # idx = 2

    W = -int(left) + int(right)
    H = -int(top) + int(bottom)
    paddingH = 0.01 * W
    paddingW = 0.02 * H
    crop_img = image[int(top + paddingH):int(bottom - paddingH), int(left - paddingW):int(right + paddingW)]

    # 进行切割放大
    crop_img = cv2.resize(crop_img, dsize=(128, 128))
    cv2.imshow("test", crop_img)
    c = cv2.waitKey(0)
