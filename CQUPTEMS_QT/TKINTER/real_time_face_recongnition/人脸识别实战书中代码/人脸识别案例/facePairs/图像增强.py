import matplotlib.image as mpimg
import cv2
import imageio
from pathlib import Path
import os
import numpy as np
from tqdm import tqdm

import dlib
detector = dlib.get_frontal_face_detector() #切割器
def clip_image(image, boundary):
    top = np.clip(boundary.top(), 0, np.Inf).astype(np.int16)
    bottom = np.clip(boundary.bottom(), 0, np.Inf).astype(np.int16)
    left = np.clip(boundary.left(), 0, np.Inf).astype(np.int16)
    right = np.clip(boundary.right(), 0, np.Inf).astype(np.int16)
    image = cv2.resize(image[top:bottom, left:right],(128,128))
    return image

path = "E:/VGGFACE2/msra/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]
print("总文件夹数目为：",len(file_dirs))    #86876
start = 22000
end = start + 2000
print("现在计算的是",start,"-",end)
counter = start
for file_dir in tqdm(file_dirs[start:end]):
    new_path = "C:/facepairs/msra_" + str(counter)
    if os.path.exists(new_path):
        counter += 1
    else:
        os.makedirs(new_path)
        counter += 1

        image_path_list = list(file_dir.glob('*.jpg'))

        image_counter = 0
        for image_path in image_path_list:
            image = np.array(mpimg.imread(image_path))
            boundarys = detector(image, 2)

            if len(boundarys) == 1:
                image_new = clip_image(image, boundarys[0])
                image_path_new = new_path + "/msra_" + str(counter) + "_" + str(image_counter) + ".jpg"  # 这里可以对保存的地点调整路径
                imageio.imsave(image_path_new, image_new)
                image_counter += 1




# with tf.device("/CPU:0"):
#     image_path = "E:/face_DATA/lfw_160_none/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"
#     img = mpimg.imread(image_path)
#     #img_1 = cv2.resize(img_1, (128, 128))
#     image_path_new = "C:/face_DATA/lfw_160_none/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"
#     imageio.imsave(image_path_new, img)

    #image = tf.image.random_flip_left_right(image)
    #image = tf.image.random_jpeg_quality(image,80,100)



