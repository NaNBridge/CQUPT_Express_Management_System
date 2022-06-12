import tensorflow as tf
from config import Config
import tensorflow_addons as tfa
from pathlib import Path
import senet
from glob import glob


def cosine_distance(matrix1, matrix2):
    matrix1_matrix2 = np.dot(matrix1, matrix2.transpose())
    matrix1_norm = np.sqrt(np.multiply(matrix1, matrix1).sum(axis=1))
    matrix1_norm = matrix1_norm[:, np.newaxis]
    matrix2_norm = np.sqrt(np.multiply(matrix2, matrix2).sum(axis=1))
    matrix2_norm = matrix2_norm[:, np.newaxis]
    cosine_distance = np.divide(matrix1_matrix2, np.dot(matrix1_norm, matrix2_norm.transpose()))
    return cosine_distance



class BaseModel(tf.keras.layers.Layer):
    def __init__(self):
        super(BaseModel, self).__init__()

    def build(self, input_shape):
        self.feature_model = tf.keras.applications.mobilenet_v2.MobileNetV2(
            input_shape=(Config.width, Config.height, 3), include_top=False,weights="./h5/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_128_no_top.h5")  # Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5
        self.senet = senet.SENet((4, 4, 1280), 128)
        self.dense_feature = (tf.keras.layers.Dense(units=128, activation=None))

        super(BaseModel, self).build(input_shape)  # 一定要在最后调用它

    def call(self, inputs):
        image_inputs = inputs

        features =self.feature_model(image_inputs)
        #pooled_features = tf.keras.layers.GlobalAveragePooling2D()(features)   #这里是替代下面的senet的
        pooled_features = self.senet(features)
        pooled_features = tf.keras.layers.Dropout(0.5217)(pooled_features)
        dense_features = self.dense_feature(pooled_features)
        embeddings = tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(tf.cast(x, dtype='float32'), axis=1))(dense_features)

        return embeddings


if __name__ == "__main__":
    with tf.device("/CPU:0"):
        image = tf.keras.Input(shape=(Config.width,Config.height,3),dtype=tf.float32)
        embedding = BaseModel()(image)
        model = tf.keras.Model(image,embedding)
        model.load_weights("./model.h5",by_name=True)

        import matplotlib.image as mpimg
        import numpy as np
        import cv2

        image_path_1_list = list(Path("C:/face_DATA/1000/1/").glob('*.jpg'))
        image_path_2_list = list(Path("C:/face_DATA/1000/2/").glob('*.jpg'))

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

        image_embedding_1 = np.array(model.predict(image_1_list))
        image_embedding_2 = np.array(model.predict(image_2_list))

        print(image_embedding_1.shape)
        print(image_embedding_2.shape)

        result = (cosine_distance(image_embedding_1,image_embedding_2))
        result = np.argmax(result, axis=-1)
        counter = 0
        for i,j in zip(result,range(900)):
            if i == j:
                counter += 1
        print("正确率为：",counter/900)