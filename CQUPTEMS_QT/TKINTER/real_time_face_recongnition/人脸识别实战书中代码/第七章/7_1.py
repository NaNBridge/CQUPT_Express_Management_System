import tensorflow_datasets as tfds
import tensorflow as tf
import math
dataset,metadata = tfds.load('fashion_mnist',as_supervised=True,with_info=True)
train_dataset,test_dataset = dataset['train'],dataset['test']

model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28,1)), 		#输入层
        tf.keras.layers.Dense(256,activation=tf.nn.relu),		#隐藏层1
        tf.keras.layers.Dense(128,activation=tf.nn.relu),		#隐藏层2
        tf.keras.layers.Dense(10,activation=tf.nn.softmax)	#输出层
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

batch_size = 256
train_dataset = train_dataset.repeat().shuffle(50000).batch(batch_size)
test_dataset = test_dataset.batch(batch_size)

model.fit(train_dataset, epochs=5, steps_per_epoch=math.ceil(50000//batch_size))
