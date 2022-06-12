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


#cv2.imshow("img",image)
#cv2.waitKey(0)
draw = image.copy()

rectangles = list(boundarys)

for rectangle in rectangles:
    print(rectangle)
    top = np.int(rectangle.top())   # idx = 1
    bottom = np.int(rectangle.bottom()) #idx = 3
    left = np.int(rectangle.left()) #idx = 0
    right = np.int(rectangle.right())   #idx = 2




    if rectangle is not None:
        W = -int(left) + int(right)
        H = -int(top) + int(bottom)
        paddingH = 0.01 * W
        paddingW = 0.02 * H
        crop_img = image[int(top+paddingH):int(bottom-paddingH), int(left-paddingW):int(right+paddingW)]
        if crop_img is None:
            continue
        if crop_img.shape[0] < 0 or crop_img.shape[1] < 0:
            continue
        cv2.rectangle(draw, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), 1)

        # for i in range(5, 15, 2):
        #     cv2.circle(draw, (int(rectangle[i + 0]), int(rectangle[i + 1])), 2, (0, 255, 0))

#cv2.imwrite("img/out.jpg",draw)

cv2.imshow("test", draw)
c = cv2.waitKey(0)


