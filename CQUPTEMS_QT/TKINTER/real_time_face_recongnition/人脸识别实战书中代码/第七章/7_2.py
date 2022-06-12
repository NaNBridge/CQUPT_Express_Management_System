import tensorflow as tf
class FashionClassic:
    def __init__(self):

        self.cnn_1 = tf.keras.layers.Conv2D(32,3,activation=tf.nn.relu)	#第一个卷积层
        self.batch_norm_1 = tf.keras.layers.BatchNormalization()		#正则化层

        self.cnn_2 = tf.keras.layers.Conv2D(64,3,activation=tf.nn.relu) 	#第二个卷积层
        self.batch_norm_2 = tf.keras.layers.BatchNormalization()		#正则化层

        self.cnn_3 = tf.keras.layers.Conv2D(128,3,activation=tf.nn.relu) 	#第三个卷积层
        self.batch_norm_3 = tf.keras.layers.BatchNormalization()		#正则化层

        self.last_dense = tf.keras.layers.Dense(10 ,activation=tf.nn.softmax)					#分类层

    def __call__(self, inputs):
        img = inputs

        img = self.cnn_1(img)									#使用第一个卷积层
        img = self.batch_norm_1(img)							#正则化

        img = self.cnn_2(img)									#使用第一个卷积层
        img = self.batch_norm_2(img)							#正则化

        img = self.cnn_3(img)									#使用第一个卷积层
        img = self.batch_norm_3(img)							#正则化

        img_flatten = tf.keras.layers.Flatten()(img)					#将数据拉平重新排列
        output = self.last_dense(img_flatten)						#使用分类器进行分类

        return output
