from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from PIL import Image
import numpy as np
import cv2


#Recreate the Model to make predictions using the calculated weights from training
def fit_pretrainedModel(path):
    model = Sequential([
        Conv2D(64, (3, 3), activation="relu", padding="same", input_shape=(180, 180, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.20),

        Conv2D(64, (3, 3), activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.20),

        Conv2D(32, (3, 3), activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.20),

        Conv2D(32, (3, 3), activation="relu", padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.20),

        Flatten(),

        Dense(units=256, activation="relu"),
        Dense(units=10, activation="softmax")
    ])
    model.compile(loss=SparseCategoricalCrossentropy(), optimizer="adam", metrics=['accuracy'])
    model.load_weights(path)
    return model


labels = [
    'Eczema', 'Melanoma', 'Atopic Dermatitis', 'Basal Cell Carcinoma', 'Melanocytic Nevi',
    'Benign Keratosis-like Lesions', 'Psoriasis pictures Lichen Planus and related diseases',
    'Seborrheic Keratoses and other Benign Tumors', 'Tinea Ringworm Candidiasis and other Fungal Infections',
    'Warts Molluscum and other Viral Infections'
]


def makePrediction(imageList: list, model):
    imageNP = np.array(imageList, dtype=np.uint8)
    imageBGR = cv2.cvtColor(imageNP, cv2.COLOR_RGB2BGR)
    imageResized = cv2.resize(imageBGR,(180,180))
    inputX = np.expand_dims(imageResized, axis=0)
    predictionsNP = model.predict(inputX)
    return np.argmax(predictionsNP)
