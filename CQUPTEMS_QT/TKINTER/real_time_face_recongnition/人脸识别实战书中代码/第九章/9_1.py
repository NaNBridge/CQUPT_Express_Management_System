import cv2

image = cv2.imread("./dataset/lfw-deepfunneled/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")	#使用openCV读取图片
cv2.imshow("image",image)	#展示图片结果
cv2.waitKey(0)	#暂停进程，按空格恢复
