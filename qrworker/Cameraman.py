from Camera import Camera
from QrDecoder import QrDecoder
import cv2 
from Postman import Postman
from multiprocessing import Process
from Picasso import Picasso

class Cameraman:
    def __init__(self):
        pass
    def record(self):
        camera = Camera()
        decoder = QrDecoder()
        while(True):
            frame  = camera.capture()
            try: 
                a,b = decoder.decode(frame)
                frame = Picasso.drawText(a,b, frame)
            except: 
                pass 
            cv2.imshow('Camera',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
        camera.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    cameraman = Cameraman()
    p1 = Process(target=cameraman.record)
    p1.start()
    print('CHUJ CI W KAKE ')
    p1.join()
