import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
data = load_iris()
iris_data = np.float32(data.data)
iris_data_1 = []
iris_data_2 = []
for iris in iris_data:
    iris_data_1.append(iris[0])
    iris_data_2.append(iris[1:4])
iris_data_1 = np.array(iris_data_1)
iris_data_2 = np.array(iris_data_2)
iris_target = np.float32(tf.keras.utils.to_categorical(data.target,num_classes=3))

input_xs_1  = tf.keras.Input(shape=(1,), name='input_xs_1')
input_xs_2  = tf.keras.Input(shape=(3,), name='input_xs_2')
input_xs = tf.concat([input_xs_1,input_xs_2],axis=-1)
out = tf.keras.layers.Dense(32, activation='relu', name='dense_1')(input_xs)
out = tf.keras.layers.Dense(64, activation='relu', name='dense_2')(out)
logits = tf.keras.layers.Dense(3, activation="softmax",name='predictions')(out)
model = tf.keras.Model(inputs=(input_xs_1,input_xs_2), outputs=logits)
print(model.summary())
opt = tf.optimizers.Adam(1e-3)
model.compile(optimizer=tf.optimizers.Adam(1e-3), loss=tf.losses.categorical_crossentropy,metrics = ['accuracy'])
model.fit(x = (iris_data_1,iris_data_2),y=iris_target,batch_size=128, epochs=500)
score = model.evaluate(x=(iris_data_1,iris_data_2),y=iris_target)
print("多头score：",score)
