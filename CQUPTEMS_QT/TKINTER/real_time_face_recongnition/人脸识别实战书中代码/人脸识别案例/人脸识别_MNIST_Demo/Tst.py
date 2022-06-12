import numpy as np
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path = "C:/Users/晓华/Desktop/Demo/mnist.npz") # 下载mnist数据集

embedding = np.load("embedding.npy")[:10]
unknow_embedding = np.load("unknow.npy")

print(embedding.shape)
print(unknow_embedding.shape)

def xiaohua_distance(vec_1,vec_2):
    vec_1 = np.array(vec_1)
    vec_2 = np.array(vec_2)

    #dist = np.sum(np.abs(vec_1 - vec_2))
    dist = np.linalg.norm(vec_1 - vec_2)
    return dist

embedding_1 = embedding
embedding_2 = unknow_embedding

# target_img = embedding_2
# result = []
# for img_1 in embedding_1:
#     dist = xiaohua_distance(target_img,img_1)
#     result.append(dist)
# print(result)
# print(np.argmin(result))
# print("=-------------------------")
# "----------------------------------------------------"

#---------------------------------#
#   比较人脸
#---------------------------------#
def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return np.empty((0))
    return np.linalg.norm(face_encodings - face_to_compare, axis=1)
def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    dis = face_distance(known_face_encodings, face_encoding_to_check)
    return list(dis <= tolerance)
#
#
known_face_encodings = embedding_1
unknow_face_encodings = embedding_2

print(known_face_encodings.shape)
print(unknow_face_encodings.shape)


for id,unknow_face_encoding in enumerate(unknow_face_encodings):
    matches = compare_faces(known_face_encodings, unknow_face_encoding, tolerance=0.6)
    face_distances = face_distance(known_face_encodings, unknow_face_encoding)
    best_match_index = np.argmin(face_distances)
    # if matches[best_match_index]:
    #     print(best_match_index)
    print(y_train[best_match_index],"-",y_test[id])
    print("----------")
# print(matches)
#
#
#

