import tensorflow as tf
#自定义输入数据
xs = tf.keras.Input( [32, 32, 32])
out = tf.keras.layers.MaxPool2D(strides=[1,1])(xs)
out = tf.keras.layers.Conv2D(filters=32,kernel_size = [2,2],padding="SAME")(xs)
out = tf.keras.layers.BatchNormalization()(xs)
out = tf.keras.layers.Add()([out,xs])
out = tf.keras.layers.Flatten()(out)
logits = tf.keras.layers.Dense(10)(out)
model = tf.keras.Model(inputs=xs, outputs=logits)
print(model.summary())
