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
print(y_train[191])
_x_train = np.expand_dims(x_train,axis=3)
print(y_test[:10])  #[7 2 1 0 4 1 4 9 5 9]
unknow_x = np.expand_dims(x_test[:1000],axis=3) #这个值是5
#unknow_x = x_test[8][np.newaxis,:,:,np.newaxis] #这个值是5

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

model.load_weights("./model.h5")
embedding = np.array(model.predict(_x_train))
unknow_embeding = np.array(model.predict(unknow_x))

np.save("embedding.npy",embedding)
np.save("unknow.npy",unknow_embeding)


# with tf.device("/CPU:0"):
#     # Compile the model
#     model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),loss=tfa.losses.TripletSemiHardLoss())
#     # Train the network
#     history = model.fit_generator(generator=generator(batch_size=32),steps_per_epoch=train_length//32,epochs=217)
#     model.save_weights("./model.h5")
# # Evaluate the network
# results = model.predict(test_dataset)
#
# # Save test embeddings for visualization in projector
# np.savetxt("vecs.tsv", results, delimiter='\t')
#
# out_m = io.open('meta.tsv', 'w', encoding='utf-8')
# for img, labels in tfds.as_numpy(test_dataset):
#     [out_m.write(str(x) + "\n") for x in labels]
# out_m.close()


# from sklearn.decomposition import PCA
#
# pca = PCA(n_components=2)
# pca.fit(X)