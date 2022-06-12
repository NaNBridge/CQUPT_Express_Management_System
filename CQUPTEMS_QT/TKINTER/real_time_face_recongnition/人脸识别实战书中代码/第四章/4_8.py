import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
data = load_iris()
iris_data = np.float32(data.data)
iris_data_1 = []
iris_data_2 = []
for iris in iris_data:
    iris_data_1.append(iris[:2])
    iris_data_2.append(iris[2:])
iris_label = np.array(data.target,dtype=np.float)
iris_target = tf.one_hot(data.target,depth=3)

iris_data_1 = np.array(iris_data_1)
iris_data_2 = np.array(iris_data_2)

input_xs_1  = tf.keras.Input(shape=(2), name='input_xs_1')
input_xs_2  = tf.keras.Input(shape=(2), name='input_xs_2')
input_xs = tf.concat([input_xs_1,input_xs_2],axis=-1)
out = tf.keras.layers.Dense(32, activation='relu', name='dense_1')(input_xs)
out = tf.keras.layers.Dense(64, activation='relu', name='dense_2')(out)
logits = tf.keras.layers.Dense(3, activation="softmax",name='predictions')(out)
label = tf.keras.layers.Dense(1,name='label')(out)
model = tf.keras.Model(inputs=(input_xs_1,input_xs_2), outputs=(logits,label))
opt = tf.optimizers.Adam(1e-3)
def my_MSE(y_true , y_pred):
    my_loss = tf.reduce_mean(tf.square(y_true - y_pred))
    return my_loss
model.compile(optimizer=tf.optimizers.Adam(1e-3), loss={'predictions': tf.losses.categorical_crossentropy, 'label': my_MSE},loss_weights={'predictions': 0.1, 'label': 0.5},metrics = ['accuracy'])
model.fit(x = (iris_data_1,iris_data_2),y=(iris_target,iris_label), epochs=500)

