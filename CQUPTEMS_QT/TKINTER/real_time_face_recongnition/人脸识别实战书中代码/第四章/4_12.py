import tensorflow as tf

resnet = tf.keras.applications.resnet50.ResNet50(weights='imagenet',include_top=False)	#加载预训练模型

img = tf.random.truncated_normal([1,224,224,3])	#随机生成一个和图片维度相同的数据
result = resnet(img)							#使用模型进行计算

print(result.shape)							#打印模型计算结果的维度
