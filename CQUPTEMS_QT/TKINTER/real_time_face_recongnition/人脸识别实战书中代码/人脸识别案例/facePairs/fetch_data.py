from pathlib import Path
import tensorflow as tf
import numpy as np
import random
import cv2
import config
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from tqdm import tqdm

image_path_1_list = list(Path("D:/1000/1/").glob('*.jpg'))
image_path_2_list = list(Path("D:/1000/2/").glob('*.jpg'))

image_1_list = []
image_2_list = []
for image_1,image_2 in zip(image_path_1_list,image_path_2_list):

    img_1 = mpimg.imread(image_1)
    img_1 = cv2.resize(img_1, (128, 128))
    image_1_list.append(img_1)

    img_2 = mpimg.imread(image_2)
    img_2 = cv2.resize(img_2, (128, 128))
    image_2_list.append(img_2)

image_1_list = np.array(image_1_list)
image_2_list = np.array(image_2_list)



path = "./dataset/lfw/"
path = Path(path)
file_dir = [x for x in path.iterdir() if x.is_dir()]

# 这里的num_people是指每个batch中有多少个人
# k指的是每个people出多少张图做比对
train_length = len(file_dir)
def generator(k=15, num_people=12):
    batch_num = train_length // num_people

    while 1 :
        np.random.shuffle(file_dir)

        for i in range(batch_num):
            start = num_people * i
            end = num_people * (i + 1)

            image_batch = []
            label_batch = []

            for j in range(start, end):
                pos_path = list(file_dir[j].glob('*.jpg'))
                if len(pos_path) > 5:
                    for image_path in random.choices(pos_path, k=k):
                        img = mpimg.imread(image_path.as_posix())/255.
                        image_batch.append(img)
                        label_batch.append(j)
            yield np.array(image_batch), np.array(label_batch)

