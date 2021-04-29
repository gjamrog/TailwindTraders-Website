import cv2

class QrDecoder:
    def __init__(self):
        self.decoder = cv2.QRCodeDetector()
    def decode(self,image):
        message, points, _ = self.decoder.detectAndDecode(image)
        cv2.rectangle(image, (points[0][0][0], points[0][0][1]), (points[0][2][0], points[0][2][1]), (255,255,0), 2)
        if(message != ''):
            print(message)
        return image
        
image = cv2.imread("C:/Users/Lenovo/Documents/QrWorker/resources/helloworld.jpg")
qrdecoder = QrDecoder()
cv2.imshow('CHUJ', qrdecoder.decode(image))
cv2.waitKey(0) 
cv2.destroyAllWindows()