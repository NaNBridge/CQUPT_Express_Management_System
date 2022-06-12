import dlib
import cv2
import numpy as np

detector = dlib.get_frontal_face_detector() #切割器

img_path = "./dataset/lfw/10240.jpg"
image = (cv2.imread(img_path))

boundarys = detector(image, 2)
print(list(boundarys))

rec_box_list = np.load("./dataset/lfw/rec_box_list.npy")
print(rec_box_list[10240])
