import streamlit as st
from PIL import Image
import components.classifier as Classifier




def imageUploader():
    st.title("Image Upload and Conversion Example")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        imagePIL = Image.open(uploaded_file)
        st.image(imagePIL, caption='Uploaded Image', use_column_width=True)
        Classifier.diseasesClassification(imagePIL=imagePIL)


imageUploader()

