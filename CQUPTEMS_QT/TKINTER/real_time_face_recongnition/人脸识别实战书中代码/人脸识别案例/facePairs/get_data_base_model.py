import tensorflow as tf
import numpy as np
import gc
import os
import config
import numpy as np
from tqdm import tqdm

img_splited_resized_saver_list = []

img_splited_resized_saver_list_64_CASIA_FaceV5 = np.load("E:/face/64_CASIA-FaceV5/img_splited_resized_saver_0_-1.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_64_CASIA_FaceV5):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_64_CASIA_FaceV5
gc.collect()
print("64_CASIA_FaceV5 done!")

img_splited_resized_saver_list_lfw_none = np.load("E:/face/lfw/img_splited_resized_saver2_0_-1.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_lfw_none):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_lfw_none
gc.collect()
print("list_lfw_none done!")

img_splited_resized_saver_list_cut144_1 = np.load("E:/face/cut144-simi1/img_splited_resized_saver_0_100000.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_cut144_1):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_cut144_1
gc.collect()
print("cut144_1 done!")

img_splited_resized_saver_list_cut144_2 = np.load("E:/face/cut144-simi1/img_splited_resized_saver_100000_200000.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_cut144_2):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_cut144_2
gc.collect()
print("cut144_2 done!")

img_splited_resized_saver_list_cut144_3 = np.load("E:/face/cut144-simi1/img_splited_resized_saver_200000_313160.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_cut144_3):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_cut144_3
gc.collect()
print("cut144_3 done!")

img_splited_resized_saver_list_chs_stars_512px = np.load("E:/face/chs_stars_512px/img_splited_resized_saver_0_-1.npy", allow_pickle=True)
for _img in tqdm(img_splited_resized_saver_list_chs_stars_512px):
    img_splited_resized_saver_list.append(_img/255. )
del img_splited_resized_saver_list_chs_stars_512px
gc.collect()
print("chs_stars_512px done!")


print("start_shuffle")
np.random.seed(17);np.random.shuffle(img_splited_resized_saver_list)

print(img_splited_resized_saver_list.shape)

print("start_splited")
val_img_splited_resized_saver_list = np.array(img_splited_resized_saver_list[-5836:])
val_target_image_embedding_list = np.ones([5836])

img_splited_resized_saver_list = np.array(img_splited_resized_saver_list[:370000])


train_length = len(img_splited_resized_saver_list)
def generator(batch_size = 128):
    batch_num = (train_length) // batch_size

    while 1:
        seed = int(np.random.random() * 1000)
        np.random.seed(seed);np.random.shuffle(img_splited_resized_saver_list)

        for i in range(batch_num):
            start = batch_size * i
            end = batch_size * (i + 1)

            real_image_batch = img_splited_resized_saver_list[start:end]
            real_label_batch = np.ones([batch_size])

            fake_image_batch = np.random.normal(loc=np.mean(real_image_batch),scale =np.std(real_image_batch) ,size=[batch_size,config.Config.width,config.Config.height,3]) + np.random.random()/5.217
            fake_label_batch = np.zeros([batch_size])

            image_batch = np.concatenate([real_image_batch,fake_image_batch])
            label_batch = np.concatenate([real_label_batch,fake_label_batch])

            np.random.seed(seed);np.random.shuffle(image_batch)
            np.random.seed(seed);np.random.shuffle(label_batch)

            yield image_batch,label_batch





