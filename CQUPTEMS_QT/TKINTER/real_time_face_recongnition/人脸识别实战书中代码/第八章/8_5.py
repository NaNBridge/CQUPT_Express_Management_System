import tensorflow as tf
#自定义输入数据
with tf.device("/CPU:0"):

    xs = tf.random.truncated_normal(shape=[50, 32, 32, 32])
    out = tf.keras.layers.MaxPool2D(strides=[1,1])(xs)
    out = tf.keras.layers.Conv2D(filters=32,kernel_size = [2,2],padding="SAME")(out)
    out = tf.keras.layers.BatchNormalization()(xs)
    out = tf.keras.layers.Flatten()(out)
    logits = tf.keras.layers.Dense(10)(out)
    print(logits.shape)

