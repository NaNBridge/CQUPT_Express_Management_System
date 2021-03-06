
import io
import numpy as np

import tensorflow as tf
import tensorflow_addons as tfa
import tensorflow_datasets as tfds


def _normalize_img(img, label):
    img = tf.cast(img, tf.float32) / 255.
    return (img, label)


train_dataset, test_dataset = tfds.load(name="mnist", split=['train', 'test'], as_supervised=True)

# Build your input pipelines
train_dataset = train_dataset.shuffle(1024).batch(256)
train_dataset = train_dataset.map(_normalize_img)

test_dataset = test_dataset.batch(32)
test_dataset = test_dataset.map(_normalize_img)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation=None),  # No activation on final dense layer
    tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1))  # L2 normalize embeddings

])
# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tfa.losses.TripletSemiHardLoss(0.217))
# Train the network
history = model.fit(
    train_dataset,
    epochs=30)

model.save_weights("./model.h5")


# Evaluate the network
results = model.predict(test_dataset)
np.save("MNIST_test.npy",results)




# # Save test embeddings for visualization in projector
# np.savetxt("vecs.tsv", results, delimiter='\t')
#
# out_m = io.open('meta.tsv', 'w', encoding='utf-8')
# for img, labels in tfds.as_numpy(test_dataset):
#     [out_m.write(str(x) + "\n") for x in labels]
# out_m.close()


