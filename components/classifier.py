import numpy as np
import cv2
from tensorflow.keras.models import load_model


modelsPATH = './../models/skinDisease_model-3.h5'


def diseasesClassification(imagePIL):
    imageNP = np.array(imagePIL)
    imageRGB = cv2.cvtColor(imageNP, cv2.COLOR_BGR2RGB)
    imageResized = cv2.resize(imageRGB, (180, 180))
    inputX = np.expand_dims(imageResized, axis=0)

    print(inputX.shape)
    model = load_model(modelsPATH)


