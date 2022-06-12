#如果import报错，读者需要先使用 pip install face_recognition 安装相应的包
import face_recognition

# 加载2张已知面孔的图片
known_obama_image = face_recognition.load_image_file("1.jpg")
known_biden_image = face_recognition.load_image_file("2.jpg")

# 计算图片对应的编码
img1_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
img2_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

known_encodings = [
    img1_face_encoding,
    img2_face_encoding
]

# 加载一张未知面孔的图片test
image_to_test = face_recognition.load_image_file("test.jpg")

# 计算图片对应的编码
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# 计算未知图片与已知的2个面孔的距离
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
print()
