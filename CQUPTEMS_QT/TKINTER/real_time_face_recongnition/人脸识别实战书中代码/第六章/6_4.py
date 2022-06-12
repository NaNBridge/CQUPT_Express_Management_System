import tensorflow as tf
input = tf.Variable(tf.random.normal([1, 5, 5, 1]))
conv = tf.keras.layers.Conv2D(1,2,strides=[2,2],padding="SAME")(input)	#strides的大小被替换
print(conv.shape)
