import streamlit as st
from PIL import Image
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
    "../model/Skin/skin_model1.h5",
    "../model/Skin/skin_model2.h5",
    "../model/Skin/skin_model3.h5",
]
# models = []
# for file in model_files:
#     models.append(tf.keras.models.load_model(file, compile=False))

# Set the title of the app
st.title("Skin Cancer Classification and Chatbot")

# Add a file uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

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

# Display the uploaded image and analyze it automatically
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    class_, type_, name = analyze_image(uploaded_file)
    st.write(f"Prediction: {name}")
