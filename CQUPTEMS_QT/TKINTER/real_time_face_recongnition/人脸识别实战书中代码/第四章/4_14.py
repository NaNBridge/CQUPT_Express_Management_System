import tensorflow as tf

resnet_layer = tf.keras.applications.resnet50.ResNet50(weights='imagenet',include_top=False,pooling = False)
resnet_layer.trainable = False						#显式地设置resnet层为不可训练
flatten_layer = tf.keras.layers.GlobalAveragePooling2D()
drop_out_layer = tf.keras.layers.Dropout(0.1)
fc_layer = tf.keras.layers.Dense(2)

binary_classes = tf.keras.Sequential([resnet_layer,flatten_layer,drop_out_layer,fc_layer])
print(binary_classes.summary())
