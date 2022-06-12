import tensorflow as tf
def identity_block(input_tensor,out_dim):
    conv1 = tf.keras.layers.Conv2D(out_dim // 4, kernel_size=1, padding="SAME", activation=tf.nn.relu)(input_tensor)
    conv2 = tf.keras.layers.BatchNormalization()(conv1)
    conv3 = tf.keras.layers.Conv2D(out_dim // 4, kernel_size=3, padding="SAME", activation=tf.nn.relu)(conv2)
    conv4 = tf.keras.layers.BatchNormalization()(conv3)
    conv5 = tf.keras.layers.Conv2D(out_dim, kernel_size=1, padding="SAME")(conv4)
    out = tf.keras.layers.Add()([input_tensor, conv5])
    out = tf.nn.relu(out)
    return out
def resnet_Model():
    input_xs = tf.keras.Input(shape=[32,32,3])
    conv_1 = tf.keras.layers.Conv2D(filters=64,kernel_size=3,padding="SAME",activation=tf.nn.relu)(input_xs)
    """--------第一层----------"""
    out_dim = 64
    identity_1 = tf.keras.layers.Conv2D(filters=out_dim, kernel_size=3, padding="SAME", activation=tf.nn.relu)(conv_1)
    identity_1 = tf.keras.layers.BatchNormalization()(identity_1)
    for _ in range(3):
        identity_1 = identity_block(identity_1,out_dim)
    """--------第二层----------"""
    out_dim = 128
    identity_2 = tf.keras.layers.Conv2D(filters=out_dim, kernel_size=3, padding="SAME", activation=tf.nn.relu)(identity_1)
    identity_2 = tf.keras.layers.BatchNormalization()(identity_2)
    for _ in range(4):
        identity_2 = identity_block(identity_2,out_dim)
    """--------第三层----------"""
    out_dim = 256
    identity_3 = tf.keras.layers.Conv2D(filters=out_dim, kernel_size=3, padding="SAME", activation=tf.nn.relu)(identity_2)
    identity_3 = tf.keras.layers.BatchNormalization()(identity_3)
    for _ in range(6):
        identity_3 = identity_block(identity_3,out_dim)
    """--------第四层----------"""
    out_dim = 512
    identity_4 = tf.keras.layers.Conv2D(filters=out_dim, kernel_size=3, padding="SAME", activation=tf.nn.relu)(identity_3)
    identity_4 = tf.keras.layers.BatchNormalization()(identity_4)
    for _ in range(3):
        identity_4 = identity_block(identity_4,out_dim)
    flat = tf.keras.layers.Flatten()(identity_4)
    flat = tf.keras.layers.Dropout(0.217)(flat)
    dense = tf.keras.layers.Dense(2048,activation=tf.nn.relu)(flat)
    dense = tf.keras.layers.BatchNormalization()(dense)
    logits = tf.keras.layers.Dense(100,activation=tf.nn.softmax)(dense)
    model = tf.keras.Model(inputs=input_xs, outputs=logits)
    return model
if __name__ == "__main__":
    resnet_model = resnet_Model()
    print(resnet_model.summary())#.2.4、使用ResNet50实战CIFAR10
