import tensorflow as tf
import numpy as np

class CustomSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, d_model, warmup_steps=7000):
        super(CustomSchedule, self).__init__()

        self.d_model = d_model
        self.d_model = tf.cast(self.d_model, tf.float32)
        self.warmup_steps = warmup_steps
    def __call__(self, step):
        arg1 = tf.math.rsqrt(step)
        arg2 = step * (self.warmup_steps ** -1.5)

        return tf.math.rsqrt(self.d_model) * tf.math.minimum(arg1, arg2)



class CosSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, init_lr_rate = 1e-4):
        super(CosSchedule, self).__init__()
        self.init_lr_rate = init_lr_rate
    def __call__(self, step):
        lr_rate = (tf.math.cos(step/100.) + 1.) * self.init_lr_rate
        return lr_rate



#learning_rate = CustomSchedule(d_model = Config.embedding_size)
#optimizer = tf.keras.optimizers.Adam(learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)