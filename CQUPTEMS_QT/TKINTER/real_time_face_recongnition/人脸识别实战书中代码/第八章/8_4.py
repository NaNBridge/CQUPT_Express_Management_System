import tensorflow as tf
#自定义输入数据
with tf.device("/CPU:0"):
    xs = tf.random.truncated_normal(shape=[50, 32, 32, 32])
    out = tf.keras.layers.AveragePooling2D(strides=[1,1])(xs)
    print(out.shape)
