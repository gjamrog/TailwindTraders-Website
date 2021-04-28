import cv2

class QrDecoder:
    def __init__(self):
        self.decoder = cv2.QRCodeDetector()
    def decode(self,image):
        message, points, _ = self.decoder.detectAndDecode(image)
        return message, points
qrdecoder = QrDecoder()
print(qrdecoder.decode(cv2.imread("C:/Users/Lenovo/Documents/QrWorker/resources/helloworld.jpg")))