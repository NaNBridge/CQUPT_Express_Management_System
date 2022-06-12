import cv2
import dlib
import numpy as np

image = cv2.imread("./dataset/lfw-deepfunneled/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")


detector = dlib.get_frontal_face_detector() #Dlib创建的切割器
boundarys = detector(image, 2)	#找到人脸框的坐标，没有则返回空集
print(list(boundarys))	#打印结果

draw = image.copy()

rectangles = list(boundarys)

for rectangle in rectangles:
    top = np.int(rectangle.top())   # idx = 1
    bottom = np.int(rectangle.bottom()) #idx = 3
    left = np.int(rectangle.left()) #idx = 0
    right = np.int(rectangle.right())   #idx = 2

print([left,top,right,bottom])
