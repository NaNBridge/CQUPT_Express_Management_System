from tensorflow.keras.layers import Conv2D, Input,MaxPool2D, Reshape,Activation,Flatten, Dense, Permute

from tensorflow.keras.models import Model, Sequential
import tensorflow as tf
import numpy as np

import cv2

#-----------------------------#
#   mtcnn的第三段
#   同时精修框并人外获得获得五个脸部特征点的坐标
#-----------------------------#
def create_Onet(weight_path):
    input = Input(shape = [48,48,3])
    # 48,48,3 -> 23,23,32
    x = Conv2D(32, (3, 3), strides=1, padding='valid', name='conv1')(input)
    x = tf.nn.relu(x)
    x = MaxPool2D(pool_size=3, strides=2, padding='same')(x)
    # 23,23,32 -> 10,10,64
    x = Conv2D(64, (3, 3), strides=1, padding='valid', name='conv2')(x)
    x = tf.nn.relu(x)
    x = MaxPool2D(pool_size=3, strides=2)(x)
    # 8,8,64 -> 4,4,64
    x = Conv2D(64, (3, 3), strides=1, padding='valid', name='conv3')(x)
    x = tf.nn.relu(x)
    x = MaxPool2D(pool_size=2)(x)
    # 4,4,64 -> 3,3,128
    x = Conv2D(128, (2, 2), strides=1, padding='valid', name='conv4')(x)
    x = tf.nn.relu(x)
    # 3,3,128 -> 128,12,12

    x = tf.transpose(x,[0,3,2,1])
    # 1152 -> 256
    x = Flatten()(x)
    x = Dense(256, name='conv5') (x)
    x = tf.nn.relu(x)

    # 鉴别
    # 256 -> 2 256 -> 4 256 -> 10
    classifier = Dense(2, activation='softmax',name='conv6-1')(x)
    bbox_regress = Dense(4,name='conv6-2')(x)
    landmark_regress = Dense(10,name='conv6-3')(x)

    model = Model([input], [classifier, bbox_regress, landmark_regress])
    model.load_weights(weight_path, by_name=True)

    return model
