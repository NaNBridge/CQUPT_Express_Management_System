import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
iris_data = np.float32(data.data)
iris_target = (data.target)
iris_target = np.float32(tf.keras.utils.to_categorical(iris_target, num_classes=3))
new_model = tf.keras.models.load_model('./saver/the_save_model.h5')  # 载入模型
new_prediction = new_model.predict(iris_data)  # 进行预测

print(tf.argmax(new_prediction, axis=-1))  # 打印预测结果
