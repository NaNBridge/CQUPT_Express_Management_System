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

path = "C:/facepairs/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]

start = 0
end = start + 10000

print("现在开始做写入NPY操作，总文件夹数目为：",len(file_dirs),"分段为：",start,"-",end)    #86876
image_lists = []
for file_dir in tqdm(file_dirs[start:end]):
    image_path_list = list(file_dir.glob('*.jpg'))

    image_list = []
    if len(image_path_list) > 2:
        for image_path in image_path_list:
            image = np.array(mpimg.imread(image_path))
            image_list.append(image)
    image_lists.append(image_list)

new_path = "C:/facepairs_NPY/" + str(start) + "_" + str(end) + ".npy"
np.save(new_path,image_lists)





