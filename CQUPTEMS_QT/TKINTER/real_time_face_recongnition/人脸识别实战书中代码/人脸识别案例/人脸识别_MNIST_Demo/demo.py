import io
import numpy as np

import tensorflow as tf
import tensorflow_addons as tfa
import tensorflow_datasets as tfds

# def _normalize_img(img, label):
#     img = tf.cast(tf.expand_dims(img,axis=3), tf.float32) / 255.
#     seed = int(np.random.random() * 10000)
#     label = label + seed
#     return (img, label)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path = "C:/Users/晓华/Desktop/Demo/mnist.npz") # 下载mnist数据集

train_length = len(x_train)
def generator(batch_size = 32):
    batch_num = (train_length)//batch_size
    while 1:

        for i in range(batch_num):
            start = i * (batch_size)
            end = (i + 1) * batch_size
            counter = 0

            train_batch = []
            label_batch = []
            seed = int(np.random.random() * 1024)
            for image,lab in zip(x_train[start:end],y_train[start:end]):
                image = np.expand_dims(image,axis=2)

                train_batch.append(image)

                label_batch.append(lab + seed) #1875/1875 [==============================] - 9s 5ms/step - loss: 0.3106

            yield np.array(train_batch),np.array(label_batch)


# train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
# test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
# # Build your input pipelines
# train_dataset = train_dataset.shuffle(1024).batch(32)
# train_dataset = train_dataset.map(_normalize_img)
#
# test_dataset = test_dataset.batch(32)
# test_dataset = test_dataset.map(_normalize_img)
import senet
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
    senet.SENet((7, 7, 32), 128),
    #tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=None), # No activation on final dense layer
    tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1)) # L2 normalize embeddings

])
with tf.device("/GPU:0"):
    #model.load_weights("./model.h5")
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),loss=tfa.losses.TripletSemiHardLoss())
    for i in range(1):
        history = model.fit_generator(generator=generator(batch_size=32),steps_per_epoch=train_length//32,epochs=19)
        model.save_weights("./model.h5")
        print("--------------{}------------------".format(str(i)))
