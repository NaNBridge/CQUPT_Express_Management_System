from cv2 import VideoCapture
import face_recognition
import cv2
import numpy as np
# import dlib


def Real_time_face_recognition(video_capture):
    """实时识别人脸
    """
    # 获取摄像头数据
    #video_capture = cv2.VideoCapture(0)

    # 读取图片，并将其编码方便后续识别
    nanqiao_gong_image = face_recognition.load_image_file("../img/face_pictures/fixed/龚南桥.jpg")
    nanqiao_gong_face_encoding = face_recognition.face_encodings(nanqiao_gong_image)[0]

    # 添加已知人脸
    known_face_encodings = [
        nanqiao_gong_face_encoding
        
    ]
    # 添加人名
    known_face_names = [
        "Nanqiao_Gong"
        
    ]

    # 初始化一些变量
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # 获取一个单一窗口
        ret, frame = video_capture.read()
        # 定义视频帧
        video_frame=0.25
        # 将视频帧大小调整为1/4，以加快人脸识别处理
        small_frame = cv2.resize(frame, (0, 0), fx=video_frame, fy=video_frame)

        #将图像从BGR颜色（OpenCV使用）转换为RGB颜色（face\u recognition使用）
        rgb_small_frame = small_frame[:, :, ::-1]

        # 仅每隔一帧处理一次视频以节省时间
        if process_this_frame:
            # 查找当前视频帧中的所有面和面编码
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # 查看获取的人脸是否与已知人脸匹配
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"



                # 匹配相似度最高的人脸
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    print(name)
                face_names.append(name)

        process_this_frame = not process_this_frame

        # 帧缩放
        frame_scale=int(1/video_frame)
        # 展示结果
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 缩放面部位置，因为我们在中检测到的帧已缩放为1/4大小
            top *= frame_scale
            right *= frame_scale
            bottom *= frame_scale
            left *= frame_scale

            # 在人脸周围绘制一个方框
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # 在面下方绘制具有名称的标签
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # 展示结果图像
        cv2.imshow('Video', frame)

        # 按‘q’关闭
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头权限
    video_capture.release()
    cv2.destroyAllWindows()    
    
    pass



if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)
    Real_time_face_recognition(video_capture)
