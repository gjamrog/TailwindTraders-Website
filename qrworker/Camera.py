import cv2
import numpy as np 

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def capture(self):
        ret, frame = self.cap.read()
        return self.to_gray(frame)
    def release(self):
        self.cap.release()
    def to_gray(self,frame):
        rgb_weights = [0.2989, 0.5870, 0.1140]
        grayscale_image = np.dot(frame[...,:3], rgb_weights)
        return frame 

