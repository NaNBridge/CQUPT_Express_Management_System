import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # 图像控件
from cv2 import VideoCapture
import face_recognition
import numpy as np



cap = cv2.VideoCapture(0)  # 创建摄像头对象


def tkImage():
    global cap
    ref, frame = cap.read()
    # frame=get_a_frame(cap)
    frame = cv2.flip(frame, 1)  # 摄像头翻转
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((image_width, image_height), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage


def face_recognition_GUI():
    # 定义root页面
    root = tk.Tk()
    root.geometry("1024x634")  # 比例接近于黄金分割率
    