import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = tf.expand_dims(train_images,axis=3)
test_images = tf.expand_dims(test_images,axis=3)

class FashionClassic:
    def __init__(self):

        self.cnn_1 = tf.keras.layers.Conv2D(32,3,activation=tf.nn.relu)
        self.batch_norm_1 = tf.keras.layers.BatchNormalization()

        self.cnn_2 = tf.keras.layers.Conv2D(64,3,activation=tf.nn.relu)
        self.batch_norm_2 = tf.keras.layers.BatchNormalization()

        self.cnn_3 = tf.keras.layers.Conv2D(128,3,activation=tf.nn.relu)
        self.batch_norm_3 = tf.keras.layers.BatchNormalization()

        self.last_dense = tf.keras.layers.Dense(10,activation=tf.nn.softmax)

    def __call__(self, inputs):
        img = inputs

        img = self.cnn_1(img)
        img = self.batch_norm_1(img)

        img = self.cnn_2(img)
        img = self.batch_norm_2(img)

        img = self.cnn_3(img)
        img = self.batch_norm_3(img)

        img_flatten = tf.keras.layers.Flatten()(img)
        output = self.last_dense(img_flatten)

        return output


if __name__ == "__main__":
    img_input = tf.keras.Input(shape=(28,28,1))
    output = FashionClassic()(img_input)
    model = tf.keras.Model(img_input,output)

    model.compile(optimizer=tf.keras.optimizers.Adam(1e-4), loss=tf.losses.sparse_categorical_crossentropy, metrics=['accuracy'])

    model.fit(x=train_images,y=train_labels, epochs=10,verbose=2)
    model.evaluate(x=test_images,y=test_labels)
