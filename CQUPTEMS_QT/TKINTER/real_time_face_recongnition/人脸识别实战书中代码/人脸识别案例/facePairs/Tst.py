import numpy as np


arr_1 = np.array([0,1,2,3,4,5,6])
arr_2 = np.array([2,3,4,6,4,5,6])

arr = sum(np.abs(arr_1 - arr_2))


def xiaohua_distance(vec_1,vec_2):
    vec_1 = np.array(vec_1)
    vec_2 = np.array(vec_2)

    #dist = np.sum(np.abs(vec_1 - vec_2))
    dist = np.linalg.norm(vec_1 - vec_2)
    return dist

embedding_1 = np.load("embedding_1.npy")
embedding_2 = np.load("embedding_2.npy")

id = 19
target_img = embedding_2[id]
result = []
for img_1 in embedding_1[:100]:
    dist = xiaohua_distance(target_img,img_1)
    result.append(dist)
print(result)
print(np.argmin(result))
print("=-------------------------")
"----------------------------------------------------"

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


known_face_encodings = embedding_1[:100]
unknow_face_encoding = embedding_2[id]

matches = compare_faces(known_face_encodings, unknow_face_encoding, tolerance = 0.6)
print(matches)
face_distances = face_distance(known_face_encodings, unknow_face_encoding)
best_match_index = np.argmin(face_distances)
print(best_match_index)
if matches[best_match_index]:
    print(best_match_index)