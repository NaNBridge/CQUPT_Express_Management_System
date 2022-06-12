from pathlib import Path
import dlib
import cv2
import numpy as np

from tqdm import tqdm
detector = dlib.get_frontal_face_detector() #人脸检测器

path = "./dataset/lfw-deepfunneled/"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]

rec_box_list = []
counter = 0
for file_dir in tqdm(file_dirs):
    image_path_list = list(Path(file_dir).glob('*.jpg'))
    for image_path in image_path_list:
        image_path = "./" + str(image_path)
        image = (cv2.imread(image_path))
        draw = image.copy()

        boundarys = detector(image, 2)
        rectangle = list(boundarys)
		#为了简便起见，作者限定每张图片中只有一个人的图
        if len(rectangle) == 1:
            rectangle = rectangle[0]
            top = np.int(rectangle.top())  # idx = 1
            bottom = np.int(rectangle.bottom())  # idx = 3
            left = np.int(rectangle.left())  # idx = 0
            right = np.int(rectangle.right())  # idx = 2

            if rectangle is not None:
                W = -int(left) + int(right)
                H = -int(top) + int(bottom)
                paddingH = 0.01 * W
                paddingW = 0.02 * H
                crop_img = image[int(top + paddingH):int(bottom - paddingH), int(left - paddingW):int(right + paddingW)]
                cv2.rectangle(draw, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), 1)

            rec_box = [top,bottom,left,right]

            rec_box_list.append(rec_box)

            new_path = "./dataset/lfw/" + str(counter) + ".jpg"
            cv2.imwrite(new_path, image)
            counter += 1

np.save("./dataset/lfw/rec_box_list.npy",rec_box_list)
