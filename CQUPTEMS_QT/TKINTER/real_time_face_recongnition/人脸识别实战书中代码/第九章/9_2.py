import cv2
import dlib

image = cv2.imread("./dataset/lfw-deepfunneled/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")


detector = dlib.get_frontal_face_detector() #Dlib创建的检测器
boundarys = detector(image, 2)	#对人脸图片进行检测，找到人脸的位置框
print(list(boundarys))	#打印位置框内容
