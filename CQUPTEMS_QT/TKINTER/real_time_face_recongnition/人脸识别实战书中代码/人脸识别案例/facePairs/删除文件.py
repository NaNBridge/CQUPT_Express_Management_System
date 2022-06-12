from pathlib import Path
import numpy as np
import dlib
import matplotlib.image as mpimg
import cv2
import imageio
from pathlib import Path
import os
from tqdm import tqdm

path = "C:/facepairs/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]

print("开始清理~")
for file_dir in tqdm(file_dirs):
    image_path_list = list(file_dir.glob('*.jpg'))
    for image_path in (image_path_list):
        image = np.array(mpimg.imread(image_path))
        if image.shape[0] == 128 and image.shape[1] == 128:
            pass
        elif image.shape[0] == 144 and image.shape[1] == 144:
            image_new = cv2.resize(image,(128,128))
            os.remove(image_path)
            imageio.imsave(image_path, image_new)
        else:
            os.remove(image_path)