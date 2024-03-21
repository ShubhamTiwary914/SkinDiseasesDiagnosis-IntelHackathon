import streamlit as st
from PIL import Image
<<<<<<< HEAD
import components.classifier as Classifier
import tensorflow as tf
import numpy as np


# Define the classes and lesion type dictionary
classes = ["nv", "mel", "bkl", "bcc", "akiec", "vasc", "df"]

lesion_type_dict = {
    'nv': 'Melanocytic nevi',
    'mel': 'Melanoma',
    'bkl': 'Benign keratosis-like lesions',
    'bcc': 'Basal cell carcinoma',
    'akiec': 'Actinic keratoses',
    'vasc': 'Vascular lesions',
    'df': 'Dermatofibroma'
}

# Load the three models
model_files = [
    "../model/Skin Cancer Models/model1.h5",
    "../model/Skin Cancer Models/model2.h5",
    "../model/Skin Cancer Models/model3.h5",
]



# Make predictions using the loaded models
def analyze_image(image):
    processed_image = preprocess_image(image)
    x = np.zeros((1, 256, 256, 3), dtype=np.uint8)
    x[0] = processed_image
    model_predictions = []
    for model in models:
        model_predictions.append(model.predict(x))
    predictions = np.mean(model_predictions, axis=0)
    class_ = np.argmax(predictions)
    type_ = classes[class_]
    name = lesion_type_dict[type_]
    return class_, type_, name

# Preprocess the image
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((256, 256))
    img = np.array(img)
    img = img.astype(np.float32) / 255.0
    return img



