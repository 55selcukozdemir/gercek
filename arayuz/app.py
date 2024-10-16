import sys
from PyQt6 import uic
from PyQt6 import QtGui
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import cv2, imutils, time
import dlib
import numpy as np
from ai import ai
import pyshine as ps

class app(QMainWindow):
    def __init__(self,application):
        self.app = application
        super().__init__()
        uic.loadUi("C:\\Users\\SELCUK\\Desktop\\dersler\\gercek\\arayuz\\app.ui", self)
        self.loadUi()
        self.btnStart.clicked.connect(self.loadImage)
        self.fps=0
        self.stop = False
    def closeEvent(self, event):
        self.stop = True
        QApplication.quit()
    def loadUi(self):
        self.label = QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\SELCUK\\Desktop\\dersler\\gercek\\arayuz\\icon.png"))
        self.label.setObjectName("label")
        self.imgLayout.addWidget(self.label)
    def loadImage(self):
        cam = True # True for webcam
        if cam:
            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture('video.mp4') # place path to your video file here
        cnt=0
        frames_to_count=20
        st = 0
        fps=0
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        model = ai()
        while(vid.isOpened()):
            QApplication.processEvents()	
            img, self.image = vid.read()
            self.image  = imutils.resize(self.image ,height = 480 )
            
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            faces = detector(gray)
            for face in faces:
                # Yüzün koordinatları alınıyor
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()

                # Yüz işaretleyicileri (landmark) hesaplanıyor
                landmarks = predictor(gray, face)

                # Her bir işaretleyici için
                for n in range(68):
                    # İşaretleyicinin koordinatları alınıyor
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y

                    # Çerçeve üzerine işaretleyici çiziliyor
                    # cv2.circle(self.image, (x, y), 2, (0, 255, 0), -1)

                points = []
                for i in range(36, 42):  # Göz bölgesi için işaretleyiciler
                    points.append([landmarks.part(i).x, landmarks.part(i).y])
                self.detect(model, points)
                points = []
                for i in range(42, 48):  # Göz bölgesi için işaretleyiciler
                    points.append([landmarks.part(i).x, landmarks.part(i).y])
                self.detect(model, points)

                        

            if cnt == frames_to_count:
                try: # To avoid divide by 0 we put it in try except
                    print(frames_to_count/(time.time()-st),'FPS') 
                    self.fps = round(frames_to_count/(time.time()-st)) 
                    st = time.time()
                    cnt=0
                except:
                    pass
            
            cnt+=1
            if self.stop:
                break

            self.update()
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    def detect(self,model,points):
        x, y, w, h = cv2.boundingRect(np.array(points))
        marginX = int(w/4)
        marginY = int(h/4)
        x -= marginX
        y -= marginY
        w += marginX*2
        h += marginY*2
        if x and y and w and h:
            temp_image = self.image[y:y+h, x:x+w]
            # temp_image = 
            model.processImage(temp_image)
            self.result = model.checkEye()
            # Ekleyeceğiniz konumu belirleyin (x, y)
            x_offset = 50  # X koordinatı
            y_offset = 200  # Y koordinatı
            self.writeText(x,y,self.result)
            # Overlay görseli, arka plana ekleyin
            self.image[y_offset:y_offset + temp_image.shape[0], x_offset:x_offset + temp_image.shape[1]] = temp_image
    def update(self):
        img = self.image
        text  =  'FPS: '+str(self.fps)
        img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(10,20,222),text_RGB=(255,255,255))
        self.setPhoto(img)
    def writeText(self, x, y, result):
        img = self.image
        if result :
            text = 'Acik'
        else :
            text = 'Kapali'
        img = ps.putBText(img,text,text_offset_x=x,text_offset_y=y-15,vspace=5,hspace=5, font_scale=0.5,background_RGB=(228,20,222),text_RGB=(255,255,255), font=cv2.FONT_HERSHEY_SIMPLEX)
    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame.data, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
if __name__ == "__main__":
    app_ = QApplication(sys.argv)
    widget = app(app_)
    widget.show()
    sys.exit(app_.exec())


    