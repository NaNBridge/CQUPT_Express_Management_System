from tensorflow.keras.layers import Conv2D, Input,MaxPool2D, Reshape,Activation,Flatten, Dense, Permute

from tensorflow.keras.models import Model, Sequential
import tensorflow as tf
import numpy as np
import cv2
#-----------------------------#
#   粗略获取人脸框
#   输出bbox位置和是否有人脸
#-----------------------------#
def create_Pnet(weight_path):
	#注意这里输入的维度为None
    input = Input(shape=[None, None, 3])

    x = Conv2D(10, (3, 3), strides=1, padding='valid', name='conv1')(input)
    x = tf.nn.relu(x)
    x = MaxPool2D(pool_size=2)(x)

    x = Conv2D(16, (3, 3), strides=1, padding='valid', name='conv2')(x)
    x = tf.nn.relu(x)

    x = Conv2D(32, (3, 3), strides=1, padding='valid', name='conv3')(x)
    x = tf.nn.relu(x)

    classifier = Conv2D(2, (1, 1), activation='softmax', name='conv4-1')(x)
    # 无激活函数，线性。
    bbox_regress = Conv2D(4, (1, 1), name='conv4-2')(x)

    model = Model([input], [classifier, bbox_regress])
    model.load_weights(weight_path, by_name=True)
    return model
