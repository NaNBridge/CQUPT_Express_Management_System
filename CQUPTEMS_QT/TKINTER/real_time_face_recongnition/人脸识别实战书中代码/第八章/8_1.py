import tensorflow as tf
with tf.device("/CPU:0"):
    #自定义输入数据
    xs = tf.random.truncated_normal(shape=[50, 32, 32, 32])
    #使用二维卷积进行计算
    out = tf.keras.layers.Conv2D(64,3,padding="SAME")(xs)
    print(out.shape)
