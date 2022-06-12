

import tensorflow as tf
with tf.device("/CPU:0"):
    input = (tf.random.normal([1, 3, 3, 1]))
    conv = tf.keras.layers.Conv2D(1,2)(input)
    print(conv)
