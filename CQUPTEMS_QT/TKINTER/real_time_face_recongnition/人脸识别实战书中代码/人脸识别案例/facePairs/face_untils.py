import numpy as np
import dlib
import os


class process_img(object):
    # Process an image, applying any transformations necessary including
    # boundaries, clipping and resizing it
    def pre_process(self, image, return_boundary=False):
        boundary = self.detector(image, 2)
        if(len(boundary) == 0):
            return None
        else:
            aligned = self.clip_image(image, boundary[0])
            resized = resize(
                aligned, [self.required_size, self.required_size, 3])
            if return_boundary:
                return resized, boundary
            return resized

    def clip_image(self, image, boundary):
        top = np.clip(boundary.top(), 0, np.Inf).astype(np.int16)
        bottom = np.clip(boundary.bottom(), 0, np.Inf).astype(np.int16)
        left = np.clip(boundary.left(), 0, np.Inf).astype(np.int16)
        right = np.clip(boundary.right(), 0, np.Inf).astype(np.int16)
        return image[top:bottom, left:right]

    def __init__(self, required_size):
        self.required_size = required_size
        self.detector = dlib.get_frontal_face_detector()