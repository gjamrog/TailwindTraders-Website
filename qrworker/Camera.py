import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def capture(self):
        ret, frame = self.cap.read()
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return grayframe 
    def release(self):
        self.cap.release()

