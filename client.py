import streamlit as st
import numpy as np
from PIL import Image
import requests


SERVER_PATH = ''



def main():
    st.title("Skin Diseases Analysis Application")
    with st.form(key='image_form'):
        image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Analyse')

    if image is not None:
        image_pil = Image.open(image)
        st.image(image_pil, caption='Uploaded Image', use_column_width=True)
        imageList = list(np.array(image_pil))
        



if __name__ == "__main__":
    main()






