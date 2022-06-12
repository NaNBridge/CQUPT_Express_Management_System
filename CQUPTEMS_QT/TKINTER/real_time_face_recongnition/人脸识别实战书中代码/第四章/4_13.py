import tensorflow as tf

resnet_layer = tf.keras.applications.resnet50.ResNet50(weights='imagenet',include_top=False,pooling = False)						#载入resnet模型和参数

flatten_layer = tf.keras.layers.GlobalAveragePooling2D()		#使用全局池化层进行数据压缩
drop_out_layer = tf.keras.layers.Dropout(0.1)				#使用dropout防止过拟合
fc_layer = tf.keras.layers.Dense(2)						#接上分类层

binary_classes = tf.keras.Sequential([resnet_layer,flatten_layer,drop_out_layer,fc_layer]) #组合模型
print(binary_classes.summary())						#打印模型结构
