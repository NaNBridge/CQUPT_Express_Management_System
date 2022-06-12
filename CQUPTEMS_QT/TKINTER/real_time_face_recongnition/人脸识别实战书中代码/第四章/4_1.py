import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
data = load_iris()
iris_target = data.target
iris_data = np.float32(data.data)
iris_target = np.float32(tf.keras.utils.to_categorical(iris_target,num_classes=3))
iris_data = tf.data.Dataset.from_tensor_slices(iris_data).batch(50)
iris_target = tf.data.Dataset.from_tensor_slices(iris_target).batch(50)
model = tf.keras.models.Sequential()
# Add layers
model.add(tf.keras.layers.Dense(32, activation="relu"))
model.add(tf.keras.layers.Dense(64, activation="relu"))
model.add(tf.keras.layers.Dense(3,activation="softmax"))
opt = tf.optimizers.Adam(1e-3)
for epoch in range(1000):
    for _data,lable in zip(iris_data,iris_target):
        with tf.GradientTape() as tape:
            logits = model(_data)
            loss_value = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_true = lable,y_pred = logits))
            grads = tape.gradient(loss_value, model.trainable_variables)
            opt.apply_gradients(zip(grads, model.trainable_variables))
    print('Training loss is :', loss_value.numpy())
