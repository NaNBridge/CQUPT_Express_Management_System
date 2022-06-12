import tensorflow as tf
weight = tf.Variable([[1.],[1.]])								#创建参数weigiht
bias  = tf.Variable([[0.17]])								#创建参数bias
input_xs = tf.constant([[1.,1.],[2.,2.]])							#创建输入值
matrix = tf.matmul(input_xs,weight) + bias						#计算结果
print(matrix)
