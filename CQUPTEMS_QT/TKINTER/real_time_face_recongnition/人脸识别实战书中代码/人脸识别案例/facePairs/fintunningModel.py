import tensorflow as tf
from config import Config
import baseModel


class PairsDemo(tf.keras.layers.Layer):
    def __init__(self):
        super(PairsDemo, self).__init__()


    def build(self, input_shape):
        self.base_model = baseModel.BaseModel()

        super(PairsDemo, self).build(input_shape)  # 一定要在最后调用它


    def call(self, inputs):
        positive_data, negative_data = inputs
        pos_out = self.base_model(positive_data)
        neg_out = self.base_model(negative_data)
        out = (pos_out - neg_out) * (pos_out - neg_out)

        flat = tf.keras.layers.Flatten()(out)


if __name__ == "__main__":
    positive_dataset = tf.keras.layers.Input(name='positive_image',shape=[Config.width,Config.height, 3],dtype=tf.float32)
    negative_dataset = tf.keras.layers.Input(name='negative_image',shape=[Config.width,Config.height, 3],dtype=tf.float32)

    PairsDemo()([positive_dataset,negative_dataset])