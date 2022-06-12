import tensorflow as tf
input = tf.Variable(tf.random.normal([1, 5, 5, 1]))			#输入图像大小变化
conv = tf.keras.layers.Conv2D(1,2,padding="SAME")(input)	#卷积核大小
print(conv.shape)
