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


def xiaohua_distance(vec_1,vec_2):
    vec_1 = np.array(vec_1)
    vec_2 = np.array(vec_2)

    dist = np.sum(np.abs(vec_1 - vec_2))
    return dist


"---------------------------------------------------------------------------------"
split_num = 40
path = "C:/facepairs/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]
file_dirs_length = len(file_dirs)
# face_pairs_list = []
# print("开始读取数据进入内存~")
# for file_dir in tqdm(file_dirs):
#     image_path_list = list(file_dir.glob('*.jpg'))
#     if len(image_path_list) > 7:    #这里是为了防止有的文件夹图片太少
#         face_pair_list = []
#         for image_path in (image_path_list):
#             image = np.array(mpimg.imread(image_path))
#             face_pair_list.append(image)
#         face_pairs_list.append(face_pair_list)
# print("数据读取完毕~")
index_list = np.linspace(0,(file_dirs_length),split_num,dtype=np.int)

def get_splited_cache(file_dirs_batch):
    face_pair_batch = []
    for file_dir in tqdm(file_dirs_batch):
        image_path_list = list(file_dir.glob('*.jpg'))
        if len(image_path_list) > 5:  # 这里是为了防止有的文件夹图片太少
            _face_pair_list = []
            for image_path in (image_path_list):
                image = np.array(mpimg.imread(image_path))/255.
                _face_pair_list.append(image)
        face_pair_batch.append(_face_pair_list)
    face_pair_batch = np.array(face_pair_batch)
    return face_pair_batch


# print(len(face_pairs_list[0]))
# print(face_pairs_list[0][0].shape)
# print(face_pairs_list[0][0])
#这里的num_people是指每个batch中有多少个人
#k指的是每个people出多少张图做比对
batch_size = 2  #实际上的batch数为batch_size - 1
train_length = (index_list[1] - index_list[0]) * batch_size
print("总共的文件数为：",train_length)
def generator(k = 8,num_people = 32,index_list = 0):
    batch_num = train_length//num_people
    while 1:

        id = np.random.choice(range(len(index_list)-batch_size))
        index_list = index_list[id:id + batch_size]
        face_pairs_list = []
        for i in range(len(index_list) - 1):
            start = index_list[i]
            end = index_list[i + 1]
            print("现在开始做", start, "到", end)
            face_pairs_list.append(get_splited_cache(file_dirs[start:end]))

        print(len(face_pairs_list))
        face_pairs_list = np.concatenate(face_pairs_list, axis=0)

        np.random.shuffle(face_pairs_list)

        for i in range(batch_num):
            start = num_people * i
            end = num_people * (i + 1)

            image_batch = []
            label_batch = []
            counter = 0
            seed = int(np.random.random() * 1024)
            for people_images_list in face_pairs_list[start:end]:
                for people_image in random.choices(people_images_list,k=k):
                    image_batch.append(people_image)

                    label_batch.append(counter)
                counter += 1
            yield np.array(image_batch),np.array(label_batch)






# class image_generator:
#     def __init__(self, path="E:/pairs_face_dataset/cut144-simi1/", K=8, num_people=32, shape=config.Config.width):
#         self.path = Path(path)
#         self.shape = shape
#         self.file_dir = [x for x in self.path.iterdir() if x.is_dir()]
#         self.K = K
#         self.num_people = num_people
#
#     # Generate images according online learning strategy.
#     def gen_image(self):
#         image_list = np.zeros(
#             [self.num_people * self.K, self.shape, self.shape, 3])
#         label_list = np.zeros([self.num_people * self.K])
#         for person in range(self.num_people):
#             counter = 0
#             positive = random.randint(0, len(self.file_dir) - 1)
#             pos_path = list(self.file_dir[positive].glob('*.jpg'))
#             for image_path in random.choices(pos_path, k=self.K):
#                 # img = cv2.cvtColor(cv2.imread(image_path.as_posix()), cv2.COLOR_RGB2BGR)/255
#                 # img = cv2.resize(img,(config.Config.width,config.Config.height))
#                 # cv2.imshow("1",img)
#                 # cv2.waitKey()
#
#                 #上面是原始的，这里我使用了自定义的方法
#                 img_raw = tf.io.read_file(image_path.as_posix())
#                 img = tf.io.decode_image(img_raw)
#                 img = tf.image.convert_image_dtype(img, tf.float32)
#                 img = tf.image.resize(img, (config.Config.width,config.Config.height))
#
#                 image_list[person * self.K + counter] = img
#                 label_list[person * self.K + counter] = person
#                 counter += 1
#         yield image_list, label_list
#
#
#
#     def return_val(self):
#         return tf.data.Dataset.from_generator(
#             self.gen_image,
#             output_types=(tf.float32, tf.int32),
#             output_shapes=((self.K * self.num_people, self.shape,
#                             self.shape, 3), (self.K * self.num_people))
#         )
#
# if __name__ == "__main__":
#     path = "E:/pairs_face_dataset/cut144-simi1/"
#     gen2 = image_generator(path = path,K= 8,num_people=32)
#     t2 = gen2.gen_image()

