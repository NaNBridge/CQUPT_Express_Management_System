import numpy as np
import dlib
import matplotlib.image as mpimg
import cv2
import imageio
from pathlib import Path
import os
from tqdm import tqdm
shape = 128

def clip_image(image, boundary):
    top = np.clip(boundary.top(), 0, np.Inf).astype(np.int16)
    bottom = np.clip(boundary.bottom(), 0, np.Inf).astype(np.int16)
    left = np.clip(boundary.left(), 0, np.Inf).astype(np.int16)
    right = np.clip(boundary.right(), 0, np.Inf).astype(np.int16)
    image = cv2.resize(image[top:bottom, left:right],(128,128))
    return image

def fun(file_dirs,start,end):
    print("here test：",str(start),"-",str(end))
    for file_dir in tqdm(file_dirs[start:end]):
        image_path_list = list(file_dir.glob('*.jpg'))
        for image_path in image_path_list:
            image = np.array(mpimg.imread(image_path))
            boundarys = detector(image, 2)
            if len(boundarys) == 1:
                image_new = clip_image(image, boundarys[0])
                os.remove(image_path)
                image_path_new = image_path #这里可以对保存的地点调整路径
                imageio.imsave(image_path_new, image_new)
            else:
                os.remove(image_path)   #原来的话，这里有问题的图片没有被删除

detector = dlib.get_frontal_face_detector() #切割器
path="E:/pairs_face_dataset/train/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]

print(len(file_dirs))   #已经做完3500
fun(file_dirs,start=8000,end=8631)





# image  = np.array(mpimg.imread(image_path))
# detector = dlib.get_frontal_face_detector()
# boundary = detector(image, 2)
#
# image_new = clip_image(image,boundary[0])
# imageio.imsave("./1.jpg",image_new)

