import cv2 

class Picasso: 

    font = cv2.FONT_HERSHEY_COMPLEX
    color = (255,0,0)
    thickness = 3 

    @classmethod
    def drawText(cls,message, points, image):
        cv2.line(image, (points[0][0][0], points[0][0][1]), (points[0][1][0], points[0][1][1]), cls.color, cls.thickness)
        cv2.line(image, (points[0][1][0], points[0][1][1]), (points[0][2][0], points[0][2][1]), cls.color, cls.thickness)
        cv2.line(image, (points[0][2][0], points[0][2][1]), (points[0][3][0], points[0][3][1]), cls.color, cls.thickness)
        cv2.line(image, (points[0][3][0], points[0][3][1]), (points[0][0][0], points[0][0][1]), cls.color, cls.thickness)
        
        cv2.putText(image,message,( int(points[0][0][0]), int(points[0][0][1])-6),cls.font,0.5,(0,255,0),1)
        
        return image 