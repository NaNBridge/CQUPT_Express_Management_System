from cv2 import VideoCapture
import face_recognition
import numpy as np
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # 图像控件
import time
import pinyin


class Face_Pickup:

    def __init__(self):
        # 创建摄像头对象
        self.cap = cv2.VideoCapture(0)
        self.face_pickup()

    def tkImage(self):

        ref, frame = self.cap.read()
        # frame=get_a_frame(cap)
        frame = cv2.flip(frame, 1)  # 摄像头翻转
        cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        pilImage = Image.fromarray(cvimage)
        pilImage = pilImage.resize((600, 371), Image.ANTIALIAS)
        tkImage = ImageTk.PhotoImage(image=pilImage)
        return tkImage

    def face_pickup(self):

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        window = Tk()

        window.geometry("1024x634")
        window.configure(bg="#00447A")

        canvas = Canvas(
            window,
            bg="#00447A",
            height=634,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        pickup_by_face = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.face_recognition_GUI,
            relief="flat"
        )
        pickup_by_face.place(
            x=437.0,
            y=434.0,
            width=150.0,
            height=94.0
        )

        canvas.create_text(
            448.0,
            528.0,
            anchor="nw",
            text="人脸取件",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )
        window.resizable(False, False)

        image_width = 600
        image_height = 371
        canvas = Canvas(window, bg='white', width=image_width,
                        height=image_height)  # 绘制画布
        Label(window, text='请直视摄像头', font=("黑体", 14), width=15,
              height=1).place(x=500, y=20, anchor='center')
        canvas.place(x=200, y=50)
        while True:
            pic = self.tkImage()
            canvas.create_image(0, 0, anchor='nw', image=pic)
            window.update()
            window.after(1)
        window.mainloop()
        pass

    def face_recognition_GUI(self):
        """实时识别人脸
        """
        print("人脸取件")
        # 获取摄像头数据
        #video_capture = cv2.VideoCapture(0)
        video_capture = self.cap
        # 读取图片，并将其编码方便后续识别
        wangjun_image = face_recognition.load_image_file(
            "D:/Project/CQUPT_Express_Management_System/CQUPTEMS_QT/TKINTER/img/face_pictures/fixed/王俊.jpg"
        )
        nanqiao_gong_image = face_recognition.load_image_file(
            "D:/Project/CQUPT_Express_Management_System/CQUPTEMS_QT/TKINTER/img/face_pictures/fixed/龚南桥.jpg")
        nanqiao_gong_face_encoding = face_recognition.face_encodings(nanqiao_gong_image)[
            0]
        wangjun_face_encoding = face_recognition.face_encodings(wangjun_image)[
            0]
        # 添加已知人脸
        known_face_encodings = [
            nanqiao_gong_face_encoding,
            wangjun_face_encoding

        ]
        # 添加人名
        known_face_names = [
            "龚南桥",
            "王俊"

        ]

        # 初始化一些变量
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        # 识别成功后提示框返回的结果
        boo = None
        while True:

            # 获取一个单一窗口
            ret, frame = video_capture.read()
            # 定义视频帧
            video_frame = 0.25
            # 将视频帧大小调整为1/4，以加快人脸识别处理
            small_frame = cv2.resize(
                frame, (0, 0), fx=video_frame, fy=video_frame)

            # 将图像从BGR颜色（OpenCV使用）转换为RGB颜色（face\u recognition使用）
            rgb_small_frame = small_frame[:, :, ::-1]

            # 仅每隔一帧处理一次视频以节省时间
            if process_this_frame:
                # 查找当前视频帧中的所有面和面编码
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # 查看获取的人脸是否与已知人脸匹配
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding)
                    name = "Unknown"

                    # 匹配相似度最高的人脸
                    face_distances = face_recognition.face_distance(
                        known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        print(name)
                    face_names.append(name)
                    boo = (name in known_face_names)
                    # if name in known_face_names:
                    #     boo=messagebox.askokcancel("成功取件提示",f"{name},您好!\n您已成功取件")
                    # messagebox.showinfo(name,"您好!\n您已成功取件")
                    # if boo==True:
                    #     cv2.destroyAllWindows()
                    # video_capture.release()
                    # cv2.destroyAllWindows()
                    # break
                    # pass

            process_this_frame = not process_this_frame

            # 帧缩放
            frame_scale = int(1/video_frame)
            # 展示结果

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # 缩放面部位置，因为我们在中检测到的帧已缩放为1/4大小
                top *= frame_scale
                right *= frame_scale
                bottom *= frame_scale
                left *= frame_scale

                # 在人脸周围绘制一个方框
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 0, 255), 2)

                # 在面下方绘制具有名称的标签
                cv2.rectangle(frame, (left, bottom - 35),
                              (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                nameStr = str()
                for char in name:
                    nameStr += pinyin.get(char)[0].upper()
                cv2.putText(frame, nameStr, (left + 6, bottom - 6),
                            font, 1.0, (255, 255, 255), 1)

            # 展示结果图像
            cv2.imshow(self.zh_ch("人脸识别中......"), frame)
            # time.sleep(5)
            """
            def creat_top_window():
                top=Toplevel()
                top.geometry("150x150")
                top.title("取件成功")
                Label(top,text=f"{name},您已成功取件!").pack()
            if boo==True:
                creat_top_window()
                
                cv2.destroyAllWindows()
                #time.sleep(5)
                break
            """
            # 按‘q’关闭
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                messagebox.askokcancel("成功取件提示", f"{name},您好!\n您已成功取件")
                break

        # 释放摄像头权限
        # video_capture.release()
        cv2.destroyAllWindows()

        pass

    def zh_ch(self, string):
        return string.encode("gbk").decode(errors="ignore")


if __name__ == "__main__":

    test = Face_Pickup()

    pass
