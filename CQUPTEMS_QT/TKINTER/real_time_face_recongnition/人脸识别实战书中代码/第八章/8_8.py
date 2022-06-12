import tensorflow as tf
import os
import numpy as np
import resnet_model
path = "./dataset/cifar-100-python"
from tensorflow.python.keras.datasets.cifar import load_batch
fpath = os.path.join(path, 'train')
x_train, y_train = load_batch(fpath, label_key='fine' + '_labels')
fpath = os.path.join(path, 'test')
x_test, y_test = load_batch(fpath, label_key='fine' + '_labels')
x_train = tf.transpose(x_train,[0,2,3,1])
y_train = np.float32(tf.keras.utils.to_categorical(y_train,num_classes=100))
x_test = tf.transpose(x_test,[0,2,3,1])
y_test = np.float32(tf.keras.utils.to_categorical(y_test,num_classes=100))
batch_size  = 48
train_data = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(batch_size*10).batch(batch_size).repeat(3)

model = resnet_model.resnet_Model()
model.compile(optimizer=tf.optimizers.Adam(1e-2), loss=tf.losses.categorical_crossentropy,metrics = ['accuracy'])
model.fit(train_data, epochs=10)
score = model.evaluate(x_test, y_test)
print("last score:",score)
