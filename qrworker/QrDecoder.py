import cv2
from Picasso import Picasso 

class QrDecoder:
    def __init__(self):
        self.decoder = cv2.QRCodeDetector()
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.color = (255,0,0)
    def decode(self,image):
        font = cv2.FONT_HERSHEY_COMPLEX
        message, points, _ = self.decoder.detectAndDecode(image)
        if(message != ''):
            return message, points
        return None 

if __name__ == "__main__":  
    image = cv2.imread("C:/Users/Lenovo/Documents/QrWorker/resources/helloworld.jpg")
    qrdecoder = QrDecoder()
    a, b = qrdecoder.decode(image)
    cv2.imshow("penis",  Picasso.drawText(a,b , image )  )
    cv2.waitKey(0)
    cv2.destroyAllWindows()