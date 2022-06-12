import tensorflow as tf
import tensorflow_addons as tfa
import senet
import numpy as np


class BaseModel(tf.keras.layers.Layer):
    def __init__(self):
        super(BaseModel, self).__init__()

    def build(self, input_shape):
        self.feature_model = tf.keras.applications.mobilenet_v2.MobileNetV2(
            input_shape=(144, 144, 3), include_top=False,weights="./h5/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_128_no_top.h5")  # Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5
        self.batch_norm = tf.keras.layers.BatchNormalization()
        self.senet = senet.SENet((4, 4, 1280), 128)
        self.dense_feature = (tf.keras.layers.Dense(units=128, activation=None))

        super(BaseModel, self).build(input_shape)  # 一定要在最后调用它


    def call(self, inputs):
        image_inputs = inputs

        features =self.feature_model(image_inputs)
        features = self.batch_norm(features)
        pooled_features = self.senet(features)

        pooled_features = tf.keras.layers.Dropout(0.5217)(pooled_features)
        dense_features = self.dense_feature(pooled_features)
        embeddings = tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(tf.cast(x, dtype='float32'), axis=1,epsilon=1e-10))(dense_features)

        return embeddings


if __name__ == "__main__":
    image = tf.keras.Input(shape=(Config.width,Config.height,3),dtype=tf.float32)
    embedding = BaseModel()(image)
    model = tf.keras.Model(image,embedding)

    import learnrate
    lr_schedule = learnrate.CosSchedule(1e-4)
    opt = tf.keras.optimizers.Adam(lr_schedule)

    los = tfa.losses.TripletSemiHardLoss()
    model.compile(optimizer=opt,loss=los)

    import fetch_data as fetch_data
    k = 12;num_people = 27

    for epoch in range(10):
        model.fit_generator(fetch_data.generator(k=k,num_people=num_people,index_list=fetch_data.index_list),steps_per_epoch=fetch_data.train_length//num_people,
                        max_queue_size=217,epochs=2)
        model.save_weights("./model.h5")



