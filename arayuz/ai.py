from keras import models
import numpy as np
from keras.preprocessing.image import img_to_array
import cv2

class ai: 
    def __init__(self) -> None:
        self.loadWeight()
    def loadWeight(self):
        self.model = models.load_model("C:\\Users\\SELCUK\\Desktop\\dersler\\gercek\\my_model.keras")
        print(self.model.summary())
    def processImage(self, image):
        # Görseli modelin beklediği boyuta getir
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (34, 26)).astype(np.uint8)   # width ve height modelin girdi boyutu

        # Görseli uygun formata dönüştür
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        self.image = image
        return self.image
    def checkEye(self):
        predictions = self.model.predict(self.image)
        # print((predictions[0]*10).astype(np.uint8) )
        # print(predictions)
        return (predictions[0]*10).astype(np.uint8) > 5