from Camera import Camera
from QrDecoder import QrDecoder
import cv2 

class Cameraman:
    def __init__(self):
        pass
    def record(self):
        camera = Camera()
        while(True):
            frame  = camera.capture()
            cv2.imshow('Camera',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
        camera.release()
        cv2.destroyAllWindows()
cameraman = Cameraman()
cameraman.record()