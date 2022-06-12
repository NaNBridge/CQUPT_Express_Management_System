import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
data = load_iris()
iris_target = data.target
iris_data = np.float32(data.data)
iris_target = np.float32(tf.keras.utils.to_categorical(iris_target,num_classes=3))
print(iris_target)
iris_data = tf.data.Dataset.from_tensor_slices(iris_data).batch(50)
iris_target = tf.data.Dataset.from_tensor_slices(iris_target).batch(50)
inputs = tf.keras.layers.Input(shape=(4,))
# 层的实例是可调用的，它以张量为参数，并且返回一个张量
x = tf.keras.layers.Dense(32, activation='relu')(inputs)
x = tf.keras.layers.Dense(64, activation='relu')(x)
predictions = tf.keras.layers.Dense(3, activation='softmax')(x)
# 这部分创建了一个包含输入层和三个全连接层的模型
model = tf.keras.Model(inputs=inputs, outputs=predictions)
opt = tf.optimizers.Adam(1e-3)
for epoch in range(1000):
    for _data,lable in zip(iris_data,iris_target):
        with tf.GradientTape() as tape:
            logits = model(_data)
            loss_value = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_true = lable,y_pred = logits))
            grads = tape.gradient(loss_value, model.trainable_variables)
            opt.apply_gradients(zip(grads, model.trainable_variables))
print('Training loss is :', loss_value.numpy())
model.save('./saver/the_save_model.h5')
