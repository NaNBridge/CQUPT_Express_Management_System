import cv2
import matplotlib.pyplot as plt
# 读取图片
img = cv2.imread('../img/face_pictures/龚南桥_fixed.jpg')
# print(f'type: {type(img)}')
# plt.axis('off')
plt.imshow(img)